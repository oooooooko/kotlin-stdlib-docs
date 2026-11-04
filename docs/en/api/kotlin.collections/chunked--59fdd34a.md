# chunked

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Splits this collection into a list of lists each not exceeding the given `size`.

The last list in the resulting list may have fewer elements than the given `size`.

@param size the number of elements to take in each list, must be positive and can be greater than the number of elements in this collection.

@sample samples.collections.Collections.Transformations.chunked

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun <T> Iterable<T>.chunked(size: Int): List<List<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3545)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public fun <T, R> Iterable<T>.chunked(size: Int, transform: (List<T>) -> R): List<R>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3559)

Splits this collection into several lists each not exceeding the given `size`
and applies the given `transform` function to an each.

@return list of results of the `transform` applied to an each list.

Note that the list passed to the `transform` function is ephemeral and is valid only inside that function.
You should not store it or allow it to escape in some way, unless you made a snapshot of it.
The last list may have fewer elements than the given `size`.

@param size the number of elements to take in each list, must be positive and can be greater than the number of elements in this collection.

@sample samples.text.Strings.chunkedTransform

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val words = "one two three four five six seven eight nine ten".split(' ')
    val chunks = words.chunked(3)

    println(chunks)
}
```

```text title="Output"
[[one, two, three], [four, five, six], [seven, eight, nine], [ten]]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L929)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val codonTable = mapOf("ATT" to "Isoleucine", "CAA" to "Glutamine", "CGC" to "Arginine", "GGC" to "Glycine")
    val dnaFragment = "ATTCGCGGCCGCCAA"

    val proteins = dnaFragment.chunked(3) { codon: CharSequence -> codonTable[codon.toString()] ?: error("Unknown codon") }

    println(proteins)
}
```

```text title="Output"
[Isoleucine, Arginine, Glycine, Arginine, Glutamine]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L82)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
