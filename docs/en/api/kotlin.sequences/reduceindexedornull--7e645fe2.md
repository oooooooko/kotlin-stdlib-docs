# reduceIndexedOrNull

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with the first element and applying `operation` from left to right
to current accumulator value and each element with its index in the original sequence.

Returns `null` if the sequence is empty.

@param `operation` function that takes the index of an element, current accumulator value and the element itself,
and calculates the next accumulator value.

The operation is _terminal_.

@sample samples.collections.Collections.Aggregates.reduceOrNull

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <S, T : S> Sequence<T>.reduceIndexedOrNull(operation: (index: Int, acc: S, T) -> S): S?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L2679)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceOrNull { acc, string -> acc + string })
    println(strings.reduceIndexedOrNull { index, acc, string -> acc + string + index })

    println(emptyList<String>().reduceOrNull { _, _ -> "" })
}
```

```text title="Output"
abcd
ab1c2d3
null
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1255)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
