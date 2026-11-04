# minByOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回第一个生成给定 `selector` 函数最小值的元素,如果没有元素,返回 `null` 函数最小值。

如果 `selector` 函数返回了多个等值最小值,则此函数返回与这些值相应的第一个元素。

请注意当数组含有零或一个元素时,不会援引 `selector` 函数,因为在这种情况下,可以清楚返回哪个元素而不援引`selector`。 因此建议避免依赖`selector`函数对每个元素的副作用。

@sample 样本、采集的样本、采集的采集量、采集的样本、 分类、 最小量By OrNull

??? note "查看英文原文"

    Returns the first element yielding the smallest value of the given `selector` function or `null` if there are no elements.
    
    If there are multiple equal minimal values returned by the `selector` function,
    this function returns the first of elements corresponding to these values.
    
    Note that the function `selector` is not invoked when the array contains zero or one elements
    because in these cases it is clear which element to return without invoking the `selector`.
    Therefore it's recommended to avoid relying on side effects being performed by the `selector` function on each element.
    
    @sample samples.collections.Collections.Aggregates.minMaxByOrNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <T, R : Comparable<R>> Array<out T>.minByOrNull(selector: (T) -> R): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19781)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> ByteArray.minByOrNull(selector: (Byte) -> R): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19811)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> ShortArray.minByOrNull(selector: (Short) -> R): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19841)

### 4. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> IntArray.minByOrNull(selector: (Int) -> R): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19871)

### 5. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> LongArray.minByOrNull(selector: (Long) -> R): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19901)

### 6. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> FloatArray.minByOrNull(selector: (Float) -> R): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19931)

### 7. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> DoubleArray.minByOrNull(selector: (Double) -> R): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19961)

### 8. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> BooleanArray.minByOrNull(selector: (Boolean) -> R): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19991)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> CharArray.minByOrNull(selector: (Char) -> R): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20021)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <T, R : Comparable<R>> Iterable<T>.minByOrNull(selector: (T) -> R): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2739)

返回第一个生成给定 `selector` 函数最小值的元素,如果没有元素,返回 `null` 函数最小值。

如果 `selector` 函数返回了多个等值最小值,则此函数返回与这些值相应的第一个元素。

请注意,当收藏含有零或一个元素时,不会援引 `selector` 函数,因为在这种情况下,清楚可以不援引`selector`函数返回哪个元素。 因此,建议避免依赖`selector`函数对每个元素的副作用。

@sample 样本、采集的样本、采集的采集量、采集的样本、 分类、 最小量By OrNull

### 11. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun <K, V, R : Comparable<R>> Map<out K, V>.minByOrNull(selector: (Map.Entry<K, V>) -> R): Map.Entry<K, V>?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L444)

返回第一个产生给定 `selector` 函数最小值的条目,如果没有输入,则返回 `null` 最小值。

如果 `selector` 函数返回了多个等值最小值,此函数返回这些值对应的第一个条目。

请注意,当地图包含零或一个条目时, 函数 `selector` 不被引用, 因为在这种情况下, 清楚可以返回哪个条目而不引用 `selector` 。 因此, 建议避免依赖 `selector` 函数对每个条目的副作用 。

@sample 样本、采集的样本、采集的采集量、采集的样本、 分类、 最小量By OrNull

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UIntArray.minByOrNull(selector: (UInt) -> R): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8611)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ULongArray.minByOrNull(selector: (ULong) -> R): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8643)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UByteArray.minByOrNull(selector: (UByte) -> R): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8675)

### 15. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UShortArray.minByOrNull(selector: (UShort) -> R): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8707)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val strings = listOf("abcd", "abc", "ab", "de", "abcde")

    val longestString = strings.maxBy { it.length }
    println(longestString)

    val shortestString = strings.minBy { it.length }
    println(shortestString)

    val emptyList = emptyList<String>()
    // maxBy() and minBy() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.maxBy { it.length } }
    assertFailsWith<NoSuchElementException> { emptyList.minBy { it.length } }
    // maxByOrNull() and minByOrNull() return null if the collection is empty
    println(emptyList.maxByOrNull { it.length })
    println(emptyList.minByOrNull { it.length })
}
```

```text title="输出"
abcde
ab
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1218)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
