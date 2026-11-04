# HexFormat.BytesHexFormat.groupSeparator

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The string used to separate adjacent groups in a line, two space characters (`"  "`) by default.

The number of bytes in each line and each group is determined by the `bytesPerLine` and
`bytesPerGroup` options, respectively.

When formatting, adjacent groups within each line are separated by this string.

When parsing, adjacent groups within each line must be separated by this string.
The parsing of this separator is performed in a case-insensitive manner.

@sample samples.text.HexFormats.ByteArrays.bytesPerGroup

## Declarations and overloads

### 1. Common

```kotlin
public val groupSeparator: String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L187)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val data = ByteArray(7) { it.toByte() }

    // By default, both bytesPerLine and bytesPerGroup are set to Int.MAX_VALUE, which exceeds data.size.
    // Hence, all bytes are formatted as a single line and a single group.
    println(data.toHexString())
    println("00010203040506".hexToByteArray().contentEquals(data))

    // Setting bytesPerGroup to 2 with the default group separator, which is two spaces.
    val twoPerGroupFormat = HexFormat {
        bytes.bytesPerGroup = 2
    }
    println(data.toHexString(twoPerGroupFormat))
    println("0001  0203  0405  06".hexToByteArray(twoPerGroupFormat).contentEquals(data))

    // Specifying a custom group separator, a dot in this case.
    val dotGroupSeparatorFormat = HexFormat {
        bytes {
            bytesPerGroup = 2
            groupSeparator = "."
        }
    }
    println(data.toHexString(dotGroupSeparatorFormat))
    println("0001.0203.0405.06".hexToByteArray(dotGroupSeparatorFormat).contentEquals(data))

    // If bytesPerLine is less than or equal to bytesPerGroup, each line is treated as a single group,
    // hence no group separator is used.
    val lessBytesPerLineFormat = HexFormat {
        bytes {
            bytesPerLine = 3
            bytesPerGroup = 4
            groupSeparator = "|"
        }
    }
    println(data.toHexString(lessBytesPerLineFormat))
    println("000102\n030405\n06".hexToByteArray(lessBytesPerLineFormat).contentEquals(data))

    // When bytesPerLine is greater than bytesPerGroup, each line is split into multiple groups.
    val moreBytesPerLineFormat = HexFormat {
        bytes {
            bytesPerLine = 5
            bytesPerGroup = 2
            groupSeparator = "."
        }
    }
    println(data.toHexString(moreBytesPerLineFormat))
    println("0001.0203.04\n0506".hexToByteArray(moreBytesPerLineFormat).contentEquals(data))

    // Parsing fails due to incorrect group separator.
    assertFailsWith<IllegalArgumentException> {
        "0001  0203  04\n0506".hexToByteArray(moreBytesPerLineFormat)
    }
}
```

```text title="Output"
00010203040506
true
0001  0203  0405  06
true
0001.0203.0405.06
true
000102
030405
06
true
0001.0203.04
0506
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L104)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
