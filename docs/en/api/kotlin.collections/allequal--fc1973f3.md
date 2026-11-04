# allEqual

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

For elements of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualArraySamples.allEqual

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun <T> Array<out T>.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14718)

### 2. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun ByteArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14743)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualByteArraySamples.allEqual

### 3. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun ShortArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14765)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualShortArraySamples.allEqual

### 4. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun IntArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14787)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualIntArraySamples.allEqual

### 5. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun LongArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14809)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualLongArraySamples.allEqual

### 6. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun FloatArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14831)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using equality semantics consistent with `Float.equals`,
and all elements are considered equal if the first element equals
every subsequent element.

`NaN` is considered equal to `NaN`, and `-0.0` is considered not equal to `0.0`,
consistent with `Float.equals`.

@sample samples.generated.allequal.AllEqualFloatArraySamples.allEqual

### 7. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun DoubleArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14856)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using equality semantics consistent with `Double.equals`,
and all elements are considered equal if the first element equals
every subsequent element.

`NaN` is considered equal to `NaN`, and `-0.0` is considered not equal to `0.0`,
consistent with `Double.equals`.

@sample samples.generated.allequal.AllEqualDoubleArraySamples.allEqual

### 8. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun BooleanArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14881)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualBooleanArraySamples.allEqual

### 9. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun CharArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14903)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualCharArraySamples.allEqual

### 10. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun <T> Iterable<T>.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2009)

Returns `true` if all elements in the collection are equal to each other.

Returns `true` for an empty collection.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

For elements of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualIterablesSamples.allEqual

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UIntArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6243)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualUIntArraySamples.allEqual

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun ULongArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6266)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualULongArraySamples.allEqual

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UByteArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6289)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualUByteArraySamples.allEqual

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UShortArray.allEqual(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6312)

Returns `true` if all elements in the array are equal to each other.

Returns `true` for an empty array.

The elements are compared sequentially using structural equality (`==`),
and all elements are considered equal if the first element equals
every subsequent element.

@sample samples.generated.allequal.AllEqualUShortArraySamples.allEqual

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().allEqual())
    println(arrayOf("apple").allEqual())

    val sameValues = arrayOf("apple", "apple", "apple")
    println(sameValues.allEqual())

    val mixedValues = arrayOf("apple", "apple", "orange")
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualArraySamples.kt#L18)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().allEqual())
    println(byteArrayOf(1).allEqual())

    val sameValues = byteArrayOf(1, 1, 1)
    println(sameValues.allEqual())

    val mixedValues = byteArrayOf(1, 1, 2)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualByteArraySamples.kt#L19)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().allEqual())
    println(shortArrayOf(1).allEqual())

    val sameValues = shortArrayOf(1, 1, 1)
    println(sameValues.allEqual())

    val mixedValues = shortArrayOf(1, 1, 2)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualShortArraySamples.kt#L19)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().allEqual())
    println(intArrayOf(1).allEqual())

    val sameValues = intArrayOf(1, 1, 1)
    println(sameValues.allEqual())

    val mixedValues = intArrayOf(1, 1, 2)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualIntArraySamples.kt#L19)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().allEqual())
    println(longArrayOf(1L).allEqual())

    val sameValues = longArrayOf(1L, 1L, 1L)
    println(sameValues.allEqual())

    val mixedValues = longArrayOf(1L, 1L, 2L)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualLongArraySamples.kt#L19)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().allEqual())
    println(floatArrayOf(1.0f).allEqual())

    val sameValues = floatArrayOf(1.0f, 1.0f, 1.0f)
    println(sameValues.allEqual())

    val mixedValues = floatArrayOf(1.0f, 1.0f, 2.0f)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualFloatArraySamples.kt#L19)

### Example 7 · JVM

```kotlin title="Example 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().allEqual())
    println(doubleArrayOf(1.0).allEqual())

    val sameValues = doubleArrayOf(1.0, 1.0, 1.0)
    println(sameValues.allEqual())

    val mixedValues = doubleArrayOf(1.0, 1.0, 2.0)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualDoubleArraySamples.kt#L19)

### Example 8 · JVM

```kotlin title="Example 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().allEqual())
    println(booleanArrayOf(true).allEqual())

    val sameValues = booleanArrayOf(true, true, true)
    println(sameValues.allEqual())

    val mixedValues = booleanArrayOf(true, true, false)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualBooleanArraySamples.kt#L18)

### Example 9 · JVM

```kotlin title="Example 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().allEqual())
    println(charArrayOf('a').allEqual())

    val sameValues = charArrayOf('a', 'a', 'a')
    println(sameValues.allEqual())

    val mixedValues = charArrayOf('a', 'a', 'b')
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualCharArraySamples.kt#L18)

### Example 10 · JVM

```kotlin title="Example 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().allEqual())
    println(listOf("apple").allEqual())

    val sameValues = listOf("apple", "apple", "apple")
    println(sameValues.allEqual())

    val mixedValues = listOf("apple", "apple", "orange")
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualIterablesSamples.kt#L18)

### Example 11 · JVM

```kotlin title="Example 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().allEqual())
    println(uintArrayOf(1u).allEqual())

    val sameValues = uintArrayOf(1u, 1u, 1u)
    println(sameValues.allEqual())

    val mixedValues = uintArrayOf(1u, 1u, 2u)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUIntArraySamples.kt#L18)

### Example 12 · JVM

```kotlin title="Example 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().allEqual())
    println(ulongArrayOf(1uL).allEqual())

    val sameValues = ulongArrayOf(1uL, 1uL, 1uL)
    println(sameValues.allEqual())

    val mixedValues = ulongArrayOf(1uL, 1uL, 2uL)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualULongArraySamples.kt#L18)

### Example 13 · JVM

```kotlin title="Example 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().allEqual())
    println(ubyteArrayOf(1u).allEqual())

    val sameValues = ubyteArrayOf(1u, 1u, 1u)
    println(sameValues.allEqual())

    val mixedValues = ubyteArrayOf(1u, 1u, 2u)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUByteArraySamples.kt#L18)

### Example 14 · JVM

```kotlin title="Example 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().allEqual())
    println(ushortArrayOf(1u).allEqual())

    val sameValues = ushortArrayOf(1u, 1u, 1u)
    println(sameValues.allEqual())

    val mixedValues = ushortArrayOf(1u, 1u, 2u)
    println(mixedValues.allEqual())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUShortArraySamples.kt#L18)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
