# MatchNamedGroupCollection

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

推广`MatchGroupCollection`, 引入一种方式, 将相匹配的团体名称配对, 当 Regex 支持它时 。

??? note "查看英文原文"

    Extends `MatchGroupCollection` by introducing a way to get matched groups by name, when regex supports it.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public interface MatchNamedGroupCollection : MatchGroupCollection
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/regex/MatchResult.kt#L30)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val match = Regex("(?<word>[a-z]+)-(?<number>[0-9]+)").matchEntire("item-42")!!
    println(match.groups["word"]?.value)
    println(match.groups["number"]?.value)
}
```

```text title="输出"
item
42
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
