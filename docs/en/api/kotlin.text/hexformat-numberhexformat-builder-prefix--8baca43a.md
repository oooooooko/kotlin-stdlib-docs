# HexFormat.NumberHexFormat.Builder.prefix

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Defines `NumberHexFormat.prefix` of the format being built, empty string by default.

The string must not contain line feed (LF) and carriage return (CR) characters.

Refer to `NumberHexFormat.prefix` for details about how this format option affects
the formatting and parsing results.

@throws IllegalArgumentException if a string containing LF or CR character is assigned to this property.

@sample samples.text.HexFormats.Numbers.prefix

## Declarations and overloads

### 1. Common

```kotlin
public var prefix: String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L549)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    // By default, `prefix` is an empty string.
    println(0x3a.toHexString())
    println("0000003a".hexToInt())

    val prefixFormat = HexFormat { number.prefix = "0x" }

    // `prefix` is placed before the hex representation.
    println(0x3a.toHexString(prefixFormat))
    println("0x0000003a".hexToInt(prefixFormat))

    // Parsing `prefix` is conducted in a case-insensitive manner.
    println("0X0000003a".hexToInt(prefixFormat))

    // Parsing fails if the input string does not start with the specified prefix.
    assertFailsWith<IllegalArgumentException> {
        "0000003a".hexToInt(prefixFormat)
    }
}
```

```text title="Output"
0000003a
58
0x0000003a
58
58
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L253)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
