# removeSurrounding

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

When this char sequence starts with the given `prefix` and ends with the given `suffix`,
returns a new char sequence having both the given `prefix` and `suffix` removed.
Otherwise, returns a new char sequence with the same characters.

@sample samples.text.Strings.removeSurroundingPrefixSuffixCharSequence

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.removeSurrounding(prefix: CharSequence, suffix: CharSequence): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L664)

### 2. Common

```kotlin
public fun String.removeSurrounding(prefix: CharSequence, suffix: CharSequence): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L678)

Removes from a string both the given `prefix` and `suffix` if and only if
it starts with the `prefix` and ends with the `suffix`.
Otherwise, returns this string unchanged.

@sample samples.text.Strings.removeSurroundingPrefixSuffixString

### 3. Common

```kotlin
public fun CharSequence.removeSurrounding(delimiter: CharSequence): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L692)

When this char sequence starts with and ends with the given `delimiter`,
returns a new char sequence having this `delimiter` removed both from the start and end.
Otherwise, returns a new char sequence with the same characters.

@sample samples.text.Strings.removeSurroundingDelimiterCharSequence

### 4. Common

```kotlin
public fun String.removeSurrounding(delimiter: CharSequence): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L701)

Removes the given `delimiter` string from both the start and the end of this string
if and only if it starts with and ends with the `delimiter`.
Otherwise, returns this string unchanged.

@sample samples.text.Strings.removeSurroundingDelimiterString

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val textCharSequence: CharSequence = StringBuilder("[content]")
    println(textCharSequence.removeSurrounding("[", "]"))
    // Does not start with prefix
    println(StringBuilder("content]").removeSurrounding("[", "]"))
    // Does not end with suffix
    println(StringBuilder("[content").removeSurrounding("[", "]"))
    // Does not start or end with prefix/suffix
    println(StringBuilder("content").removeSurrounding("[", "]"))
    // Empty content
    println(StringBuilder("[]").removeSurrounding("[", "]"))
    // Different delimiters
    println(StringBuilder("<content>").removeSurrounding("[", "]"))
}
```

```text title="Output"
content
content]
[content
content

<content>
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1068)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val textString = "[content]"
    println(textString.removeSurrounding("[", "]"))
    // Does not start with prefix
    println("content]".removeSurrounding("[", "]"))
    // Does not end with suffix
    println("[content".removeSurrounding("[", "]"))
    // Does not start or end with prefix/suffix
    println("content".removeSurrounding("[", "]"))
    // Empty content
    println("[]".removeSurrounding("[", "]"))
    // Different delimiters
    println("<content>".removeSurrounding("[", "]"))
}
```

```text title="Output"
content
content]
[content
content

<content>
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1052)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val textCharSequence: CharSequence = StringBuilder("***content***")
    println(textCharSequence.removeSurrounding("***"))
    // Does not end with delimiter
    println(StringBuilder("##content").removeSurrounding("##"))
    // Does not start with delimiter
    println(StringBuilder("content##").removeSurrounding("##"))
    // No delimiters
    println(StringBuilder("content").removeSurrounding("##"))
    // Empty content
    println(StringBuilder("****").removeSurrounding("**"))
    // Delimiter is single char, removes only one pair
    println(StringBuilder("!!!content!!!").removeSurrounding("!"))
}
```

```text title="Output"
content
##content
content##
content

!!content!!
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1100)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val textString = "***content***"
    println(textString.removeSurrounding("***"))
    // Does not end with delimiter
    println("##content".removeSurrounding("##"))
    // Does not start with delimiter
    println("content##".removeSurrounding("##"))
    // No delimiters
    println("content".removeSurrounding("##"))
    // Empty content
    println("****".removeSurrounding("**"))
    // Delimiter is single char, removes only one pair
    println("!!!content!!!".removeSurrounding("!"))
}
```

```text title="Output"
content
##content
content##
content

!!content!!
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1084)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
