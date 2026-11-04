# hexToByte

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses a `Byte` value from this string using the specified `format`.

The string must conform to the structure defined by the `format`.
Note that only the `HexFormat.number` property of the `format` instance affects the parsing of a numeric value.

The input string must start with the prefix and end with the suffix defined in the `HexFormat.number` property.
It must also contain at least one hexadecimal digit between them. If the number of hexadecimal digits
exceeds two, the excess leading digits must be zeros. This ensures that the value represented by the
hexadecimal digits fits into an 8-bit `Byte`.
Parsing is performed in a case-insensitive manner, including for the hexadecimal digits, prefix, and suffix.

Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on parsing.

@param format the `HexFormat` to use for parsing, `HexFormat.Default` by default.
@return the `Byte` value parsed from this string.

@throws IllegalArgumentException if this string does not conform to the specified `format`, or if the hexadecimal
  digits represent a value that does not fit into a `Byte`.

@sample samples.text.HexFormats.Extensions.hexToByte

## Declarations and overloads

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun String.hexToByte(format: HexFormat = HexFormat.Default): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L675)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    // Using the default format
    println("3a".hexToByte())

    // Parsing is case-insensitive
    println("3A".hexToByte())

    // Up to 2 hexadecimal digits can fit into a Byte
    println("ff".hexToByte())

    // Excess leading hexadecimal digits must be zeros
    println("00ff".hexToByte())
    assertFailsWith<IllegalArgumentException> { "0100".hexToByte() }

    // Parsing an UByte results in the unsigned version of the same value
    // In this case, (-1).toUByte() = UByte.MAX_VALUE
    println("ff".hexToULong())

    // Using a custom format
    val format = HexFormat { number.prefix = "0x" }
    println("0x3A".hexToByte(format))

    // Parsing fails if the input string does not conform to the specified format.
    // In this case, the prefix is not present.
    assertFailsWith<IllegalArgumentException> { "3A".hexToByte(format) }
}
```

```text title="Output"
58
58
-1
-1
255
58
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L446)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
