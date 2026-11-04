@file:OptIn(org.jetbrains.kotlin.compiler.plugin.ExperimentalCompilerApi::class, org.jetbrains.kotlin.ir.symbols.UnsafeDuringIrConstructionAPI::class)

import java.io.File
import org.jetbrains.kotlin.backend.common.extensions.IrGenerationExtension
import org.jetbrains.kotlin.backend.common.extensions.IrPluginContext
import org.jetbrains.kotlin.compiler.plugin.CompilerPluginRegistrar
import org.jetbrains.kotlin.config.CompilerConfiguration
import org.jetbrains.kotlin.ir.IrElement
import org.jetbrains.kotlin.ir.declarations.*
import org.jetbrains.kotlin.ir.expressions.*
import org.jetbrains.kotlin.ir.util.fqNameWhenAvailable
import org.jetbrains.kotlin.ir.visitors.IrVisitorVoid
import org.jetbrains.kotlin.ir.visitors.acceptChildrenVoid

class ExampleCallsPlugin : CompilerPluginRegistrar() {
    override val pluginId = "stdlib-docs-example-calls"
    override val supportsK2 = true
    override fun ExtensionStorage.registerExtensions(configuration: CompilerConfiguration) {
        IrGenerationExtension.registerExtension(object : IrGenerationExtension {
            override fun generate(moduleFragment: IrModuleFragment, pluginContext: IrPluginContext) {
                val output = System.getenv("STDLIB_DOCS_CALLS") ?: return
                moduleFragment.files.forEach { file ->
                    val names = sortedSetOf<String>()
                    file.acceptChildrenVoid(object : IrVisitorVoid() {
                        override fun visitElement(element: IrElement) { element.acceptChildrenVoid(this) }
                        override fun visitSimpleFunction(declaration: IrSimpleFunction) {
                            if (declaration.name.asString() == "main" || declaration.parent !is IrFile) {
                                declaration.acceptChildrenVoid(this)
                            }
                        }
                        override fun visitCall(expression: IrCall) {
                            val visited=mutableSetOf<IrSimpleFunction>()
                            fun record(function: IrSimpleFunction) {
                                if (!visited.add(function)) return
                                val property = function.correspondingPropertySymbol?.owner
                                (property?.fqNameWhenAvailable ?: function.fqNameWhenAvailable)?.asString()?.let(names::add)
                                function.overriddenSymbols.forEach { record(it.owner) }
                            }
                            record(expression.symbol.owner)
                            expression.acceptChildrenVoid(this)
                        }
                        override fun visitConstructorCall(expression: IrConstructorCall) {
                            (expression.symbol.owner.parent as? IrClass)?.fqNameWhenAvailable?.asString()?.let {
                                names.add(it)
                                names.add("$it.constructor")
                            }
                            expression.acceptChildrenVoid(this)
                        }
                        override fun visitGetObjectValue(expression: IrGetObjectValue) {
                            expression.symbol.owner.fqNameWhenAvailable?.asString()?.let(names::add)
                        }
                        override fun visitGetEnumValue(expression: IrGetEnumValue) {
                            expression.symbol.owner.fqNameWhenAvailable?.asString()?.let(names::add)
                        }
                    })
                    val symbols = names.filter { it.startsWith("kotlin.") || it.startsWith("java.") }.joinToString(",") { "\"$it\"" }
                    File(output).appendText("{\"file\":\"${File(file.fileEntry.name).name}\",\"symbols\":[$symbols]}\n")
                }
            }
        })
    }
}
