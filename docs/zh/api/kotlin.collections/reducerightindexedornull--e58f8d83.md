# reduceRightIndexedOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

积累值,从最后一个元素开始,对每个元素从右到左应用`operation`,并按其原有数组和当前累积值的索引计算。

如果数组为空,则返回`null`。

@param `operation` 函数,该函数采用元素的索引、元素本身和当前累积值,并计算下一个累积值。

@sample 样本、采集的样本、采集的采集物、分类、 分选的RiightOrnull

??? note "查看英文原文"

    Accumulates value starting with the last element and applying `operation` from right to left
    to each element with its index in the original array and current accumulator value.
    
    Returns `null` if the array is empty.
    
    @param `operation` function that takes the index of an element, the element itself and current accumulator value,
    and calculates the next accumulator value.
    
    @sample samples.collections.Collections.Aggregates.reduceRightOrNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <S, T : S> Array<out T>.reduceRightIndexedOrNull(operation: (index: Int, T, acc: S) -> S): S?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23794)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public inline fun ByteArray.reduceRightIndexedOrNull(operation: (index: Int, Byte, acc: Byte) -> Byte): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23817)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public inline fun ShortArray.reduceRightIndexedOrNull(operation: (index: Int, Short, acc: Short) -> Short): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23840)

### 4. Common

```kotlin
@SinceKotlin("1.4")
public inline fun IntArray.reduceRightIndexedOrNull(operation: (index: Int, Int, acc: Int) -> Int): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23863)

### 5. Common

```kotlin
@SinceKotlin("1.4")
public inline fun LongArray.reduceRightIndexedOrNull(operation: (index: Int, Long, acc: Long) -> Long): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23886)

### 6. Common

```kotlin
@SinceKotlin("1.4")
public inline fun FloatArray.reduceRightIndexedOrNull(operation: (index: Int, Float, acc: Float) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23909)

### 7. Common

```kotlin
@SinceKotlin("1.4")
public inline fun DoubleArray.reduceRightIndexedOrNull(operation: (index: Int, Double, acc: Double) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23932)

### 8. Common

```kotlin
@SinceKotlin("1.4")
public inline fun BooleanArray.reduceRightIndexedOrNull(operation: (index: Int, Boolean, acc: Boolean) -> Boolean): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23955)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public inline fun CharArray.reduceRightIndexedOrNull(operation: (index: Int, Char, acc: Char) -> Char): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23978)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <S, T : S> List<T>.reduceRightIndexedOrNull(operation: (index: Int, T, acc: S) -> S): S?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3237)

积累值,从最后一个元素开始,对每个元素从右到左应用`operation`,同时在原始列表中的索引和当前累积值中应用`operation`。

如果列表为空,则返回`null`。

@param `operation` 函数,该函数采用元素的索引、元素本身和当前累积值,并计算下一个累积值。

@sample 样本、采集的样本、采集的采集物、分类、 分选的RiightOrnull

### 11. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reduceRightIndexedOrNull(operation: (index: Int, UInt, acc: UInt) -> UInt): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10531)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reduceRightIndexedOrNull(operation: (index: Int, ULong, acc: ULong) -> ULong): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10556)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reduceRightIndexedOrNull(operation: (index: Int, UByte, acc: UByte) -> UByte): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10581)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reduceRightIndexedOrNull(operation: (index: Int, UShort, acc: UShort) -> UShort): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10606)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceRightOrNull { string, acc -> acc + string })
    println(strings.reduceRightIndexedOrNull { index, string, acc -> acc + string + index })

    println(emptyList<String>().reduceRightOrNull { _, _ -> "" })
}
```

```text title="输出"
dcba
dc2b1a0
null
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1264)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
