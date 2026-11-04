# HexFormat.Builder

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Provides an API for building a `HexFormat`.

This class is a [builder](https://en.wikipedia.org/wiki/Builder_pattern) for `HexFormat`, and
serves as the receiver type of the lambda expression used in the `HexFormat { }` builder function to create a
new format. Each option in this class corresponds to an option in `HexFormat` and defines it in the resulting
format. For example, use `val format = HexFormat { bytes.byteSeparator = ":" }` to set
`BytesHexFormat.byteSeparator` option of the `HexFormat.bytes` property.

Refer to `HexFormat` for details about how the configured format options affect formatting and parsing results.

@sample samples.text.HexFormats.HexFormatClass.hexFormatBuilderFunction

## Declarations and overloads

### 1. Common

```kotlin
public class Builder @PublishedApi internal constructor()
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L632)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Specifying format options for numeric values.
    println(58.toHexString(HexFormat { number.removeLeadingZeros = true }))
    println("0x3a".hexToInt(HexFormat { number.prefix = "0x" }))

    // Specifying format options for byte arrays.
    val macAddressFormat = HexFormat {
        upperCase = true
        bytes {
            bytesPerGroup = 2
            groupSeparator = "."
        }
    }
    val macAddressBytes = byteArrayOf(0x00, 0x1b, 0x63, 0x84.toByte(), 0x45, 0xe6.toByte())
    println(macAddressBytes.toHexString(macAddressFormat))
    println("001B.6384.45E6".hexToByteArray(macAddressFormat).contentEquals(macAddressBytes))

    // Creating a format that defines options for both byte arrays and numeric values.
    val customHexFormat = HexFormat {
        upperCase = true
        number {
            removeLeadingZeros = true
            prefix = "0x"
        }
        bytes {
            bytesPerGroup = 2
            groupSeparator = "."
        }
    }
    // Formatting numeric values utilizes the `upperCase` and `number` options.
    println(58.toHexString(customHexFormat))
    // Formatting byte arrays utilizes the `upperCase` and `bytes` options.
    println(macAddressBytes.toHexString(customHexFormat))
}
```

```text title="Output"
3a
58
001B.6384.45E6
true
0x3A
001B.6384.45E6
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L15)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
