# isSortedDescending

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparable.compareTo`,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

For elements of floating-point types (`Double`, `Float`), `NaN` is considered greater
than any other value (including positive infinity), and `-0.0` is considered less than `0.0`,
consistent with `Double.compareTo` and `Float.compareTo`.

@sample samples.generated.issorted.IsSortedArraySamples.isSortedDescending

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Array<out T>.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6237)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public fun ByteArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6258)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedByteArraySamples.isSortedDescending

### 3. Common

```kotlin
@SinceKotlin("2.4")
public fun ShortArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6278)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedShortArraySamples.isSortedDescending

### 4. Common

```kotlin
@SinceKotlin("2.4")
public fun IntArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6298)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedIntArraySamples.isSortedDescending

### 5. Common

```kotlin
@SinceKotlin("2.4")
public fun LongArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6318)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedLongArraySamples.isSortedDescending

### 6. Common

```kotlin
@SinceKotlin("2.4")
public fun FloatArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6338)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Float.compareTo`,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

For floating-point arrays, `NaN` is considered greater than any other value
(including positive infinity), and `-0.0` is considered less than `0.0`,
consistent with `Float.compareTo`.

@sample samples.generated.issorted.IsSortedFloatArraySamples.isSortedDescending

### 7. Common

```kotlin
@SinceKotlin("2.4")
public fun DoubleArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6362)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Double.compareTo`,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

For floating-point arrays, `NaN` is considered greater than any other value
(including positive infinity), and `-0.0` is considered less than `0.0`,
consistent with `Double.compareTo`.

@sample samples.generated.issorted.IsSortedDoubleArraySamples.isSortedDescending

### 8. Common

```kotlin
@SinceKotlin("2.4")
public fun BooleanArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6386)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedBooleanArraySamples.isSortedDescending

### 9. Common

```kotlin
@SinceKotlin("2.4")
public fun CharArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6406)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedCharArraySamples.isSortedDescending

### 10. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Iterable<T>.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1087)

Returns `true` if each element in the collection is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the collection has fewer than two elements.

The elements are compared sequentially using `Comparable.compareTo`,
and the collection is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

Note that the result depends on the iteration order of the collection.
The iteration order of some `Iterable` implementations may be unstable
(change from one invocation to the next),
in which case this function may return inconsistent results.

For elements of floating-point types (`Double`, `Float`), `NaN` is considered greater
than any other value (including positive infinity), and `-0.0` is considered less than `0.0`,
consistent with `Double.compareTo` and `Float.compareTo`.

@sample samples.generated.issorted.IsSortedIterablesSamples.isSortedDescending

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UIntArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3067)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedUIntArraySamples.isSortedDescending

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun ULongArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3088)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedULongArraySamples.isSortedDescending

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UByteArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3109)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedUByteArraySamples.isSortedDescending

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UShortArray.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3130)

Returns `true` if each element in the array is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

@sample samples.generated.issorted.IsSortedUShortArraySamples.isSortedDescending

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSortedDescending())
    println(arrayOf("cherry").isSortedDescending())

    val sorted = arrayOf("cherry", "banana", "apple")
    println(sorted.isSortedDescending())

    val unsorted = arrayOf("banana", "cherry", "apple")
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L30)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSortedDescending())
    println(byteArrayOf(5).isSortedDescending())

    val sorted = byteArrayOf(5, 4, 3, 2, 1)
    println(sorted.isSortedDescending())

    val unsorted = byteArrayOf(4, 5, 3, 2, 1)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L31)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSortedDescending())
    println(shortArrayOf(5).isSortedDescending())

    val sorted = shortArrayOf(5, 4, 3, 2, 1)
    println(sorted.isSortedDescending())

    val unsorted = shortArrayOf(4, 5, 3, 2, 1)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L31)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSortedDescending())
    println(intArrayOf(5).isSortedDescending())

    val sorted = intArrayOf(5, 4, 3, 2, 1)
    println(sorted.isSortedDescending())

    val unsorted = intArrayOf(4, 5, 3, 2, 1)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L31)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSortedDescending())
    println(longArrayOf(5L).isSortedDescending())

    val sorted = longArrayOf(5L, 4L, 3L, 2L, 1L)
    println(sorted.isSortedDescending())

    val unsorted = longArrayOf(4L, 5L, 3L, 2L, 1L)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L31)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSortedDescending())
    println(floatArrayOf(3.14f).isSortedDescending())

    val sorted = floatArrayOf(3.14f, 2.5f, 1.0f)
    println(sorted.isSortedDescending())

    val unsorted = floatArrayOf(2.5f, 3.14f, 1.0f)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L31)

### Example 7 · JVM

```kotlin title="Example 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSortedDescending())
    println(doubleArrayOf(3.14).isSortedDescending())

    val sorted = doubleArrayOf(3.14, 2.5, 1.0)
    println(sorted.isSortedDescending())

    val unsorted = doubleArrayOf(2.5, 3.14, 1.0)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L31)

### Example 8 · JVM

```kotlin title="Example 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSortedDescending())
    println(booleanArrayOf(true).isSortedDescending())

    val sorted = booleanArrayOf(true, false, false)
    println(sorted.isSortedDescending())

    val unsorted = booleanArrayOf(false, true, false)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L30)

### Example 9 · JVM

```kotlin title="Example 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSortedDescending())
    println(charArrayOf('c').isSortedDescending())

    val sorted = charArrayOf('c', 'b', 'a')
    println(sorted.isSortedDescending())

    val unsorted = charArrayOf('b', 'c', 'a')
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L30)

### Example 10 · JVM

```kotlin title="Example 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSortedDescending())
    println(listOf("cherry").isSortedDescending())

    val sorted = listOf("cherry", "banana", "apple")
    println(sorted.isSortedDescending())

    val unsorted = listOf("banana", "cherry", "apple")
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L30)

### Example 11 · JVM

```kotlin title="Example 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSortedDescending())
    println(uintArrayOf(5u).isSortedDescending())

    val sorted = uintArrayOf(5u, 4u, 3u, 2u, 1u)
    println(sorted.isSortedDescending())

    val unsorted = uintArrayOf(4u, 5u, 3u, 2u, 1u)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L30)

### Example 12 · JVM

```kotlin title="Example 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSortedDescending())
    println(ulongArrayOf(5uL).isSortedDescending())

    val sorted = ulongArrayOf(5uL, 4uL, 3uL, 2uL, 1uL)
    println(sorted.isSortedDescending())

    val unsorted = ulongArrayOf(4uL, 5uL, 3uL, 2uL, 1uL)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L30)

### Example 13 · JVM

```kotlin title="Example 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSortedDescending())
    println(ubyteArrayOf(5u).isSortedDescending())

    val sorted = ubyteArrayOf(5u, 4u, 3u, 2u, 1u)
    println(sorted.isSortedDescending())

    val unsorted = ubyteArrayOf(4u, 5u, 3u, 2u, 1u)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L30)

### Example 14 · JVM

```kotlin title="Example 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSortedDescending())
    println(ushortArrayOf(5u).isSortedDescending())

    val sorted = ushortArrayOf(5u, 4u, 3u, 2u, 1u)
    println(sorted.isSortedDescending())

    val unsorted = ushortArrayOf(4u, 5u, 3u, 2u, 1u)
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L30)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
