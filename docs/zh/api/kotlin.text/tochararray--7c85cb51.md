# toCharArray

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 a `CharArray` 包含此字符串的字符。

??? note "查看英文原文"

    Returns a `CharArray` containing characters of this string.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun String.toCharArray(): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L283)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun String.toCharArray(startIndex: Int = 0, endIndex: Int = this.length): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L289)

a `CharArray` 返回包含此字符串或其子字符串字符的字符。

@param 开始于子字符串的起始( 包括) 0 默认为 0。 @param 默认为 0 。 默认为 @param endIndex 默认为 5 结尾为 5 结尾为 5 , 此字符串的长度 。

@throws 指数外在值为`startIndex`以下为0或`endIndex`大于此字符串的长度,则除外。 @throws 非法辩护如果8,0005大于`endIndex`,则不在此列。

### 3. Common

```kotlin
@SinceKotlin("2.0")
@IgnorableReturnValue
public expect fun String.toCharArray(
    destination: CharArray,
    destinationOffset: Int = 0,
    startIndex: Int = 0,
    endIndex: Int = length
): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L301)

从此字符串复制字符到 `destination` 字符数组,并返回该数组。

@param 将复制的数组设定为 @param 目标 。 @param 目标 。 将复制的数组位置设定为 @param 开始Index 将子字符串的起始部分( 包括) 替换为 @param endIndex 复制的子字符串的结尾部分( 不包括) 。

@throws 指数外溢值或 `IllegalArgumentException` 当 `startIndex` 或 `endIndex` 超出此字符串构建指数的范围时,或者当 `startIndex > endIndex` 或 @throws 指数外溢值时,或者当子序列不适应从指定的 `destinationOffset` 开始的 `destination` 矩阵时,或者当该指数不在 `destination` 矩阵指数范围内时,则 `IllegalArgumentException` 或 `endIndex` 指数外外溢值。

### 4. Common

```kotlin
@SinceKotlin("1.4")
public expect fun StringBuilder.toCharArray(destination: CharArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = this.length)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L418)

从此字符串构建器复制字符到 `destination` 字符数组 。

@param 将复制的数组设定为 @param 目标 。 @param 将要复制的数组位置设为 0 。 @param 默认开始Index 将复制的数组的起始( 包括) 。 @param 默认是 0 。 @param endIndex 将复制的数组的结尾( 排他) , 默认是此字符串构建器的长度 。

@throws 指数外溢值或 `IllegalArgumentException` 当 `startIndex` 或 `endIndex` 超出此字符串构建指数的范围时,或者当 `startIndex > endIndex` 或 @throws 指数外溢值时,或者当子序列不适应从指定的 `destinationOffset` 开始的 `destination` 矩阵时,或者当该指数不在 `destination` 矩阵指数范围内时,则 `IllegalArgumentException` 或 `endIndex` 指数外外溢值。

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
    val result = source.`toCharArray`()
    println(result.contentToString())
}
```

```text title="输出"
[k, o, t, l, i, n]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
