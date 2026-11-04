# HexFormat.NumberHexFormat.minLength

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Specifies the minimum number of hexadecimal digits to be used in the representation of a numeric value,
`1` by default.

The hexadecimal representation of a value is calculated by mapping each four-bit chunk of its binary
representation to the corresponding hexadecimal digit, starting with the most significant bits.

When formatting:
  - If this option is less than the length of the hexadecimal representation:
      - If `removeLeadingZeros` is `true`, leading zeros are removed until the length matches `minLength`.
      - If `removeLeadingZeros` is `false`, the representation remains unchanged, as no leading zeros are removed.
  - If this option is greater than the length of the hexadecimal representation, the
    representation is padded with zeros at the start to reach the specified `minLength`.
  - If this option matches the length of the hexadecimal representation, the representation remains unchanged.

When parsing, this option is ignored. However, there must be at least one hexadecimal digit in the input
string. If the number of hexadecimal digits exceeds the capacity of the type being parsed, based on its bit
size, the excess leading digits must be zeros.

@sample samples.text.HexFormats.Numbers.minLength

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.0")
        public val minLength: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L487)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    // By default, minLength is 1 and removeLeadingZeros is false.
    println(0x3a.toHexString())

    // Specifying a minLength shorter than the hex representation with removeLeadingZeros set to false.
    println(0x3a.toHexString(HexFormat { number.minLength = 4 }))

    // Specifying a minLength shorter than the hex representation with removeLeadingZeros set to true.
    val shorterLengthFormat = HexFormat {
        number.removeLeadingZeros = true
        number.minLength = 4
    }
    println(0x3a.toHexString(shorterLengthFormat))
    println(0xff80ed.toHexString(shorterLengthFormat))

    // Specifying a minLength longer than the hex representation.
    // removeLeadingZeros is ignored in this case.
    val longerLengthFormat = HexFormat {
        number.removeLeadingZeros = true
        number.minLength = 12
    }
    println(0x3a.toHexString(longerLengthFormat))

    // When parsing, minLength is ignored.
    println("3a".hexToInt(longerLengthFormat))

    // The number of hex digits can be greater than what can fit into the type.
    println("00000000003a".hexToInt())
    println("0000ffffffff".hexToInt())
    // But excess leading digits must be zeros.
    assertFailsWith<IllegalArgumentException> { "000100000000".hexToInt() }
}
```

```text title="Output"
0000003a
0000003a
003a
ff80ed
00000000003a
58
58
-1
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L329)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
