# HexFormat.NumberHexFormat

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents hexadecimal format options for formatting and parsing numeric values.

These options are utilized by functions like `Int.toHexString` for formatting and `String.hexToInt` for parsing.
The formatting and parsing functions are available for all integer numeric types.

When formatting, the result consists of a `prefix` string, the hexadecimal representation of the numeric value,
and a `suffix` string. The hexadecimal representation of a value is calculated by mapping each four-bit chunk
of its binary representation to the corresponding hexadecimal digit, starting with the most significant bits.
The `upperCase` option determines the case (`A-F` or `a-f`) of the hexadecimal digits.
If `removeLeadingZeros` is `true` and the hexadecimal representation is longer than `minLength`, leading zeros
are removed until the length matches `minLength`. However, if `minLength` exceeds the length of the hexadecimal
representation, `removeLeadingZeros` is ignored, and zeros are added to the start of the representation to
achieve the specified `minLength`.

For example, the binary representation of the `Int` value `58` (32-bit long `00000000000000000000000000111010`)
converts to the hexadecimal representation `0000003a` or `0000003A`, depending on `upperCase`.
With `removeLeadingZeros` set to `true`, it shortens to `3a`. However, if `minLength` is set to `6`, the removal of
leading zeros stops once the length is reduced to `00003a`. Setting `minLength` to `12` results in
`00000000003a`, where the `removeLeadingZeros` option is ignored due to the minimum length requirement.

To format a value into a hexadecimal string of a particular length, start by converting the value to a type with
the suitable bit size. For instance, to format an `Int` value into a 4-digit hexadecimal string, convert the value
using `toShort()` before hexadecimal formatting. To obtain a maximum of 4 digits without leading zeros,
additionally set `removeLeadingZeros` to `true`.

When parsing, the input string must start with the `prefix` and end with the `suffix`. It must contain at least
one hexadecimal digit between them. If the number of hexadecimal digits exceeds the capacity of the type being
parsed, based on its bit size, the excess leading digits must be zeros. Parsing of the `prefix`, `suffix`, and
hexadecimal digits is performed in a case-insensitive manner. The `removeLeadingZeros` and `minLength` options
are ignored during parsing.

This class is immutable and cannot be created or configured directly. To create a new format, use the
`HexFormat { }` builder function and configure the options of the `number` property inside the braces. For
example, use `val format = HexFormat { number.prefix = "0x" }` to set the `prefix`. The `number` property is of
type `NumberHexFormat.Builder`, whose options are configurable and correspond to the options of this class.

@sample samples.text.HexFormats.Numbers.numberHexFormat

## Declarations and overloads

### 1. Common

```kotlin
public class NumberHexFormat internal constructor(
        /**
         * The string that immediately precedes the hexadecimal representation of a numeric value,
         * empty string by default.
         *
         * When formatting, this string is placed before the hexadecimal representation.
         * When parsing, the string being parsed must start with this string.
         * The parsing of this prefix is performed in a case-insensitive manner.
         *
         * @sample samples.text.HexFormats.Numbers.prefix
         */
        public val prefix: String,

        /**
         * The string that immediately succeeds the hexadecimal representation of a numeric value,
         * empty string by default.
         *
         * When formatting, this string is placed after the hexadecimal representation.
         * When parsing, the string being parsed must end with this string.
         * The parsing of this suffix is performed in a case-insensitive manner.
         *
         * @sample samples.text.HexFormats.Numbers.suffix
         */
        public val suffix: String,

        /**
         * Specifies whether to remove leading zeros in the hexadecimal representation of a numeric value,
         * `false` by default.
         *
         * The hexadecimal representation of a value is calculated by mapping each four-bit chunk of its binary
         * representation to the corresponding hexadecimal digit, starting with the most significant bits.
         *
         * When formatting, if this option is `true` and the length of the hexadecimal representation exceeds
         * [minLength], leading zeros are removed until the length matches [minLength]. If the length
         * does not exceed [minLength], this option has no effect on the formatting result.
         *
         * When parsing, this option is ignored.
         *
         * @sample samples.text.HexFormats.Numbers.removeLeadingZeros
         */
        public val removeLeadingZeros: Boolean,

        /**
         * Specifies the minimum number of hexadecimal digits to be used in the representation of a numeric value,
         * `1` by default.
         *
         * The hexadecimal representation of a value is calculated by mapping each four-bit chunk of its binary
         * representation to the corresponding hexadecimal digit, starting with the most significant bits.
         *
         * When formatting:
         *   - If this option is less than the length of the hexadecimal representation:
         *       - If [removeLeadingZeros] is `true`, leading zeros are removed until the length matches [minLength].
         *       - If [removeLeadingZeros] is `false`, the representation remains unchanged, as no leading zeros are removed.
         *   - If this option is greater than the length of the hexadecimal representation, the
         *     representation is padded with zeros at the start to reach the specified [minLength].
         *   - If this option matches the length of the hexadecimal representation, the representation remains unchanged.
         *
         * When parsing, this option is ignored. However, there must be at least one hexadecimal digit in the input
         * string. If the number of hexadecimal digits exceeds the capacity of the type being parsed, based on its bit
         * size, the excess leading digits must be zeros.
         *
         * @sample samples.text.HexFormats.Numbers.minLength
         */
        @SinceKotlin("2.0")
        public val minLength: Int
    )
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L406)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val numberHexFormat = HexFormat {
        upperCase = true
        number {
            removeLeadingZeros = true
            minLength = 4
            prefix = "0x"
        }
    }

    println(0x3a.toHexString(numberHexFormat))
    println("0x003A".hexToInt(numberHexFormat))
    // Parsing is case-insensitive
    println("0X003a".hexToInt(numberHexFormat))
}
```

```text title="Output"
0x003A
58
58
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L236)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
