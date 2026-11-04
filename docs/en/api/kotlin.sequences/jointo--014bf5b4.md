# joinTo

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends the string from all the elements separated using `separator` and using the given `prefix` and `postfix` if supplied.

If the collection has no elements, the function appends only `prefix` followed by `postfix` to `buffer` (both are empty by default).

If the collection is huge, you can specify a non-negative value of `limit`, in which case only the first `limit`
elements will be appended, followed by the `truncated` string (which defaults to "...").

@return the `buffer` argument with appended elements.

The operation is _terminal_.

@sample samples.collections.Collections.Transformations.joinTo

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public fun <T, A : Appendable> Sequence<T>.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((T) -> CharSequence)? = null): A
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3308)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val sb = StringBuilder("An existing string and a list: ")
    val numbers = listOf(1, 2, 3)
    println(numbers.joinTo(sb, prefix = "[", postfix = "]").toString())

    val lotOfNumbers: Iterable<Int> = 1..100
    val firstNumbers = StringBuilder("First five numbers: ")
    println(lotOfNumbers.joinTo(firstNumbers, limit = 5).toString())

    // If the receiver is empty, the result only contains prefix and postfix
    println(emptyList<Int>().joinTo(StringBuilder()).toString().isEmpty())
    println(emptyList<Int>().joinTo(StringBuilder(), prefix = "[", postfix = "]").toString())
}
```

```text title="Output"
An existing string and a list: [1, 2, 3]
First five numbers: 1, 2, 3, 4, 5, ...
true
[]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L852)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
