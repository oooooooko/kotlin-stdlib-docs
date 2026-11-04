# HexFormat.Companion.UpperCase

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The hexadecimal format options configured to use upper-case hexadecimal digits.

This `HexFormat` instance adopts default values for all format options, except for `upperCase`,
which is set to `true`. As a result, formatting functions will use upper-case hexadecimal digits
(`0-9`, `A-F`) for both byte arrays and numeric values.

In all other aspects, this format is identical to the `Default` format.

## Declarations and overloads

### 1. Common

```kotlin
public val UpperCase: HexFormat
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L795)

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
    val source = kotlin.text.HexFormat.Companion
    val result = source.`UpperCase`
    println(result)
}
```

```text title="Output"
HexFormat(
    upperCase = true,
    bytes = BytesHexFormat(
        bytesPerLine = 2147483647,
        bytesPerGroup = 2147483647,
        groupSeparator = "  ",
        byteSeparator = "",
        bytePrefix = "",
        byteSuffix = ""
    ),
    number = NumberHexFormat(
        prefix = "",
        suffix = "",
        removeLeadingZeros = false,
        minLength = 1
    )
)
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
