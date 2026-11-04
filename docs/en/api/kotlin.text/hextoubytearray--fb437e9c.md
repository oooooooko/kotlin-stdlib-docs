# hexToUByteArray

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses a byte array from this string using the specified `format`.

The string must conform to the structure defined by the `format`.
Note that only the `HexFormat.bytes` property of the `format` instance affects the parsing of a byte array.

Parsing is performed in a case-insensitive manner for both the hexadecimal digits and the elements
(prefix, suffix, separators) defined in the `HexFormat.bytes` property. Additionally, any of the
char sequences CRLF, LF and CR is considered a valid line separator.

Refer to `HexFormat.BytesHexFormat` for details about the available format options and their impact on parsing.

@param format the `HexFormat` to use for parsing, `HexFormat.Default` by default.
@return the byte array parsed from this string.

@throws IllegalArgumentException if this string does not conform to the specified `format`.

@sample samples.text.HexFormats.Extensions.hexToByteArray

## Declarations and overloads

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@ExperimentalUnsignedTypes
@InlineOnly
public inline fun String.hexToUByteArray(format: HexFormat = HexFormat.Default): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L74)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val expectedData = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte(), 0x5C, 0x0E)

    // Using the default format
    println("de2d02c05c0e".hexToByteArray().contentEquals(expectedData))

    // Parsing is case-insensitive
    println("DE2D02C05C0E".hexToByteArray().contentEquals(expectedData))

    // Using a custom format
    val format = HexFormat {
        bytes {
            bytesPerLine = 4
            byteSeparator = " " // One space
            bytePrefix = "0x"
        }
    }
    println("0xDE 0x2D 0x02 0xC0\n0x5C 0x0E".hexToByteArray(format).contentEquals(expectedData))

    // Parsing unsigned bytes results in the unsigned versions of the same bytes
    val expectedUnsignedData = expectedData.toUByteArray()
    println("de2d02c05c0e".hexToUByteArray().contentEquals(expectedUnsignedData))

    // Parsing fails if the input string does not conform to the specified format.
    // In this case, there is no line separator after the fourth formatted byte.
    assertFailsWith<IllegalArgumentException> {
        "0xDE 0x2D 0x02 0xC0 0x5C 0x0E".hexToByteArray(format)
    }
}
```

```text title="Output"
true
true
true
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L391)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
