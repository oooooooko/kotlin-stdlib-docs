# split

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Splits this char sequence to a list of strings around occurrences of the specified `delimiters`.

The last element of the resulting list corresponds to a subsequence starting right after the last
delimiter occurrence (or at the beginning of this char sequence if there were no such occurrences)
and ending at the end of this char sequence. That implies that if this char sequence does not
contain `delimiters`, the resulting list will contain a single element corresponding to
the whole char sequence. It also implies that for char sequences ending with one of `delimiters`,
the resulting list will end with an empty string.

To avoid ambiguous results when strings in `delimiters` have characters in common, this method proceeds from
the beginning to the end of this string, and matches at each position the first element in `delimiters`
that is equal to a delimiter in this instance at that position.

@param delimiters One or more strings to be used as delimiters.
@param ignoreCase `true` to ignore character case when matching a delimiter. By default `false`.
@param limit The maximum number of substrings to return. Zero by default means no limit is set.

@sample samples.text.Strings.splitWithStringDelimiters

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.split(vararg delimiters: String, ignoreCase: Boolean = false, limit: Int = 0): List<String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1406)

### 2. Common

```kotlin
public fun CharSequence.split(vararg delimiters: Char, ignoreCase: Boolean = false, limit: Int = 0): List<String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1456)

Splits this char sequence to a list of strings around occurrences of the specified `delimiters`.

The last element of the resulting list corresponds to a subsequence starting right after the last
delimiter occurrence (or at the beginning of this char sequence if there were no such occurrences)
and ending at the end of this char sequence. That implies that if this char sequence does not
contain `delimiters`, the resulting list will contain a single element corresponding to
the whole char sequence. It also implies that for char sequences ending with one of `delimiters`,
the resulting list will end with an empty string.

@param delimiters One or more characters to be used as delimiters.
@param ignoreCase `true` to ignore character case when matching a delimiter. By default `false`.
@param limit The maximum number of substrings to return.
@sample samples.text.Strings.splitWithCharDelimiters

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.split(regex: Regex, limit: Int = 0): List<String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1517)

Splits this char sequence to a list of strings around matches of the given regular expression.

The last element of the resulting list corresponds to a subsequence starting right after the last
`regex` match (or at the beginning of this char sequence if there were no matches)
and ending at the end of this char sequence. That implies that if this char sequences does not
contain subsequences matching `regex`, the resulting list will contain a single element
corresponding to the whole char sequence.
It also implies that for char sequences ending with a `regex` match,
the resulting list will end with an empty string.

@param limit Non-negative value specifying the maximum number of substrings to return.
Zero by default means no limit is set.
@sample samples.text.Strings.splitWithRegex

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val multiCharDelimiter = "apple--banana--cherry".split("--")
    println(multiCharDelimiter)

    val multipleSplit = "apple->banana;;cherry:::orange".split("->", ";;", ":::")
    println(multipleSplit)

    val longerDelimiterFirst = "apple<-banana<--cherry".split("<--", "<-")
    println(longerDelimiterFirst)

    val shorterDelimiterFirst = "apple<-banana<--cherry".split("<-", "<--")
    println(shorterDelimiterFirst)

    val limitSplit = "a->b->c->d->e".split("->", limit = 3)
    println(limitSplit)

    val emptyInputResult = "".split("sep")
    println(emptyInputResult == listOf(""))

    val emptyDelimiterSplit = "abc".split("")
    println(emptyDelimiterSplit)

    val mixedCase = "abcXYZdef".split("xyz")
    println(mixedCase)  // No match with case sensitivity

    val mixedCaseIgnored = "abcXYZdef".split("xyz", ignoreCase = true)
    println(mixedCaseIgnored)  // Matches with case insensitivity

    val emptyResults = "##a##b##c##".split("##")
    println(emptyResults)

    val consecutiveSeparators = "a--b------c".split("--")
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L672)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val commaSplit = "apple,banana,cherry".split(',')
    println(commaSplit)

    val charSplit = "apple,banana;cherry".split(',', ';')
    println(charSplit)

    val limitSplit = "a,b,c,d,e".split(',', limit = 3)
    println(limitSplit)

    val emptyInputResult = "".split('|')
    println(emptyInputResult == listOf(""))

    val mixedCase = "abcXdef".split('x')
    println(mixedCase)  // No match with case sensitivity

    val mixedCaseIgnored = "abcXdef".split('x', ignoreCase = true)
    println(mixedCaseIgnored)  // Matches with case insensitivity

    val emptyResults = ",a,b,c,".split(',')
    println(emptyResults)

    val consecutiveSeparators = "a,,b,,,c".split(',')
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L746)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val digitSplit = "apple123banana456cherry".split(Regex("\\d+"))
    println(digitSplit)

    val wordBoundarySplit = "The quick brown fox".split(Regex("\\s+"))
    println(wordBoundarySplit)

    val limitSplit = "a,b,c,d,e".split(Regex(","), limit = 3)
    println(limitSplit)

    val patternGroups = "abc-123def_456ghi".split(Regex("[\\-_]\\d+"))
    println(patternGroups)

    val caseInsensitiveSplit = "Apple123Banana45CHERRY".split(Regex("[a-z]+", RegexOption.IGNORE_CASE))
    println(caseInsensitiveSplit)

    val emptyInputResult = "".split(Regex("sep"))
    println(emptyInputResult == listOf(""))

    val emptyDelimiterSplit = "abc".split(Regex(""))
    println(emptyDelimiterSplit)

    val splitByMultipleSpaces = "a  b    c".split(Regex("\\s+"))
    println(splitByMultipleSpaces)

    val splitBySingleSpace = "a  b    c".split(Regex("\\s"))
    println(splitBySingleSpace)
}
```

```text title="Output"
[apple, banana, cherry]
[The, quick, brown, fox]
[a, b, c,d,e]
[abc, def, ghi]
[, 123, 45, ]
true
[, a, b, c, ]
[a, b, c]
[a, , b, , , , c]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L802)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
