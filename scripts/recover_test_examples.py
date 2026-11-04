"""Run already compiled test-derived programs inside a restricted macOS sandbox."""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

from collect_api import ROOT
from prepare_examples import extract_tests


def main():
    samples=extract_tests()
    classes={p.parent.name:p.parents[2] for p in (ROOT/".tools/test-examples").glob("classes-*/generated/t*/T*Kt.class")}
    libs=ROOT/".tools/maven-kotlinc/lib"
    classpath=":".join(str(libs/p) for p in ("kotlin-stdlib.jar","kotlin-test.jar"))+":"+str(ROOT/".tools/kotlin-reflect-2.4.21.jar")
    tasks=[]
    for key,entry in samples.items():
        ident="t"+hashlib.sha256(key.encode()).hexdigest()[:12]
        if ident in classes:
            source=(ROOT/".tools/test-examples"/(ident+".kt")).read_text()
            annotation,_,rest=source.split("\n",2)
            entry["code"]=annotation+"\n"+rest
            tasks.append((key,ident,entry))
    print(f"Reusing {len(tasks)} compiled test programs",flush=True)
    def run(task):
        key,ident,entry=task
        try:
            with tempfile.TemporaryDirectory(prefix="stdlib-test-") as cwd:
                profile=f'(version 1) (allow default) (deny network*) (deny file-write*) (allow file-write* (subpath "{cwd}") (subpath "/private/tmp") (subpath "/tmp")) (deny file-read* (subpath "{Path.home()}")) (allow file-read-metadata) (allow file-read* (subpath "{ROOT / ".tools"}"))'
                command=["sandbox-exec","-p",profile,"java","-Dfile.encoding=UTF-8","-cp",str(classes[ident])+":"+classpath,"generated."+ident+"."+ident.capitalize()+"Kt"]
                env={key:os.environ[key] for key in ("PATH","JAVA_HOME","LANG") if key in os.environ}
                env.update({"TMPDIR":cwd,"TZ":"UTC"})
                a=subprocess.run(command,cwd=cwd,env=env,capture_output=True,text=True,timeout=4)
                if a.returncode:
                    return key,None
                b=subprocess.run(command,cwd=cwd,env=env,capture_output=True,text=True,timeout=4)
                if b.returncode:
                    return key,None
                return key,{"code":entry["code"],"output":a.stdout,"deterministic":a.stdout==b.stdout,"source":entry["source"],"line":entry["line"],"verified_version":"2.4.21","platform":"JVM","dependencies":["kotlin-test:2.4.21","kotlin-reflect:2.4.21"]}
        except subprocess.TimeoutExpired:
            return key,None
    verified={}
    with ThreadPoolExecutor(max_workers=8) as pool:
        for index,(key,entry) in enumerate(pool.map(run,tasks),1):
            if entry:
                verified[key]=entry
            if index%100==0:
                print(f"Rechecked {index}/{len(tasks)}: {len(verified)} verified",flush=True)
    (ROOT/"data/test-examples.json").write_text(json.dumps(verified,ensure_ascii=False,indent=2)+"\n")
    print(f"Verified {len(verified)} test-derived programs")


if __name__=="__main__":
    main()
