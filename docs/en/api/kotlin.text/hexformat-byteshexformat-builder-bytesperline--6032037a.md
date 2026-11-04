# HexFormat.BytesHexFormat.Builder.bytesPerLine

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Defines `BytesHexFormat.bytesPerLine` of the format being built, `Int.MAX_VALUE` by default.

The value must be positive.

Refer to `BytesHexFormat.bytesPerLine` for details about how this format option affects
the formatting and parsing results.

@throws IllegalArgumentException if a non-positive value is assigned to this property.

@sample samples.text.HexFormats.ByteArrays.bytesPerLine

## Declarations and overloads

### 1. Common

```kotlin
public var bytesPerLine: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L284)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val data = ByteArray(7) { it.toByte() }

    // By default, bytesPerLine is set to Int.MAX_VALUE, which exceeds data.size.
    // Therefore, all bytes are formatted as a single line without any line breaks.
    println(data.toHexString())
    println("00010203040506".hexToByteArray().contentEquals(data))

    // Setting bytesPerLine to 3 splits the output into 3 lines with 3, 3, and 1 bytes, respectively.
    // Each line is separated by a line feed (LF) character.
    val threePerLineFormat = HexFormat {
        bytes.bytesPerLine = 3
    }
    println(data.toHexString(threePerLineFormat))

    // When parsing, any of the line separators CRLF, LF, and CR are accepted.
    println("000102\n030405\r\n06".hexToByteArray(threePerLineFormat).contentEquals(data))

    // Parsing fails if the input string does not conform to specified format.
    // In this case, lines do not consist of the expected number of bytes.
    assertFailsWith<IllegalArgumentException> {
        "0001\n0203\n0405\n06".hexToByteArray(threePerLineFormat)
    }
}
```

```text title="Output"
00010203040506
true
000102
030405
06
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L78)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
