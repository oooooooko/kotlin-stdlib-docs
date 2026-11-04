# reduceOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

积累值,从第一个元素开始,从左向右应用 `operation` ,到目前的累积值和每个元素。

如果数组为空,则返回`null`。

@param `operation` 函数,它使用当前累积值和元素,计算下一个累积值。

@sample 样本、采集的样本、采集的采集物、分类、Ornull

??? note "查看英文原文"

    Accumulates value starting with the first element and applying `operation` from left to right
    to current accumulator value and each element.
    
    Returns `null` if the array is empty.
    
    @param `operation` function that takes current accumulator value and an element,
    and calculates the next accumulator value.
    
    @sample samples.collections.Collections.Aggregates.reduceOrNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <S, T : S> Array<out T>.reduceOrNull(operation: (acc: S, T) -> S): S?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23191)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public inline fun ByteArray.reduceOrNull(operation: (acc: Byte, Byte) -> Byte): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23213)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public inline fun ShortArray.reduceOrNull(operation: (acc: Short, Short) -> Short): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23235)

### 4. Common

```kotlin
@SinceKotlin("1.4")
public inline fun IntArray.reduceOrNull(operation: (acc: Int, Int) -> Int): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23257)

### 5. Common

```kotlin
@SinceKotlin("1.4")
public inline fun LongArray.reduceOrNull(operation: (acc: Long, Long) -> Long): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23279)

### 6. Common

```kotlin
@SinceKotlin("1.4")
public inline fun FloatArray.reduceOrNull(operation: (acc: Float, Float) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23301)

### 7. Common

```kotlin
@SinceKotlin("1.4")
public inline fun DoubleArray.reduceOrNull(operation: (acc: Double, Double) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23323)

### 8. Common

```kotlin
@SinceKotlin("1.4")
public inline fun BooleanArray.reduceOrNull(operation: (acc: Boolean, Boolean) -> Boolean): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23345)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public inline fun CharArray.reduceOrNull(operation: (acc: Char, Char) -> Char): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23367)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <S, T : S> Iterable<T>.reduceOrNull(operation: (acc: S, T) -> S): S?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3168)

积累值,从第一个元素开始,从左向右应用 `operation` ,到目前的累积值和每个元素。

如果收藏为空,则返回`null`。

@param `operation` 函数,它使用当前累积值和元素,计算下一个累积值。

@sample 样本、采集的样本、采集的采集物、分类、Ornull

### 11. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reduceOrNull(operation: (acc: UInt, UInt) -> UInt): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10231)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reduceOrNull(operation: (acc: ULong, ULong) -> ULong): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10255)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reduceOrNull(operation: (acc: UByte, UByte) -> UByte): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10279)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reduceOrNull(operation: (acc: UShort, UShort) -> UShort): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10303)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceOrNull { acc, string -> acc + string })
    println(strings.reduceIndexedOrNull { index, acc, string -> acc + string + index })

    println(emptyList<String>().reduceOrNull { _, _ -> "" })
}
```

```text title="输出"
abcd
ab1c2d3
null
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1255)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
