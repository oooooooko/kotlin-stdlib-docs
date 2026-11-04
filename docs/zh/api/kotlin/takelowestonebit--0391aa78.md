# takeLowestOneBit

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个数字,如果数字为零,则在 `Int` 这个数字中最小的一组位的位置上设置一个位数,或者零位。

??? note "查看英文原文"

    Returns a number having a single bit set in the position of the least significant set bit of this `Int` number,
    or zero, if this number is zero.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun Int.takeLowestOneBit(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L35)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun Long.takeLowestOneBit(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L95)

返回一个数字,如果数字为零,则在 `Long` 这个数字中最小的一组位的位置上设置一个位数,或者零位。

### 3. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun Byte.takeLowestOneBit(): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L157)

返回一个数字,如果数字为零,则在 `Byte` 这个数字中最小的一组位的位置上设置一个位数,或者零位。

### 4. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun Short.takeLowestOneBit(): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L224)

返回一个数字,如果数字为零,则在 `Short` 这个数字中最小的一组位的位置上设置一个位数,或者零位。

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UInt.takeLowestOneBit(): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L38)

返回一个数字,如果数字为零,则在 `UInt` 这个数字中最小的一组位的位置上设置一个位数,或者零位。

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun ULong.takeLowestOneBit(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L105)

返回一个数字,如果数字为零,则在 `ULong` 这个数字中最小的一组位的位置上设置一个位数,或者零位。

### 7. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UByte.takeLowestOneBit(): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L170)

返回一个数字,如果数字为零,则在 `UByte` 这个数字中最小的一组位的位置上设置一个位数,或者零位。

### 8. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UShort.takeLowestOneBit(): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L236)

返回一个数字,如果数字为零,则在 `UShort` 这个数字中最小的一组位的位置上设置一个位数,或者零位。

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
    val result = source.`takeLowestOneBit`()
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
