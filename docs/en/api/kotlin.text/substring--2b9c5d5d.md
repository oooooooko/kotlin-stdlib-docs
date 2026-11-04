# substring

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a substring of this string that starts at the specified `startIndex` and continues to the end of the string.

@param startIndex the start index (inclusive).

@throws IndexOutOfBoundsException when `startIndex` is negative or exceeds the length if the string.

@sample samples.text.Strings.substringFromStartIndex

## Declarations and overloads

### 1. Common

```kotlin
public expect fun String.substring(startIndex: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L382)

### 2. Common

```kotlin
public expect fun String.substring(startIndex: Int, endIndex: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L393)

Returns the substring of this string starting at the `startIndex` and ending right before the `endIndex`.

@param startIndex the start index (inclusive).
@param endIndex the end index (exclusive).

@throws IndexOutOfBoundsException when `startIndex` is negative, `endIndex` exceeds the length if the string, or
 if `startIndex` is greater than `endIndex`.

@sample samples.text.Strings.substringByStartAndEndIndices

### 3. Common

```kotlin
public fun String.substring(range: IntRange): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L400)

Returns a substring specified by the given `range` of indices.

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.substring(startIndex: Int, endIndex: Int = length): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L422)

Returns a substring of chars from a range of this char sequence starting at the `startIndex` and ending right before the `endIndex`.

@param startIndex the start index (inclusive).
@param endIndex the end index (exclusive). If not specified, the length of the char sequence is used.

### 5. Common

```kotlin
public fun CharSequence.substring(range: IntRange): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L431)

Returns a substring of chars at indices from the specified `range` of this char sequence.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val str = "abcde"
    println(str.substring(0))
    println(str.substring(1))
    // startIndex exceeds the string length
    assertFailsWith<IndexOutOfBoundsException> { str.substring(6) }
}
```

```text title="Output"
abcde
bcde
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L854)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val str = "abcde"
    println(str.substring(0, 0))
    println(str.substring(0, 1))
    println(str.substring(5, 5))
    // endIndex exceeds string length
    assertFailsWith<IndexOutOfBoundsException> { str.substring(0, 6) }
    // endIndex is smaller than the startIndex
    assertFailsWith<IndexOutOfBoundsException> { str.substring(1, 0) }
}
```

```text title="Output"

a
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L863)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
