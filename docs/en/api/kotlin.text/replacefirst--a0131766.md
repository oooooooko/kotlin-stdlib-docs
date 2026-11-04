# replaceFirst

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new string with the first occurrence of `oldChar` replaced with `newChar`.

## Declarations and overloads

### 1. Common

```kotlin
public expect fun String.replaceFirst(oldChar: Char, newChar: Char, ignoreCase: Boolean = false): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L429)

### 2. Common

```kotlin
public expect fun String.replaceFirst(oldValue: String, newValue: String, ignoreCase: Boolean = false): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L434)

Returns a new string obtained by replacing the first occurrence of the `oldValue` substring in this string
with the specified `newValue` string.

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.replaceFirst(regex: Regex, replacement: String): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L807)

Replaces the first occurrence of the given regular expression `regex` in this char sequence
with the specified `replacement` expression.

This is a convenience function that is equivalent to `regex.replaceFirst(this, replacement)`.
For details about its behaviour and the substitution syntax of `replacement` expression, refer to `Regex.replaceFirst`.

@sample samples.text.Strings.replaceFirstWithExpression

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val text = "The events are on 15-09-2024 and 16-10-2024."
    // Regex to match dates in dd-mm-yyyy format
    val dateRegex = "(?<day>\\d{2})-(?<month>\\d{2})-(?<year>\\d{4})".toRegex()
    // Replacement expression that puts day, month and year values in the ISO 8601 recommended yyyy-mm-dd format
    val replacement = "\${year}-\${month}-\${day}"

    // Replacing the first occurrence of a date from dd-mm-yyyy to yyyy-mm-dd format
    println(text.replaceFirst(dateRegex, replacement))

    // One can also reference the matched groups by index
    println(text.replaceFirst(dateRegex, "$3-$2-$1"))

    // Using a backslash to include the special character '$' as a literal in the result
    println(text.replaceFirst(dateRegex, "$3-\\$2-$1"))
}
```

```text title="Output"
The events are on 2024-09-15 and 16-10-2024.
The events are on 2024-09-15 and 16-10-2024.
The events are on 2024-$2-15 and 16-10-2024.
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L943)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
