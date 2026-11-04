# StringBuilder.substring

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个新的 `String` , 包含字符串构建器中的字符, 值为 `startIndex` ( 包含在内) , 最高值为 `length` ( 不包括在内) 。

@throws 指数外在值除以`startIndex` 低于零或大于此字符串构建器长度的值。

??? note "查看英文原文"

    Returns a new `String` that contains characters in this string builder at `startIndex` (inclusive) and up to the `length` (exclusive).
    
    @throws IndexOutOfBoundsException if `startIndex` is less than zero or greater than the length of this string builder.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
    public fun substring(startIndex: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L299)

### 2. Common

```kotlin
@SinceKotlin("1.4")
    public fun substring(startIndex: Int, endIndex: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L307)

返回一个新的 `String` , 包含字符串构建器中的字符, 值为 `startIndex` ( 包含在内) , 最高值为 `endIndex` ( 不包括在内) 。

@throws 指数外在值为`startIndex` 或 `endIndex`时,当`startIndex` 或 `endIndex` 时,当@throws 指数超出该字符串构建指数的范围时,或当 `startIndex > endIndex`时,则`IllegalArgumentException` 或 `endIndex` 指数外外在值为@throws 。

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
    val result = source.`substring`(0)
    println(result)
}
```

```text title="输出"
kotlin
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
