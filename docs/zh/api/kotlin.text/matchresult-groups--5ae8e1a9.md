# MatchResult.groups

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

集合一组配有正则表达式的组 。

此收藏的大小为 `groupCount + 1`, 即正常表达式中的组数为 `groupCount`。 组数由 1 到 `groupCount` 索引, 组数由 0 和 整个匹配值对应 。

??? note "查看英文原文"

    A collection of groups matched by the regular expression.
    
    This collection has size of `groupCount + 1` where `groupCount` is the count of groups in the regular expression.
    Groups are indexed from 1 to `groupCount` and group with the index 0 corresponds to the entire match.

## 声明与重载

### 1. Common

```kotlin
public val groups: MatchGroupCollection
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/regex/MatchResult.kt#L53)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.text.*

fun main() {
    val source = Regex("[a-z]+").find("hello 42")!!
    val result = source.`groups`
    println(result)
}
```

```text title="输出"
[MatchGroup(value=hello, range=0..4)]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
