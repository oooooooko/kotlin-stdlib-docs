# max

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the largest element.

If any of elements is `NaN`, this function returns `NaN`.

The operation is _terminal_.

@throws NoSuchElementException if the sequence is empty.

@sample samples.collections.Collections.Aggregates.maxMinFloating

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun Sequence<Double>.max(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1659)

### 2. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun Sequence<Float>.max(): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1684)

### 3. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun <T : Comparable<T>> Sequence<T>.max(): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1709)

Returns the largest element.

If there are multiple equal maximal elements, this function returns the first of those elements.

The operation is _terminal_.

@throws NoSuchElementException if the sequence is empty.

@sample samples.collections.Collections.Aggregates.maxMinGeneric

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

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
