"""Install the pinned Kotlin compiler and documentation verification libraries locally."""

from pathlib import Path
import shutil
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
BASE="https://repo.maven.apache.org/maven2/"
ARTIFACTS=[
    ("org.jetbrains.kotlin","kotlin-compiler-embeddable","2.4.21","kotlin-compiler.jar"),
    ("org.jetbrains.kotlin","kotlin-stdlib","2.4.21","kotlin-stdlib.jar"),
    ("org.jetbrains.kotlin","kotlin-test","2.4.21","kotlin-test.jar"),
    ("org.jetbrains.kotlin","kotlin-script-runtime","2.4.21","kotlin-script-runtime.jar"),
    ("org.jetbrains.kotlin","kotlin-build-tools-api","2.4.21","kotlin-build-tools-api.jar"),
    ("org.jetbrains.kotlin","kotlin-reflect","1.6.10","kotlin-reflect-1.6.10.jar"),
    ("org.jetbrains.kotlinx","kotlinx-coroutines-core-jvm","1.8.0","kotlinx-coroutines-core-jvm-1.8.0.jar"),
    ("org.jetbrains","annotations","13.0","annotations-13.0.jar"),
]


def download(group,artifact,version,target):
    if target.is_file():
        return
    url=f"{BASE}{group.replace('.','/')}/{artifact}/{version}/{artifact}-{version}.jar"
    temporary=target.with_suffix(".download")
    print(f"Downloading {artifact}:{version}",flush=True)
    with urllib.request.urlopen(url,timeout=60) as response,temporary.open("wb") as output:
        shutil.copyfileobj(response,output)
    temporary.replace(target)


def main():
    toolchain=ROOT/".tools/maven-kotlinc"
    (toolchain/"bin").mkdir(parents=True,exist_ok=True)
    (toolchain/"lib").mkdir(exist_ok=True)
    for group,artifact,version,name in ARTIFACTS:
        download(group,artifact,version,toolchain/"lib"/name)
    download("org.jetbrains.kotlin","kotlin-reflect","2.4.21",ROOT/".tools/kotlin-reflect-2.4.21.jar")
    command=toolchain/"bin/kotlinc"
    command.write_text('#!/bin/sh\ncompiler_home=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)\nexec java -cp "$compiler_home/lib/*" org.jetbrains.kotlin.cli.jvm.K2JVMCompiler "$@"\n')
    command.chmod(0o755)
    print("Kotlin / stdlib 2.4.21 toolchain ready.")


if __name__=="__main__":
    main()
