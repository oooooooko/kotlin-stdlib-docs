# isSortedBy

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if each element in the sequence yields a `selector` value
that is less than or equal to the `selector` value of the following element
according to the natural sort order of the selector values.

Returns `true` if the sequence has fewer than two elements.

The `selector` values of adjacent elements are compared sequentially using `compareValues`,
and the sequence is considered sorted if for each pair of adjacent elements
the `selector` value of the preceding element is not greater than that of the following one.

If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.

Note that the result depends on the iteration order of the sequence.
The iteration order of some `Sequence` implementations may be unstable
(change from one invocation to the next),
in which case this function may return inconsistent results.

The operation is _terminal_.

@sample samples.generated.issorted.IsSortedSequencesSamples.isSortedBy

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Sequence<T>.isSortedBy(selector: (T) -> R?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L614)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(sequenceOf<String>().isSortedBy { it.length })
    println(sequenceOf("c").isSortedBy { it.length })

    println(sequenceOf("c", "bb", "aaa").isSortedBy { it.length })
    println(sequenceOf("c", "bb", "aaa").isSortedBy { it })
    println(sequenceOf("a", "b").isSortedBy { if (it == "a") null else it })
    println(sequenceOf(null, "a", "b").isSortedBy { it })
    println(sequenceOf(null, "c", "bb").isSortedBy { it?.length })
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
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedSequencesSamples.kt#L58)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
