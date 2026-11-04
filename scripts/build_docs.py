"""Render both languages from the versioned API inventory and verified example fixtures."""

from collections import defaultdict
import json
from pathlib import Path
import re

import yaml

from collect_api import ROOT, VERSION
from translate_kdoc import blocks, chunks, markdown_doc, protected, restore
from verify_examples import output_can_vary, normalize_output

PACKAGES = {
    "kotlin":("核心类型与函数","Core types and functions"),
    "kotlin.collections":("集合","Collections"), "kotlin.sequences":("序列","Sequences"),
    "kotlin.text":("字符串与正则","Text and regular expressions"), "kotlin.ranges":("区间与步进","Ranges and progressions"),
    "kotlin.comparisons":("比较与排序","Comparisons"), "kotlin.math":("数学函数","Math"),
    "kotlin.random":("随机数","Random"), "kotlin.time":("时间与时长","Time"), "kotlin.uuid":("UUID","UUID"),
    "kotlin.io":("输入输出","Input and output"), "kotlin.io.path":("文件路径","File paths"), "kotlin.io.encoding":("编码","Encoding"),
    "kotlin.concurrent":("并发","Concurrency"), "kotlin.concurrent.atomics":("原子操作","Atomics"),
    "kotlin.coroutines":("协程基础","Coroutine primitives"), "kotlin.coroutines.intrinsics":("协程底层 API","Coroutine intrinsics"),
    "kotlin.reflect":("反射类型","Reflection types"), "kotlin.properties":("属性委托","Property delegates"),
    "kotlin.jvm":("JVM 互操作","JVM interoperability"), "kotlin.js":("JS 互操作","JS interoperability"),
    "kotlin.native":("Native API","Native APIs"), "kotlin.wasm":("Wasm API","Wasm APIs"),
    "kotlin.annotation":("注解","Annotations"), "kotlin.contracts":("契约","Contracts"),
}


def source_link(declaration):
    return f"https://github.com/JetBrains/kotlin/blob/v{VERSION}/{declaration['source']}#L{declaration['line']}"


def write(language, relative, value):
    path = ROOT/"docs"/language/relative
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(value.rstrip()+"\n",encoding="utf-8")


def repair_translation(original, translated):
    _, symbols = protected(original)
    def repair(match):
        index = int(match[1])
        return symbols[index-1] if 0<index<=len(symbols) else match[0]
    translated = re.sub(r"8[0]+([1-9]\d*?)(?=80|\D|$)", repair, translated)
    # Incomplete identifier substitution is never presented as a finished translation.
    if any(symbol not in translated for symbol in symbols) or re.search(r"8[0]{2,}\d+|[XZ]{5,}|ZX\d+X",translated):
        return None
    return translated.replace("溪流","流").replace("丢弃一个例外","抛出异常").replace("抛出一个例外","抛出异常")


def localized_doc(doc, language, translations):
    if language == "en":
        return markdown_doc(doc)
    result=[]
    for block in blocks(doc):
        if not block or block.isspace() or block.startswith("```"):
            result.append(block)
            continue
        localized=[]
        for chunk in chunks(block):
            translated = repair_translation(chunk,translations[chunk]) if chunk in translations else None
            if translated:
                localized.append(translated)
            else:
                # Retain the authoritative prose if machine translation loses an identifier.
                localized.append(chunk)
        result.append(" ".join(localized))
    return "".join(result)


def example_block(example, language, index):
    zh = language=="zh"
    title = f"示例 {index}" if zh else f"Example {index}"
    output_title = "输出" if zh else "Output"
    target = example.get("platform", "JVM")
    value = f"### {title} · {target}\n\n```kotlin title=\"{title}\" linenums=\"1\"\n{example['code'].rstrip()}\n```\n\n```text title=\"{output_title}\"\n{normalize_output(example['output']).rstrip()}\n```\n\n"
    for filename,code in example.get("files",{}).items():
        value+=f"```kotlin title=\"{filename}\"\n{code.rstrip()}\n```\n\n"
    if example.get("compiler_options"):
        value+=("编译选项：" if zh else "Compiler options: ")+" ".join(f"`{flag}`" for flag in example["compiler_options"])+"\n\n"
    if example.get("stdin"):
        value+=f"```text title=\"{'标准输入' if zh else 'Standard input'}\"\n{example['stdin'].rstrip()}\n```\n\n"
    if example.get("stderr"):
        value += f"```text title=\"{'标准错误输出' if zh else 'Standard error'}\"\n{normalize_output(example['stderr']).rstrip()}\n```\n\n"
    if not example.get("deterministic",True) or output_can_vary(example["code"],example["output"]):
        value += ("本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。\n\n" if zh else "The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.\n\n")
    if "import kotlin.test" in example["code"]:
        value += ("此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。\n\n" if zh else "This edge-case sample also uses assertions from `kotlin-test:2.4.21`.\n\n")
    if "kotlin-reflect:2.4.21" in example.get("dependencies",[]):
        value += ("此示例需要 `kotlin-reflect:2.4.21`。\n\n" if zh else "This example requires `kotlin-reflect:2.4.21`.\n\n")
    if example.get("source"):
        value += f"[{'示例来源' if zh else 'Sample source'}]({source_link(example)})\n\n"
    return value


def build():
    api=json.loads((ROOT/"data/api.json").read_text())
    official=json.loads((ROOT/"data/examples.json").read_text())
    manual_path=ROOT/"data/manual-examples.json"
    manual=json.loads(manual_path.read_text()) if manual_path.exists() else {}
    manual_text_path=ROOT/"data/manual-api-text.json"
    manual_text=json.loads(manual_text_path.read_text()) if manual_text_path.exists() else {}
    generated=json.loads((ROOT/"data/generated-examples.json").read_text())
    test_path=ROOT/"data/test-examples.json"
    tests=json.loads(test_path.read_text()) if test_path.exists() else {}
    resolved_path=ROOT/"data/example-api-index.json"
    resolved=json.loads(resolved_path.read_text()) if resolved_path.exists() else {}
    translations=json.loads((ROOT/"data/translations.json").read_text())
    by_package=defaultdict(list)
    covered=[]
    gaps=[]
    for group in api["groups"]:
        keys=list(dict.fromkeys(s for d in group["declarations"] for s in d["samples"] if s in official))
        examples=[official[key] for key in keys]
        if group["key"] in generated:
            examples.append(generated[group["key"]])
        if not examples:
            related=[]
            for reference in resolved.get(group["key"],[]):
                namespace,key=reference.split(":",1)
                fixture={"official":official,"generated":generated,"tests":tests}[namespace].get(key)
                if fixture:
                    related.append(fixture)
            if related:
                examples.append(min(related,key=lambda e: len(e["code"])+len(e["output"])))
        if group["key"] in manual:
            examples=[manual[group["key"]]]
        group["has_example"]=bool(examples)
        (covered if examples else gaps).append(group["key"])
        by_package[group["package"]].append(group)
        for language in ("zh","en"):
            zh=language=="zh"
            title=".".join(filter(None,(group["owner"],group["name"])))
            platforms=" · ".join(sorted({d["platform"] for d in group["declarations"]}))
            page=f"# {title}\n\n`{group['package']}` · **{VERSION}** · {platforms}\n\n"
            if examples:
                verified_targets=" / ".join(sorted({example.get("platform","JVM") for example in examples}))
                page+=(f"本文含经 Kotlin / stdlib 2.4.21 在 **{verified_targets}** 上编译运行的代表性示例。\n\n" if zh else f"Representative examples on this page were compiled and executed on **{verified_targets}** with Kotlin / stdlib 2.4.21.\n\n")
            else:
                page+=("!!! info \"示例尚未完成\"\n    当前已收录固定版本的声明和说明，但此 API 尚没有经运行验证的示例。它不计入用法示例覆盖率。\n\n" if zh else "!!! info \"Example not yet available\"\n    This entry contains the pinned declarations and documentation, but does not yet have an execution-verified example. It is excluded from example coverage.\n\n")
            docs=list(dict.fromkeys(d["kdoc"] for d in group["declarations"] if d["kdoc"]))
            if not docs and group["key"] in manual_text:
                page+=f"## {'用途与说明' if zh else 'Description'}\n\n"+manual_text[group["key"]][language]+"\n\n"
            if docs:
                description=manual_text.get(group["key"],{}).get(language) or localized_doc(docs[0],language,translations)
                page+=f"## {'用途与说明' if zh else 'Description'}\n\n"+description+"\n\n"
                if zh:
                    original="\n".join("    "+line for line in markdown_doc(docs[0]).splitlines())
                    page+='??? note "查看英文原文"\n\n'+original+"\n\n"
            declarations={}
            for declaration in group["declarations"]:
                signature=declaration["signature"]
                # Actual/expect variants retain their source and target instead of being silently collapsed.
                identity=(signature,declaration["kdoc"])
                declarations.setdefault(identity,[]).append(declaration)
            page+=f"## {'声明与重载' if zh else 'Declarations and overloads'}\n\n"
            for index,((signature,kdoc),variants) in enumerate(declarations.items(),1):
                targets=" · ".join(sorted({d["platform"] for d in variants}))
                page+=f"### {index}. {targets}\n\n```kotlin\n{signature}\n```\n\n"
                page+=" · ".join(f"[{d['platform']} {'源码' if zh else 'source'}]({source_link(d)})" for d in variants)+"\n\n"
                if kdoc and docs and kdoc!=docs[0] and group["key"] not in manual_text:
                    page+=localized_doc(kdoc,language,translations)+"\n\n"
            if examples:
                page+=f"## {'用法示例与输出' if zh else 'Usage examples and output'}\n\n"
                for index,example in enumerate(examples,1):
                    page+=example_block(example,language,index)
            page+=f"## {'版本与来源' if zh else 'Version and sources'}\n\n"
            if group["key"] in manual_text:
                page+=("本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。\n" if zh else "This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.\n")
            else:
                page+=("声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。\n" if zh else "Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.\n")
            write(language,group["path"],page)

    stats={"version":VERSION,"commit":api["commit"],"packages":len(by_package),"api_entries":len(api["groups"]),"declarations":sum(len(g["declarations"]) for g in api["groups"]),"entries_with_verified_examples":len(covered),"entries_missing_examples":len(gaps),"official_programs":len(official),"generated_programs":len(generated),"test_derived_programs":len(tests),"parse_errors":api["parse_errors"]}
    stats["scope"]="Common"
    (ROOT/"data/coverage.json").write_text(json.dumps({**stats,"missing_examples":gaps},ensure_ascii=False,indent=2)+"\n")
    for language in ("zh","en"):
        zh=language=="zh"
        home=(f"# Kotlin {'标准库用法' if zh else 'Standard Library Usage'}\n\n**kotlin-stdlib {VERSION}**\n\n")
        home+=("按包、类型和函数查找 API，结合完整程序和实际输出理解用法。\n\n" if zh else "Browse APIs by package, type, and function, with complete programs and captured output.\n\n")
        home+=("仅收录 **Common 通用 API**，不收录 JVM、JS、Native、Wasm 专有 API 或平台互操作注解。示例使用 JVM 验证；不代表每个平台行为均已验证。\n\n" if zh else "Only **Common APIs** are included. Platform-specific APIs and interop annotations are excluded. Examples are verified on the JVM; this does not establish identical behavior on every target.\n\n")
        home+=(f"当前收录 **{stats['api_entries']}** 个通用 API 条目、**{stats['declarations']}** 条声明。\n\n" if zh else f"The inventory contains **{stats['api_entries']} Common API entries** and **{stats['declarations']} declarations**.\n\n")
        home+=f"[{'阅读 map 教程' if zh else 'Read the map tutorial'}](collections/map.md){{ .md-button .md-button--primary }}\n\n"
        home+=f"## {'按包查找' if zh else 'Browse packages'}\n\n| {'包' if zh else 'Package'} | {'内容' if zh else 'Contents'} | API |\n| --- | --- | ---: |\n"
        for package,groups in by_package.items():
            label=PACKAGES.get(package,(package,package))[0 if zh else 1]
            home+=f"| [`{package}`](api/{package}/index.md) | {label} | {len(groups)} |\n"
            index=f"# {label}\n\n`{package}` · {VERSION}\n\n"
            index+=f"| API | {'类型' if zh else 'Kind'} | {'示例' if zh else 'Examples'} |\n| --- | --- | --- |\n"
            for group in groups:
                name=".".join(filter(None,(group["owner"],group["name"])))
                kind=group["declarations"][0]["kind"].replace("_declaration","")
                status=("已验证" if zh else "Verified") if group["has_example"] else ("待补齐" if zh else "Pending")
                index+=f"| [`{name}`]({Path(group['path']).name}) | {kind} | {status} |\n"
            write(language,f"api/{package}/index.md",index)
        write(language,"index.md",home)
    config=yaml.safe_load((ROOT/"mkdocs.yml").read_text())
    config["site_url"]="https://oooooooko.github.io/kotlin-stdlib-docs/"
    config["repo_url"]="https://github.com/oooooooko/kotlin-stdlib-docs"
    config["repo_name"]="kotlin-stdlib-docs"
    config["edit_uri"]=""
    config["theme"]["features"]=[feature for feature in config["theme"]["features"] if feature!="navigation.instant"]
    def member_nav(groups,owner=""):
        items=[]
        for group in groups:
            if group["owner"]!=owner:
                continue
            qualified=".".join(filter(None,(owner,group["name"])))
            nested=member_nav(groups,qualified)
            if nested:
                items.append({group["name"]:[{"概览":group["path"]},*nested]})
            else:
                items.append({group["name"]:group["path"]})
        if not owner and len(items)>32:
            buckets=defaultdict(list)
            for item in items:
                label=next(iter(item))
                buckets[label[0].upper() if label[0].isalpha() else "#"].append(item)
            return [{letter:entries} for letter,entries in sorted(buckets.items())]
        return items
    package_nav=[{PACKAGES.get(p,(p,p))[0]+" · "+p:[{"概览":f"api/{p}/index.md"},*member_nav(groups)]} for p,groups in by_package.items()]
    config["nav"]=[{VERSION:[{"开始阅读":"index.md"},{"API 目录":package_nav}]}]
    translations_nav={"开始阅读":"Getting started","API 目录":"API reference","概览":"Overview"}
    translations_nav.update({PACKAGES.get(p,(p,p))[0]+" · "+p:PACKAGES.get(p,(p,p))[1]+" · "+p for p in by_package})
    config["plugins"]=[{"i18n":{"docs_structure":"folder","languages":[{"locale":"zh","name":"简体中文","default":True,"build":True},{"locale":"en","name":"English","build":True,"site_name":"Kotlin Standard Library Usage","site_description":"Bilingual usage documentation for kotlin-stdlib 2.4.21.","nav_translations":translations_nav}]}},{"search":{"lang":["zh","en"]}}]
    config["validation"]={"nav":{"omitted_files":"ignore"}}
    (ROOT/"mkdocs.yml").write_text(yaml.safe_dump(config,allow_unicode=True,sort_keys=False))
    print(json.dumps(stats,ensure_ascii=False))


if __name__=="__main__":
    build()
