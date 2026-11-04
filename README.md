# Kotlin 标准库中文用法手册

**简体中文** | [English](README.en.md)

基于 **kotlin-stdlib 2.4.21** 的中英文用法文档站，使用 **MkDocs + Material**。视觉参照 [BRV 文档](https://liangjingkanji.github.io/BRV/)：白色顶栏、紧凑字号、左右导航，以及可展开的版本菜单。

- [中文网站](https://oooooooko.github.io/kotlin-stdlib-docs/)
- [English website](https://oooooooko.github.io/kotlin-stdlib-docs/en/)
- [覆盖进度](https://oooooooko.github.io/kotlin-stdlib-docs/coverage/)

## 内容与进度

仅收录 **Common 通用 API**，排除 JVM、JS、Native、Wasm 专有 API、平台互操作注解和晚于 2.4.21 的声明。示例在 JVM 上使用固定版本工具链验证。

API 清单固定来自 [Kotlin v2.4.21](https://github.com/JetBrains/kotlin/tree/v2.4.21)。按包、类型、函数与属性组织，保留通用声明、重载、KDoc 和固定版本源码链接；语言按钮可切换到同一页面的另一种语言。

当前覆盖 **23 个包、2,590 个通用 API 分组、6,611 条声明**。每个分组都有实际编译运行的代表性示例和输出；中英文各有 2,617 个内容页。[data/coverage.json](data/coverage.json) 记录覆盖统计，待补分组为 **0**。同名重载集中展示，代表性示例不表示每个重载或每个平台都已单独验证。

英文 KDoc 保留官方原文；中文 KDoc 为自动翻译初稿，尚未逐条人工审校。术语标识符无法可靠保留时会回退到英文，每页也可展开英文原文。`map` 教程和 `Preconditions.kt` 已另外编写中文、英文说明。

本地验证共通过 **2,413 个独立程序**，其中 **2,187 份固定输出**与快照一致。

示例展示完整程序与运行输出。随机数、当前时间、临时路径、对象标识和系统相关输出可能随环境变化。部分官方边界示例使用 `kotlin-test`，部分反射示例需要 `kotlin-reflect`，均固定为 2.4.21；相关依赖在页面上注明。

`Preconditions.kt` 已覆盖 `require`、`requireNotNull`、`check`、`checkNotNull`、`error` 共 5 组 API、9 个重载，提供不依赖测试库的成功与异常示例，并逐项校验异常类型、消息及输出。

## 本地预览

需要 Python 3.12+；运行 Kotlin 示例还需要 JDK 17。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/mkdocs serve -a 127.0.0.1:8765
```

打开 [中文首页](http://127.0.0.1:8765/) 或 [英文首页](http://127.0.0.1:8765/en/)。左侧目前只有 **2.4.21**，点击版本号可展开详细菜单。

## 构建与验证

```sh
.venv/bin/python scripts/bootstrap_kotlin.py
.venv/bin/python scripts/verify_examples.py --fixtures
.venv/bin/python scripts/build_docs.py
.venv/bin/python scripts/check_docs.py --require-complete
.venv/bin/mkdocs build --strict
```

工具链自动下载到忽略提交的 `.tools/`。正常构建不需要下载翻译模型或上游源码，静态网站输出到 `site/`。

验证会对独立程序去重，分批编译并运行。固定输出按快照比较，随机和时间等输出只检查程序能正常执行。从官方测试提取的程序会隔离运行：macOS 使用 `sandbox-exec`，Linux 使用 Docker（GitHub Actions 已提供）。

只检查手工整理的前置条件示例：

```sh
.venv/bin/python scripts/verify_examples.py --manual-only
```

`python scripts/check_docs.py --require-complete` 会在仍有 API 缺少验证示例时失败。这个全覆盖检查和“网站成功构建”是两个不同的检查。

## 重新提取 API 与示例

```sh
git clone --depth 1 --filter=blob:none --sparse --branch v2.4.21 https://github.com/JetBrains/kotlin.git .tools/kotlin-source
git -C .tools/kotlin-source sparse-checkout set libraries/stdlib license
.venv/bin/python scripts/collect_api.py
.venv/bin/python scripts/prepare_examples.py
.venv/bin/python scripts/generate_examples.py
.venv/bin/python scripts/index_example_calls.py
.venv/bin/python scripts/curate_common_examples.py
.venv/bin/python scripts/build_docs.py
```

清单使用该版本 Kotlin 编译器自身的语法解析器，按标准库构建配置排除旧 DOM 兼容源码，并保留该版本通用的公开和受保护声明。示例关联通过编译器解析后的 IR 符号核对，不只按同名方法匹配。从官方测试提取的独立程序会经过初次隔离运行，验证结果作为仓库数据保存。特殊上下文（契约、协程、多平台声明等）的手工示例由 `scripts/curate_common_examples.py` 生成；需要的编译选项、附加文件和标准输入均在页面中展示。

需要重新生成中文草稿时，安装 `requirements-translation.txt` 并运行 `scripts/translate_kdoc.py`。日常构建直接使用仓库中的翻译缓存，不下载模型。

## 部署

推送到 `main` 后，GitHub Actions 会验证示例、检查中英文页面配对并严格构建网站。待补示例归零后才会自动发布到 GitHub Pages；本仓库已满足示例覆盖检查。Pull Request 运行构建检查，不发布。

## 来源与许可

上游 Kotlin 声明、KDoc 和示例的来源、修改说明与字体许可见 [LICENSE](LICENSE) 和 [NOTICE](NOTICE)。这是非官方文档项目，与 JetBrains 或 Kotlin Foundation 无隶属关系。
