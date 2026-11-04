# chunkedSequence

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Splits this char sequence into a sequence of strings each not exceeding the given `size`.

The last string in the resulting sequence may have fewer characters than the given `size`.

@param size the number of elements to take in each string, must be positive and can be greater than the number of elements in this char sequence.

@sample samples.text.Strings.chunkedSequence

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun CharSequence.chunkedSequence(size: Int): Sequence<String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2341)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public fun <R> CharSequence.chunkedSequence(size: Int, transform: (CharSequence) -> R): Sequence<R>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2355)

Splits this char sequence into several char sequences each not exceeding the given `size`
and applies the given `transform` function to an each.

@return sequence of results of the `transform` applied to an each char sequence.

Note that the char sequence passed to the `transform` function is ephemeral and is valid only inside that function.
You should not store it or allow it to escape in some way, unless you made a snapshot of it.
The last char sequence may have fewer characters than the given `size`.

@param size the number of elements to take in each char sequence, must be positive and can be greater than the number of elements in this char sequence.

@sample samples.text.Strings.chunkedTransformToSequence

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val dnaFragment = "ATTCGCCAAXXX"
    val knownAcids = setOf("ATT", "CGC", "CAA") // XXX would cause error if processed
    val codons = dnaFragment.chunkedSequence(3).onEach { check(it in knownAcids) }
    val firstTwo = codons.take(2).toList()

    println(firstTwo)
}
```

```text title="Output"
[ATT, CGC]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L72)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val codonTable = mapOf("ATT" to "Isoleucine", "CAA" to "Glutamine", "CGC" to "Arginine", "GGC" to "Glycine")
    val dnaFragment = "ATTCGCGGCCGCCAACGG"

    val proteins = dnaFragment.chunkedSequence(3) { codon: CharSequence -> codonTable[codon.toString()] ?: error("Unknown codon") }

    // sequence is evaluated lazily, so that unknown codon is not reached
    println(proteins.take(5).toList())
}
```

```text title="Output"
[Isoleucine, Arginine, Glycine, Arginine, Glutamine]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L92)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
