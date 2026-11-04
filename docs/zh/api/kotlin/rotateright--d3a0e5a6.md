# rotateRight

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将这个 `Int` 数字的二进制表示法旋转为指定的 `bitCount` 位数。从右侧推出的最小的位数作为左侧最重要的位数重新输入。

右转数字的负位数与以负位数旋转数字的负位数相同,即 `number.rotateRight(-n) == number.rotateLeft(n)` 。

乘以 `Int.SIZE_BITS` (32)乘以乘以 `Int.SIZE_BITS` , 返回相同数, 或更一般的 `number.rotateRight(n) == number.rotateRight(n % 32)`

??? note "查看英文原文"

    Rotates the binary representation of this `Int` number right by the specified `bitCount` number of bits.
    The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.
    
    Rotating the number right by a negative bit count is the same as rotating it left by the negated bit count:
    `number.rotateRight(-n) == number.rotateLeft(n)`
    
    Rotating by a multiple of `Int.SIZE_BITS` (32) returns the same number, or more generally
    `number.rotateRight(n) == number.rotateRight(n % 32)`

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
public expect fun Int.rotateRight(bitCount: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L56)

### 2. Common

```kotlin
@SinceKotlin("1.6")
public expect fun Long.rotateRight(bitCount: Int): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L115)

将这个 `Long` 数字的二进制表示法旋转为指定的 `bitCount` 位数。从右侧推出的最小的位数作为左侧最重要的位数重新输入。

右转数字的负位数与以负位数旋转数字的负位数相同,即 `number.rotateRight(-n) == number.rotateLeft(n)` 。

乘以 `Long.SIZE_BITS` (64)乘以乘以 `Long.SIZE_BITS` , 返回相同数, 或更一般的 `number.rotateRight(n) == number.rotateRight(n % 64)`

### 3. Common

```kotlin
@SinceKotlin("1.6")
public fun Byte.rotateRight(bitCount: Int): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L180)

将这个 `Byte` 数字的二进制表示法旋转为指定的 `bitCount` 位数。从右侧推出的最小的位数作为左侧最重要的位数重新输入。

右转数字的负位数与以负位数旋转数字的负位数相同,即 `number.rotateRight(-n) == number.rotateLeft(n)` 。

乘以 `Byte.SIZE_BITS` (8)乘以乘以 `Byte.SIZE_BITS` (8), 返回相同数字, 或更一般的 `number.rotateRight(n) == number.rotateRight(n % 8)`

### 4. Common

```kotlin
@SinceKotlin("1.6")
public fun Short.rotateRight(bitCount: Int): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L247)

将这个 `Short` 数字的二进制表示法旋转为指定的 `bitCount` 位数。从右侧推出的最小的位数作为左侧最重要的位数重新输入。

右转数字的负位数与以负位数旋转数字的负位数相同,即 `number.rotateRight(-n) == number.rotateLeft(n)` 。

乘以 `Short.SIZE_BITS` (16)乘以乘以 `Short.SIZE_BITS` (16),返回同数,或更一般地说, `number.rotateRight(n) == number.rotateRight(n % 16)` 。

### 5. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun UInt.rotateRight(bitCount: Int): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L61)

将这个 `UInt` 数字的二进制表示法旋转为指定的 `bitCount` 位数。从右侧推出的最小的位数作为左侧最重要的位数重新输入。

右转数字的负位数与以负位数旋转数字的负位数相同,即 `number.rotateRight(-n) == number.rotateLeft(n)` 。

乘以 `UInt.SIZE_BITS` (32)乘以乘以 `UInt.SIZE_BITS` , 返回相同数, 或更一般的 `number.rotateRight(n) == number.rotateRight(n % 32)`

### 6. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun ULong.rotateRight(bitCount: Int): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L127)

将这个 `ULong` 数字的二进制表示法旋转为指定的 `bitCount` 位数。从右侧推出的最小的位数作为左侧最重要的位数重新输入。

右转数字的负位数与以负位数旋转数字的负位数相同,即 `number.rotateRight(-n) == number.rotateLeft(n)` 。

乘以 `ULong.SIZE_BITS` (64)乘以乘以 `ULong.SIZE_BITS` , 返回相同数, 或更一般的 `number.rotateRight(n) == number.rotateRight(n % 64)`

### 7. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun UByte.rotateRight(bitCount: Int): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L193)

将这个 `UByte` 数字的二进制表示法旋转为指定的 `bitCount` 位数。从右侧推出的最小的位数作为左侧最重要的位数重新输入。

右转数字的负位数与以负位数旋转数字的负位数相同,即 `number.rotateRight(-n) == number.rotateLeft(n)` 。

乘以 `UByte.SIZE_BITS` (8)乘以乘以 `UByte.SIZE_BITS` (8), 返回相同数字, 或更一般的 `number.rotateRight(n) == number.rotateRight(n % 8)`

### 8. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun UShort.rotateRight(bitCount: Int): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L259)

将这个 `UShort` 数字的二进制表示法旋转为指定的 `bitCount` 位数。从右侧推出的最小的位数作为左侧最重要的位数重新输入。

右转数字的负位数与以负位数旋转数字的负位数相同,即 `number.rotateRight(-n) == number.rotateLeft(n)` 。

乘以 `UShort.SIZE_BITS` (16)乘以乘以 `UShort.SIZE_BITS` (16),返回同数,或更一般地说, `number.rotateRight(n) == number.rotateRight(n % 16)` 。

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
    val result = source.`rotateRight`(2)
    println(result)
}
```

```text title="输出"
1073741825
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
