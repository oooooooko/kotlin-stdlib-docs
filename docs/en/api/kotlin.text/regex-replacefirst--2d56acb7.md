# Regex.replaceFirst

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Replaces the first occurrence of this regular expression in the specified `input` string with specified `replacement` expression.

The replacement string may contain references to the captured groups during a match. Occurrences of `${name}` or `$index`
in the replacement string will be substituted with the subsequences corresponding to the captured groups with the specified name or index.
In case of `$index`, the first digit after '$' is always treated as a part of group reference. Subsequent digits are incorporated
into `index` only if they would form a valid group reference. Only the digits '0'..'9' are considered as potential components
of the group reference. Note that indexes of captured groups start from 1, and the group with index 0 is the whole match.
In case of `${name}`, the `name` can consist of latin letters 'a'..'z' and 'A'..'Z', or digits '0'..'9'. The first character must be
a letter.

Backslash character '\' can be used to include the succeeding character as a literal in the replacement string, e.g, `\$` or `\\`.
`Regex.escapeReplacement` can be used if `replacement` have to be treated as a literal string.

@param input the char sequence to find a match of this regular expression in
@param replacement the expression to replace the found match with
@return the result of replacing the first occurrence of this regular expression in `input` with the result of evaluating the `replacement` expression
@throws RuntimeException if `replacement` expression is malformed, or capturing group with specified `name` or `index` does not exist

@sample samples.text.Regexps.replaceFirstWithExpression

## Declarations and overloads

### 1. Common

```kotlin
public fun replaceFirst(input: CharSequence, replacement: String): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L99)

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
    val result = source.`replaceFirst`("AQID", "o")
    println(result)
}
```

```text title="Output"
AQID
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
