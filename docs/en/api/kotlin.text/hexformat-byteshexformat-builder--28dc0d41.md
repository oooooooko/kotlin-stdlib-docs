# HexFormat.BytesHexFormat.Builder

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Provides an API for building a `BytesHexFormat`.

This class is a [builder](https://en.wikipedia.org/wiki/Builder_pattern) for `BytesHexFormat`, and
serves as the type of the `bytes` property when creating a new format using the `HexFormat { }` builder
function. Each option in this class corresponds to an option in `BytesHexFormat` and defines it in the
resulting format. For example, use `val format = HexFormat { bytes.byteSeparator = true }` to set
`BytesHexFormat.byteSeparator`. Refer to `BytesHexFormat` for details about how the configured
format options affect formatting and parsing results.

## Declarations and overloads

### 1. Common

```kotlin
public class Builder internal constructor()
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L273)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val format = HexFormat {
        bytes { byteSeparator = ":"; upperCase = true }
        number { prefix = "0x"; removeLeadingZeros = true }
    }
    println(byteArrayOf(10, 15).toHexString(format))
    println(255.toHexString(format))
    println(format.bytes.toString())
    println(format.number.toString())
    println(format.toString())
}
```

```text title="Output"
0A:0F
0xFF
BytesHexFormat(
    bytesPerLine = 2147483647,
    bytesPerGroup = 2147483647,
    groupSeparator = "  ",
    byteSeparator = ":",
    bytePrefix = "",
    byteSuffix = ""
)
NumberHexFormat(
    prefix = "0x",
    suffix = "",
    removeLeadingZeros = true,
    minLength = 1
)
HexFormat(
    upperCase = true,
    bytes = BytesHexFormat(
        bytesPerLine = 2147483647,
        bytesPerGroup = 2147483647,
        groupSeparator = "  ",
        byteSeparator = ":",
        bytePrefix = "",
        byteSuffix = ""
    ),
    number = NumberHexFormat(
        prefix = "0x",
        suffix = "",
        removeLeadingZeros = true,
        minLength = 1
    )
)
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
