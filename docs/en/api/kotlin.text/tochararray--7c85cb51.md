# toCharArray

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a `CharArray` containing characters of this string.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun String.toCharArray(): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L283)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun String.toCharArray(startIndex: Int = 0, endIndex: Int = this.length): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L289)

Returns a `CharArray` containing characters of this string or its substring.

@param startIndex the beginning (inclusive) of the substring, 0 by default.
@param endIndex the end (exclusive) of the substring, length of this string by default.

@throws IndexOutOfBoundsException if `startIndex` is less than zero or `endIndex` is greater than the length of this string.
@throws IllegalArgumentException if `startIndex` is greater than `endIndex`.

### 3. Common

```kotlin
@SinceKotlin("2.0")
@IgnorableReturnValue
public expect fun String.toCharArray(
    destination: CharArray,
    destinationOffset: Int = 0,
    startIndex: Int = 0,
    endIndex: Int = length
): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L301)

Copies characters from this string into the `destination` character array and returns that array.

@param destination the array to copy to.
@param destinationOffset the position in the array to copy to.
@param startIndex the start offset (inclusive) of the substring to copy.
@param endIndex the end offset (exclusive) of the substring to copy.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of this string builder indices or when `startIndex > endIndex`.
@throws IndexOutOfBoundsException when the subrange doesn't fit into the `destination` array starting at the specified `destinationOffset`,
 or when that index is out of the `destination` array indices range.

### 4. Common

```kotlin
@SinceKotlin("1.4")
public expect fun StringBuilder.toCharArray(destination: CharArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = this.length)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L418)

Copies characters from this string builder into the `destination` character array.

@param destination the array to copy to.
@param destinationOffset the position in the array to copy to, 0 by default.
@param startIndex the beginning (inclusive) of the range to copy, 0 by default.
@param endIndex the end (exclusive) of the range to copy, length of this string builder by default.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of this string builder indices or when `startIndex > endIndex`.
@throws IndexOutOfBoundsException when the subrange doesn't fit into the `destination` array starting at the specified `destinationOffset`,
 or when that index is out of the `destination` array indices range.

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
    val source = "kotlin"
    val result = source.`toCharArray`()
    println(result.contentToString())
}
```

```text title="Output"
[k, o, t, l, i, n]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
