"""Use Kotlin IR to index real resolved API references in verified example programs."""

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from zipfile import ZipFile

from collect_api import ROOT


def main():
    lib=ROOT/".tools/maven-kotlinc/lib"
    compiler=ROOT/".tools/maven-kotlinc/bin/kotlinc"
    plugin=ROOT/".tools/calls-plugin.jar"
    subprocess.run([str(compiler),str(ROOT/"scripts/ExampleCalls.kt"),"-no-stdlib","-classpath",str(lib/"kotlin-stdlib.jar")+":"+str(lib/"kotlin-compiler.jar"),"-d",str(plugin)],check=True)
    with ZipFile(plugin,"a") as jar:
        jar.writestr("META-INF/services/org.jetbrains.kotlin.compiler.plugin.CompilerPluginRegistrar","ExampleCallsPlugin\n")
    registry={}
    for namespace,filename,prefix in [("official","examples.json","s"),("generated","generated-examples.json","g"),("tests","test-examples.json","t")]:
        if not (ROOT/"data"/filename).exists():
            continue
        for key,entry in json.loads((ROOT/"data"/filename).read_text()).items():
            ident=prefix+hashlib.sha256(key.encode()).hexdigest()[:12]
            registry[ident+".kt"]=(namespace+":"+key,entry)
    work=ROOT/".tools/call-index"
    work.mkdir(exist_ok=True)
    output=work/"calls.jsonl"
    plugin_digest=hashlib.sha256((ROOT/"scripts/ExampleCalls.kt").read_bytes()).hexdigest()
    marker=work/"plugin.sha256"
    compatible=marker.exists() and marker.read_text()==plugin_digest
    previous_records={row["file"]:row for row in (json.loads(line) for line in output.read_text().splitlines())} if output.exists() and compatible else {}
    if not compatible:
        output.write_text("")
    paths=[]
    for filename,(key,entry) in registry.items():
        annotation,rest=entry["code"].split("\n",1)
        path=work/filename
        value=annotation+"\npackage indexed."+path.stem+"\n"+rest
        if path.name not in previous_records or not path.exists() or path.read_text()!=value:
            path.write_text(value)
            paths.append(path)
    if not output.exists():
        output.write_text("")
    classpath=":".join(str(lib/name) for name in ("kotlin-stdlib.jar","kotlin-test.jar","kotlin-reflect-1.6.10.jar"))
    for offset in range(0,len(paths),100):
        command=[str(compiler),"-nowarn","-no-stdlib","-no-reflect","-classpath",classpath,"-Xplugin="+str(plugin),"-d",str(work/f"batch-{offset}"),*(str(p) for p in paths[offset:offset+100])]
        result=subprocess.run(command,capture_output=True,text=True,env={**os.environ,"STDLIB_DOCS_CALLS":str(output)},timeout=180)
        if result.returncode:
            raise RuntimeError(result.stdout+result.stderr)
        print(f"Indexed {min(offset+100,len(paths))}/{len(paths)} programs",flush=True)
    api=json.loads((ROOT/"data/api.json").read_text())
    keys={g["key"].replace("/","."):g["key"] for g in api["groups"]}
    aliases={}
    for group in api["groups"]:
        for declaration in group["declarations"]:
            if declaration["kind"]=="type_alias":
                target=re.search(r"=\s*(java\.[\w.]+)",declaration["signature"])
                if target:
                    aliases[target[1]]=group["key"].replace("/",".")
    references={}
    records={row["file"]:row for row in (json.loads(line) for line in output.read_text().splitlines())}
    for row in records.values():
        if row["file"] not in registry:
            continue
        program,entry=registry[row["file"]]
        for symbol in row["symbols"]:
            variants=[symbol]
            for original,alias in aliases.items():
                if symbol==original or symbol.startswith(original+"."):
                    variants.append(alias+symbol[len(original):])
            for variant in variants:
                if variant in keys:
                    references.setdefault(keys[variant],set()).add(program)
    programs_by_id={ident:entry for ident,entry in registry.values()}
    result={key:sorted(programs,key=lambda p:len(programs_by_id[p]["code"]))[:3] for key,programs in references.items()}
    (ROOT/"data/example-api-index.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    marker.write_text(plugin_digest)
    print(f"Resolved example references for {len(result)} API entries.")


if __name__=="__main__":
    main()
