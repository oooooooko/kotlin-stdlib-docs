# thenByDescending

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a descending comparator using the primary comparator and
the function to transform value to a `Comparable` instance for comparison.

@sample samples.comparisons.Comparisons.thenByDescending

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Comparator<T>.thenByDescending(crossinline selector: (T) -> Comparable<*>?): Comparator<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L160)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T, K> Comparator<T>.thenByDescending(comparator: Comparator<in K>, crossinline selector: (T) -> K): Comparator<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L173)

Creates a descending comparator comparing values after the primary comparator defined them equal. It uses
the `selector` function to transform values and then compares them with the given `comparator`.

@sample samples.comparisons.Comparisons.thenByDescendingWithComparator

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("aa", "b", "bb", "a")

    val lengthComparator = compareBy<String> { it.length }
    println(list.sortedWith(lengthComparator))

    val lengthThenStringDesc = lengthComparator.thenByDescending { it }
    println(list.sortedWith(lengthThenStringDesc))
}
```

```text title="Output"
[b, a, aa, bb]
[b, a, bb, aa]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L141)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("A", "aa", "b", "bb", "a")

    val lengthComparator = compareBy<String> { it.length }
    println(list.sortedWith(lengthComparator))

    val lengthThenCaseInsensitive = lengthComparator
        .thenByDescending(String.CASE_INSENSITIVE_ORDER) { it }
    println(list.sortedWith(lengthThenCaseInsensitive))
}
```

```text title="Output"
[A, b, a, aa, bb]
[b, A, a, bb, aa]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L152)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
