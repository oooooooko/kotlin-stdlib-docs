@file:OptIn(org.jetbrains.kotlin.CoreEnvironmentDeprecation::class, org.jetbrains.kotlin.config.CompilerConfiguration.Internals::class, org.jetbrains.kotlin.compiler.plugin.ExperimentalCompilerApi::class)

import java.io.File
import org.jetbrains.kotlin.cli.extensionsStorage
import org.jetbrains.kotlin.compiler.plugin.CompilerPluginRegistrar
import org.jetbrains.kotlin.cli.jvm.compiler.EnvironmentConfigFiles
import org.jetbrains.kotlin.cli.jvm.compiler.KotlinCoreEnvironment
import org.jetbrains.kotlin.com.intellij.openapi.util.Disposer
import org.jetbrains.kotlin.com.intellij.psi.PsiErrorElement
import org.jetbrains.kotlin.com.intellij.psi.util.PsiTreeUtil
import org.jetbrains.kotlin.config.CompilerConfiguration
import org.jetbrains.kotlin.lexer.KtTokens
import org.jetbrains.kotlin.psi.*

private fun json(value: Any?): String = when (value) {
    null -> "null"
    is String -> "\"" + value.map { c -> when (c) {
        '\\' -> "\\\\"; '"' -> "\\\""; '\n' -> "\\n"; '\r' -> "\\r"; '\t' -> "\\t"
        else -> if (c.code < 32) "\\u%04x".format(c.code) else c.toString()
    }}.joinToString("") + "\""
    is Map<*, *> -> value.entries.joinToString(",", "{", "}") { json(it.key.toString()) + ":" + json(it.value) }
    is Iterable<*> -> value.joinToString(",", "[", "]") { json(it) }
    else -> value.toString()
}

fun main(args: Array<String>) {
    val root = File(args[0]).canonicalFile
    val disposable = Disposer.newDisposable()
    try {
        val configuration = CompilerConfiguration()
        configuration.extensionsStorage = CompilerPluginRegistrar.ExtensionStorage()
        val environment = KotlinCoreEnvironment.createForProduction(disposable, configuration, EnvironmentConfigFiles.JVM_CONFIG_FILES)
        val factory = KtPsiFactory(environment.project, false)
        generateSequence(::readlnOrNull).forEach { relative ->
            val source = File(root, relative).readText()
            val file = factory.createFile(File(relative).name, source)
            val pkg = file.packageFqName.asString()
            if (pkg.isEmpty() || pkg.split('.').contains("internal")) return@forEach
            val errors = PsiTreeUtil.collectElementsOfType(file, PsiErrorElement::class.java)
            if (errors.isNotEmpty()) System.err.println("PARSE $relative: ${errors.first().errorDescription}")

            fun walk(declaration: KtDeclaration, owners: List<String>) {
                if (listOf(KtTokens.PRIVATE_KEYWORD, KtTokens.INTERNAL_KEYWORD).any(declaration::hasModifier)) return
                val annotations = declaration.modifierList?.text.orEmpty()
                if (Regex("(?:DeprecationLevel\\.)?HIDDEN\\b").containsMatchIn(annotations)) return
                val name = when (declaration) {
                    is KtConstructor<*> -> "constructor"
                    is KtNamedDeclaration -> declaration.name ?: return
                    else -> return
                }
                val kind = when (declaration) {
                    is KtEnumEntry -> "enum_entry"
                    is KtObjectDeclaration -> "object_declaration"
                    is KtClass -> "class_declaration"
                    is KtConstructor<*> -> "secondary_constructor"
                    is KtNamedFunction -> "function_declaration"
                    is KtProperty, is KtParameter -> "property_declaration"
                    is KtTypeAlias -> "type_alias"
                    else -> return
                }
                val end = when (declaration) {
                    is KtClassOrObject -> declaration.body?.textRange?.startOffset
                    is KtNamedFunction -> (declaration.equalsToken ?: declaration.bodyExpression)?.textRange?.startOffset
                    is KtProperty -> listOfNotNull(declaration.equalsToken, declaration.getter, declaration.setter, declaration.delegate).minOfOrNull { it.textRange.startOffset }
                    is KtConstructor<*> -> declaration.bodyExpression?.textRange?.startOffset
                    else -> null
                } ?: declaration.textRange.endOffset
                val parameters = when(declaration) {
                    is KtCallableDeclaration -> declaration.valueParameters
                    is KtClass -> declaration.primaryConstructorParameters
                    else -> emptyList()
                }
                val callable = declaration as? KtCallableDeclaration
                val kdoc = declaration.docComment?.text.orEmpty()
                if (args.getOrNull(1)=="--tests") {
                    if (declaration is KtNamedFunction && declaration.annotationEntries.any { it.shortName?.asString() in setOf("Test","Sample") }) {
                        val helpers=mutableListOf<String>()
                        var ancestor=declaration.parent
                        while (ancestor!=null) {
                            val siblings=when(ancestor) {
                                is KtClassOrObject -> ancestor.declarations
                                is KtFile -> ancestor.declarations
                                else -> emptyList()
                            }
                            siblings.filter { sibling ->
                                sibling !== declaration && sibling !is KtConstructor<*> &&
                                PsiTreeUtil.collectElementsOfType(sibling,KtAnnotationEntry::class.java).none { it.shortName?.asString() in setOf("Test","Sample","BeforeTest","AfterTest","Before","After") }
                            }.forEach { helpers.add(it.text) }
                            ancestor=ancestor.parent
                        }
                        val imports=file.importDirectives.map { it.text }.filter { it.startsWith("import kotlin.") || it.startsWith("import java.") || it.startsWith("import javax.") }
                        val body=declaration.bodyExpression?.text?.removePrefix("{")?.removeSuffix("}").orEmpty()
                        val program=imports.joinToString("\n")+"\n\n"+helpers.distinct().joinToString("\n\n")+"\n\nfun main() {\n$body\n}\n"
                        val programFile=factory.createFile("Example.kt",program)
                        val calls=PsiTreeUtil.collectElementsOfType(programFile,KtCallExpression::class.java).filter { it.calleeExpression?.text?.startsWith("assert")==true }.map { call ->
                            linkedMapOf("start" to call.textRange.startOffset,"end" to call.textRange.endOffset,"callee" to call.calleeExpression?.text,"arguments" to call.valueArguments.map { it.getArgumentExpression()?.text.orEmpty() })
                        }
                        println(json(linkedMapOf("key" to (pkg+"."+(owners+name).joinToString(".")),"source" to relative,"line" to (source.take(declaration.textRange.startOffset).count { it=='\n' }+1),"code" to program,"assertions" to calls)))
                    }
                } else println(json(linkedMapOf(
                    "package" to pkg, "owner" to owners.joinToString("."), "name" to name,
                    "kind" to kind, "signature" to source.substring(declaration.textRange.startOffset, end).trim().replace(Regex("^/\\*\\*[\\s\\S]*?\\*/\\s*"), ""),
                    "visibility" to if (declaration.hasModifier(KtTokens.PROTECTED_KEYWORD)) "protected" else "public",
                    "source" to relative, "line" to (source.take(declaration.textRange.startOffset).count { it == '\n' } + 1),
                    "kdoc" to kdoc, "receiver" to callable?.receiverTypeReference?.text,
                    "return_type" to callable?.typeReference?.text,
                    "parameters" to parameters.map { p -> linkedMapOf("name" to p.name, "type" to p.typeReference?.text, "optional" to p.hasDefaultValue(), "vararg" to p.isVarArg) },
                    "samples" to Regex("@sample\\s+(\\S+)").findAll(kdoc).map { it.groupValues[1] }.toList(),
                    "since" to Regex("@SinceKotlin\\(\"([^\"]+)\"\\)").findAll(annotations).map { it.groupValues[1] }.toList()
                )))
                if (declaration is KtClassOrObject && declaration !is KtEnumEntry) {
                    val next = owners + name
                    if (declaration is KtClass) {
                        declaration.primaryConstructor?.let { walk(it, next) }
                        declaration.primaryConstructorParameters.filter { it.hasValOrVar() }.forEach { walk(it, next) }
                    }
                    declaration.declarations.forEach { walk(it, next) }
                }
            }
            file.declarations.forEach { walk(it, emptyList()) }
        }
    } finally { Disposer.dispose(disposable) }
}
