# allDistinct

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

For elements of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctArraySamples.allDistinct

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun <T> Array<out T>.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14283)

### 2. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun ByteArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14308)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctByteArraySamples.allDistinct

### 3. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun ShortArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14332)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctShortArraySamples.allDistinct

### 4. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun IntArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14356)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctIntArraySamples.allDistinct

### 5. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun LongArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14378)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctLongArraySamples.allDistinct

### 6. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun FloatArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14400)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using equality semantics consistent with `Float.equals`.
The operation returns `false` as soon as a duplicate element is found.

`NaN` is considered equal to `NaN`, and `-0.0` is considered not equal to `0.0`,
consistent with `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctFloatArraySamples.allDistinct

### 7. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun DoubleArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14425)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using equality semantics consistent with `Double.equals`.
The operation returns `false` as soon as a duplicate element is found.

`NaN` is considered equal to `NaN`, and `-0.0` is considered not equal to `0.0`,
consistent with `Double.equals`.

@sample samples.generated.alldistinct.AllDistinctDoubleArraySamples.allDistinct

### 8. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun BooleanArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14450)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctBooleanArraySamples.allDistinct

### 9. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun CharArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14469)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctCharArraySamples.allDistinct

### 10. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun <T> Iterable<T>.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1950)

Returns `true` if all elements in the collection are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty collection.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

For elements of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctIterablesSamples.allDistinct

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UIntArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6043)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctUIntArraySamples.allDistinct

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun ULongArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6066)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctULongArraySamples.allDistinct

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UByteArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6089)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctUByteArraySamples.allDistinct

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UShortArray.allDistinct(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6114)

Returns `true` if all elements in the array are distinct from each other,
that is, no two elements are equal.

Returns `true` for an empty array.

The elements are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate element is found.

@sample samples.generated.alldistinct.AllDistinctUShortArraySamples.allDistinct

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().allDistinct())
    println(arrayOf("apple").allDistinct())

    val distinctValues = arrayOf("apple", "mango", "peach")
    println(distinctValues.allDistinct())

    val duplicateValues = arrayOf("apple", "mango", "apple")
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctArraySamples.kt#L18)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(byteArrayOf().allDistinct())
    println(byteArrayOf(1).allDistinct())

    val distinctValues = byteArrayOf(1, 2, 3)
    println(distinctValues.allDistinct())

    val duplicateValues = byteArrayOf(1, 2, 1)
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctByteArraySamples.kt#L18)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(shortArrayOf().allDistinct())
    println(shortArrayOf(1).allDistinct())

    val distinctValues = shortArrayOf(1, 2, 3)
    println(distinctValues.allDistinct())

    val duplicateValues = shortArrayOf(1, 2, 1)
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctShortArraySamples.kt#L18)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(intArrayOf().allDistinct())
    println(intArrayOf(1).allDistinct())

    val distinctValues = intArrayOf(1, 2, 3)
    println(distinctValues.allDistinct())

    val duplicateValues = intArrayOf(1, 2, 1)
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctIntArraySamples.kt#L18)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(longArrayOf().allDistinct())
    println(longArrayOf(1L).allDistinct())

    val distinctValues = longArrayOf(1L, 2L, 3L)
    println(distinctValues.allDistinct())

    val duplicateValues = longArrayOf(1L, 2L, 1L)
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctLongArraySamples.kt#L18)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(floatArrayOf().allDistinct())
    println(floatArrayOf(1.0f).allDistinct())

    val distinctValues = floatArrayOf(1.0f, 2.0f, 3.0f)
    println(distinctValues.allDistinct())

    val duplicateValues = floatArrayOf(1.0f, 2.0f, 1.0f)
    println(duplicateValues.allDistinct())

    println(floatArrayOf(Float.NaN, Float.NaN).allDistinct())
    println(floatArrayOf(0.0f, -0.0f).allDistinct())
}
```

```text title="Output"
true
true
true
false
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctFloatArraySamples.kt#L18)

### Example 7 · JVM

```kotlin title="Example 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(doubleArrayOf().allDistinct())
    println(doubleArrayOf(1.0).allDistinct())

    val distinctValues = doubleArrayOf(1.0, 2.0, 3.0)
    println(distinctValues.allDistinct())

    val duplicateValues = doubleArrayOf(1.0, 2.0, 1.0)
    println(duplicateValues.allDistinct())

    println(doubleArrayOf(Double.NaN, Double.NaN).allDistinct())
    println(doubleArrayOf(0.0, -0.0).allDistinct())
}
```

```text title="Output"
true
true
true
false
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctDoubleArraySamples.kt#L18)

### Example 8 · JVM

```kotlin title="Example 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().allDistinct())
    println(booleanArrayOf(true).allDistinct())

    val distinctValues = booleanArrayOf(true, false)
    println(distinctValues.allDistinct())

    val duplicateValues = booleanArrayOf(true, false, true)
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctBooleanArraySamples.kt#L18)

### Example 9 · JVM

```kotlin title="Example 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().allDistinct())
    println(charArrayOf('a').allDistinct())

    val distinctValues = charArrayOf('a', 'b', 'c')
    println(distinctValues.allDistinct())

    val duplicateValues = charArrayOf('a', 'b', 'a')
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctCharArraySamples.kt#L18)

### Example 10 · JVM

```kotlin title="Example 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().allDistinct())
    println(listOf("apple").allDistinct())

    val distinctValues = listOf("apple", "mango", "peach")
    println(distinctValues.allDistinct())

    val duplicateValues = listOf("apple", "mango", "apple")
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctIterablesSamples.kt#L18)

### Example 11 · JVM

```kotlin title="Example 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().allDistinct())
    println(uintArrayOf(1u).allDistinct())

    val distinctValues = uintArrayOf(1u, 2u, 3u)
    println(distinctValues.allDistinct())

    val duplicateValues = uintArrayOf(1u, 2u, 1u)
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUIntArraySamples.kt#L18)

### Example 12 · JVM

```kotlin title="Example 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().allDistinct())
    println(ulongArrayOf(1uL).allDistinct())

    val distinctValues = ulongArrayOf(1uL, 2uL, 3uL)
    println(distinctValues.allDistinct())

    val duplicateValues = ulongArrayOf(1uL, 2uL, 1uL)
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctULongArraySamples.kt#L18)

### Example 13 · JVM

```kotlin title="Example 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().allDistinct())
    println(ubyteArrayOf(1u).allDistinct())

    val distinctValues = ubyteArrayOf(1u, 2u, 3u)
    println(distinctValues.allDistinct())

    val duplicateValues = ubyteArrayOf(1u, 2u, 1u)
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUByteArraySamples.kt#L18)

### Example 14 · JVM

```kotlin title="Example 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().allDistinct())
    println(ushortArrayOf(1u).allDistinct())

    val distinctValues = ushortArrayOf(1u, 2u, 3u)
    println(distinctValues.allDistinct())

    val duplicateValues = ushortArrayOf(1u, 2u, 1u)
    println(duplicateValues.allDistinct())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUShortArraySamples.kt#L18)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
