# compareValuesBy

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Compares two values using the specified functions `selectors` to calculate the result of the comparison.
The functions are called sequentially, receive the given values `a` and `b` and return `Comparable`
objects. As soon as the `Comparable` instances returned by a function for `a` and `b` values do not
compare as equal, the result of that comparison is returned.

@sample samples.comparisons.Comparisons.compareValuesByWithSelectors

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> compareValuesBy(a: T, b: T, vararg selectors: (T) -> Comparable<*>?): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L10)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> compareValuesBy(a: T, b: T, selector: (T) -> Comparable<*>?): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L33)

Compares two values using the specified `selector` function to calculate the result of the comparison.
The function is applied to the given values `a` and `b` and return `Comparable` objects.
The result of comparison of these `Comparable` instances is returned.

@sample samples.comparisons.Comparisons.compareValuesByWithSingleSelector

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T, K> compareValuesBy(a: T, b: T, comparator: Comparator<in K>, selector: (T) -> K): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L45)

Compares two values using the specified `selector` function to calculate the result of the comparison.
The function is applied to the given values `a` and `b` and return objects of type K which are then being
compared with the given `comparator`.

@sample samples.comparisons.Comparisons.compareValuesByWithComparator

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun compareLengthThenString(a: String, b: String): Int =
        compareValuesBy(a, b, { it.length }, { it })

    println(compareLengthThenString("b", "aa") < 0)

    println(compareLengthThenString("a", "b") < 0)
    println(compareLengthThenString("b", "a") > 0)
    println(compareLengthThenString("a", "a") == 0)
}
```

```text title="Output"
true
true
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L33)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun compareLength(a: String, b: String): Int =
        compareValuesBy(a, b) { it.length }

    println(compareLength("a", "b") == 0)
    println(compareLength("bb", "a") > 0)
    println(compareLength("a", "bb") < 0)
}
```

```text title="Output"
true
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L23)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun compareInsensitiveOrder(a: Char, b: Char): Int =
        compareValuesBy(a, b, String.CASE_INSENSITIVE_ORDER, { c -> c.toString() })

    println(compareInsensitiveOrder('a', 'a') == 0)
    println(compareInsensitiveOrder('a', 'A') == 0)

    println(compareInsensitiveOrder('a', 'b') < 0)
    println(compareInsensitiveOrder('A', 'b') < 0)
    println(compareInsensitiveOrder('b', 'a') > 0)
}
```

```text title="Output"
true
true
true
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L45)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
