# replaceRange

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a char sequence with content of this char sequence where its part at the given range
is replaced with the `replacement` char sequence.
@param startIndex the index of the first character to be replaced.
@param endIndex the index of the first character after the replacement to keep in the string.

@sample samples.text.Strings.replaceRange

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.replaceRange(startIndex: Int, endIndex: Int, replacement: CharSequence): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L508)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.replaceRange(startIndex: Int, endIndex: Int, replacement: CharSequence): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L526)

Replaces the part of the string at the given range with the `replacement` char sequence.
@param startIndex the index of the first character to be replaced.
@param endIndex the index of the first character after the replacement to keep in the string.

@sample samples.text.Strings.replaceRange

### 3. Common

```kotlin
public fun CharSequence.replaceRange(range: IntRange, replacement: CharSequence): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L537)

Returns a char sequence with content of this char sequence where its part at the given `range`
is replaced with the `replacement` char sequence.

The end index of the `range` is included in the part to be replaced.

@sample samples.text.Strings.replaceRange

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.replaceRange(range: IntRange, replacement: CharSequence): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L548)

Replace the part of string at the given `range` with the `replacement` string.

The end index of the `range` is included in the part to be replaced.

@sample samples.text.Strings.replaceRange

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val text = "Hello, world!"

    // Replacing the range that corresponds to the "world" substring with "Kotlin"
    println(text.replaceRange(startIndex = 7, endIndex = 12, replacement = "Kotlin"))

    // Also possible to replace using a Range
    println(text.replaceRange(7..11, replacement = "Kotlin"))

    // Empty replacement effectively removes the range
    println(text.replaceRange(7..11, ""))

    // Replacing at the end of the string: endIndex is exclusive
    println(text.replaceRange(0, 5, "Hey"))

    // But for the overload accepting the range, range's end is inclusive (thus the comma is also replaced)
    println(text.replaceRange(0..5, "Hey"))

    // Throws if startIndex is greater than endIndex
    assertFails { text.replaceRange(startIndex = 7, endIndex = 4, replacement = "Kotlin") }
    // Throws if startIndex or endIndex is out of the string indices range
    assertFails { text.replaceRange(startIndex = 7, endIndex = 20, replacement = "Kotlin") }
    // For ranges, the end is inclusive, so it has to be lower than the length of a char sequence
    assertFails { text.replaceRange(7..text.length, replacement = "Kotlin") }
}
```

```text title="Output"
Hello, Kotlin!
Hello, Kotlin!
Hello, !
Hey, world!
Hey world!
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1025)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
