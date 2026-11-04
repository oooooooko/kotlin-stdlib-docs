# isSortedWith

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if each element in the sequence is less than or equal
to the following element according to the specified `comparator`.

Returns `true` if the sequence has fewer than two elements.

The elements are compared sequentially using `Comparator.compare`,
and the sequence is considered sorted if for each pair of adjacent elements
the preceding element is not greater than the following one.

Note that the result depends on the iteration order of the sequence.
The iteration order of some `Sequence` implementations may be unstable
(change from one invocation to the next),
in which case this function may return inconsistent results.

The operation is _terminal_.

@sample samples.generated.issorted.IsSortedSequencesSamples.isSortedWith

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
public fun <T> Sequence<T>.isSortedWith(comparator: Comparator<in T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L723)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(sequenceOf<String>().isSortedWith(naturalOrder()))
    println(sequenceOf("apple").isSortedWith(naturalOrder()))

    println(sequenceOf("apple", "banana", "cherry").isSortedWith(naturalOrder()))
    println(sequenceOf("apple", "banana", "cherry").isSortedWith(reverseOrder()))

    println(sequenceOf("cherry", "banana", "apple").isSortedWith(reverseOrder()))

    println(sequenceOf("Apple", "banana", "Cherry").isSortedWith(String.CASE_INSENSITIVE_ORDER))

    println(sequenceOf(null, "apple", "banana").isSortedWith(nullsFirst(naturalOrder())))
    println(sequenceOf(null, "apple", "banana").isSortedWith(nullsLast(naturalOrder())))
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
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedSequencesSamples.kt#L42)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
