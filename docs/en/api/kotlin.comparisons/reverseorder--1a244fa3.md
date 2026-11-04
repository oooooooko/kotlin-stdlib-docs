# reverseOrder

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a comparator that compares `Comparable` objects in reversed natural order.

The natural order of a `Comparable` type here means the order established by its `compareTo` function.

@sample samples.comparisons.Comparisons.nullsFirstLastWithComparator

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Comparable<T>> reverseOrder(): Comparator<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L285)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf(4, null, 1, -2, 3)

    val nullsFirstList = list.sortedWith(nullsFirst(reverseOrder()))
    println(nullsFirstList)

    val nullsLastList = list.sortedWith(nullsLast(reverseOrder()))
    println(nullsLastList)
}
```

```text title="Output"
[null, 4, 3, 1, -2]
[4, 3, 1, -2, null]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L213)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
