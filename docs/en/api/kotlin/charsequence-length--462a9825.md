# CharSequence.length

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the length of this character sequence.

The length is measured in the number of `Char`s constituting the sequence.
It implies that the length may not correspond to the number of printed graphemes:
some `Char`s could represent control, non-printable, or diaeresis symbols, others could form UTF-16 surrogate pairs,
required to encode Unicode code points not representable by a single `Char`.

@sample samples.text.CharSequences.charSequenceLength

## Declarations and overloads

### 1. Common

```kotlin
public val length: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/CharSequence.kt#L13)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("".length)
    println("Kotlin".length)
    // 🥦 is represented by a pair of UTF-16 characters, thus the string's length is 2, not 1
    println("🥦".length)
}
```

```text title="Output"
0
6
2
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/CharSequences.kt#L12)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
