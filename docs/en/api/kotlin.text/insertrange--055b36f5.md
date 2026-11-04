# insertRange

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Inserts characters in a subarray of the specified character array `value` into this string builder at the specified `index` and returns this instance.

The inserted characters go in same order as in the `value` array, starting at `index`.

@param index the position in this string builder to insert at.
@param value the array from which characters are inserted.
@param startIndex the beginning (inclusive) of the subarray to insert.
@param endIndex the end (exclusive) of the subarray to insert.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of the `value` array indices or when `startIndex > endIndex`.
@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue public expect fun StringBuilder.insertRange(index: Int, value: CharArray, startIndex: Int, endIndex: Int): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L459)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue public expect fun StringBuilder.insertRange(index: Int, value: CharSequence, startIndex: Int, endIndex: Int): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L475)

Inserts characters in a subsequence of the specified character sequence `value` into this string builder at the specified `index` and returns this instance.

The inserted characters go in the same order as in the `value` character sequence, starting at `index`.

@param index the position in this string builder to insert at.
@param value the character sequence from which a subsequence is inserted.
@param startIndex the beginning (inclusive) of the subsequence to insert.
@param endIndex the end (exclusive) of the subsequence to insert.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of the `value` character sequence indices or when `startIndex > endIndex`.
@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

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
    val result = source.`insertRange`(0, charArrayOf('a', 'b', 'c'), 0, 2)
    println(result)
}
```

```text title="Output"
abkotlin
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
