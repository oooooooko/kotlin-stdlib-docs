# contains

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if this char sequence contains the specified `other` sequence of characters as a substring.

@param ignoreCase `true` to ignore character case when comparing strings. By default `false`.
@sample samples.text.Strings.contains

## Declarations and overloads

### 1. Common

```kotlin
@Suppress("INAPPLICABLE_OPERATOR_MODIFIER")
public operator fun CharSequence.contains(other: CharSequence, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1183)

### 2. Common

```kotlin
@Suppress("INAPPLICABLE_OPERATOR_MODIFIER")
public operator fun CharSequence.contains(char: Char, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1198)

Returns `true` if this char sequence contains the specified character `char`.

@param ignoreCase `true` to ignore character case when comparing characters. By default `false`.
@sample samples.text.Strings.containsChar

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun CharSequence.contains(regex: Regex): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1208)

Returns `true` if this char sequence contains at least one match of the specified regular expression `regex`.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "Kotlin 2.2.0"
    println("K" in string)

    // The string only contains capital K
    println("k" in string)
    // However, it will be located if the case is ignored
    println(string.contains("k", ignoreCase = true))

    // Every string contains an empty string
    println("" in string)
    // The string contains itself ...
    println(string in string)
    // ... even if it is empty
    println("" in "")

    // String's prefix is shorter than a string, so it can't contain it
    println(string in "Kotlin")
}
```

```text title="Output"
true
false
true
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L561)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val text = "kotlin"

    // The string contains lowercase 'k'
    println('k' in text)

    // The string does not contain uppercase 'K' (case-sensitive check)
    println('K' in text)

    // However, it will be located if the case is ignored
    println(text.contains('K', ignoreCase = true))

    // The string does not contain 'z'
    println('z' in text)
}
```

```text title="Output"
true
false
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L582)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
