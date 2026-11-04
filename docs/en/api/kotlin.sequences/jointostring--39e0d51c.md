# joinToString

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a string from all the elements separated using `separator` and using the given `prefix` and `postfix` if supplied.

If the collection has no elements, the result consists of only `prefix` followed by `postfix` (both are empty by default).

If the collection is huge, you can specify a non-negative value of `limit`, in which case only the first `limit`
elements will be appended, followed by the `truncated` string (which defaults to "...").

The operation is _terminal_.

@sample samples.collections.Collections.Transformations.joinToString

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Sequence<T>.joinToString(separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((T) -> CharSequence)? = null): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3337)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers = listOf(1, 2, 3, 4, 5, 6)
    println(numbers.joinToString())
    println(numbers.joinToString(prefix = "[", postfix = "]"))
    println(numbers.joinToString(prefix = "<", postfix = ">", separator = "•"))

    val chars = charArrayOf('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q')
    println(chars.joinToString(limit = 5, truncated = "...!") { it.uppercaseChar().toString() })

    // If the receiver is empty, the result only contains prefix and postfix
    println(emptyList<Int>().joinToString().isEmpty())
    println(emptyList<Int>().joinToString(prefix = "[", postfix = "]"))
}
```

```text title="Output"
1, 2, 3, 4, 5, 6
[1, 2, 3, 4, 5, 6]
<1•2•3•4•5•6>
A, B, C, D, E, ...!
true
[]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L867)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
