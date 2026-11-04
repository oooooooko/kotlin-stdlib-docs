# zipWithNext

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list of pairs of each two adjacent characters in this char sequence.

The returned list is empty if this char sequence contains less than two characters.

@sample samples.collections.Collections.Transformations.zipWithNext

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun CharSequence.zipWithNext(): List<Pair<Char, Char>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2541)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public inline fun <R> CharSequence.zipWithNext(transform: (a: Char, b: Char) -> R): List<R>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2553)

Returns a list containing the results of applying the given `transform` function
to an each pair of two adjacent characters in this char sequence.

The returned list is empty if this char sequence contains less than two characters.

@sample samples.collections.Collections.Transformations.zipWithNextToFindDeltas

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val letters = ('a'..'f').toList()
    val pairs = letters.zipWithNext()

    println(letters)
    println(pairs)
}
```

```text title="Output"
[a, b, c, d, e, f]
[(a, b), (b, c), (c, d), (d, e), (e, f)]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L937)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val values = listOf(1, 4, 9, 16, 25, 36)
    val deltas = values.zipWithNext { a, b -> b - a }

    println(deltas)
}
```

```text title="Output"
[3, 5, 7, 9, 11]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L946)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
