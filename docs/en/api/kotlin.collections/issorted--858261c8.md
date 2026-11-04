# isSorted

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparable.compareTo`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

For elements of floating-point types (`Double`, `Float`), `NaN` is considered greater
than any other value (including positive infinity), and `-0.0` is considered less than `0.0`,
consistent with `Double.compareTo` and `Float.compareTo`.

@sample samples.generated.issorted.IsSortedArraySamples.isSorted

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Array<out T>.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5553)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public fun ByteArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5574)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedByteArraySamples.isSorted

### 3. Common

```kotlin
@SinceKotlin("2.4")
public fun ShortArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5594)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedShortArraySamples.isSorted

### 4. Common

```kotlin
@SinceKotlin("2.4")
public fun IntArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5614)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedIntArraySamples.isSorted

### 5. Common

```kotlin
@SinceKotlin("2.4")
public fun LongArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5634)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedLongArraySamples.isSorted

### 6. Common

```kotlin
@SinceKotlin("2.4")
public fun FloatArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5654)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Float.compareTo`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

For floating-point arrays, `NaN` is considered greater than any other value
(including positive infinity), and `-0.0` is considered less than `0.0`,
consistent with `Float.compareTo`.

@sample samples.generated.issorted.IsSortedFloatArraySamples.isSorted

### 7. Common

```kotlin
@SinceKotlin("2.4")
public fun DoubleArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5678)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Double.compareTo`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

For floating-point arrays, `NaN` is considered greater than any other value
(including positive infinity), and `-0.0` is considered less than `0.0`,
consistent with `Double.compareTo`.

@sample samples.generated.issorted.IsSortedDoubleArraySamples.isSorted

### 8. Common

```kotlin
@SinceKotlin("2.4")
public fun BooleanArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5702)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedBooleanArraySamples.isSorted

### 9. Common

```kotlin
@SinceKotlin("2.4")
public fun CharArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5722)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedCharArraySamples.isSorted

### 10. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Iterable<T>.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L984)

Returns `true` if each element in the collection is less than or equal
to the following element according to their natural sort order.

Returns `true` if the collection has fewer than two elements.

The elements are compared sequentially using `Comparable.compareTo`,
and the collection is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

Note that the result depends on the iteration order of the collection.
The iteration order of some `Iterable` implementations may be unstable
(change from one invocation to the next),
in which case this function may return inconsistent results.

For elements of floating-point types (`Double`, `Float`), `NaN` is considered greater
than any other value (including positive infinity), and `-0.0` is considered less than `0.0`,
consistent with `Double.compareTo` and `Float.compareTo`.

@sample samples.generated.issorted.IsSortedIterablesSamples.isSorted

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UIntArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2755)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedUIntArraySamples.isSorted

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun ULongArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2776)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedULongArraySamples.isSorted

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UByteArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2797)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedUByteArraySamples.isSorted

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UShortArray.isSorted(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2818)

Returns `true` if each element in the array is less than or equal
to the following element according to their natural sort order.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedUShortArraySamples.isSorted

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSorted())
    println(arrayOf("apple").isSorted())

    val sorted = arrayOf("apple", "banana", "cherry")
    println(sorted.isSorted())

    val unsorted = arrayOf("banana", "apple", "cherry")
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L18)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSorted())
    println(byteArrayOf(1).isSorted())

    val sorted = byteArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSorted())

    val unsorted = byteArrayOf(2, 1, 3, 4, 5)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L19)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSorted())
    println(shortArrayOf(1).isSorted())

    val sorted = shortArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSorted())

    val unsorted = shortArrayOf(2, 1, 3, 4, 5)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L19)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSorted())
    println(intArrayOf(1).isSorted())

    val sorted = intArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSorted())

    val unsorted = intArrayOf(2, 1, 3, 4, 5)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L19)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSorted())
    println(longArrayOf(1L).isSorted())

    val sorted = longArrayOf(1L, 2L, 3L, 4L, 5L)
    println(sorted.isSorted())

    val unsorted = longArrayOf(2L, 1L, 3L, 4L, 5L)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L19)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSorted())
    println(floatArrayOf(1.0f).isSorted())

    val sorted = floatArrayOf(1.0f, 2.5f, 3.14f)
    println(sorted.isSorted())

    val unsorted = floatArrayOf(2.5f, 1.0f, 3.14f)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L19)

### Example 7 · JVM

```kotlin title="Example 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSorted())
    println(doubleArrayOf(1.0).isSorted())

    val sorted = doubleArrayOf(1.0, 2.5, 3.14)
    println(sorted.isSorted())

    val unsorted = doubleArrayOf(2.5, 1.0, 3.14)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L19)

### Example 8 · JVM

```kotlin title="Example 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSorted())
    println(booleanArrayOf(false).isSorted())

    val sorted = booleanArrayOf(false, false, true)
    println(sorted.isSorted())

    val unsorted = booleanArrayOf(false, true, false)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L18)

### Example 9 · JVM

```kotlin title="Example 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSorted())
    println(charArrayOf('a').isSorted())

    val sorted = charArrayOf('a', 'b', 'c')
    println(sorted.isSorted())

    val unsorted = charArrayOf('b', 'a', 'c')
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L18)

### Example 10 · JVM

```kotlin title="Example 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSorted())
    println(listOf("apple").isSorted())

    val sorted = listOf("apple", "banana", "cherry")
    println(sorted.isSorted())

    val unsorted = listOf("banana", "apple", "cherry")
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L18)

### Example 11 · JVM

```kotlin title="Example 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSorted())
    println(uintArrayOf(1u).isSorted())

    val sorted = uintArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSorted())

    val unsorted = uintArrayOf(2u, 1u, 3u, 4u, 5u)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L18)

### Example 12 · JVM

```kotlin title="Example 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSorted())
    println(ulongArrayOf(1uL).isSorted())

    val sorted = ulongArrayOf(1uL, 2uL, 3uL, 4uL, 5uL)
    println(sorted.isSorted())

    val unsorted = ulongArrayOf(2uL, 1uL, 3uL, 4uL, 5uL)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L18)

### Example 13 · JVM

```kotlin title="Example 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSorted())
    println(ubyteArrayOf(1u).isSorted())

    val sorted = ubyteArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSorted())

    val unsorted = ubyteArrayOf(2u, 1u, 3u, 4u, 5u)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L18)

### Example 14 · JVM

```kotlin title="Example 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSorted())
    println(ushortArrayOf(1u).isSorted())

    val sorted = ushortArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSorted())

    val unsorted = ushortArrayOf(2u, 1u, 3u, 4u, 5u)
    println(unsorted.isSorted())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L18)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
