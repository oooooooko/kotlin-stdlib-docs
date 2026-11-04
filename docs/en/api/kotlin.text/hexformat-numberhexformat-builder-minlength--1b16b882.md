# HexFormat.NumberHexFormat.Builder.minLength

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Defines `NumberHexFormat.minLength` of the format being built, `1` by default.

The value must be positive.

Refer to `NumberHexFormat.minLength` for details about how the format option affects
the formatting and parsing results.

@throws IllegalArgumentException if a non-positive value is assigned to this property.

@sample samples.text.HexFormats.Numbers.minLength

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.0")
            public var minLength: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L597)

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
