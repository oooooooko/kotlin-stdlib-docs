# Kotlin 标准库用法

**kotlin-stdlib 2.4.21**

按包、类型和函数查找 API，结合完整程序和实际输出理解用法。

仅收录 **Common 通用 API**，不收录 JVM、JS、Native、Wasm 专有 API 或平台互操作注解。示例使用 JVM 验证；不代表每个平台行为均已验证。

当前收录 **2590** 个通用 API 条目、**6611** 条声明；**2590** 个条目已有验证示例，待补条目 **0** 个。

[阅读 map 教程](collections/map.md){ .md-button .md-button--primary }

[查看覆盖进度](coverage.md){ .md-button }

## 各包进度

| 包 | API | 已有示例 | 待补示例 |
| --- | ---: | ---: | ---: |
| [`kotlin.annotation`](api/kotlin.annotation/index.md) | 28 | 28 | 0 |
| [`kotlin.collections`](api/kotlin.collections/index.md) | 606 | 606 | 0 |
| [`kotlin.comparisons`](api/kotlin.comparisons/index.md) | 16 | 16 | 0 |
| [`kotlin.concurrent.atomics`](api/kotlin.concurrent.atomics/index.md) | 85 | 85 | 0 |
| [`kotlin.contracts`](api/kotlin.contracts/index.md) | 23 | 23 | 0 |
| [`kotlin.coroutines.cancellation`](api/kotlin.coroutines.cancellation/index.md) | 2 | 2 | 0 |
| [`kotlin.coroutines.debug`](api/kotlin.coroutines.debug/index.md) | 2 | 2 | 0 |
| [`kotlin.coroutines.intrinsics`](api/kotlin.coroutines.intrinsics/index.md) | 5 | 5 | 0 |
| [`kotlin.coroutines`](api/kotlin.coroutines/index.md) | 42 | 42 | 0 |
| [`kotlin.enums`](api/kotlin.enums/index.md) | 2 | 2 | 0 |
| [`kotlin.experimental`](api/kotlin.experimental/index.md) | 10 | 10 | 0 |
| [`kotlin.io.encoding`](api/kotlin.io.encoding/index.md) | 18 | 18 | 0 |
| [`kotlin.io`](api/kotlin.io/index.md) | 4 | 4 | 0 |
| [`kotlin.math`](api/kotlin.math/index.md) | 42 | 42 | 0 |
| [`kotlin.properties`](api/kotlin.properties/index.md) | 18 | 18 | 0 |
| [`kotlin.random`](api/kotlin.random/index.md) | 21 | 21 | 0 |
| [`kotlin.ranges`](api/kotlin.ranges/index.md) | 145 | 145 | 0 |
| [`kotlin.reflect`](api/kotlin.reflect/index.md) | 50 | 50 | 0 |
| [`kotlin.sequences`](api/kotlin.sequences/index.md) | 151 | 151 | 0 |
| [`kotlin.text`](api/kotlin.text/index.md) | 443 | 443 | 0 |
| [`kotlin.time`](api/kotlin.time/index.md) | 123 | 123 | 0 |
| [`kotlin.uuid`](api/kotlin.uuid/index.md) | 31 | 31 | 0 |
| [`kotlin`](api/kotlin/index.md) | 723 | 723 | 0 |

## 覆盖口径

- API 条目按包、所属类型和名称分组；同名重载集中展示，不把一个示例视为每个重载都已验证。
- 收录公开和受保护声明，排除私有、内部和 `HIDDEN` 声明，以及标准库构建配置排除的旧 DOM 兼容源码。
- “已有示例”表示至少有一个真实运行通过的代表性程序；每个平台声明仍保留固定版本源码链接。
- 中文 KDoc 是自动翻译初稿；英文保留官方原文。尚未完成的示例逐项列在仓库 `data/coverage.json` 中。
