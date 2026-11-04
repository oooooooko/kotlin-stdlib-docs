# MatchResult.Destructured.toList

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回解结构组值,作为字符串列表。返回列表中的第一个值与第一个组的值相对应,等等。

@sample 样本.text.regexpics.regexpics. 匹配结构改变到群集价值

??? note "查看英文原文"

    Returns destructured group values as a list of strings.
     First value in the returned list corresponds to the value of the first group, and so on.
    
    @sample samples.text.Regexps.matchDestructuringToGroupValues

## 声明与重载

### 1. Common

```kotlin
public fun toList(): List<String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/regex/MatchResult.kt#L119)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val match = Regex("(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)").matchEntire("abcdefghij")!!
    val groups = match.destructured
    val (a, b, c, d, e, f, g, h, i, j) = groups
    println(listOf(a, b, c, d, e, f, g, h, i, j))
    println(groups.toList())
    println(groups.match.value)
}
```

```text title="输出"
[a, b, c, d, e, f, g, h, i, j]
[a, b, c, d, e, f, g, h, i, j]
abcdefghij
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
