# isSortedBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedArraySamples.isSortedBy

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Array<out T>.isSortedBy(selector: (T) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5742)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> ByteArray.isSortedBy(selector: (Byte) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5769)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedByteArraySamples.isSortedBy

### 3. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> ShortArray.isSortedBy(selector: (Short) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5796)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedShortArraySamples.isSortedBy

### 4. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> IntArray.isSortedBy(selector: (Int) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5823)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedIntArraySamples.isSortedBy

### 5. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> LongArray.isSortedBy(selector: (Long) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5850)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedLongArraySamples.isSortedBy

### 6. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> FloatArray.isSortedBy(selector: (Float) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5877)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedFloatArraySamples.isSortedBy

### 7. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> DoubleArray.isSortedBy(selector: (Double) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5904)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedDoubleArraySamples.isSortedBy

### 8. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> BooleanArray.isSortedBy(selector: (Boolean) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5931)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedBooleanArraySamples.isSortedBy

### 9. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> CharArray.isSortedBy(selector: (Char) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5958)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedCharArraySamples.isSortedBy

### 10. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Iterable<T>.isSortedBy(selector: (T) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1010)

Returns `true` if each element in the collection yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the collection has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the collection is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

Note that the result depends on the iteration order of the collection.
The iteration order of some `Iterable` implementations may be unstable
(change from one invocation to the next),
in which case this function may return inconsistent results.

@sample samples.generated.issorted.IsSortedIterablesSamples.isSortedBy

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UIntArray.isSortedBy(selector: (UInt) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2839)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedUIntArraySamples.isSortedBy

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> ULongArray.isSortedBy(selector: (ULong) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2867)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedULongArraySamples.isSortedBy

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UByteArray.isSortedBy(selector: (UByte) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2895)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedUByteArraySamples.isSortedBy

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UShortArray.isSortedBy(selector: (UShort) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2923)

Returns `true` if each element in the array yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the array has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the array is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

@sample samples.generated.issorted.IsSortedUShortArraySamples.isSortedBy

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSortedBy { it.length })
    println(arrayOf("c").isSortedBy { it.length })

    val values = arrayOf("c", "bb", "aaa")
    println(values.isSortedBy { it.length })
    println(values.isSortedBy { it })
    println(arrayOf("a", "b").isSortedBy { if (it == "a") null else it })
    println(arrayOf(null, "a", "b").isSortedBy { it })
    println(arrayOf(null, "c", "bb").isSortedBy { it?.length })
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
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L62)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSortedBy { it * it })
    println(byteArrayOf(1).isSortedBy { it * it })

    val values = byteArrayOf(1, -2, 3, -4, 5)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it.toInt()) })
    println(values.isSortedBy { it })
    println(byteArrayOf(1, 2).isSortedBy { if (it.toInt() == 1) null else it })
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L56)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSortedBy { it * it })
    println(shortArrayOf(1).isSortedBy { it * it })

    val values = shortArrayOf(1, -2, 3, -4, 5)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it.toInt()) })
    println(values.isSortedBy { it })
    println(shortArrayOf(1, 2).isSortedBy { if (it.toInt() == 1) null else it })
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L56)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSortedBy { it * it })
    println(intArrayOf(1).isSortedBy { it * it })

    val values = intArrayOf(1, -2, 3, -4, 5)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it) })
    println(values.isSortedBy { it })
    println(intArrayOf(1, 2).isSortedBy { if (it == 1) null else it })
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L56)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSortedBy { it * it })
    println(longArrayOf(1L).isSortedBy { it * it })

    val values = longArrayOf(1L, -2L, 3L, -4L, 5L)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it) })
    println(values.isSortedBy { it })
    println(longArrayOf(1L, 2L).isSortedBy { if (it == 1L) null else it })
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L56)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSortedBy { it * it })
    println(floatArrayOf(-0.5f).isSortedBy { it * it })

    val values = floatArrayOf(-0.5f, 1.0f, -1.5f, 2.0f)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it) })
    println(values.isSortedBy { it })
    println(floatArrayOf(1.0f, 2.5f).isSortedBy { if (it == 1.0f) null else it })
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L56)

### Example 7 · JVM

```kotlin title="Example 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSortedBy { it * it })
    println(doubleArrayOf(-0.5).isSortedBy { it * it })

    val values = doubleArrayOf(-0.5, 1.0, -1.5, 2.0)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it) })
    println(values.isSortedBy { it })
    println(doubleArrayOf(1.0, 2.5).isSortedBy { if (it == 1.0) null else it })
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L56)

### Example 8 · JVM

```kotlin title="Example 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSortedBy { it.compareTo(false) })
    println(booleanArrayOf(false).isSortedBy { it.compareTo(false) })

    val values = booleanArrayOf(false, false, true)
    println(values.isSortedBy { it.compareTo(false) })
    println(values.isSortedBy { it })
    println(values.isSortedBy { !it })
    println(booleanArrayOf(false, true).isSortedBy { if (it == false) null else it })
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L55)

### Example 9 · JVM

```kotlin title="Example 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSortedBy { it.uppercaseChar() })
    println(charArrayOf('A').isSortedBy { it.uppercaseChar() })

    val values = charArrayOf('A', 'b', 'C')
    println(values.isSortedBy { it.uppercaseChar() })
    println(values.isSortedBy { it.lowercaseChar() })
    println(values.isSortedBy { it })
    println(charArrayOf('a', 'b').isSortedBy { if (it == 'a') null else it })
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L55)

### Example 10 · JVM

```kotlin title="Example 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSortedBy { it.length })
    println(listOf("c").isSortedBy { it.length })

    val values = listOf("c", "bb", "aaa")
    println(values.isSortedBy { it.length })
    println(values.isSortedBy { it })
    println(listOf("a", "b").isSortedBy { if (it == "a") null else it })
    println(listOf(null, "a", "b").isSortedBy { it })
    println(listOf(null, "c", "bb").isSortedBy { it?.length })
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
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L62)

### Example 11 · JVM

```kotlin title="Example 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSortedBy { it % 3u })
    println(uintArrayOf(3u).isSortedBy { it % 3u })

    val values = uintArrayOf(3u, 1u, 4u, 2u)
    println(values.isSortedBy { it % 3u })
    println(values.isSortedBy { it })
    println(uintArrayOf(1u, 2u).isSortedBy { if (it == 1u) null else it })
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L55)

### Example 12 · JVM

```kotlin title="Example 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSortedBy { it % 3uL })
    println(ulongArrayOf(3uL).isSortedBy { it % 3uL })

    val values = ulongArrayOf(3uL, 1uL, 4uL, 2uL)
    println(values.isSortedBy { it % 3uL })
    println(values.isSortedBy { it })
    println(ulongArrayOf(1uL, 2uL).isSortedBy { if (it == 1uL) null else it })
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L55)

### Example 13 · JVM

```kotlin title="Example 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSortedBy { it.toUInt() % 3u })
    println(ubyteArrayOf(3u).isSortedBy { it.toUInt() % 3u })

    val values = ubyteArrayOf(3u, 1u, 4u, 2u)
    println(values.isSortedBy { it.toUInt() % 3u })
    println(values.isSortedBy { it })
    println(ubyteArrayOf(1u, 2u).isSortedBy { if (it.toUInt() == 1u) null else it })
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L55)

### Example 14 · JVM

```kotlin title="Example 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSortedBy { it.toUInt() % 3u })
    println(ushortArrayOf(3u).isSortedBy { it.toUInt() % 3u })

    val values = ushortArrayOf(3u, 1u, 4u, 2u)
    println(values.isSortedBy { it.toUInt() % 3u })
    println(values.isSortedBy { it })
    println(ushortArrayOf(1u, 2u).isSortedBy { if (it.toUInt() == 1u) null else it })
}
```

```text title="Output"
true
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L55)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
