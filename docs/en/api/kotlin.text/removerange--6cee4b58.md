# removeRange

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a `CharSequence` obtained by removing the specified subsequence from this char sequence.

@param startIndex the beginning (inclusive) of the subsequence to remove.
@param endIndex the end (exclusive) of the subsequence to remove.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of this char sequence indices
  or when `startIndex > endIndex`.

@sample samples.text.Strings.removeRangeCharSequence

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.removeRange(startIndex: Int, endIndex: Int): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L559)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.removeRange(startIndex: Int, endIndex: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L583)

Returns a `String` obtained by removing the specified substring from this string.

@param startIndex the beginning (inclusive) of the substring to remove.
@param endIndex the end (exclusive) of the substring to remove.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of this string indices
  or when `startIndex > endIndex`.

@sample samples.text.Strings.removeRangeString

### 3. Common

```kotlin
public fun CharSequence.removeRange(range: IntRange): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L598)

Returns a `CharSequence` obtained by removing the specified subsequence from this char sequence.

@param range the range of indexes of the subsequence to remove.
  Note: the character at index `IntRange.endInclusive` of the `range` is removed as well.

@sample samples.text.Strings.removeRangeCharSequence

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.removeRange(range: IntRange): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L608)

Returns a `String` obtained by removing the specified substring from this char sequence.

@param range the range of indexes of the substring to remove.
  Note: the character at index `IntRange.endInclusive` of the `range` is removed as well.

@sample samples.text.Strings.removeRangeString

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val text = StringBuilder("Hello, world!")

    // Removing the range that correspond to the "world" subsequence
    println(text.removeRange(startIndex = 7, endIndex = 12))

    // Also possible to remove using a Range
    println(text.removeRange(7..11))

    // The original char sequence is not changed
    println(text)

    // Throws if startIndex is greater than endIndex
    assertFails { text.removeRange(startIndex = 7, endIndex = 4) }
    // Throws if startIndex or endIndex is out of range of the char sequence indices
    assertFails { text.removeRange(startIndex = 7, endIndex = 20) }
}
```

```text title="Output"
Hello, !
Hello, !
Hello, world!
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L980)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val text = "Hello, world!"

    // Removing the range that correspond to the "world" substring
    println(text.removeRange(startIndex = 7, endIndex = 12))

    // Also possible to remove using a Range
    println(text.removeRange(7..11))

    // The original string is not changed
    println(text)

    // Throws if startIndex is greater than endIndex
    assertFails { text.removeRange(startIndex = 7, endIndex = 4) }
    // Throws if startIndex or endIndex is out of range of the string indices
    assertFails { text.removeRange(startIndex = 7, endIndex = 20) }
}
```

```text title="Output"
Hello, !
Hello, !
Hello, world!
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L961)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
