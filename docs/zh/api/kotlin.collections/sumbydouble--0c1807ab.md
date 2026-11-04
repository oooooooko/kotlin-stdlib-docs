# sumByDouble

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 `selector` 函数产生的所有数值的和,这些数值适用于数组中的每一元素。

??? note "查看英文原文"

    Returns the sum of all values produced by `selector` function applied to each element in the array.

## 声明与重载

### 1. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun <T> Array<out T>.sumByDouble(selector: (T) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25459)

### 2. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun ByteArray.sumByDouble(selector: (Byte) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25472)

### 3. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun ShortArray.sumByDouble(selector: (Short) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25485)

### 4. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun IntArray.sumByDouble(selector: (Int) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25498)

### 5. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun LongArray.sumByDouble(selector: (Long) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25511)

### 6. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun FloatArray.sumByDouble(selector: (Float) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25524)

### 7. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun DoubleArray.sumByDouble(selector: (Double) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25537)

### 8. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun BooleanArray.sumByDouble(selector: (Boolean) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25550)

### 9. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun CharArray.sumByDouble(selector: (Char) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25563)

### 10. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun <T> Iterable<T>.sumByDouble(selector: (T) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3430)

返回 `selector` 函数产生的所有数值的总和,该函数适用于收藏中的每个元素。

### 11. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.sumByDouble(selector: (UInt) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11347)

### 12. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.sumByDouble(selector: (ULong) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11363)

### 13. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.sumByDouble(selector: (UByte) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11379)

### 14. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.sumByDouble(selector: (UShort) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11395)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

private class OperationOnRange<E, R>(
        val element: E,
        val fromIndex: Int,
        val toIndex: Int,
        val expectedResult: R
    )

private fun UIntArray.toUByteArray(): UByteArray {
    return UByteArray(size) { get(it).toUByte() }
}

private fun UIntArray.toUShortArray(): UShortArray {
    return UShortArray(size) { get(it).toUShort() }
}

private fun UIntArray.toULongArray(): ULongArray {
    return ULongArray(size) { get(it).toULong() }
}

fun main() {

        println(ubyteArrayOf(0u, 1u, 2u).sumByDouble { it.toDouble() })
        println(ushortArrayOf(0u, 1u, 2u).sumByDouble { (it % 2u).toDouble() })
        println(uintArrayOf(0u, 2u, 4u).sumByDouble { (it % 2u).toDouble() })
        println(ulongArrayOf(2u, 3u, 4u).sumByDouble { (it - 1u).toDouble() })
    
}
```

```text title="输出"
3.0
1.0
0.0
6.0
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/UnsignedArraysTest.kt#L365)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
