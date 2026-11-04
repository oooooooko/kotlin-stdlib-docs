"""Convert the pinned official samples into standalone programs and record actual JVM output."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import textwrap

from collect_api import PARSER, ROOT, SOURCE, children, name, text


def transformed(node):
    replacements = []

    def visit(current):
        if current.type == "call_expression":
            callee = text(current.named_children[0]) if current.named_children else ""
            arguments_node = next(iter(children(current, "value_arguments")), None)
            arguments = arguments_node.named_children if arguments_node else []
            args = [re.sub(r"^[A-Za-z_]\w*\s*=\s*(?!=)", "", text(a)) for a in arguments]
            replacement = None
            if callee in {"assertPrints", "assertTrue", "assertFalse", "assertNull"} and args:
                replacement = f"println({args[0]})"
            elif callee in {"assertEquals", "assertSame", "assertNotSame", "assertContentEquals"} and len(args) >= 2:
                if callee == "assertSame":
                    replacement = f"println({args[0]} === {args[1]})"
                elif callee == "assertNotSame":
                    replacement = f"println({args[0]} !== {args[1]})"
                elif callee == "assertContentEquals":
                    replacement = f"println(({args[1]}).contentToString())"
                else:
                    replacement = f"println({args[1]})"
            elif callee == "assertNotNull" and args:
                replacement = f"println(checkNotNull({args[0]}))"
            if replacement:
                # Only replace the outer assertion; its nested expression is preserved verbatim.
                replacements.append((current.start_byte-node.start_byte, current.end_byte-node.start_byte, replacement.encode()))
                return
        for child in current.named_children:
            visit(child)

    visit(node)
    value = node.text
    for start, end, replacement in sorted(replacements, reverse=True):
        value = value[:start] + replacement + value[end:]
    return value.decode()


def extract():
    result = {}
    for file in sorted((SOURCE / "libraries/stdlib/samples/test/samples").rglob("*.kt")):
        root = PARSER.parse(file.read_bytes()).root_node
        package = text(next(iter(children(root, "package_header")), None)).removeprefix("package ").strip()
        imports = [text(n) for n in children(root, "import") if not text(n).startswith(("import samples.", "import org.junit."))]

        def walk(container, owners=(), inherited_helpers=()):
            declarations = [n for n in container.named_children if n.type in {"function_declaration", "property_declaration", "class_declaration", "object_declaration"}]
            helpers = list(inherited_helpers)
            for n in declarations:
                if "@Sample" not in text(n) and n.type != "class_declaration":
                    helpers.append(transformed(n))
                elif n.type == "class_declaration" and "@Sample" not in text(n):
                    helpers.append(text(n))
            for n in declarations:
                if n.type == "function_declaration" and re.search(r"@Sample\b", text(n).split("fun ", 1)[0]):
                    body = next(iter(children(n, "function_body")), None)
                    if not body or not text(body).startswith("{"):
                        continue
                    key = ".".join((package, *owners, name(n)))
                    body_text = textwrap.dedent(transformed(body)[1:-1]).strip()
                    prelude = "\n".join(dict.fromkeys(imports))
                    helper_text = "\n\n".join(dict.fromkeys(helpers))
                    code = (prelude + "\n\n" + helper_text + "\n\nfun main() {\n" + textwrap.indent(body_text, "    ") + "\n}\n").strip()+"\n"
                    # Use positional destructuring supported by the 2.4.21 compiler.
                    code = re.sub(r"\[([A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)+)\]", r"(\1)", code)
                    if not re.search(r"\bassert[A-Z]", code):
                        code = re.sub(r"^import kotlin\.test\..*\n", "", code, flags=re.MULTILINE).lstrip()
                    result[key] = {"source":str(file.relative_to(SOURCE)), "line":n.start_point.row+1, "code":code}
                elif n.type in {"class_declaration", "object_declaration"}:
                    for body in n.named_children:
                        if body.type in {"class_body", "enum_class_body"}:
                            walk(body, (*owners, name(n)), tuple(helpers))
        walk(root)
    return result


def extract_tests():
    paths=[]
    for directory in ("test","common/test","jvm/test","jdk7/test","jdk8/test"):
        paths.extend(sorted((SOURCE/"libraries/stdlib"/directory).rglob("*.kt")))
    parsed=subprocess.run(["java","-Xmx3g","-cp",str(ROOT/".tools/collector.jar")+":"+str(ROOT/".tools/maven-kotlinc/lib/*"),"ExtractApiKt",str(SOURCE),"--tests"],input="\n".join(str(p.relative_to(SOURCE)) for p in paths)+"\n",capture_output=True,text=True,check=True,timeout=120)
    coverage=json.loads((ROOT/"data/coverage.json").read_text())
    wanted={key.rsplit(".",1)[-1].split("/")[-1] for key in coverage["missing_examples"]}
    result={}
    forbidden=re.compile(r"getenv\s*\(|getProperties\s*\(|user\.home|ProcessBuilder|Runtime\.getRuntime|\.exec\s*\(|System\.exit")
    for line in parsed.stdout.splitlines():
        sample=json.loads(line)
        if forbidden.search(sample["code"]):
            continue
        if not any(re.search(r"\b"+re.escape(symbol)+r"\b",sample["code"]) for symbol in wanted):
            continue
        replacements=[]
        for call in sorted(sample["assertions"],key=lambda c:(c["start"],-c["end"])):
            if any(start<=call["start"]<end for start,end,_ in replacements):
                continue
            callee,args=call["callee"],call["arguments"]
            replacement=None
            if callee in {"assertPrints","assertTrue","assertFalse","assertNull"} and args:
                replacement=f"println({args[0]})"
            elif callee=="assertEquals" and len(args)>=2:
                replacement=f"println({args[1]})"
            elif callee in {"assertSame","assertNotSame"} and len(args)>=2:
                replacement=f"println({args[0]} {'===' if callee=='assertSame' else '!=='} {args[1]})"
            if replacement:
                replacements.append((call["start"],call["end"],replacement))
        raw=sample["code"].encode("utf-16-le")
        for start,end,replacement in sorted(replacements,reverse=True):
            raw=raw[:start*2]+replacement.encode("utf-16-le")+raw[end*2:]
        code=raw.decode("utf-16-le")
        code=re.sub(r"\[([A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)+)\]",r"(\1)",code)
        if "assertPrints" in code:
            continue
        result[sample["key"]]={"source":sample["source"],"line":sample["line"],"code":code}
    print(f"Selected {len(result)} test-derived programs",flush=True)
    return result


def prepare(compiler, batch_size, test_mode=False):
    examples = extract_tests() if test_mode else extract()
    work = ROOT / (".tools/test-examples" if test_mode else ".tools/examples")
    work.mkdir(exist_ok=True)
    api = json.loads((ROOT / "data/api.json").read_text())
    referenced = {s for g in api["groups"] for d in g["declarations"] for s in d["samples"]}
    selected = examples if test_mode else {key:value for key,value in examples.items() if key in referenced}
    for index, (key, entry) in enumerate(sorted(selected.items())):
        ident = ("t" if test_mode else "s")+hashlib.sha256(key.encode()).hexdigest()[:12]
        entry["id"] = ident
        entry["file"] = str(work / (ident+".kt"))
        opt_in = "@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)\n"
        entry["code"] = opt_in + entry["code"]
        code = opt_in + "package generated."+ident+"\n\n"+entry["code"][len(opt_in):]
        Path(entry["file"]).write_text(code)
    lib = ROOT / ".tools/maven-kotlinc/lib"
    classpath = ":".join(str(lib / n) for n in ["kotlin-stdlib.jar", "kotlin-test.jar"])+":"+str(ROOT/".tools/kotlin-reflect-2.4.21.jar")
    entries = list(selected.items())
    compile_failures = {}
    runtime_failures = {}
    passed = {}
    for offset in range(0, len(entries), batch_size):
        batch = dict(entries[offset:offset+batch_size])
        classes = work / f"classes-{offset}"
        classes.mkdir(exist_ok=True)
        while batch:
            command = [str(compiler), "-nowarn", "-no-stdlib", "-no-reflect", "-classpath", classpath, "-d", str(classes), *(v["file"] for v in batch.values())]
            compiled = subprocess.run(command, capture_output=True, text=True, timeout=120)
            if compiled.returncode == 0:
                break
            messages = compiled.stdout + compiled.stderr
            bad = {key for key,entry in batch.items() if Path(entry["file"]).name+":" in messages}
            if not bad:
                raise RuntimeError(messages[:10000])
            for key in bad:
                filename = Path(batch[key]["file"]).name
                compile_failures[key] = "\n".join(line for line in messages.splitlines() if filename+":" in line)[:1800]
                del batch[key]

        def run(item):
            key, entry = item
            try:
                with tempfile.TemporaryDirectory(prefix="stdlib-docs-") as cwd:
                    command = ["java", "-Dfile.encoding=UTF-8", "-cp", str(classes)+":"+classpath, "generated."+entry["id"]+"."+entry["id"].capitalize()+"Kt"]
                    if test_mode:
                        profile=f'(version 1) (allow default) (deny network*) (deny file-write*) (allow file-write* (subpath "{cwd}") (subpath "/private/tmp") (subpath "/tmp")) (deny file-read* (subpath "{Path.home()}")) (allow file-read-metadata) (allow file-read* (subpath "{ROOT / ".tools"}"))'
                        command=["sandbox-exec","-p",profile,*command]
                    environment={key:os.environ[key] for key in ("PATH","JAVA_HOME","LANG","LC_ALL") if key in os.environ}
                    environment.update({"TMPDIR":cwd,"TZ":"UTC"})
                    first = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, text=True, timeout=10)
                    if first.returncode:
                        return key, None, first.stderr[-1500:]
                    second = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, text=True, timeout=10)
                    if second.returncode:
                        return key, None, second.stderr[-1500:]
                    return key, {"source":entry["source"], "line":entry["line"], "code":entry["code"], "output":first.stdout, "deterministic":first.stdout==second.stdout, "platform":"JVM", "verified_version":"2.4.21"}, None
            except subprocess.TimeoutExpired:
                return key, None, "Execution exceeded 10 seconds."
        with ThreadPoolExecutor(max_workers=4) as pool:
            for key, value, error in pool.map(run, batch.items()):
                if value:
                    passed[key] = value
                else:
                    runtime_failures[key] = error
        print(f"Samples {min(offset+batch_size,len(entries))}/{len(entries)}: {len(passed)} verified", flush=True)
        (ROOT / ("data/test-examples.json" if test_mode else "data/examples.json")).write_text(json.dumps(passed, ensure_ascii=False, indent=2)+"\n")
    report = {"available":len(examples), "referenced":len(referenced), "selected":len(selected), "verified":len(passed), "missing_sample_sources":sorted(referenced-examples.keys()), "compile_failures":compile_failures, "runtime_failures":runtime_failures}
    (ROOT / ("data/test-example-report.json" if test_mode else "data/example-report.json")).write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({key:val for key,val in report.items() if isinstance(val,int)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kotlinc", default=str(ROOT/".tools/maven-kotlinc/bin/kotlinc"))
    parser.add_argument("--batch-size", default=80, type=int)
    parser.add_argument("--tests",action="store_true")
    options = parser.parse_args()
    prepare(Path(options.kotlinc).resolve(), options.batch_size, options.tests)
