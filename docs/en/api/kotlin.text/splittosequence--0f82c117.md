# splitToSequence

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Splits this char sequence to a sequence of strings around occurrences of the specified `delimiters`.

The last element of the resulting sequence corresponds to a subsequence starting right after the last
delimiter occurrence (or at the beginning of this char sequence if there were no such occurrences)
and ending at the end of this char sequence. That implies that if this char sequence does not
contain `delimiters`, the resulting sequence will contain a single element corresponding to
the whole char sequence. It also implies that for char sequences ending with one of `delimiters`,
the resulting sequence will end with an empty string.

To avoid ambiguous results when strings in `delimiters` have characters in common, this method proceeds from
the beginning to the end of this string, and finds at each position the first element in `delimiters`
that matches this string at that position.

@param delimiters One or more strings to be used as delimiters.
@param ignoreCase `true` to ignore character case when matching a delimiter. By default `false`.
@param limit The maximum number of substrings to return. Zero by default means no limit is set.

@sample samples.text.Strings.splitToSequenceWithStringDelimiters

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.splitToSequence(vararg delimiters: String, ignoreCase: Boolean = false, limit: Int = 0): Sequence<String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1383)

### 2. Common

```kotlin
public fun CharSequence.splitToSequence(vararg delimiters: Char, ignoreCase: Boolean = false, limit: Int = 0): Sequence<String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1437)

Splits this char sequence to a sequence of strings around occurrences of the specified `delimiters`.

The last element of the resulting sequence corresponds to a subsequence starting right after the last
delimiter occurrence (or at the beginning of this char sequence if there were no such occurrences)
and ending at the end of this char sequence. That implies that if this char sequence does not
contain `delimiters`, the resulting sequence will contain a single element corresponding to
the whole char sequence. It also implies that for char sequences ending with one of `delimiters`,
the resulting sequence will end with an empty string.

@param delimiters One or more characters to be used as delimiters.
@param ignoreCase `true` to ignore character case when matching a delimiter. By default `false`.
@param limit The maximum number of substrings to return.

@sample samples.text.Strings.splitToSequenceWithCharDelimiters

### 3. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun CharSequence.splitToSequence(regex: Regex, limit: Int = 0): Sequence<String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1535)

Splits this char sequence to a sequence of strings around matches of the given regular expression.

The last element of the resulting sequence corresponds to a subsequence starting right after the last
`regex` match (or at the beginning of this char sequence if there were no matches)
and ending at the end of this char sequence. That implies that if this char sequences does not
contain subsequences matching `regex`, the resulting sequence will contain a single element
corresponding to the whole char sequence.
It also implies that for char sequences ending with a `regex` match,
the resulting sequence will end with an empty string.

@param limit Non-negative value specifying the maximum number of substrings to return.
Zero by default means no limit is set.
@sample samples.text.Strings.splitToSequence

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun Sequence<String>.toPrettyString() = joinToString(", ", "[", "]")

    val multiCharDelimiter = "apple--banana--cherry".splitToSequence("--").toPrettyString()
    println(multiCharDelimiter)

    val multipleSplit = "apple->banana;;cherry:::orange".splitToSequence("->", ";;", ":::").toPrettyString()
    println(multipleSplit)

    val longerDelimiterFirst = "apple<-banana<--cherry".splitToSequence("<--", "<-").toPrettyString()
    println(longerDelimiterFirst)

    val shorterDelimiterFirst = "apple<-banana<--cherry".splitToSequence("<-", "<--").toPrettyString()
    println(shorterDelimiterFirst)

    val limitSplit = "a->b->c->d->e".splitToSequence("->", limit = 3).toPrettyString()
    println(limitSplit)

    val emptyInputResult = "".splitToSequence("sep").toList()
    println(emptyInputResult == listOf(""))

    val emptyDelimiterSplit = "abc".splitToSequence("").toPrettyString()
    println(emptyDelimiterSplit)

    val mixedCase = "abcXYZdef".splitToSequence("xyz").toPrettyString()
    println(mixedCase)  // No match with case sensitivity

    val mixedCaseIgnored = "abcXYZdef".splitToSequence("xyz", ignoreCase = true).toPrettyString()
    println(mixedCaseIgnored)  // Matches with case insensitivity

    val emptyResults = "##a##b##c##".splitToSequence("##").toPrettyString()
    println(emptyResults)

    val consecutiveSeparators = "a--b------c".splitToSequence("--").toPrettyString()
    println(consecutiveSeparators)
}
```

```text title="Output"
[apple, banana, cherry]
[apple, banana, cherry, orange]
[apple, banana, cherry]
[apple, banana, -cherry]
[a, b, c->d->e]
true
[, a, b, c, ]
[abcXYZdef]
[abc, def]
[, a, b, c, ]
[a, b, , , c]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L708)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun Sequence<String>.toPrettyString() = joinToString(", ", "[", "]")

    val commaSplit = "apple,banana,cherry".splitToSequence(',').toPrettyString()
    println(commaSplit)

    val charSplit = "apple,banana;cherry".splitToSequence(',', ';').toPrettyString()
    println(charSplit)

    val limitSplit = "a,b,c,d,e".splitToSequence(',', limit = 3).toPrettyString()
    println(limitSplit)

    val emptyInputResult = "".splitToSequence('|').toList()
    println(emptyInputResult == listOf(""))

    val mixedCase = "abcXdef".splitToSequence('x').toPrettyString()
    println(mixedCase)  // No match with case sensitivity

    val mixedCaseIgnored = "abcXdef".splitToSequence('x', ignoreCase = true).toPrettyString()
    println(mixedCaseIgnored)  // Matches with case insensitivity

    val emptyResults = ",a,b,c,".splitToSequence(',').toPrettyString()
    println(emptyResults)

    val consecutiveSeparators = "a,,b,,,c".splitToSequence(',').toPrettyString()
    println(consecutiveSeparators)
}
```

```text title="Output"
[apple, banana, cherry]
[apple, banana, cherry]
[a, b, c,d,e]
true
[abcXdef]
[abc, def]
[, a, b, c, ]
[a, , b, , , c]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L773)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val colors = "green, red , brown&blue, orange, pink&green"
    val regex = "[,\\s]+".toRegex()

    val mixedColor = colors.splitToSequence(regex)
        .onEach { println(it) }
        .firstOrNull { it.contains('&') }

    println(mixedColor)
}
```

```text title="Output"
green
red
brown&blue
brown&blue
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L660)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
