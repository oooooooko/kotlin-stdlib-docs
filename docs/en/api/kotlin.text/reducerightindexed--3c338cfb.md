# reduceRightIndexed

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with the last character and applying `operation` from right to left
to each character with its index in the original char sequence and current accumulator value.

Throws an exception if this char sequence is empty. If the char sequence can be empty in an expected way,
please use `reduceRightIndexedOrNull` instead. It returns `null` when its receiver is empty.

@param `operation` function that takes the index of a character, the character itself and current accumulator value,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduceRight

## Declarations and overloads

### 1. Common

```kotlin
public inline fun CharSequence.reduceRightIndexed(operation: (index: Int, Char, acc: Char) -> Char): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2011)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceRight { string, acc -> acc + string })
    println(strings.reduceRightIndexed { index, string, acc -> acc + string + index })

    assertFails { emptyList<Int>().reduceRight { _, _ -> 0 } }
}
```

```text title="Output"
dcba
dc2b1a0
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1246)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
