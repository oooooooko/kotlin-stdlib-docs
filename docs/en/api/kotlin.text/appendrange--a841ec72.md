# appendRange

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends a subsequence of the specified character sequence `value` to this Appendable and returns this instance.

@param value the character sequence from which a subsequence is appended.
@param startIndex the beginning (inclusive) of the subsequence to append.
@param endIndex the end (exclusive) of the subsequence to append.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of the `value` character sequence indices or when `startIndex > endIndex`.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
public fun <T : Appendable> T.appendRange(value: CharSequence, startIndex: Int, endIndex: Int): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L45)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue public expect fun StringBuilder.appendRange(value: CharArray, startIndex: Int, endIndex: Int): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L433)

Appends characters in a subarray of the specified character array `value` to this string builder and returns this instance.

Characters are appended in order, starting at specified `startIndex`.

@param value the array from which characters are appended.
@param startIndex the beginning (inclusive) of the subarray to append.
@param endIndex the end (exclusive) of the subarray to append.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of the `value` array indices or when `startIndex > endIndex`.

### 3. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue public expect fun StringBuilder.appendRange(value: CharSequence, startIndex: Int, endIndex: Int): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L447)

Appends a subsequence of the specified character sequence `value` to this string builder and returns this instance.

@param value the character sequence from which a subsequence is appended.
@param startIndex the beginning (inclusive) of the subsequence to append.
@param endIndex the end (exclusive) of the subsequence to append.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of the `value` character sequence indices or when `startIndex > endIndex`.

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
    val source = StringBuilder("kotlin")
    val result = source.`appendRange`(charArrayOf('a', 'b', 'c'), 0, 2)
    println(result)
}
```

```text title="Output"
kotlinab
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
