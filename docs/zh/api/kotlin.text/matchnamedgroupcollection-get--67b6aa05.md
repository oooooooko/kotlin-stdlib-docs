# MatchNamedGroupCollection.get

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回指定的 `name` 中的名称组。
@return举例说,`MatchGroup`如果该组与指定`name`匹配或匹配`null`否则。
如果没有组别在正方形模式中定义了指定的`name`,则@throws非法辩护除外。
@throws 不支持的操作例外 如果匹配组收藏不支持获取匹配组的名称,
例如,当它不为当前平台支持时。

??? note "查看英文原文"

    Returns a named group with the specified `name`.
    @return An instance of `MatchGroup` if the group with the specified `name` was matched or `null` otherwise.
    @throws IllegalArgumentException if there is no group with the specified `name` defined in the regex pattern.
    @throws UnsupportedOperationException if this match group collection doesn't support getting match groups by name,
    for example, when it's not supported by the current platform.

## 声明与重载

### 1. Common

```kotlin
public operator fun get(name: String): MatchGroup?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/regex/MatchResult.kt#L35)

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
