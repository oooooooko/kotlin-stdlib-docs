# HexFormat.BytesHexFormat.Builder.byteSeparator

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Defines `BytesHexFormat.byteSeparator` of the format being built, empty string by default.

The string must not contain line feed (LF) and carriage return (CR) characters.

Refer to `BytesHexFormat.byteSeparator` for details about how this format option affects
the formatting and parsing results.

@throws IllegalArgumentException if a string containing LF or CR character is assigned to this property.

@sample samples.text.HexFormats.ByteArrays.byteSeparator

## Declarations and overloads

### 1. Common

```kotlin
public var byteSeparator: String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L332)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val data = ByteArray(7) { it.toByte() }

    // By default, the byteSeparator is an empty string, hence all bytes are concatenated without any separator.
    println(data.toHexString())
    println("00010203040506".hexToByteArray().contentEquals(data))

    // Specifying a custom byte separator, a colon in this case.
    val colonByteSeparatorFormat = HexFormat { bytes.byteSeparator = ":" }
    println(data.toHexString(colonByteSeparatorFormat))
    println("00:01:02:03:04:05:06".hexToByteArray(colonByteSeparatorFormat).contentEquals(data))

    // Only adjacent bytes within a group are separated by the byteSeparator.
    val groupFormat = HexFormat {
        bytes.bytesPerGroup = 3
        bytes.byteSeparator = ":"
    }
    println(data.toHexString(groupFormat))
    println("00:01:02  03:04:05  06".hexToByteArray(groupFormat).contentEquals(data))

    // Parsing fails due to incorrect byte separator.
    // In this case, the input string is lacking the necessary byte separators within groups.
    assertFailsWith<IllegalArgumentException> {
        "000102  030405  06".hexToByteArray(groupFormat)
    }
}
```

```text title="Output"
00010203040506
true
00:01:02:03:04:05:06
true
00:01:02  03:04:05  06
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L159)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
