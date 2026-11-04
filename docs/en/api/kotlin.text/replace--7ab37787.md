# replace

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new string with all occurrences of `oldChar` replaced with `newChar`.

@sample samples.text.Strings.replace

## Declarations and overloads

### 1. Common

```kotlin
public expect fun String.replace(oldChar: Char, newChar: Char, ignoreCase: Boolean = false): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L414)

### 2. Common

```kotlin
public expect fun String.replace(oldValue: String, newValue: String, ignoreCase: Boolean = false): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L421)

Returns a new string obtained by replacing all occurrences of the `oldValue` substring in this string
with the specified `newValue` string.

@sample samples.text.Strings.replace

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.replace(regex: Regex, replacement: String): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L786)

Replaces all occurrences of the given regular expression `regex` in this char sequence
with the specified `replacement` expression.

This is a convenience function that is equivalent to `regex.replace(this, replacement)`.
For details about its behaviour and the substitution syntax of `replacement` expression, refer to `Regex.replace`.

@sample samples.text.Strings.replaceWithExpression

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.replace(regex: Regex, noinline transform: (MatchResult) -> CharSequence): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L798)

Returns a new string obtained by replacing each substring of this char sequence that matches the given regular expression
with the result of the given function `transform` that takes `MatchResult` and returns a string to be used as a
replacement for that match.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val inputString0 = "Mississippi"
    val inputString1 = "Insufficient data for meaningful answer."

    println(inputString0.replace('s', 'z'))
    println(inputString1.replace("data", "information"))
}
```

```text title="Output"
Mizzizzippi
Insufficient information for meaningful answer.
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L612)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val text = "The events are on 15-09-2024 and 16-10-2024."
    // Regex to match dates in dd-mm-yyyy format
    val dateRegex = "(?<day>\\d{2})-(?<month>\\d{2})-(?<year>\\d{4})".toRegex()
    // Replacement expression that puts day, month and year values in the ISO 8601 recommended yyyy-mm-dd format
    val replacement = "\${year}-\${month}-\${day}"

    // Replacing all occurrences of dates from dd-mm-yyyy to yyyy-mm-dd format
    println(text.replace(dateRegex, replacement))

    // One can also reference the matched groups by index
    println(text.replace(dateRegex, "$3-$2-$1"))

    // Using a backslash to include the special character '$' as a literal in the result
    println(text.replace(dateRegex, "$3-\\$2-$1"))
}
```

```text title="Output"
The events are on 2024-09-15 and 2024-10-16.
The events are on 2024-09-15 and 2024-10-16.
The events are on 2024-$2-15 and 2024-$2-16.
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L925)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
