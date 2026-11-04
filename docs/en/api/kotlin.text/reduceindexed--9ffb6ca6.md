# reduceIndexed

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with the first character and applying `operation` from left to right
to current accumulator value and each character with its index in the original char sequence.

Throws an exception if this char sequence is empty. If the char sequence can be empty in an expected way,
please use `reduceIndexedOrNull` instead. It returns `null` when its receiver is empty.

@param `operation` function that takes the index of a character, current accumulator value and the character itself,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduce

## Declarations and overloads

### 1. Common

```kotlin
public inline fun CharSequence.reduceIndexed(operation: (index: Int, acc: Char, Char) -> Char): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L1923)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduce { acc, string -> acc + string })
    println(strings.reduceIndexed { index, acc, string -> acc + string + index })

    assertFails { emptyList<Int>().reduce { _, _ -> 0 } }
}
```

```text title="Output"
abcd
ab1c2d3
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1237)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
