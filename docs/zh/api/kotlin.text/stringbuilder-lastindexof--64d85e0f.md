# StringBuilder.lastIndexOf

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回指定 `string` 最后一次出现的字符串构建器中的索引。 空字符串 `""` 最后一次出现的时间等于 `this.length` 。

如果指定的 `string` 不在此字符串构建器中发生, 返回 `-1` 。

??? note "查看英文原文"

    Returns the index within this string builder of the last occurrence of the specified `string`.
    The last occurrence of empty string `""` is considered to be at the index equal to `this.length`.
    
    Returns `-1` if the specified `string` does not occur in this string builder.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
    public fun lastIndexOf(string: String): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L160)

### 2. Common

```kotlin
@SinceKotlin("1.4")
    public fun lastIndexOf(string: String, startIndex: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L169)

返回指定 `string` 最后一次出现的字符串构建器中的索引,从指定的 `startIndex` 开始到开始。

如果指定的 `string` 没有出现在从指定的`startIndex`开始的字符串构建器中,则返回 `-1` 。

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
    val source = StringBuilder("kotlin")
    val result = source.`lastIndexOf`("o")
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
