# HexFormat.NumberHexFormat.removeLeadingZeros

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Specifies whether to remove leading zeros in the hexadecimal representation of a numeric value,
`false` by default.

The hexadecimal representation of a value is calculated by mapping each four-bit chunk of its binary
representation to the corresponding hexadecimal digit, starting with the most significant bits.

When formatting, if this option is `true` and the length of the hexadecimal representation exceeds
`minLength`, leading zeros are removed until the length matches `minLength`. If the length
does not exceed `minLength`, this option has no effect on the formatting result.

When parsing, this option is ignored.

@sample samples.text.HexFormats.Numbers.removeLeadingZeros

## Declarations and overloads

### 1. Common

```kotlin
public val removeLeadingZeros: Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L470)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // By default, removeLeadingZeroes is `false`
    println(0x3a.toHexString())

    val removeLeadingZerosFormat = HexFormat { number.removeLeadingZeros = true }

    // If there are no leading zeros, removeLeadingZeroes has no effect
    println(0x3a.toByte().toHexString(removeLeadingZerosFormat))

    // The leading zeros in the hex representation are removed until minLength is reached.
    // By default, minLength is 1.
    println(0x3a.toHexString(removeLeadingZerosFormat))
    println(0.toHexString(removeLeadingZerosFormat))

    // Here minLength is set to 6.
    val shorterLengthFormat = HexFormat {
        number.removeLeadingZeros = true
        number.minLength = 6
    }
    println(0x3a.toHexString(shorterLengthFormat))

    // When minLength is longer than the hex representation, the hex representation is padded with zeros.
    // removeLeadingZeros is ignored in this case.
    val longerLengthFormat = HexFormat {
        number.removeLeadingZeros = true
        number.minLength = 12
    }
    println(0x3a.toHexString(longerLengthFormat))

    // When parsing, removeLeadingZeros is ignored
    println("0000003a".hexToInt(removeLeadingZerosFormat))
}
```

```text title="Output"
0000003a
3a
3a
0
00003a
00000000003a
58
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L295)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
