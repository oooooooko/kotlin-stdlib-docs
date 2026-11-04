# rotateLeft

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

旋转指定的 `bitCount` 位数所剩的 `Int` 数字的二进制表示式。
左侧最显著的位元从左侧推出, 重新输入数字, 成为右侧最小的位元 。

以负位数旋转剩下的数字,与以负位数旋转的右键相同: `number.rotateLeft(-n) == number.rotateRight(n)`

乘以 `Int.SIZE_BITS` (32)乘以乘以 `Int.SIZE_BITS` , 返回相同数, 或更一般的 `number.rotateLeft(n) == number.rotateLeft(n % 32)`

??? note "查看英文原文"

    Rotates the binary representation of this `Int` number left by the specified `bitCount` number of bits.
    The most significant bits pushed out from the left side reenter the number as the least significant bits on the right side.
    
    Rotating the number left by a negative bit count is the same as rotating it right by the negated bit count:
    `number.rotateLeft(-n) == number.rotateRight(n)`
    
    Rotating by a multiple of `Int.SIZE_BITS` (32) returns the same number, or more generally
    `number.rotateLeft(n) == number.rotateLeft(n % 32)`

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
public expect fun Int.rotateLeft(bitCount: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L42)

### 2. Common

```kotlin
@SinceKotlin("1.6")
public expect fun Long.rotateLeft(bitCount: Int): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L102)

旋转指定的 `bitCount` 位数所剩的 `Long` 数字的二进制表示式。
左侧最显著的位元从左侧推出, 重新输入数字, 成为右侧最小的位元 。

以负位数旋转剩下的数字,与以负位数旋转的右键相同: `number.rotateLeft(-n) == number.rotateRight(n)`

乘以 `Long.SIZE_BITS` (64)乘以乘以 `Long.SIZE_BITS` , 返回相同数, 或更一般的 `number.rotateLeft(n) == number.rotateLeft(n % 64)`

### 3. Common

```kotlin
@SinceKotlin("1.6")
public fun Byte.rotateLeft(bitCount: Int): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L166)

旋转指定的 `bitCount` 位数所剩的 `Byte` 数字的二进制表示式。
左侧最显著的位元从左侧推出, 重新输入数字, 成为右侧最小的位元 。

以负位数旋转剩下的数字,与以负位数旋转的右键相同: `number.rotateLeft(-n) == number.rotateRight(n)`

乘以 `Byte.SIZE_BITS` (8)乘以乘以 `Byte.SIZE_BITS` (8), 返回相同数字, 或更一般的 `number.rotateLeft(n) == number.rotateLeft(n % 8)`

### 4. Common

```kotlin
@SinceKotlin("1.6")
public fun Short.rotateLeft(bitCount: Int): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L233)

旋转指定的 `bitCount` 位数所剩的 `Short` 数字的二进制表示式。
左侧最显著的位元从左侧推出, 重新输入数字, 成为右侧最小的位元 。

以负位数旋转剩下的数字,与以负位数旋转的右键相同: `number.rotateLeft(-n) == number.rotateRight(n)`

乘以 `Short.SIZE_BITS` (16)乘以乘以 `Short.SIZE_BITS` (16),返回同数,或更一般地说, `number.rotateLeft(n) == number.rotateLeft(n % 16)` 。

### 5. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun UInt.rotateLeft(bitCount: Int): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L46)

旋转指定的 `bitCount` 位数所剩的 `UInt` 数字的二进制表示式。
左侧最显著的位元从左侧推出, 重新输入数字, 成为右侧最小的位元 。

以负位数旋转剩下的数字,与以负位数旋转的右键相同: `number.rotateLeft(-n) == number.rotateRight(n)`

乘以 `UInt.SIZE_BITS` (32)乘以乘以 `UInt.SIZE_BITS` , 返回相同数, 或更一般的 `number.rotateLeft(n) == number.rotateLeft(n % 32)`

### 6. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun ULong.rotateLeft(bitCount: Int): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L113)

旋转指定的 `bitCount` 位数所剩的 `ULong` 数字的二进制表示式。
左侧最显著的位元从左侧推出, 重新输入数字, 成为右侧最小的位元 。

以负位数旋转剩下的数字,与以负位数旋转的右键相同: `number.rotateLeft(-n) == number.rotateRight(n)`

乘以 `ULong.SIZE_BITS` (64)乘以乘以 `ULong.SIZE_BITS` , 返回相同数, 或更一般的 `number.rotateLeft(n) == number.rotateLeft(n % 64)`

### 7. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun UByte.rotateLeft(bitCount: Int): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L179)

旋转指定的 `bitCount` 位数所剩的 `UByte` 数字的二进制表示式。
左侧最显著的位元从左侧推出, 重新输入数字, 成为右侧最小的位元 。

以负位数旋转剩下的数字,与以负位数旋转的右键相同: `number.rotateLeft(-n) == number.rotateRight(n)`

乘以 `UByte.SIZE_BITS` (8)乘以乘以 `UByte.SIZE_BITS` (8), 返回相同数字, 或更一般的 `number.rotateLeft(n) == number.rotateLeft(n % 8)`

### 8. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun UShort.rotateLeft(bitCount: Int): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L245)

旋转指定的 `bitCount` 位数所剩的 `UShort` 数字的二进制表示式。
左侧最显著的位元从左侧推出, 重新输入数字, 成为右侧最小的位元 。

以负位数旋转剩下的数字,与以负位数旋转的右键相同: `number.rotateLeft(-n) == number.rotateRight(n)`

乘以 `UShort.SIZE_BITS` (16)乘以乘以 `UShort.SIZE_BITS` (16),返回同数,或更一般地说, `number.rotateLeft(n) == number.rotateLeft(n % 16)` 。

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
    val result = source.`rotateLeft`(2)
    println(result)
}
```

```text title="输出"
20
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
