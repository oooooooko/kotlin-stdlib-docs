# HexFormat.NumberHexFormat.suffix

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The string that immediately succeeds the hexadecimal representation of a numeric value,
empty string by default.

When formatting, this string is placed after the hexadecimal representation.
When parsing, the string being parsed must end with this string.
The parsing of this suffix is performed in a case-insensitive manner.

@sample samples.text.HexFormats.Numbers.suffix

## Declarations and overloads

### 1. Common

```kotlin
public val suffix: String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L458)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    // By default, `suffix` is an empty string
    println(0x3a.toHexString())
    println("0000003a".hexToInt())

    val suffixFormat = HexFormat { number.suffix = "h" }

    // `suffix` is placed after the hex representation
    println(0x3a.toHexString(suffixFormat))
    println("0000003ah".hexToByte(suffixFormat))

    // Parsing `suffix` is conducted in a case-insensitive manner
    println("0000003aH".hexToInt(suffixFormat))

    // Parsing fails if the input string does not end with the specified suffix.
    assertFailsWith<IllegalArgumentException> {
        "0000003a".hexToInt(suffixFormat)
    }
}
```

```text title="Output"
0000003a
58
0000003ah
58
58
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L274)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
