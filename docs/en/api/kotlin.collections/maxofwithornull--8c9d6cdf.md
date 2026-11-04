# maxOfWithOrNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithGeneric

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R> Array<out T>.maxOfWithOrNull(comparator: Comparator<in R>, selector: (T) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18591)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> ByteArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Byte) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18615)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 3. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> ShortArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Short) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18639)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 4. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> IntArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Int) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18663)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 5. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> LongArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Long) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18687)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 6. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> FloatArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Float) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18711)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 7. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> DoubleArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Double) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18735)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 8. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> BooleanArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Boolean) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18759)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 9. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> CharArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Char) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18783)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 10. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R> Iterable<T>.maxOfWithOrNull(comparator: Comparator<in R>, selector: (T) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2520)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the collection or `null` if the collection is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithGeneric

### 11. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V, R> Map<out K, V>.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Map.Entry<K, V>) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L384)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each entry in the map or `null` if the map is empty.

If multiple entries produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithGeneric

### 12. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UIntArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (UInt) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8079)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 13. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> ULongArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (ULong) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8104)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 14. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UByteArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (UByte) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8129)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

### 15. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UShortArray.maxOfWithOrNull(comparator: Comparator<in R>, selector: (UShort) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8154)

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithPrimitive

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
Silver Bullet
Red Sand
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1190)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
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

```text title="Output"
-64
1
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1169)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
