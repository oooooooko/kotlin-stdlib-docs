# toHexString

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Formats bytes in this array using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.bytes` properties of the `format` instance affect
the formatting result of this byte array.

Each byte in the array is converted into two hexadecimal digits. The first digit represents the most significant 4 bits,
and the second digit represents the least significant 4 bits of the byte. The `HexFormat.upperCase` property determines whether
upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`) hexadecimal digits are used for this conversion.
The `HexFormat.bytes` property specifies the strings that prefix and suffix each byte representation, and defines
how these representations are arranged.

Refer to `HexFormat.BytesHexFormat` for details about the available format options and their impact on formatting.

@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this array using the specified `format`.

@throws IllegalArgumentException if the result length exceeds the maximum capacity of `String`.

@sample samples.text.HexFormats.Extensions.byteArrayToHexString

## Declarations and overloads

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun ByteArray.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L60)

### 2. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun ByteArray.toHexString(
    startIndex: Int = 0,
    endIndex: Int = size,
    format: HexFormat = HexFormat.Default
): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L85)

Formats bytes in this array using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.bytes` properties of the `format` instance affect
the formatting result of this byte array.

Each byte in the array is converted into two hexadecimal digits. The first digit represents the most significant 4 bits,
and the second digit represents the least significant 4 bits of the byte. The `HexFormat.upperCase` property determines whether
upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`) hexadecimal digits are used for this conversion.
The `HexFormat.bytes` property specifies the strings that prefix and suffix each byte representation, and defines
how these representations are arranged.

Refer to `HexFormat.BytesHexFormat` for details about the available format options and their impact on formatting.

@param startIndex the beginning (inclusive) of the subrange to format, 0 by default.
@param endIndex the end (exclusive) of the subrange to format, size of this array by default.
@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this array using the specified `format`.

@throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of this array indices.
@throws IllegalArgumentException when `startIndex > endIndex`.
@throws IllegalArgumentException if the result length exceeds the maximum capacity of `String`.

@sample samples.text.HexFormats.Extensions.byteArrayToHexString

### 3. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun Byte.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L634)

Formats this `Byte` value using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.number` properties of the `format` instance affect
the formatting result of this numeric value.

This function converts the `Byte` value into its hexadecimal representation by mapping each four-bit chunk
of its binary representation to the corresponding hexadecimal digit, starting from the most significant bits.
The `HexFormat.upperCase` property determines whether upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`)
hexadecimal digits are used for this conversion.
The `HexFormat.number` property adjusts the length of the hexadecimal representation by adding or removing
leading zeros as needed, and specifies the strings that prefix and suffix the resulting representation.

Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on formatting.

@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this value using the specified `format`.

@sample samples.text.HexFormats.Extensions.byteToHexString

### 4. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun Short.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L732)

Formats this `Short` value using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.number` properties of the `format` instance affect
the formatting result of this numeric value.

This function converts the `Short` value into its hexadecimal representation by mapping each four-bit chunk
of its binary representation to the corresponding hexadecimal digit, starting from the most significant bits.
The `HexFormat.upperCase` property determines whether upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`)
hexadecimal digits are used for this conversion.
The `HexFormat.number` property adjusts the length of the hexadecimal representation by adding or removing
leading zeros as needed, and specifies the strings that prefix and suffix the resulting representation.

Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on formatting.

@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this value using the specified `format`.

@sample samples.text.HexFormats.Extensions.shortToHexString

### 5. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun Int.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L832)

Formats this `Int` value using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.number` properties of the `format` instance affect
the formatting result of this numeric value.

This function converts the `Int` value into its hexadecimal representation by mapping each four-bit chunk
of its binary representation to the corresponding hexadecimal digit, starting from the most significant bits.
The `HexFormat.upperCase` property determines whether upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`)
hexadecimal digits are used for this conversion.
The `HexFormat.number` property adjusts the length of the hexadecimal representation by adding or removing
leading zeros as needed, and specifies the strings that prefix and suffix the resulting representation.

Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on formatting.

@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this value using the specified `format`.

@sample samples.text.HexFormats.Extensions.intToHexString

### 6. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun Long.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L936)

Formats this `Long` value using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.number` properties of the `format` instance affect
the formatting result of this numeric value.

This function converts the `Long` value into its hexadecimal representation by mapping each four-bit chunk
of its binary representation to the corresponding hexadecimal digit, starting from the most significant bits.
The `HexFormat.upperCase` property determines whether upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`)
hexadecimal digits are used for this conversion.
The `HexFormat.number` property adjusts the length of the hexadecimal representation by adding or removing
leading zeros as needed, and specifies the strings that prefix and suffix the resulting representation.

Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on formatting.

@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this value using the specified `format`.

@sample samples.text.HexFormats.Extensions.longToHexString

### 7. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@ExperimentalUnsignedTypes
@InlineOnly
public inline fun UByteArray.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L12)

### 8. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@ExperimentalUnsignedTypes
@InlineOnly
public inline fun UByteArray.toHexString(
    startIndex: Int = 0,
    endIndex: Int = size,
    format: HexFormat = HexFormat.Default
): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L39)

Formats bytes in this array using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.bytes` properties of the `format` instance affect
the formatting result of this byte array.

Each byte in the array is converted into two hexadecimal digits. The first digit represents the most significant 4 bits,
and the second digit represents the least significant 4 bits of the byte. The `HexFormat.upperCase` property determines whether
upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`) hexadecimal digits are used for this conversion.
The `HexFormat.bytes` property specifies the strings that prefix and suffix each byte representation, and defines
how these representations are arranged.

Refer to `HexFormat.BytesHexFormat` for details about the available format options and their impact on formatting.

@param startIndex the beginning (inclusive) of the subrange to format, 0 by default.
@param endIndex the end (exclusive) of the subrange to format, size of this array by default.
@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this array using the specified `format`.

@throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of this array indices.
@throws IllegalArgumentException when `startIndex > endIndex`.
@throws IllegalArgumentException if the result length exceeds the maximum capacity of `String`.

@sample samples.text.HexFormats.Extensions.byteArrayToHexString

### 9. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun UByte.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L102)

Formats this `UByte` value using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.number` properties of the `format` instance affect
the formatting result of this numeric value.

This function converts the `UByte` value into its hexadecimal representation by mapping each four-bit chunk
of its binary representation to the corresponding hexadecimal digit, starting from the most significant bits.
The `HexFormat.upperCase` property determines whether upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`)
hexadecimal digits are used for this conversion.
The `HexFormat.number` property adjusts the length of the hexadecimal representation by adding or removing
leading zeros as needed, and specifies the strings that prefix and suffix the resulting representation.

Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on formatting.

@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this value using the specified `format`.

@sample samples.text.HexFormats.Extensions.byteToHexString

### 10. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun UShort.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L156)

Formats this `UShort` value using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.number` properties of the `format` instance affect
the formatting result of this numeric value.

This function converts the `UShort` value into its hexadecimal representation by mapping each four-bit chunk
of its binary representation to the corresponding hexadecimal digit, starting from the most significant bits.
The `HexFormat.upperCase` property determines whether upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`)
hexadecimal digits are used for this conversion.
The `HexFormat.number` property adjusts the length of the hexadecimal representation by adding or removing
leading zeros as needed, and specifies the strings that prefix and suffix the resulting representation.

Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on formatting.

@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this value using the specified `format`.

@sample samples.text.HexFormats.Extensions.shortToHexString

### 11. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun UInt.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L210)

Formats this `UInt` value using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.number` properties of the `format` instance affect
the formatting result of this numeric value.

This function converts the `UInt` value into its hexadecimal representation by mapping each four-bit chunk
of its binary representation to the corresponding hexadecimal digit, starting from the most significant bits.
The `HexFormat.upperCase` property determines whether upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`)
hexadecimal digits are used for this conversion.
The `HexFormat.number` property adjusts the length of the hexadecimal representation by adding or removing
leading zeros as needed, and specifies the strings that prefix and suffix the resulting representation.

Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on formatting.

@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this value using the specified `format`.

@sample samples.text.HexFormats.Extensions.intToHexString

### 12. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun ULong.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L264)

Formats this `ULong` value using the specified `format`.

Note that only the `HexFormat.upperCase` and `HexFormat.number` properties of the `format` instance affect
the formatting result of this numeric value.

This function converts the `ULong` value into its hexadecimal representation by mapping each four-bit chunk
of its binary representation to the corresponding hexadecimal digit, starting from the most significant bits.
The `HexFormat.upperCase` property determines whether upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`)
hexadecimal digits are used for this conversion.
The `HexFormat.number` property adjusts the length of the hexadecimal representation by adding or removing
leading zeros as needed, and specifies the strings that prefix and suffix the resulting representation.

Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on formatting.

@param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
@return the result of formatting this value using the specified `format`.

@sample samples.text.HexFormats.Extensions.longToHexString

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val data = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte(), 0x5C, 0x0E)

    // Using the default format
    println(data.toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        bytes {
            bytesPerLine = 4
            byteSeparator = " " // One space
            bytePrefix = "0x"
        }
    }
    println(data.toHexString(format))

    // Formatting a segment of the byte array
    println(data.toHexString(startIndex = 2, endIndex = 5, format))

    // Formatting unsigned bytes with the same binary representations yields the same string
    val unsignedData = data.toUByteArray()
    println(unsignedData.toHexString(format))
}
```

```text title="Output"
de2d02c05c0e
0xDE 0x2D 0x02 0xC0
0x5C 0x0E
0x02 0xC0 0x5C
0xDE 0x2D 0x02 0xC0
0x5C 0x0E
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L365)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Using the default format
    val value: Byte = 58
    println(value.toHexString())

    // Converts the Byte to an unsigned hexadecimal representation
    println((-1).toByte().toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        number {
            prefix = "\\u" // A Unicode escape prefix
            minLength = 4
        }
    }
    println(value.toHexString(format))

    // Formatting an unsigned value with the same binary representations yields the same string
    val uValue: UByte = 58u
    println(uValue.toHexString(format))
}
```

```text title="Output"
3a
ff
\u003A
\u003A
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L422)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Using the default format
    val value: Short = 58
    println(value.toHexString())

    // Converts the Short to an unsigned hexadecimal representation
    println((-1).toShort().toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        number {
            prefix = "0x"
            removeLeadingZeros = true
        }
    }
    println(value.toHexString(format))

    // Formatting an unsigned value with the same binary representations yields the same string
    val uValue: UShort = 58u
    println(uValue.toHexString(format))
}
```

```text title="Output"
003a
ffff
0x3A
0x3A
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L474)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Using the default format
    val value = 58
    println(value.toHexString())

    // Converts the Int to an unsigned hexadecimal representation
    println((-1).toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        number {
            prefix = "#"
            removeLeadingZeros = true
            minLength = 6
        }
    }
    println(value.toHexString(format))

    // Formatting an unsigned value with the same binary representations yields the same string
    val uValue = 58u
    println(uValue.toHexString(format))
}
```

```text title="Output"
0000003a
ffffffff
#00003A
#00003A
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L526)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Using the default format
    val value = 58L
    println(value.toHexString())

    // Converts the Long to an unsigned hexadecimal representation
    println((-1L).toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        number.removeLeadingZeros = true
    }
    println(value.toHexString(format))

    // Formatting an unsigned value with the same binary representations yields the same string
    val uValue = 58uL
    println(uValue.toHexString(format))
}
```

```text title="Output"
000000000000003a
ffffffffffffffff
3A
3A
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L579)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
