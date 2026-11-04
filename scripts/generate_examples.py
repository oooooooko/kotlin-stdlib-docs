"""Create representative API calls from declared types, then compile and execute each candidate.

Only successful programs become documentation examples. Unsupported signatures and
non-JVM declarations remain visible as coverage gaps instead of fabricated examples.
"""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

from collect_api import ROOT

RECEIVERS = {
    "Any":"Any()", "Unit":"Unit", "Nothing":None, "Boolean":"true", "Char":"'A'",
    "Byte":"5.toByte()", "Short":"5.toShort()", "Int":"5", "Long":"5L", "Float":"5.5f", "Double":"5.5",
    "UByte":"5.toUByte()", "UShort":"5.toUShort()", "UInt":"5u", "ULong":"5uL", "Number":"5",
    "String":'"kotlin"', "CharSequence":'"kotlin"', "StringBuilder":'StringBuilder("kotlin")',
    "Array":"arrayOf(1, 2, 3)", "Iterable":"listOf(1, 2, 3)", "Collection":"listOf(1, 2, 3)", "List":"listOf(1, 2, 3)",
    "MutableIterable":"mutableListOf(1, 2, 3)", "MutableCollection":"mutableListOf(1, 2, 3)", "MutableList":"mutableListOf(1, 2, 3)",
    "ArrayList":"arrayListOf(1, 2, 3)", "ArrayDeque":"ArrayDeque(listOf(1, 2, 3))",
    "Set":"linkedSetOf(1, 2, 3)", "MutableSet":"linkedSetOf(1, 2, 3)", "HashSet":"hashSetOf(1, 2, 3)", "LinkedHashSet":"linkedSetOf(1, 2, 3)",
    "Map":'linkedMapOf("a" to 1, "b" to 2)', "MutableMap":'linkedMapOf("a" to 1, "b" to 2)', "HashMap":'hashMapOf("a" to 1)', "LinkedHashMap":'linkedMapOf("a" to 1)',
    "Map.Entry":'mapOf("a" to 1).entries.first()', "MutableMap.MutableEntry":'mutableMapOf("a" to 1).entries.first()',
    "Entry":'mapOf("a" to 1).entries.first()', "MutableEntry":'mutableMapOf("a" to 1).entries.first()',
    "Iterator":"listOf(1, 2, 3).iterator()", "MutableIterator":"mutableListOf(1, 2, 3).iterator()",
    "ListIterator":"listOf(1, 2, 3).listIterator()", "MutableListIterator":"mutableListOf(1, 2, 3).listIterator()",
    "Sequence":"sequenceOf(1, 2, 3)", "Grouping":"listOf(1, 2, 3).groupingBy { it % 2 }",
    "IntRange":"1..3", "LongRange":"1L..3L", "CharRange":"'a'..'c'", "UIntRange":"1u..3u", "ULongRange":"1uL..3uL",
    "IntProgression":"1..5 step 2", "LongProgression":"1L..5L step 2", "CharProgression":"'a'..'e' step 2",
    "UIntProgression":"1u..5u step 2", "ULongProgression":"1uL..5uL step 2", "ClosedRange":"1..3", "OpenEndRange":"1..<3",
    "Comparable":"5", "Comparator":"naturalOrder<Int>()", "Random":"Random(42)",
    "Pair":'Pair(1, "one")', "Triple":'Triple(1, "one", true)', "Result":"Result.success(42)", "Lazy":"lazy { 42 }",
    "Regex":'Regex("[a-z]+")', "MatchResult":'Regex("[a-z]+").find("hello 42")!!',
    "MatchGroup":'MatchGroup("hello", 0..4)', "MatchGroupCollection":'Regex("([a-z]+)").find("hello")!!.groups',
    "Duration":"2.seconds", "Instant":"Instant.fromEpochMilliseconds(0)", "TimeMark":"TimeSource.Monotonic.markNow()",
    "ComparableTimeMark":"TimeSource.Monotonic.markNow()", "ValueTimeMark":"TimeSource.Monotonic.markNow()",
    "TimeSource.Monotonic":"TimeSource.Monotonic", "Clock.System":"Clock.System",
    "Uuid":'Uuid.parse("550e8400-e29b-41d4-a716-446655440000")', "Uuid.Companion":"Uuid", "Base64":"Base64",
    "File":'File("sample.txt").apply { writeText("hello\\nworld") }',
    "Path":'java.nio.file.Files.writeString(java.nio.file.Path.of("sample.txt"), "hello\\nworld")',
    "ByteArrayInputStream":"java.io.ByteArrayInputStream(byteArrayOf(65, 66))", "InputStream":"java.io.ByteArrayInputStream(byteArrayOf(65, 66))",
    "OutputStream":"java.io.ByteArrayOutputStream()", "Reader":'java.io.StringReader("hello\\nworld")', "BufferedReader":'java.io.StringReader("hello\\nworld").buffered()',
    "Writer":"java.io.StringWriter()", "Closeable":'java.io.StringReader("hello")', "AutoCloseable":'AutoCloseable { println("closed") }',
    "CoroutineContext":"kotlin.coroutines.EmptyCoroutineContext", "EmptyCoroutineContext":"kotlin.coroutines.EmptyCoroutineContext",
    "Throwable":'IllegalArgumentException("example")', "Exception":'IllegalArgumentException("example")',
    "Enum":"Demo.FIRST", "EnumEntries":"Demo.entries", "KClass":"String::class", "KType":"typeOf<List<String>>()",
    "RandomAccess":"object : RandomAccess {}",
    "AbstractList":"object : AbstractList<Int>() { override val size = 3; override fun get(index: Int) = index + 1 }",
    "AbstractCollection":"object : AbstractCollection<Int>() { override val size = 3; override fun iterator() = listOf(1, 2, 3).iterator() }",
    "AbstractSet":"object : AbstractSet<Int>() { override val size = 3; override fun iterator() = setOf(1, 2, 3).iterator() }",
    "AbstractMap":'object : AbstractMap<String, Int>() { override val entries = mapOf("a" to 1).entries }',
    "AbstractMutableCollection":"object : AbstractMutableCollection<Int>() { private val data = mutableListOf(1, 2, 3); override val size get() = data.size; override fun add(element: Int) = data.add(element); override fun iterator() = data.iterator() }",
    "AbstractMutableList":"object : AbstractMutableList<Int>() { private val data = mutableListOf(1, 2, 3); override val size get() = data.size; override fun get(index: Int) = data[index]; override fun set(index: Int, element: Int) = data.set(index, element); override fun add(index: Int, element: Int) { data.add(index, element) }; override fun removeAt(index: Int) = data.removeAt(index) }",
    "AbstractMutableSet":"object : AbstractMutableSet<Int>() { private val data = mutableSetOf(1, 2, 3); override val size get() = data.size; override fun add(element: Int) = data.add(element); override fun iterator() = data.iterator() }",
    "AbstractMutableMap":'object : AbstractMutableMap<String, Int>() { private val data = mutableMapOf("a" to 1); override val entries get() = data.entries; override fun put(key: String, value: Int) = data.put(key, value) }',
    "AbstractIterator":"object : AbstractIterator<Int>() { override fun computeNext() { setNext(1) } }",
    "AtomicInt":"kotlin.concurrent.atomics.AtomicInt(1)", "AtomicLong":"kotlin.concurrent.atomics.AtomicLong(1L)", "AtomicReference":"kotlin.concurrent.atomics.AtomicReference(1)",
    "AtomicIntArray":"kotlin.concurrent.atomics.AtomicIntArray(3)", "AtomicLongArray":"kotlin.concurrent.atomics.AtomicLongArray(3)", "AtomicArray":"kotlin.concurrent.atomics.AtomicArray(arrayOf(1, 2, 3))",
    "KProperty":"::demoProperty", "KProperty0":"::demoProperty", "KMutableProperty":"::demoMutable", "KMutableProperty0":"::demoMutable",
    "KCallable":"::demoProperty", "KFunction":"::demoFunction", "KProperty.Getter":"::demoProperty.getter", "KProperty0.Getter":"::demoProperty.getter",
    "KMutableProperty.Setter":"::demoMutable.setter", "KMutableProperty0.Setter":"::demoMutable.setter",
    "ReadOnlyProperty":"kotlin.properties.ReadOnlyProperty<Any?, Int> { _, _ -> 42 }",
    "ReadWriteProperty":"object : kotlin.properties.ReadWriteProperty<Any?, Int> { private var data = 42; override fun getValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>) = data; override fun setValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>, value: Int) { data = value } }",
    "Function":"{ 42 }",
}
for arity in range(23):
    RECEIVERS[f"Function{arity}"] = "{ "+", ".join(f"p{i}: Int" for i in range(arity))+" -> 42 }" if arity else "{ 42 }"
for scalar, values in {"Boolean":"true, false, true", "Char":"'a', 'b', 'c'", "Byte":"1, 2, 3", "Short":"1, 2, 3", "Int":"1, 2, 3", "Long":"1L, 2L, 3L", "Float":"1f, 2f, 3f", "Double":"1.0, 2.0, 3.0", "UByte":"1u, 2u, 3u", "UShort":"1u, 2u, 3u", "UInt":"1u, 2u, 3u", "ULong":"1uL, 2uL, 3uL"}.items():
    RECEIVERS[scalar+"Array"] = scalar.lower()+"ArrayOf("+values+")"
    if not scalar.startswith("U"):
        RECEIVERS[scalar+"Iterator"] = RECEIVERS[scalar+"Array"]+".iterator()"
RECEIVERS.update({
    "KParameter":"::demoFunction.parameters.single()",
    "KTypeParameter":"DemoBox::class.typeParameters.single()",
    "KClassifier":"String::class",
    "KProperty1":"DemoBox<Int>::value", "KMutableProperty1":"DemoBox<Int>::value",
    "KProperty1.Getter":"(DemoBox<Int>::value).getter", "KMutableProperty1.Setter":"(DemoBox<Int>::value).setter",
})
for kind in ("Byte", "Short", "Int", "Long", "Float", "Double", "Char", "Boolean", "String", "Duration", "Instant"):
    RECEIVERS[kind+".Companion"] = kind

OPT_IN = "@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)"
IMPORTS = """import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
"""


def base(value):
    value = re.sub(r"@(?:[\w.]+)(?:\([^)]*\))?\s*", "", value or "")
    return re.sub(r"<.*", "", value).rstrip("?").removeprefix("kotlin.").removeprefix("java.io.").removeprefix("java.nio.file.")


def parameter(p, receiver, enums):
    typ = p["type"] or ""
    raw = base(typ)
    key = p["name"] or ""
    if p["optional"]:
        return None
    if "->" in typ:
        if "MutableList" in typ or "MutableSet" in typ:
            return "{ add(1); add(2) }"
        if "MutableMap" in typ:
            return '{ put("a", 1) }'
        if "StringBuilder." in typ:
            return '{ append("hello") }'
        if "SequenceScope" in typ:
            return "{ yield(1); yield(2) }"
        if key in {"predicate", "condition"}:
            return "{ it.toString().length > 0 }"
        if key == "action" or typ.rstrip().endswith("-> Unit"):
            return "{ println(it) }" if re.search(r"\([^)]*\w[^)]*\)\s*->", typ) else '{ println("called") }'
        if key in {"selector", "keySelector", "valueSelector"}:
            return "{ it.toString().length }"
        if key in {"transform", "valueTransform"}:
            if "Iterable<" in typ or "Sequence<" in typ:
                return "{ _, value -> listOf(value, value) }" if "," in typ.split("->",1)[0] else "{ listOf(it, it) }"
            if "," in typ.split("->",1)[0]:
                return '{ index, value -> "$index:$value" }'
            return "{ it.toString() }"
        arguments = typ.split("->",1)[0]
        if "," in arguments:
            return "{ a, _ -> a }"
        if "()" in arguments or ".()" in arguments:
            return "{ 42 }"
        return "{ it }"
    if "Comparator" in typ:
        return "naturalOrder()"
    if raw in enums:
        return enums[raw]
    if raw in {"Int", "Long", "Short", "Byte", "UInt", "ULong", "UShort", "UByte", "Float", "Double"}:
        number = "0" if any(part in key.lower() for part in ("index", "offset")) and key.lower() not in {"endindex", "toindex", "lastindex"} else "2"
        suffix = {"Long":"L", "UInt":"u", "ULong":"uL", "Float":"f", "Double":".0"}.get(raw, "")
        if raw in {"UShort", "UByte", "Short", "Byte"}:
            return number+".to"+raw+"()"
        return number+suffix
    if raw == "Boolean":
        return "false"
    if raw == "Char":
        return "'o'"
    if raw in {"String", "CharSequence"}:
        return '"AQID"' if key in {"source", "input"} else '"o"'
    if raw in {"T", "E", "R", "V", "S", "Comparable"} or re.fullmatch(r"P\d+",raw):
        return "1"
    if raw == "K":
        return '"a"'
    if raw in {"Any", "Object"}:
        return "1"
    if raw == "KClass":
        return "String::class"
    if raw.startswith("KProperty"):
        return "::demoProperty"
    if raw in {"T","E"} and receiver.startswith(("KProperty1","KMutableProperty1")):
        return "DemoBox(42)"
    if raw=="Map" and "KParameter" in typ:
        return "mapOf(source.parameters.single() to 1)" if receiver=="KFunction" else "emptyMap()"
    if raw == "File":
        return 'File("destination.txt")'
    if raw == "Path":
        return 'java.nio.file.Path.of("destination.txt")'
    if raw in {"Appendable", "StringBuilder"}:
        return "StringBuilder()"
    if raw in {"Iterable", "Collection", "List", "Set", "Sequence", "Array"} or raw.endswith("Array"):
        if "Pair<" in typ:
            return {"Array":"arrayOf", "Sequence":"sequenceOf"}.get(raw,"listOf")+'("c" to 3, "d" to 4)'
        return RECEIVERS.get(raw)
    if raw in RECEIVERS:
        return RECEIVERS[raw]
    if raw.endswith("Exception") or raw == "Throwable":
        return 'IllegalArgumentException("example")'
    if typ.endswith("?"):
        return "null"
    return None


def candidate(group, declaration, enums, class_receivers):
    owner, symbol, pkg = group["owner"], group["name"], group["package"]
    receiver = declaration.get("receiver") or owner
    if receiver and receiver not in RECEIVERS:
        receiver = base(receiver)
    receiver_code = RECEIVERS.get(receiver) or enums.get(receiver) or class_receivers.get(pkg+"."+receiver)
    kind = declaration["kind"]
    if symbol.startswith("to") and symbol.endswith("Array") and receiver_code and receiver in {"Collection","List","Iterable"}:
        scalar=symbol[2:-5]
        if scalar in {"Byte","Short","Float","Double","Char","Boolean","UByte","UShort","UInt","ULong","Int","Long"}:
            primitive=RECEIVERS.get(scalar+"Array")
            receiver_code=primitive+".toList()" if primitive else receiver_code
    if kind == "enum_entry":
        expression = pkg+"."+owner+"."+symbol
        return OPT_IN+"\n\nfun main() {\n    val value = "+expression+"\n    println(value)\n}\n"
    if kind in {"class_declaration", "object_declaration", "type_alias"}:
        code = RECEIVERS.get(".".join(filter(None,(owner,symbol)))) or class_receivers.get(pkg+"."+".".join(filter(None,(owner,symbol))))
        if kind=="object_declaration":
            code=pkg+"."+".".join(filter(None,(owner,symbol)))
        if not code:
            code = enums.get(symbol)
        if not code:
            return None
        body = "    val value = "+code+"\n    println(value"+(".next()" if symbol.endswith("Iterator") else "")+")\n"
    elif kind=="secondary_constructor":
        code=RECEIVERS.get(owner) or class_receivers.get(pkg+"."+owner)
        if not code:
            return None
        body="    val value = "+code+"\n    println(value)\n"
    elif kind in {"property_declaration", "function_declaration"}:
        if receiver and not receiver_code:
            return None
        if receiver_code and base(receiver) in {"String", "CharSequence"} and symbol.startswith(("toInt", "toLong", "toDouble", "toFloat", "toShort", "toByte", "toUInt", "toULong", "toUByte", "toUShort")):
            receiver_code = '"42"'
        args = []
        for p in declaration.get("parameters",[]):
            if p["optional"]:
                continue
            argument = parameter(p,receiver,enums)
            if argument is None:
                return None
            args.append(argument)
        call = ("source." if receiver_code else "")+"`"+symbol+"`"+("("+", ".join(args)+")" if kind == "function_declaration" else "")
        if declaration.get("visibility")=="protected":
            if not receiver_code or not receiver_code.endswith("}"):
                return None
            exposed="`"+symbol+"`"+("("+", ".join(args)+")" if kind=="function_declaration" else "")
            receiver_code=receiver_code[:-1]+"; fun demonstrate() = "+exposed+" }"
            call="source.demonstrate()"
        body = ("    val source = "+receiver_code+"\n" if receiver_code else "")+"    val result = "+call+"\n"
        result_type = declaration.get("return_type") or ""
        if base(result_type).endswith("Array"):
            body += "    println(result.contentToString())\n"
        elif base(result_type) == "Sequence":
            body += "    println(result.toList())\n"
        elif base(result_type) in {"Iterator", "ListIterator"}:
            body += "    println(result.asSequence().toList())\n"
        else:
            body += "    println(result)\n"
        if result_type == "Unit" and receiver_code and base(receiver) in {"MutableList", "ArrayList", "MutableSet", "MutableMap", "StringBuilder"}:
            body += "    println(source)\n"
    else:
        return None
    prelude = IMPORTS+"import "+pkg+".*\n"
    if "Demo" in body:
        prelude += "\nenum class Demo { FIRST, SECOND }\n"
    if "demoProperty" in body or "demoMutable" in body or "demoFunction" in body:
        prelude += "\nval demoProperty = 42\nvar demoMutable = 42\nfun demoFunction(value: Int): Int = value + 1\n"
    if "DemoBox" in body:
        prelude += "\nclass DemoBox<T>(var value: T)\n"
    return OPT_IN+"\n\n"+prelude+"\nfun main() {\n"+body+"}\n"


def generate():
    api = json.loads((ROOT/"data/api.json").read_text())
    official = json.loads((ROOT/"data/examples.json").read_text())
    enums = {}
    for group in api["groups"]:
        if any(d["kind"]=="enum_entry" and d["platform"] in {"JVM","Common"} for d in group["declarations"]):
            enums.setdefault(group["owner"],group["package"]+"."+group["owner"]+"."+group["name"])
    class_receivers={}
    for group in api["groups"]:
        for d in group["declarations"]:
            if d["kind"] not in {"class_declaration","object_declaration","type_alias"} or d["platform"] not in {"Common","JVM"}:
                continue
            qualified=group["key"].replace("/",".")
            if d["kind"]=="object_declaration":
                class_receivers[qualified]=qualified
                continue
            if re.search(r"\b(?:abstract|interface|enum|sealed)\b",d["signature"]):
                continue
            if d["kind"]=="type_alias" and "java.lang." not in d["signature"]:
                continue
            arguments=[]
            for p in d.get("parameters",[]):
                if p["optional"]:
                    continue
                value=parameter(p,"",enums)
                if value is None:
                    break
                arguments.append(value)
            else:
                generics=re.search(r"\bclass\s+\w+\s*<([^>]+)>",d["signature"])
                type_args="<"+", ".join("Int" for _ in generics[1].split(","))+">" if generics else ""
                class_receivers[qualified]=qualified+type_args+"("+", ".join(arguments)+")"
                break
    candidates = []
    destination=ROOT/"data/generated-examples.json"
    previous=json.loads(destination.read_text()) if destination.exists() else {}
    verified={}
    for group in api["groups"]:
        if any(s in official for d in group["declarations"] for s in d["samples"]):
            continue
        for declaration in sorted(group["declarations"],key=lambda d:d["platform"]!="Common"):
            if declaration["platform"] not in {"JVM","Common"}:
                continue
            code = candidate(group,declaration,enums,class_receivers)
            if code:
                dependencies=["kotlin-reflect:2.4.21"] if group["package"]=="kotlin.reflect" else []
                old=previous.get(group["key"])
                if old and old["code"]==code and old.get("dependencies",[])==dependencies:
                    verified[group["key"]]=old
                else:
                    candidates.append((group["key"],code,dependencies))
                break
    work = ROOT/".tools/generated-examples"
    work.mkdir(exist_ok=True)
    lib = ROOT/".tools/maven-kotlinc/lib"
    classpath = str(lib/"kotlin-stdlib.jar")
    compiler = ROOT/".tools/maven-kotlinc/bin/kotlinc"
    failures = {}
    print(f"Generated candidates: {len(candidates)}",flush=True)
    for offset in range(0,len(candidates),160):
        batch = {}
        for key,code,dependencies in candidates[offset:offset+160]:
            ident = "g"+hashlib.sha256(key.encode()).hexdigest()[:12]
            path = work/(ident+".kt")
            annotated,rest=code.split("\n",1)
            path.write_text(annotated+"\npackage generated."+ident+"\n"+rest)
            batch[key] = (ident,path,code,dependencies)
        classes = work/f"classes-{offset}"
        while batch:
            result = subprocess.run([str(compiler),"-nowarn","-no-stdlib","-no-reflect","-classpath",classpath,"-d",str(classes),*(str(v[1]) for v in batch.values())],capture_output=True,text=True,timeout=120)
            if not result.returncode:
                break
            errors=result.stderr+result.stdout
            bad = [key for key,(_,path,_,_) in batch.items() if path.name+":" in errors]
            if not bad:
                raise RuntimeError(errors[:5000])
            for key in bad:
                failures[key] = "Compilation failed"
                del batch[key]

        def run(item):
            key,(ident,path,code,dependencies)=item
            runtime_classpath=classpath+(":"+str(ROOT/".tools/kotlin-reflect-2.4.21.jar") if dependencies else "")
            command=["java","-Dfile.encoding=UTF-8","-cp",str(classes)+":"+runtime_classpath,"generated."+ident+"."+ident.capitalize()+"Kt"]
            try:
                with tempfile.TemporaryDirectory(prefix="stdlib-api-") as cwd:
                    a=subprocess.run(command,cwd=cwd,capture_output=True,text=True,timeout=8)
                    if a.returncode or not a.stdout:
                        return key,None
                    b=subprocess.run(command,cwd=cwd,capture_output=True,text=True,timeout=8)
                    if b.returncode:
                        return key,None
                    return key,{"code":code,"output":a.stdout,"deterministic":a.stdout==b.stdout,"verified_version":"2.4.21","platform":"JVM","dependencies":dependencies}
            except subprocess.TimeoutExpired:
                return key,None
        with ThreadPoolExecutor(max_workers=8) as pool:
            for key,value in pool.map(run,batch.items()):
                if value:
                    verified[key]=value
                else:
                    failures[key]="Execution failed"
        (ROOT/"data/generated-examples.json").write_text(json.dumps(verified,ensure_ascii=False,indent=2)+"\n")
        print(f"Generated {min(offset+160,len(candidates))}/{len(candidates)}: {len(verified)} verified",flush=True)
    (ROOT/"data/generated-example-report.json").write_text(json.dumps({"candidates":len(candidates),"verified":len(verified),"failures":failures},ensure_ascii=False,indent=2)+"\n")


if __name__ == "__main__":
    generate()
