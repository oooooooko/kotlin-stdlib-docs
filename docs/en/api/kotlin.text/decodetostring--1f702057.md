# decodeToString

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Decodes a string from the bytes in UTF-8 encoding in this array.

Malformed byte sequences are replaced by the replacement char `\uFFFD`.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun ByteArray.decodeToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L322)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun ByteArray.decodeToString(
    startIndex: Int = 0,
    endIndex: Int = this.size,
    throwOnInvalidSequence: Boolean = false
): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L330)

Decodes a string from the bytes in UTF-8 encoding in this array or its subrange.

@param startIndex the beginning (inclusive) of the subrange to decode, 0 by default.
@param endIndex the end (exclusive) of the subrange to decode, size of this array by default.
@param throwOnInvalidSequence specifies whether to throw an exception on malformed byte sequence or replace it by the replacement char `\uFFFD`.

@throws IndexOutOfBoundsException if `startIndex` is less than zero or `endIndex` is greater than the size of this array.
@throws IllegalArgumentException if `startIndex` is greater than `endIndex`.
@throws CharacterCodingException if the byte array contains malformed UTF-8 byte sequence and `throwOnInvalidSequence` is true.

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
    val source = byteArrayOf(1, 2, 3)
    val result = source.`decodeToString`()
    println(result)
}
```

```text title="Output"

```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
