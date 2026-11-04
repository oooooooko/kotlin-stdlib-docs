# maxOfWithOrNull

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the largest value according to the provided `comparator`
among all values produced by `selector` function applied to each character in the char sequence or `null` if the char sequence is empty.

If multiple characters produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithGeneric

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R> CharSequence.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Char) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L1467)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    data class Book(val title: String, val publishYear: Int, val rating: Double)

    // A custom Comparator that orders strings by their length
    val lengthComparator = compareBy<String> { it.length }

    // The longest and shortest book titles
    val books = listOf(
        Book("Red Sand", 2004, 3.5),
        Book("Silver Bullet", 2009, 4.4),
        Book("Clear Water", 2018, 4.1),
        Book("Night Sky", 2023, 3.8)
    )
    println(books.maxOfWith(lengthComparator) { it.title })
    println(books.minOfWith(lengthComparator) { it.title })

    val emptyList = listOf<Book>()

    // maxOfWith() and minOfWith() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.maxOfWith(lengthComparator) { it.title } }
    assertFailsWith<NoSuchElementException> { emptyList.minOfWith(lengthComparator) { it.title } }

    // maxOfWithOrNull() and minOfWithOrNull() return null if the collection is empty
    println(emptyList.maxOfWithOrNull(lengthComparator) { it.title })
    println(emptyList.minOfWithOrNull(lengthComparator) { it.title })
}
```

```text title="Output"
Silver Bullet
Red Sand
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1190)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
