"""Extract public declarations and official samples from the pinned Kotlin source tree."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

from tree_sitter import Language, Parser
import tree_sitter_kotlin

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".tools/kotlin-source"
VERSION = "2.4.21"
PLATFORM_PACKAGES = ("kotlin.jvm", "kotlin.js", "kotlin.native", "kotlin.wasm", "org.w3c")
PARSER = Parser(Language(tree_sitter_kotlin.language()))
KINDS = {"class_declaration", "object_declaration", "function_declaration", "property_declaration", "type_alias", "secondary_constructor", "enum_entry"}


def text(node):
    return node.text.decode("utf-8") if node else ""


def children(node, kind):
    return [n for n in node.named_children if n.type == kind]


def name(node):
    found = node.child_by_field_name("name")
    if not found:
        variable = next(iter(children(node, "variable_declaration")), None)
        found = variable.child_by_field_name("name") if variable else None
        if variable and not found:
            found = next(iter(children(variable, "identifier")), None)
    if not found:
        found = next(iter(children(node, "identifier")), None)
    return text(found).strip("`") or ("constructor" if node.type == "secondary_constructor" else "Companion" if "companion object" in text(node)[:100] else "")


def slug(key):
    return re.sub(r"[^a-z0-9-]+", "-", key.lower()).strip("-")[:100] + "--" + hashlib.sha256(key.encode()).hexdigest()[:8]


def doc_before(node):
    previous = node.prev_named_sibling
    return text(previous) if previous and previous.type == "block_comment" and text(previous).startswith("/**") else ""


def clean_doc(value):
    value = re.sub(r"^/\*\*|\*/$", "", value.strip())
    return "\n".join(re.sub(r"^\s*\* ?", "", line) for line in value.splitlines()).strip()


def signature(node):
    stop = next((n.start_byte for n in node.children if n.type in {"class_body", "enum_class_body", "function_body", "getter", "setter"} or n.type == "="), node.end_byte)
    value = node.text[:stop-node.start_byte].decode().strip()
    # Keep source annotations (including opt-in and deprecation requirements).
    return value.rstrip("{ ").strip()


def platform(path):
    p = str(path)
    if p.startswith("kotlin-native/"):
        return "Native"
    for part, label in [("/jvm/", "JVM"), ("/jdk7/", "JVM"), ("/jdk8/", "JVM"), ("/js/", "JS"), ("/wasm/", "Wasm"), ("/native-wasm/", "Native / Wasm"), ("/common-js-wasmjs/", "JS / Wasm-JS"), ("/common-non-jvm/", "JS / Native / Wasm")]:
        if part in p:
            return label
    return "Common"


def common_groups(groups):
    """Keep Common declarations, excluding optional platform annotation families."""
    def available(declaration):
        version = tuple(map(int, VERSION.split(".")))
        if any(tuple(map(int, since.split("."))) > version for since in declaration.get("since", [])):
            return False
        hidden = re.search(r'hiddenSince\s*=\s*"([\d.]+)"', declaration["signature"])
        return not hidden or tuple(map(int, hidden[1].split("."))) > version
    optional = {g["key"] for g in groups if any(
        d["platform"] == "Common" and "@OptionalExpectation" in d["signature"]
        for d in g["declarations"]
    )}
    unavailable_types = {g["key"] for g in groups if any(d["kind"] == "class_declaration" for d in g["declarations"]) and not any(d["platform"] == "Common" and available(d) for d in g["declarations"])}
    result = []
    for group in groups:
        if any(group["package"] == p or group["package"].startswith(p + ".") for p in PLATFORM_PACKAGES):
            continue
        if any(group["key"] == key or group["key"].startswith(key + ".") for key in optional):
            continue
        if any(group["key"] == key or group["key"].startswith(key + ".") for key in unavailable_types):
            continue
        declarations = [d for d in group["declarations"] if d["platform"] == "Common" and available(d)]
        if declarations:
            result.append({**group, "declarations": declarations})
    return result


def sources():
    stdlib = SOURCE / "libraries/stdlib"
    selected = {}
    for path in stdlib.rglob("*.kt"):
        relative = path.relative_to(stdlib)
        parts = set(relative.parts)
        if parts & {"test", "tests", "testData", "samples", "benchmarks", "jklib-for-test", "jvm-minimal-for-test", "js-ir-minimal-for-test"}:
            continue
        if not (parts & {"src", "runtime", "builtins", "generated", "wasi", "stubs", "internal"}):
            continue
        # Match the source exclusions in the pinned stdlib build.gradle.kts.
        # Legacy DOM/browser declarations belong to kotlin-dom-api-compat.
        if any(str(relative).startswith(prefix) for prefix in ("js/src/kotlin/browser/", "js/src/kotlin/dom/", "js/src/kotlinx/", "js/src/org.w3c/")):
            continue
        source_path=str(path.relative_to(SOURCE))
        if platform(source_path)=="Common":
            selected[source_path] = path
    return sorted(selected.items())


def collect():
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=SOURCE, text=True).strip()
    tag_commit = subprocess.check_output(["git", "rev-parse", f"v{VERSION}^{{commit}}"], cwd=SOURCE, text=True).strip()
    if commit != tag_commit:
        raise SystemExit(f"Checkout does not match v{VERSION}")
    groups = {}
    files = sources()
    toolchain = ROOT / ".tools/maven-kotlinc"
    collector = ROOT / ".tools/collector.jar"
    kotlin_file = ROOT / "scripts/ExtractApi.kt"
    if not collector.exists() or collector.stat().st_mtime < kotlin_file.stat().st_mtime:
        subprocess.run([str(toolchain / "bin/kotlinc"), str(kotlin_file), "-no-stdlib", "-classpath", str(toolchain/"lib/kotlin-stdlib.jar")+":"+str(toolchain/"lib/kotlin-compiler.jar"), "-d", str(collector)], check=True)
    extracted = subprocess.run(["java", "-Xmx2g", "-cp", str(collector)+":"+str(toolchain/"lib/*"), "ExtractApiKt", str(SOURCE)], input="\n".join(p for p,_ in files)+"\n", capture_output=True, text=True, check=True)
    parse_errors = [line for line in extracted.stderr.splitlines() if line.startswith("PARSE ")]
    if parse_errors:
        raise RuntimeError("Kotlin parser errors:\n"+"\n".join(parse_errors))
    for line in extracted.stdout.splitlines():
        declaration = json.loads(line)
        package, owner, symbol = (declaration.pop(k) for k in ("package", "owner", "name"))
        qualified_name = ".".join(filter(None, (owner, symbol)))
        key = package + "/" + qualified_name
        group = groups.setdefault(key, {"key":key,"package":package,"owner":owner,"name":symbol,"path":f"api/{package}/{slug(qualified_name)}.md","declarations":[]})
        declaration["platform"] = platform(declaration["source"])
        declaration["kdoc"] = clean_doc(declaration["kdoc"])
        group["declarations"].append(declaration)
    result = {"version": VERSION, "scope": "Common", "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=SOURCE, text=True).strip(), "source_files": len(files), "parse_errors": parse_errors, "groups": common_groups(sorted(groups.values(), key=lambda g:g["key"]))}
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data/api.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"scope":"Common","groups":len(result["groups"]), "declarations":sum(len(g['declarations']) for g in result["groups"]),"parse_errors":len(parse_errors),"files":len(files)}))


if __name__ == "__main__":
    collect()
