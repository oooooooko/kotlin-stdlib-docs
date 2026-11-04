# takeHighestOneBit

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个数字,如果数字为零,则返回以 `Int` 这一数值中最重要的一组位数的位置设置一个位数,或者零位数。

??? note "查看英文原文"

    Returns a number having a single bit set in the position of the most significant set bit of this `Int` number,
    or zero, if this number is zero.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun Int.takeHighestOneBit(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L28)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun Long.takeHighestOneBit(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L88)

返回一个数字,如果数字为零,则返回以 `Long` 这一数值中最重要的一组位数的位置设置一个位数,或者零位数。

### 3. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun Byte.takeHighestOneBit(): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L149)

返回一个数字,如果数字为零,则返回以 `Byte` 这一数值中最重要的一组位数的位置设置一个位数,或者零位数。

### 4. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun Short.takeHighestOneBit(): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L216)

返回一个数字,如果数字为零,则返回以 `Short` 这一数值中最重要的一组位数的位置设置一个位数,或者零位数。

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UInt.takeHighestOneBit(): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L30)

返回一个数字,如果数字为零,则返回以 `UInt` 这一数值中最重要的一组位数的位置设置一个位数,或者零位数。

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun ULong.takeHighestOneBit(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L97)

返回一个数字,如果数字为零,则返回以 `ULong` 这一数值中最重要的一组位数的位置设置一个位数,或者零位数。

### 7. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UByte.takeHighestOneBit(): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L162)

返回一个数字,如果数字为零,则返回以 `UByte` 这一数值中最重要的一组位数的位置设置一个位数,或者零位数。

### 8. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UShort.takeHighestOneBit(): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L228)

返回一个数字,如果数字为零,则返回以 `UShort` 这一数值中最重要的一组位数的位置设置一个位数,或者零位数。

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
import kotlin.*

fun main() {
    val source = 5
    val result = source.`takeHighestOneBit`()
    println(result)
}
```

```text title="输出"
4
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
