# HexFormat.Companion.Default

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The default hexadecimal format options.

This `HexFormat` instance adopts default values for all format options.

Formatting functions use lower-case hexadecimal digits (`0-9`, `a-f`) for both byte arrays and
numeric values. Specifically, `upperCase` is set to `false`.

No line separator, group separator, byte separator, byte prefix, or byte suffix is used
when formatting or parsing byte arrays. Specifically:
  * `bytes.bytesPerLine``BytesHexFormat.bytesPerLine` is set to `Int.MAX_VALUE`.
  * `bytes.bytesPerGroup``BytesHexFormat.bytesPerGroup` is set to `Int.MAX_VALUE`.
  * `bytes.byteSeparator``BytesHexFormat.byteSeparator`, `bytes.bytePrefix``BytesHexFormat.bytePrefix`,
  and `bytes.byteSuffix``BytesHexFormat.byteSuffix` are empty strings.

No prefix or suffix is used, and leading zeros are not removed from the hexadecimal representation
when formatting or parsing numeric values. Specifically:
  * `number.prefix``NumberHexFormat.prefix` and `number.suffix``NumberHexFormat.suffix` are empty strings.
  * `number.removeLeadingZeros``NumberHexFormat.removeLeadingZeros` is set to `false`.

## Declarations and overloads

### 1. Common

```kotlin
public val Default: HexFormat
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L769)

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
    val result = source.`Default`
    println(result)
}
```

```text title="Output"
HexFormat(
    upperCase = false,
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
