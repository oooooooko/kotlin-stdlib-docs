# maxOfWith

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与基因的混合样本、与基因的混合样本、

??? note "查看英文原文"

    Returns the largest value according to the provided `comparator`
    among all values produced by `selector` function applied to each element in the array.
    
    If multiple elements produce the maximal value, this function returns the first of those values.
    
    @throws NoSuchElementException if the array is empty.
    
    @sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithGeneric

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R> Array<out T>.maxOfWith(comparator: Comparator<in R>, selector: (T) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18357)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> ByteArray.maxOfWith(comparator: Comparator<in R>, selector: (Byte) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18383)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 3. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> ShortArray.maxOfWith(comparator: Comparator<in R>, selector: (Short) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18409)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 4. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> IntArray.maxOfWith(comparator: Comparator<in R>, selector: (Int) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18435)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 5. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> LongArray.maxOfWith(comparator: Comparator<in R>, selector: (Long) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18461)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 6. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> FloatArray.maxOfWith(comparator: Comparator<in R>, selector: (Float) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18487)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 7. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> DoubleArray.maxOfWith(comparator: Comparator<in R>, selector: (Double) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18513)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 8. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> BooleanArray.maxOfWith(comparator: Comparator<in R>, selector: (Boolean) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18539)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 9. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> CharArray.maxOfWith(comparator: Comparator<in R>, selector: (Char) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18565)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 10. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R> Iterable<T>.maxOfWith(comparator: Comparator<in R>, selector: (T) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2493)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值,`selector`函数适用于收藏中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 否 元素 , 收藏为空时除外 。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与基因的混合样本、与基因的混合样本、

### 11. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V, R> Map<out K, V>.maxOfWith(comparator: Comparator<in R>, selector: (Map.Entry<K, V>) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L366)

返回在以 `selector` 函数生成的800 0002 函数产生的所有数值中,根据提供的`comparator` 中的最大值,返回适用于地图中每个条目的最大值。

如果多个条目产生最大值,此函数返回这些值的第一个。

@throws 否 元素, 如果地图为空则例外 。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与基因的混合样本、与基因的混合样本、

### 12. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UIntArray.maxOfWith(comparator: Comparator<in R>, selector: (UInt) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7971)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 13. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> ULongArray.maxOfWith(comparator: Comparator<in R>, selector: (ULong) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7998)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 14. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UByteArray.maxOfWith(comparator: Comparator<in R>, selector: (UByte) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8025)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

### 15. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UShortArray.maxOfWith(comparator: Comparator<in R>, selector: (UShort) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8052)

返回根据 `comparator` 提供的`selector`函数产生的所有数值中最大值的最大值,该数值适用于数组中的每个元素。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 无效元素,如果数组为空,则例外。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与初始企业的混合样本

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    data class Book(val title: String, val publishYear: Int, val rating: Double)

    // A custom Comparator that orders strings by their length
    val lengthComparator = compareBy<String> { it.length }

    // The longest and shortest book titles
    val books = listOf(
        Book("Red Sand", 2004, 3.5),
        Book("Silver Bullet", 2009, 4.4),
        Book("Clear Water", 2018, 4.1),
        Book("Night Sky", 2023, 3.8)
    )
    println(books.maxOfWith(lengthComparator) { it.title })
    println(books.minOfWith(lengthComparator) { it.title })

    val emptyList = listOf<Book>()

    // maxOfWith() and minOfWith() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.maxOfWith(lengthComparator) { it.title } }
    assertFailsWith<NoSuchElementException> { emptyList.minOfWith(lengthComparator) { it.title } }

    // maxOfWithOrNull() and minOfWithOrNull() return null if the collection is empty
    println(emptyList.maxOfWithOrNull(lengthComparator) { it.title })
    println(emptyList.minOfWithOrNull(lengthComparator) { it.title })
}
```

```text title="输出"
Silver Bullet
Red Sand
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1190)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    // A custom Comparator that orders numbers by their absolute values
    val absComparator = compareBy<Int> { it.absoluteValue }

    // The largest and smallest cubic values when compared by absolute value
    val numbers = intArrayOf(-2, 3, -4, 1)
    println(numbers.maxOfWith(absComparator) { it * it * it })
    println(numbers.minOfWith(absComparator) { it * it * it })

    val emptyArray = intArrayOf()

    // maxOfWith() and minOfWith() throw if the array is empty
    assertFailsWith<NoSuchElementException> { emptyArray.maxOfWith(absComparator) { it * it * it } }
    assertFailsWith<NoSuchElementException> { emptyArray.minOfWith(absComparator) { it * it * it } }

    // maxOfWithOrNull() and minOfWithOrNull() return null if the array is empty
    println(emptyArray.maxOfWithOrNull(absComparator) { it * it * it })
    println(emptyArray.minOfWithOrNull(absComparator) { it * it * it })
}
```

```text title="输出"
-64
1
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1169)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
