# HexFormat.BytesHexFormat.Builder.byteSuffix

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Defines `BytesHexFormat.byteSuffix` of the format being built, empty string by default.

The string must not contain line feed (LF) and carriage return (CR) characters.

Refer to `BytesHexFormat.byteSuffix` for details about how this format option affects
the formatting and parsing results.

@throws IllegalArgumentException if a string containing LF or CR character is assigned to this property.

@sample samples.text.HexFormats.ByteArrays.byteSuffix

## Declarations and overloads

### 1. Common

```kotlin
public var byteSuffix: String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L370)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val data = ByteArray(4) { it.toByte() }

    // By default, the byteSuffix is an empty string, so bytes are formatted without any suffix.
    println(data.toHexString())
    println("00010203".hexToByteArray().contentEquals(data))

    // Specifying a custom byte suffix, a semicolon in this case, to follow each byte.
    val byteSuffixFormat = HexFormat {
        bytes.byteSuffix = ";"
    }
    println(data.toHexString(byteSuffixFormat))
    println("00;01;02;03;".hexToByteArray(byteSuffixFormat).contentEquals(data))

    // Parsing fails due to incorrect byte suffix.
    // In this case, the input string is lacking the necessary byte suffixes.
    assertFailsWith<IllegalArgumentException> {
        "00010203".hexToByteArray(byteSuffixFormat)
    }
}
```

```text title="Output"
00010203
true
00;01;02;03;
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L212)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
