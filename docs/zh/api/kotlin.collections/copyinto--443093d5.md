# copyInto

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此数组或其子组合复制为 `destination` 数组并返回该数组。

它可以通过`destination`的相同阵列 甚至指定子阵列 以便与目的地范围重叠

@param 将复制的数组复制为 @param 目的端点 。 `destination` 将 `destination` 数组的位置切换为 0 。 @param 开始于 将子范围开始( 包括) 复制, 0 默认为 0 。 @param 结束于 Index 将子范围结束( 排他) 复制, 默认为此数组大小 。

当`startIndex`或`endIndex`不在这种阵列指数范围或`startIndex > endIndex`时,@throws指数外出或`IllegalArgumentException`。
@throws 指数外观除以子序列不适应`destination`阵列时的例外,该子序列从指定的`destinationOffset`开始,
当该索引超出`destination` 矩阵指数范围时。

@return `destination` 阵列。

??? note "查看英文原文"

    Copies this array or its subrange into the `destination` array and returns that array.
    
    It's allowed to pass the same array in the `destination` and even specify the subrange so that it overlaps with the destination range.
    
    @param destination the array to copy to.
    @param destinationOffset the position in the `destination` array to copy to, 0 by default.
    @param startIndex the beginning (inclusive) of the subrange to copy, 0 by default.
    @param endIndex the end (exclusive) of the subrange to copy, size of this array by default.
    
    @throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of this array indices or when `startIndex > endIndex`.
    @throws IndexOutOfBoundsException when the subrange doesn't fit into the `destination` array starting at the specified `destinationOffset`,
    or when that index is out of the `destination` array indices range.
    
    @return the `destination` array.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public expect fun <T> Array<out T>.copyInto(destination: Array<T>, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): Array<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8496)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public expect fun ByteArray.copyInto(destination: ByteArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8516)

### 3. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public expect fun ShortArray.copyInto(destination: ShortArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): ShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8536)

### 4. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public expect fun IntArray.copyInto(destination: IntArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): IntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8556)

### 5. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public expect fun LongArray.copyInto(destination: LongArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): LongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8576)

### 6. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public expect fun FloatArray.copyInto(destination: FloatArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): FloatArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8596)

### 7. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public expect fun DoubleArray.copyInto(destination: DoubleArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): DoubleArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8616)

### 8. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public expect fun BooleanArray.copyInto(destination: BooleanArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): BooleanArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8636)

### 9. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public expect fun CharArray.copyInto(destination: CharArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8656)

### 10. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.copyInto(destination: UIntArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): UIntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4043)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.copyInto(destination: ULongArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4068)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.copyInto(destination: UByteArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4093)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.copyInto(destination: UShortArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): UShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4118)

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
import kotlin.collections.*

fun main() {
    val source = arrayOf(1, 2, 3)
    val result = source.`copyInto`(arrayOf(1, 2, 3))
    println(result.contentToString())
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
