# isSortedDescending

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if each element in the sequence is greater than or equal
to the following element according to their natural sort order.

Returns `true` if the sequence has fewer than two elements.

The elements are compared sequentially using `Comparable.compareTo`,
and the sequence is considered sorted in descending order if for each
pair of adjacent elements the preceding element is not less than the following one.

Note that the result depends on the iteration order of the sequence.
The iteration order of some `Sequence` implementations may be unstable
(change from one invocation to the next),
in which case this function may return inconsistent results.

For elements of floating-point types (`Double`, `Float`), `NaN` is considered greater
than any other value (including positive infinity), and `-0.0` is considered less than `0.0`,
consistent with `Double.compareTo` and `Float.compareTo`.

The operation is _terminal_.

@sample samples.generated.issorted.IsSortedSequencesSamples.isSortedDescending

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Sequence<T>.isSortedDescending(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L695)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(sequenceOf<String>().isSortedDescending())
    println(sequenceOf("cherry").isSortedDescending())

    val sorted = sequenceOf("cherry", "banana", "apple")
    println(sorted.isSortedDescending())

    val unsorted = sequenceOf("banana", "cherry", "apple")
    println(unsorted.isSortedDescending())
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedSequencesSamples.kt#L30)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
