# HexFormat

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents hexadecimal format options for formatting and parsing byte arrays and integer numeric values,
both signed and unsigned.

An instance of this class is passed to formatting and parsing functions and specifies how formatting and parsing
should be conducted. The options of the `bytes` property apply only when formatting and parsing byte arrays,
while the `number` property applies when formatting and parsing numeric values. The `upperCase` option affects both.

This class is immutable and cannot be created or configured directly. To create a new format, use the
`HexFormat { }` builder function and configure the options inside the braces. For example, use
`val format = HexFormat { upperCase = true }` to enable upper-case formatting.

Two predefined instances are provided by this class's companion object: `Default` and `UpperCase`.
The `Default` instance has the `upperCase` option set to `false`, and the options of `bytes` and `number` properties
set to their default values as specified in `BytesHexFormat` and `NumberHexFormat`, respectively.
The `UpperCase` instance has the `upperCase` option set to `true`, and the options of `bytes` and `number` properties
set to their default values.

@sample samples.text.HexFormats.HexFormatClass.hexFormatBuilderFunction

@see ByteArray.toHexString
@see String.hexToByteArray
@see Int.toHexString
@see String.hexToInt

## Declarations and overloads

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public class HexFormat internal constructor(
    /**
     * Specifies whether upper-case hexadecimal digits should be used for formatting, `false` by default.
     *
     * When this option is set to `true`, formatting functions will use upper-case hexadecimal digits (`0-9`, `A-F`)
     * to create the hexadecimal representation of the values being formatted. Otherwise, lower-case hexadecimal digits
     * (`0-9`, `a-f`) will be used.
     *
     * This option affects the formatting results for both byte arrays and numeric values. However, it **has no effect
     * on parsing**, which is always performed in a case-insensitive manner.
     *
     * Note: This option **affects only the case of hexadecimal digits** and does not influence other elements like
     * [BytesHexFormat.bytePrefix] or [NumberHexFormat.suffix].
     *
     * @sample samples.text.HexFormats.HexFormatClass.upperCase
     */
    public val upperCase: Boolean,

    /**
     * Specifies the hexadecimal format used for formatting and parsing byte arrays.
     *
     * This property defines how byte arrays are formatted into hexadecimal strings and parsed back from strings into
     * byte arrays. It is utilized by [ByteArray.toHexString] for formatting and [String.hexToByteArray] for parsing.
     * These functions are available for [UByteArray] as well.
     *
     * Refer to [BytesHexFormat] for details about the available format options, their impact on formatting and
     * parsing results, and their default settings.
     */
    public val bytes: BytesHexFormat,

    /**
     * Specifies the hexadecimal format used for formatting and parsing numeric values.
     *
     * This property defines how numeric values are formatted into hexadecimal strings and parsed back from strings
     * into numeric values. It is utilized by functions like [Int.toHexString] for formatting and [String.hexToInt] for
     * parsing. These functions are available for all integer numeric types.
     *
     * Refer to [NumberHexFormat] for details about the available format options, their impact on formatting and
     * parsing results, and their default settings.
     */
    public val number: NumberHexFormat
)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L10)

### 2. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun HexFormat(builderAction: HexFormat.Builder.() -> Unit): HexFormat
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L812)

Builds a new `HexFormat` by configuring its format options using the specified `builderAction`,
and returns the resulting format.

The resulting format can be passed to formatting and parsing functions to dictate how formatting and parsing
should be conducted. For example, `val format = HexFormat { number.prefix = "0x" }` creates a new `HexFormat` and
assigns it to the `format` variable. When this `format` is passed to a number formatting function, the resulting
string will include `"0x"` as the prefix of the hexadecimal representation of the numeric value being formatted.
For instance, calling `58.toHexString(format)` will produce `"0x0000003a"`.

Refer to `HexFormat.Builder` for details on configuring format options, and see `HexFormat` for
information on how the configured format options affect formatting and parsing results.

The builder provided as a receiver to the `builderAction` is valid only within that function.
Using it outside the function can produce an unspecified behavior.

@param builderAction The function that configures the format options of the `HexFormat.Builder` receiver.
@return A new instance of `HexFormat` configured as specified by the `builderAction`.

@sample samples.text.HexFormats.HexFormatClass.hexFormatBuilderFunction

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
