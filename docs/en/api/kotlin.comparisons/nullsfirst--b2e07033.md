# nullsFirst

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Extends the given `comparator` of non-nullable values to a comparator of nullable values
considering `null` value less than any other value.
Non-null values are compared with the provided `comparator`.

@sample samples.comparisons.Comparisons.nullsFirstLastWithComparator

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Any> nullsFirst(comparator: Comparator<in T>): Comparator<T?>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L224)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T : Comparable<T>> nullsFirst(): Comparator<T?>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L240)

Provides a comparator of nullable `Comparable` values
considering `null` value less than any other value.
Non-null values are compared according to their `natural order``naturalOrder`.

@sample samples.comparisons.Comparisons.nullsFirstLastComparator

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

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf(4, null, -1, 1)

    val nullsFirstList = list.sortedWith(nullsFirst())
    println(nullsFirstList)

    val nullsLastList = list.sortedWith(nullsLast())
    println(nullsLastList)
}
```

```text title="Output"
[null, -1, 1, 4]
[-1, 1, 4, null]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L202)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
