# mapIndexed

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含对每个字符及其索引应用给定的 `transform` 函数的结果的列表。 @param `transform` 函数,该函数将字符的索引和字符本身,并返回对字符应用的变换结果。

??? note "查看英文原文"

    Returns a list containing the results of applying the given `transform` function
    to each character and its index in the original char sequence.
    @param `transform` function that takes the index of a character and the character itself
    and returns the result of the transform applied to the character.

## 声明与重载

### 1. Common

```kotlin
public inline fun <R> CharSequence.mapIndexed(transform: (index: Int, Char) -> R): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L997)

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
    val source = "kotlin"
    val result = source.`mapIndexed`({ index, value -> "$index:$value" })
    println(result)
}
```

```text title="输出"
[0:k, 1:o, 2:t, 3:l, 4:i, 5:n]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
