# minBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回产生给定 `selector` 函数最小值的第一个元素。

如果 `selector` 函数返回了多个等值最小值,则此函数返回与这些值相应的第一个元素。

请注意当数组含有零或一个元素时,不会援引 `selector` 函数,因为在这种情况下,可以清楚返回哪个元素而不援引`selector`。 因此建议避免依赖`selector`函数对每个元素的副作用。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的采集量、采集的样本、 分类、 最小量By OrNull

??? note "查看英文原文"

    Returns the first element yielding the smallest value of the given `selector` function.
    
    If there are multiple equal minimal values returned by the `selector` function,
    this function returns the first of elements corresponding to these values.
    
    Note that the function `selector` is not invoked when the array contains zero or one elements
    because in these cases it is clear which element to return without invoking the `selector`.
    Therefore it's recommended to avoid relying on side effects being performed by the `selector` function on each element.
    
    @throws NoSuchElementException if the array is empty.
    
    @sample samples.collections.Collections.Aggregates.minMaxByOrNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <T, R : Comparable<R>> Array<out T>.minBy(selector: (T) -> R): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19475)

### 2. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> ByteArray.minBy(selector: (Byte) -> R): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19509)

### 3. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> ShortArray.minBy(selector: (Short) -> R): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19543)

### 4. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> IntArray.minBy(selector: (Int) -> R): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19577)

### 5. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> LongArray.minBy(selector: (Long) -> R): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19611)

### 6. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> FloatArray.minBy(selector: (Float) -> R): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19645)

### 7. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> DoubleArray.minBy(selector: (Double) -> R): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19679)

### 8. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> BooleanArray.minBy(selector: (Boolean) -> R): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19713)

### 9. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> CharArray.minBy(selector: (Char) -> R): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19747)

### 10. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <T, R : Comparable<R>> Iterable<T>.minBy(selector: (T) -> R): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2705)

返回产生给定 `selector` 函数最小值的第一个元素。

如果 `selector` 函数返回了多个等值最小值,则此函数返回与这些值相应的第一个元素。

请注意,当收藏含有零或一个元素时,不会援引 `selector` 函数,因为在这种情况下,清楚可以不援引`selector`函数返回哪个元素。 因此,建议避免依赖`selector`函数对每个元素的副作用。

@throws 否 元素 , 收藏为空时除外 。

@sample 样本、采集的样本、采集的采集量、采集的样本、 分类、 最小量By OrNull

### 11. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <K, V, R : Comparable<R>> Map<out K, V>.minBy(selector: (Map.Entry<K, V>) -> R): Map.Entry<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L422)

返回第一个产生给定 `selector` 函数最小值的条目。

如果 `selector` 函数返回了多个等值最小值,此函数返回这些值对应的第一个条目。

请注意,当地图包含零或一个条目时, 函数 `selector` 不被引用, 因为在这种情况下, 清楚可以返回哪个条目而不引用 `selector` 。 因此, 建议避免依赖 `selector` 函数对每个条目的副作用 。

@throws 否 元素, 如果地图为空则例外 。

@sample 样本、采集的样本、采集的采集量、采集的样本、 分类、 最小量By OrNull

### 12. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow-U")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> UIntArray.minBy(selector: (UInt) -> R): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8467)

### 13. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow-U")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> ULongArray.minBy(selector: (ULong) -> R): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8503)

### 14. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow-U")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> UByteArray.minBy(selector: (UByte) -> R): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8539)

### 15. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow-U")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> UShortArray.minBy(selector: (UShort) -> R): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8575)

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
