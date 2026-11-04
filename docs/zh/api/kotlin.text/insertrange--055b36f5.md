# insertRange

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在指定的 `index` 的字符串构建器中插入指定字符数组`value`的子数组中的字符,并返回此实例。

插入的字符与 `value` 矩阵中的字符顺序相同,从 `index` 开始。

@param 索引 显示此字符串构建器中的位置, 以插入字符的数组值 。 @param 开始 INdex 显示子组的起始( 包括) 插入 。 @param 结尾 内 内 内 插入 。

@throws 指数外溢值或 `IllegalArgumentException` , 当 `startIndex` 或 `endIndex` 超出 `value` 阵列指数的范围时, 或当 `startIndex > endIndex` @throws 指数外溢值值超过 `startIndex > endIndex` 或 @throws 时, 或当 `index` 低于 零或 大于 字符串构建器长度时, 则有 `IllegalArgumentException` 指数外溢值 。

??? note "查看英文原文"

    Inserts characters in a subarray of the specified character array `value` into this string builder at the specified `index` and returns this instance.
    
    The inserted characters go in same order as in the `value` array, starting at `index`.
    
    @param index the position in this string builder to insert at.
    @param value the array from which characters are inserted.
    @param startIndex the beginning (inclusive) of the subarray to insert.
    @param endIndex the end (exclusive) of the subarray to insert.
    
    @throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of the `value` array indices or when `startIndex > endIndex`.
    @throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue public expect fun StringBuilder.insertRange(index: Int, value: CharArray, startIndex: Int, endIndex: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L459)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue public expect fun StringBuilder.insertRange(index: Int, value: CharSequence, startIndex: Int, endIndex: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L475)

在指定的 `index` 的字符串构建器中插入指定字符序列`value`的子序列中的字符,并返回此实例。

插入字符的顺序与 `value` 字符序列中的顺序相同,从 `index` 开始。

@param 索引此字符串构建器中的位置,以插入以下序列的字符序列。 @param 值。 @param 开头 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内 内

@throws 指数外溢值或 `IllegalArgumentException` , 当 `startIndex` 或 `endIndex` 超出 `value` 字符序列指数的范围时, 或当 `startIndex > endIndex` @throws 指数外溢值值在 `index` 低于 0 或大于 字符串构建器长度时, 或当 `startIndex > endIndex` @throws 指数外溢值时, 或 `IllegalArgumentException` 。

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
    val result = source.`insertRange`(0, charArrayOf('a', 'b', 'c'), 0, 2)
    println(result)
}
```

```text title="输出"
abkotlin
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
