# isSortedByDescending

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedArraySamples.isSortedByDescending

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Array<out T>.isSortedByDescending(selector: (T) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5985)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> ByteArray.isSortedByDescending(selector: (Byte) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6013)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedByteArraySamples.isSortedByDescending

### 3. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> ShortArray.isSortedByDescending(selector: (Short) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6041)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedShortArraySamples.isSortedByDescending

### 4. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> IntArray.isSortedByDescending(selector: (Int) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6069)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedIntArraySamples.isSortedByDescending

### 5. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> LongArray.isSortedByDescending(selector: (Long) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6097)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedLongArraySamples.isSortedByDescending

### 6. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> FloatArray.isSortedByDescending(selector: (Float) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6125)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedFloatArraySamples.isSortedByDescending

### 7. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> DoubleArray.isSortedByDescending(selector: (Double) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6153)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedDoubleArraySamples.isSortedByDescending

### 8. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> BooleanArray.isSortedByDescending(selector: (Boolean) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6181)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedBooleanArraySamples.isSortedByDescending

### 9. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> CharArray.isSortedByDescending(selector: (Char) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6209)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedCharArraySamples.isSortedByDescending

### 10. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Iterable<T>.isSortedByDescending(selector: (T) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1047)

Returns `true` if each element in the collection yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the collection has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the collection is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

Note that the result depends on the iteration order of the collection.
The iteration order of some `Iterable` implementations may be unstable
(change from one invocation to the next),
in which case this function may return inconsistent results.

@sample samples.generated.issorted.IsSortedIterablesSamples.isSortedByDescending

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UIntArray.isSortedByDescending(selector: (UInt) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2951)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedUIntArraySamples.isSortedByDescending

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> ULongArray.isSortedByDescending(selector: (ULong) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2980)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedULongArraySamples.isSortedByDescending

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UByteArray.isSortedByDescending(selector: (UByte) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3009)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedUByteArraySamples.isSortedByDescending

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UShortArray.isSortedByDescending(selector: (UShort) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3038)

Returns `true` if each element in the array yields a `selector` value
that is greater than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted in descending order if for each pair
of adjacent elements the `selector` value of the preceding element is not less
than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedUShortArraySamples.isSortedByDescending

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSortedByDescending { it.length })
    println(arrayOf("aaa").isSortedByDescending { it.length })

    val values = arrayOf("aaa", "bb", "c")
    println(values.isSortedByDescending { it.length })
    println(values.isSortedByDescending { it })
    println(arrayOf("b", "a").isSortedByDescending { if (it == "a") null else it })
    println(arrayOf("aaa", "bb", null).isSortedByDescending { it?.length })
}
```

```text title="Output"
true
true
true
false
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L75)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSortedByDescending { it * it })
    println(byteArrayOf(5).isSortedByDescending { it * it })

    val values = byteArrayOf(5, -4, 3, -2, 1)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it.toInt()) })
    println(values.isSortedByDescending { it })
    println(byteArrayOf(2, 1).isSortedByDescending { if (it.toInt() == 1) null else it })
}
```

```text title="Output"
true
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L68)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSortedByDescending { it * it })
    println(shortArrayOf(5).isSortedByDescending { it * it })

    val values = shortArrayOf(5, -4, 3, -2, 1)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it.toInt()) })
    println(values.isSortedByDescending { it })
    println(shortArrayOf(2, 1).isSortedByDescending { if (it.toInt() == 1) null else it })
}
```

```text title="Output"
true
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L68)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSortedByDescending { it * it })
    println(intArrayOf(5).isSortedByDescending { it * it })

    val values = intArrayOf(5, -4, 3, -2, 1)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it) })
    println(values.isSortedByDescending { it })
    println(intArrayOf(2, 1).isSortedByDescending { if (it == 1) null else it })
}
```

```text title="Output"
true
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L68)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSortedByDescending { it * it })
    println(longArrayOf(5L).isSortedByDescending { it * it })

    val values = longArrayOf(5L, -4L, 3L, -2L, 1L)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it) })
    println(values.isSortedByDescending { it })
    println(longArrayOf(2L, 1L).isSortedByDescending { if (it == 1L) null else it })
}
```

```text title="Output"
true
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L68)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSortedByDescending { it * it })
    println(floatArrayOf(2.0f).isSortedByDescending { it * it })

    val values = floatArrayOf(2.0f, -1.5f, 1.0f, -0.5f)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it) })
    println(values.isSortedByDescending { it })
    println(floatArrayOf(2.5f, 1.0f).isSortedByDescending { if (it == 1.0f) null else it })
}
```

```text title="Output"
true
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L68)

### Example 7 · JVM

```kotlin title="Example 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSortedByDescending { it * it })
    println(doubleArrayOf(2.0).isSortedByDescending { it * it })

    val values = doubleArrayOf(2.0, -1.5, 1.0, -0.5)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it) })
    println(values.isSortedByDescending { it })
    println(doubleArrayOf(2.5, 1.0).isSortedByDescending { if (it == 1.0) null else it })
}
```

```text title="Output"
true
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L68)

### Example 8 · JVM

```kotlin title="Example 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSortedByDescending { it.compareTo(false) })
    println(booleanArrayOf(true).isSortedByDescending { it.compareTo(false) })

    val values = booleanArrayOf(true, false, false)
    println(values.isSortedByDescending { it.compareTo(false) })
    println(values.isSortedByDescending { it })
    println(values.isSortedByDescending { !it })
    println(booleanArrayOf(true, false).isSortedByDescending { if (it == false) null else it })
}
```

```text title="Output"
true
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L67)

### Example 9 · JVM

```kotlin title="Example 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSortedByDescending { it.uppercaseChar() })
    println(charArrayOf('C').isSortedByDescending { it.uppercaseChar() })

    val values = charArrayOf('C', 'b', 'A')
    println(values.isSortedByDescending { it.uppercaseChar() })
    println(values.isSortedByDescending { it.lowercaseChar() })
    println(values.isSortedByDescending { it })
    println(charArrayOf('b', 'a').isSortedByDescending { if (it == 'a') null else it })
}
```

```text title="Output"
true
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L67)

### Example 10 · JVM

```kotlin title="Example 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSortedByDescending { it.length })
    println(listOf("aaa").isSortedByDescending { it.length })

    val values = listOf("aaa", "bb", "c")
    println(values.isSortedByDescending { it.length })
    println(values.isSortedByDescending { it })
    println(listOf("b", "a").isSortedByDescending { if (it == "a") null else it })
    println(listOf("aaa", "bb", null).isSortedByDescending { it?.length })
}
```

```text title="Output"
true
true
true
false
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L75)

### Example 11 · JVM

```kotlin title="Example 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSortedByDescending { it % 3u })
    println(uintArrayOf(2u).isSortedByDescending { it % 3u })

    val values = uintArrayOf(2u, 4u, 1u, 3u)
    println(values.isSortedByDescending { it % 3u })
    println(values.isSortedByDescending { it })
    println(uintArrayOf(2u, 1u).isSortedByDescending { if (it == 1u) null else it })
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L66)

### Example 12 · JVM

```kotlin title="Example 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSortedByDescending { it % 3uL })
    println(ulongArrayOf(2uL).isSortedByDescending { it % 3uL })

    val values = ulongArrayOf(2uL, 4uL, 1uL, 3uL)
    println(values.isSortedByDescending { it % 3uL })
    println(values.isSortedByDescending { it })
    println(ulongArrayOf(2uL, 1uL).isSortedByDescending { if (it == 1uL) null else it })
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L66)

### Example 13 · JVM

```kotlin title="Example 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSortedByDescending { it.toUInt() % 3u })
    println(ubyteArrayOf(2u).isSortedByDescending { it.toUInt() % 3u })

    val values = ubyteArrayOf(2u, 4u, 1u, 3u)
    println(values.isSortedByDescending { it.toUInt() % 3u })
    println(values.isSortedByDescending { it })
    println(ubyteArrayOf(2u, 1u).isSortedByDescending { if (it.toUInt() == 1u) null else it })
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L66)

### Example 14 · JVM

```kotlin title="Example 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSortedByDescending { it.toUInt() % 3u })
    println(ushortArrayOf(2u).isSortedByDescending { it.toUInt() % 3u })

    val values = ushortArrayOf(2u, 4u, 1u, 3u)
    println(values.isSortedByDescending { it.toUInt() % 3u })
    println(values.isSortedByDescending { it })
    println(ushortArrayOf(2u, 1u).isSortedByDescending { if (it.toUInt() == 1u) null else it })
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L66)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
