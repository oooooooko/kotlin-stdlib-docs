# lastIndexOfAny

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Finds the index of the last occurrence of any of the specified `chars` in this char sequence,
starting from the specified `startIndex` and optionally ignoring the case.

@param startIndex The index of character to start searching at. The search proceeds backward toward the beginning of the string.
@param ignoreCase `true` to ignore character case when matching a character. By default `false`.
@return An index of the last occurrence of matched character from `chars` or -1 if none of `chars` are found.

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.lastIndexOfAny(chars: CharArray, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L990)

### 2. Common

```kotlin
public fun CharSequence.lastIndexOfAny(strings: Collection<String>, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1106)

Finds the index of the last occurrence of any of the specified `strings` in this char sequence,
starting from the specified `startIndex` and optionally ignoring the case.

To avoid ambiguous results when strings in `strings` have characters in common, this method proceeds from
the end toward the beginning of this string, and finds at each position the first element in `strings`
that matches this string at that position.

@param startIndex The index of character to start searching at. The search proceeds backward toward the beginning of the string.
@param ignoreCase `true` to ignore character case when matching a string. By default `false`.
@return An index of the last occurrence of matched string from `strings` or -1 if none of `strings` are found.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.text.*

fun main() {
    val source = "kotlin"
    val result = source.`lastIndexOfAny`(charArrayOf('a', 'b', 'c'))
    println(result)
}
```

```text title="Output"
-1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
