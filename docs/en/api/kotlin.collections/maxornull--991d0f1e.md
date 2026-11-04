# maxOrNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the largest element or `null` if the array is empty.

If any of elements is `NaN`, this function returns `NaN`.

@sample samples.collections.Collections.Aggregates.maxMinFloating

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public fun Array<out Double>.maxOrNull(): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18807)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public fun Array<out Float>.maxOrNull(): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18825)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Comparable<T>> Array<out T>.maxOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18843)

Returns the largest element or `null` if the array is empty.

If there are multiple equal maximal elements, this function returns the first of those elements.

@sample samples.collections.Collections.Aggregates.maxMinGeneric

### 4. Common

```kotlin
@SinceKotlin("1.4")
public fun ByteArray.maxOrNull(): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18861)

Returns the largest element or `null` if the array is empty.

@sample samples.collections.Collections.Aggregates.maxMinPrimitive

### 5. Common

```kotlin
@SinceKotlin("1.4")
public fun ShortArray.maxOrNull(): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18877)

Returns the largest element or `null` if the array is empty.

@sample samples.collections.Collections.Aggregates.maxMinPrimitive

### 6. Common

```kotlin
@SinceKotlin("1.4")
public fun IntArray.maxOrNull(): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18893)

Returns the largest element or `null` if the array is empty.

@sample samples.collections.Collections.Aggregates.maxMinPrimitive

### 7. Common

```kotlin
@SinceKotlin("1.4")
public fun LongArray.maxOrNull(): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18909)

Returns the largest element or `null` if the array is empty.

@sample samples.collections.Collections.Aggregates.maxMinPrimitive

### 8. Common

```kotlin
@SinceKotlin("1.4")
public fun FloatArray.maxOrNull(): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18925)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public fun DoubleArray.maxOrNull(): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18943)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public fun CharArray.maxOrNull(): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18961)

Returns the largest element or `null` if the array is empty.

@sample samples.collections.Collections.Aggregates.maxMinPrimitive

### 11. Common

```kotlin
@SinceKotlin("1.4")
public fun Iterable<Double>.maxOrNull(): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2545)

Returns the largest element or `null` if the collection is empty.

If any of elements is `NaN`, this function returns `NaN`.

@sample samples.collections.Collections.Aggregates.maxMinFloating

### 12. Common

```kotlin
@SinceKotlin("1.4")
public fun Iterable<Float>.maxOrNull(): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2564)

Returns the largest element or `null` if the collection is empty.

If any of elements is `NaN`, this function returns `NaN`.

@sample samples.collections.Collections.Aggregates.maxMinFloating

### 13. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Comparable<T>> Iterable<T>.maxOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2583)

Returns the largest element or `null` if the collection is empty.

If there are multiple equal maximal elements, this function returns the first of those elements.

@sample samples.collections.Collections.Aggregates.maxMinGeneric

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UIntArray.maxOrNull(): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8179)

Returns the largest element or `null` if the array is empty.

@sample samples.collections.Collections.Aggregates.maxMinPrimitive

### 15. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun ULongArray.maxOrNull(): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8196)

Returns the largest element or `null` if the array is empty.

@sample samples.collections.Collections.Aggregates.maxMinPrimitive

### 16. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UByteArray.maxOrNull(): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8213)

Returns the largest element or `null` if the array is empty.

@sample samples.collections.Collections.Aggregates.maxMinPrimitive

### 17. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UShortArray.maxOrNull(): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8230)

Returns the largest element or `null` if the array is empty.

@sample samples.collections.Collections.Aggregates.maxMinPrimitive

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    // The largest and smallest elements in the array
    val numbers = doubleArrayOf(3.0, 7.2, 2.4, 6.5)
    println(numbers.max())
    println(numbers.min())

    // max() and min() return `NaN` if any of elements is `NaN`
    val numbersWithNaN = doubleArrayOf(3.0, Double.NaN, 7.2, 2.4, 6.5)
    println(numbersWithNaN.max())
    println(numbersWithNaN.min())

    val emptyArray = doubleArrayOf()

    // max() and min() throw if the array is empty
    assertFailsWith<NoSuchElementException> { emptyArray.max() }
    assertFailsWith<NoSuchElementException> { emptyArray.min() }

    // maxOrNull() and minOrNull() return null if the array is empty
    println(emptyArray.maxOrNull())
    println(emptyArray.minOrNull())
}
```

```text title="Output"
7.2
2.4
NaN
NaN
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1061)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    // The largest and smallest elements according to String.compareTo
    val names = listOf("Alice", "Bob", "Carol")
    println(names.max())
    println(names.min())

    val emptyList = emptyList<Int>()

    // max() and min() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.max() }
    assertFailsWith<NoSuchElementException> { emptyList.min() }

    // maxOrNull() and minOrNull() return null if the collection is empty
    println(emptyList.maxOrNull())
    println(emptyList.minOrNull())
}
```

```text title="Output"
Carol
Alice
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1084)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    // The largest and smallest elements in the array
    val numbers = intArrayOf(3, 7, 2, 6)
    println(numbers.max())
    println(numbers.min())

    val emptyArray = intArrayOf()

    // max() and min() throw if the array is empty
    assertFailsWith<NoSuchElementException> { emptyArray.max() }
    assertFailsWith<NoSuchElementException> { emptyArray.min() }

    // maxOrNull() and minOrNull() return null if the array is empty
    println(emptyArray.maxOrNull())
    println(emptyArray.minOrNull())
}
```

```text title="Output"
7
2
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1043)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
