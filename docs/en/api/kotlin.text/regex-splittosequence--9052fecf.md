# Regex.splitToSequence

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Splits the `input` CharSequence to a sequence of strings around matches of this regular expression.

The last element of the resulting sequence corresponds to an `input` subsequence starting right
after the last match (or at the beginning of `input` char sequence if there were no matches)
and ending at the end of `input`. That implies that if `input` does not contain subsequences
matching `this` regular expression, the resulting sequence will contain a single element
corresponding to the whole `input` sequence.
It also implies that for char sequences ending with a `this` regular expression match,
the resulting sequence will end with an empty string.

@param limit Non-negative value specifying the maximum number of substrings the string can be split to.
Zero by default means no limit is set.
@sample samples.text.Regexps.splitToSequence

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.6")
    public fun splitToSequence(input: CharSequence, limit: Int = 0): Sequence<String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L159)

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
    val source = Regex("[a-z]+")
    val result = source.`splitToSequence`("AQID")
    println(result.toList())
}
```

```text title="Output"
[AQID]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
