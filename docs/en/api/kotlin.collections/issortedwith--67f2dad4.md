# isSortedWith

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedArraySamples.isSortedWith

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
public fun <T> Array<out T>.isSortedWith(comparator: Comparator<in T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6426)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public fun ByteArray.isSortedWith(comparator: Comparator<in Byte>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6446)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedByteArraySamples.isSortedWith

### 3. Common

```kotlin
@SinceKotlin("2.4")
public fun ShortArray.isSortedWith(comparator: Comparator<in Short>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6466)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedShortArraySamples.isSortedWith

### 4. Common

```kotlin
@SinceKotlin("2.4")
public fun IntArray.isSortedWith(comparator: Comparator<in Int>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6486)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedIntArraySamples.isSortedWith

### 5. Common

```kotlin
@SinceKotlin("2.4")
public fun LongArray.isSortedWith(comparator: Comparator<in Long>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6506)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedLongArraySamples.isSortedWith

### 6. Common

```kotlin
@SinceKotlin("2.4")
public fun FloatArray.isSortedWith(comparator: Comparator<in Float>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6526)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedFloatArraySamples.isSortedWith

### 7. Common

```kotlin
@SinceKotlin("2.4")
public fun DoubleArray.isSortedWith(comparator: Comparator<in Double>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6546)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedDoubleArraySamples.isSortedWith

### 8. Common

```kotlin
@SinceKotlin("2.4")
public fun BooleanArray.isSortedWith(comparator: Comparator<in Boolean>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6566)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedBooleanArraySamples.isSortedWith

### 9. Common

```kotlin
@SinceKotlin("2.4")
public fun CharArray.isSortedWith(comparator: Comparator<in Char>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6586)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedCharArraySamples.isSortedWith

### 10. Common

```kotlin
@SinceKotlin("2.4")
public fun <T> Iterable<T>.isSortedWith(comparator: Comparator<in T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1113)

Returns `true` if each element in the collection is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the collection has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the collection is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

Note that the result depends on the iteration order of the collection.
The iteration order of some `Iterable` implementations may be unstable
(change from one invocation to the next),
in which case this function may return inconsistent results.

@sample samples.generated.issorted.IsSortedIterablesSamples.isSortedWith

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UIntArray.isSortedWith(comparator: Comparator<in UInt>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3151)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedUIntArraySamples.isSortedWith

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun ULongArray.isSortedWith(comparator: Comparator<in ULong>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3172)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedULongArraySamples.isSortedWith

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UByteArray.isSortedWith(comparator: Comparator<in UByte>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3193)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedUByteArraySamples.isSortedWith

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UShortArray.isSortedWith(comparator: Comparator<in UShort>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3214)

Returns `true` if each element in the array is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the array has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the array is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

@sample samples.generated.issorted.IsSortedUShortArraySamples.isSortedWith

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSortedWith(naturalOrder()))
    println(arrayOf("apple").isSortedWith(naturalOrder()))

    val sorted = arrayOf("apple", "banana", "cherry")
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = arrayOf("cherry", "banana", "apple")
    println(reversed.isSortedWith(reverseOrder()))

    val caseInsensitive = arrayOf("Apple", "banana", "Cherry")
    println(caseInsensitive.isSortedWith(String.CASE_INSENSITIVE_ORDER))

    val withNulls = arrayOf(null, "apple", "banana")
    println(withNulls.isSortedWith(nullsFirst(naturalOrder())))
    println(withNulls.isSortedWith(nullsLast(naturalOrder())))
}
```

```text title="Output"
true
true
true
false
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L42)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSortedWith(naturalOrder()))
    println(byteArrayOf(1).isSortedWith(naturalOrder()))

    val sorted = byteArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = byteArrayOf(5, 4, 3, 2, 1)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L43)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSortedWith(naturalOrder()))
    println(shortArrayOf(1).isSortedWith(naturalOrder()))

    val sorted = shortArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = shortArrayOf(5, 4, 3, 2, 1)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L43)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSortedWith(naturalOrder()))
    println(intArrayOf(1).isSortedWith(naturalOrder()))

    val sorted = intArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = intArrayOf(5, 4, 3, 2, 1)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L43)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSortedWith(naturalOrder()))
    println(longArrayOf(1L).isSortedWith(naturalOrder()))

    val sorted = longArrayOf(1L, 2L, 3L, 4L, 5L)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = longArrayOf(5L, 4L, 3L, 2L, 1L)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L43)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSortedWith(naturalOrder()))
    println(floatArrayOf(1.0f).isSortedWith(naturalOrder()))

    val sorted = floatArrayOf(1.0f, 2.5f, 3.14f)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = floatArrayOf(3.14f, 2.5f, 1.0f)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L43)

### Example 7 · JVM

```kotlin title="Example 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSortedWith(naturalOrder()))
    println(doubleArrayOf(1.0).isSortedWith(naturalOrder()))

    val sorted = doubleArrayOf(1.0, 2.5, 3.14)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = doubleArrayOf(3.14, 2.5, 1.0)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L43)

### Example 8 · JVM

```kotlin title="Example 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSortedWith(naturalOrder()))
    println(booleanArrayOf(false).isSortedWith(naturalOrder()))

    val sorted = booleanArrayOf(false, false, true)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = booleanArrayOf(true, false, false)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L42)

### Example 9 · JVM

```kotlin title="Example 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSortedWith(naturalOrder()))
    println(charArrayOf('a').isSortedWith(naturalOrder()))

    val sorted = charArrayOf('a', 'b', 'c')
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = charArrayOf('c', 'b', 'a')
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L42)

### Example 10 · JVM

```kotlin title="Example 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSortedWith(naturalOrder()))
    println(listOf("apple").isSortedWith(naturalOrder()))

    val sorted = listOf("apple", "banana", "cherry")
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = listOf("cherry", "banana", "apple")
    println(reversed.isSortedWith(reverseOrder()))

    val caseInsensitive = listOf("Apple", "banana", "Cherry")
    println(caseInsensitive.isSortedWith(String.CASE_INSENSITIVE_ORDER))

    val withNulls = listOf(null, "apple", "banana")
    println(withNulls.isSortedWith(nullsFirst(naturalOrder())))
    println(withNulls.isSortedWith(nullsLast(naturalOrder())))
}
```

```text title="Output"
true
true
true
false
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L42)

### Example 11 · JVM

```kotlin title="Example 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSortedWith(naturalOrder()))
    println(uintArrayOf(1u).isSortedWith(naturalOrder()))

    val sorted = uintArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = uintArrayOf(5u, 4u, 3u, 2u, 1u)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L42)

### Example 12 · JVM

```kotlin title="Example 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSortedWith(naturalOrder()))
    println(ulongArrayOf(1uL).isSortedWith(naturalOrder()))

    val sorted = ulongArrayOf(1uL, 2uL, 3uL, 4uL, 5uL)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = ulongArrayOf(5uL, 4uL, 3uL, 2uL, 1uL)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L42)

### Example 13 · JVM

```kotlin title="Example 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSortedWith(naturalOrder()))
    println(ubyteArrayOf(1u).isSortedWith(naturalOrder()))

    val sorted = ubyteArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = ubyteArrayOf(5u, 4u, 3u, 2u, 1u)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L42)

### Example 14 · JVM

```kotlin title="Example 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSortedWith(naturalOrder()))
    println(ushortArrayOf(1u).isSortedWith(naturalOrder()))

    val sorted = ushortArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = ushortArrayOf(5u, 4u, 3u, 2u, 1u)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L42)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
