# HexFormat.BytesHexFormat

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents hexadecimal format options for formatting and parsing byte arrays.

These options are utilized by `ByteArray.toHexString` and `String.hexToByteArray` functions for formatting and
parsing, respectively. The formatting and parsing functions are available for `UByteArray` as well.

When formatting a byte array, one can assume the following steps:
1. The bytes are split into lines with `bytesPerLine` bytes in each line,
   except for the last line, which may have fewer bytes.
2. Each line is split into groups with `bytesPerGroup` bytes in each group,
   except for the last group in a line, which may have fewer bytes.
3. All bytes are converted to their two-digit hexadecimal representation,
   each prefixed by `bytePrefix` and suffixed by `byteSuffix`.
4. Adjacent formatted bytes within each group are separated by `byteSeparator`.
5. Adjacent groups within each line are separated by `groupSeparator`.
6. Adjacent lines are separated by the line feed (LF) character `'\n'`.

For example, consider the snippet below:
```kotlin
val byteArray = byteArrayOf(0, 1, 2, 3, 4, 5, 6, 7)
val format = HexFormat {
    bytes {
        bytesPerLine = 6
        bytesPerGroup = 4
        groupSeparator = "|" // vertical bar
        byteSeparator = " " // one space
        bytePrefix = "0x"
        byteSuffix = "" // empty string
    }
}

println(byteArray.toHexString(format))
```
Given the `byteArray` and `format`, the formatting proceeds as follows:
1. The 8 bytes are split into lines of 6 bytes each. The first line contains `0, 1, 2, 3, 4, 5`,
   and the second (and last) line contains `6, 7`.
2. Each line is then divided into groups of 4 bytes. The first line forms two groups: `0, 1, 2, 3` and `4, 5`;
   the second line forms one group: `6, 7`.
3. Each byte is converted to its hexadecimal representation, prefixed by `"0x"` and suffixed by an empty string.
4. Bytes within each group are separated by a single space `" "`.
5. Groups within each line are separated by a vertical bar character `"|"`.
6. Lines are separated by the LF character `'\n'`.

The `byteArray.toHexString(format)` call will result in `"0x00 0x01 0x02 0x03|0x04 0x05\n0x06 0x07"`,
and printing it to the console outputs:
```
0x00 0x01 0x02 0x03|0x04 0x05
0x06 0x07
```

When parsing, the input string must conform to the format specified by these options.
However, parsing is somewhat lenient, allowing any of the char sequences CRLF, LF, or CR to be used as the line
separator. Additionally, parsing of `groupSeparator`, `byteSeparator`, `bytePrefix`, `byteSuffix`, and the
hexadecimal digits is performed in a case-insensitive manner.

This class is immutable and cannot be created or configured directly. To create a new format, use the
`HexFormat { }` builder function and configure the options of the `bytes` property inside the braces. For example,
use `val format = HexFormat { bytes.bytesPerLine = 16 }` to set the `bytesPerLine`. The `bytes` property is of
type `BytesHexFormat.Builder`, whose options are configurable and correspond to the options of this class.

## Declarations and overloads

### 1. Common

```kotlin
public class BytesHexFormat internal constructor(
        /**
         * The maximum number of bytes per line, [Int.MAX_VALUE] by default.
         *
         * When formatting, bytes are split into lines with [bytesPerLine] bytes in each line, except for the last
         * line, which may have fewer bytes if the total number of bytes does not divide evenly by this value. Adjacent
         * lines are separated by the line feed (LF) character `'\n'`. Note that if this value is greater than or equal
         * to the size of the byte array, the entire array will be formatted as a single line without any line breaks.
         *
         * When parsing, the input string must be split into lines accordingly, with [bytesPerLine] bytes in each line,
         * except for the last line, which may have fewer bytes. Any of the char sequences CRLF, LF, or CR
         * is considered a valid line separator.
         *
         * @sample samples.text.HexFormats.ByteArrays.bytesPerLine
         */
        public val bytesPerLine: Int,

        /**
         * The maximum number of bytes per group in a line, [Int.MAX_VALUE] by default.
         *
         * The number of bytes in each line is determined by the [bytesPerLine] option.
         *
         * When formatting, each line is split into groups with [bytesPerGroup] bytes in each group, except for the
         * last group in a line, which may have fewer bytes if the number of bytes in the line does not divide evenly
         * by this value. Adjacent groups within each line are separated by [groupSeparator]. Note that if this value
         * is greater than or equal to the number of bytes in a line, the bytes are not split into groups.
         *
         * When parsing, each line in the input string must be split into groups of [bytesPerGroup] bytes, except for
         * the last group in a line, which may have fewer bytes. Adjacent groups within each line must be separated by
         * [groupSeparator]. The parsing of the separator is performed in a case-insensitive manner.
         *
         * @sample samples.text.HexFormats.ByteArrays.bytesPerGroup
         */
        public val bytesPerGroup: Int,

        /**
         * The string used to separate adjacent groups in a line, two space characters (`"  "`) by default.
         *
         * The number of bytes in each line and each group is determined by the [bytesPerLine] and
         * [bytesPerGroup] options, respectively.
         *
         * When formatting, adjacent groups within each line are separated by this string.
         *
         * When parsing, adjacent groups within each line must be separated by this string.
         * The parsing of this separator is performed in a case-insensitive manner.
         *
         * @sample samples.text.HexFormats.ByteArrays.bytesPerGroup
         */
        public val groupSeparator: String,

        /**
         * The string used to separate adjacent bytes within a group.
         *
         * The number of bytes in each group is determined by the [bytesPerGroup] option.
         *
         * When formatting, adjacent bytes within each group are separated by this string.
         *
         * When parsing, adjacent bytes within each group must be separated by this string
         * The parsing of this separator is performed in a case-insensitive manner.
         *
         * @sample samples.text.HexFormats.ByteArrays.byteSeparator
         */
        public val byteSeparator: String,

        /**
         * The string that immediately precedes the two-digit hexadecimal representation of each byte.
         *
         * When formatting, this string is used as a prefix for the hexadecimal representation of each byte.
         *
         * When parsing, the hexadecimal representation of each byte must be prefixed by this string.
         * The parsing of this prefix is performed in a case-insensitive manner.
         *
         * @sample samples.text.HexFormats.ByteArrays.bytePrefix
         */
        public val bytePrefix: String,

        /**
         * The string that immediately follows the two-digit hexadecimal representation of each byte.
         *
         * When formatting, this string is used as a suffix for the hexadecimal representation of each byte.
         *
         * When parsing, the hexadecimal representation of each byte must be suffixed by this string.
         * The parsing of this suffix is performed in a case-insensitive manner.
         *
         * @sample samples.text.HexFormats.ByteArrays.byteSuffix
         */
        public val byteSuffix: String
    )
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L92)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val format = HexFormat {
        bytes { byteSeparator = ":"; upperCase = true }
        number { prefix = "0x"; removeLeadingZeros = true }
    }
    println(byteArrayOf(10, 15).toHexString(format))
    println(255.toHexString(format))
    println(format.bytes.toString())
    println(format.number.toString())
    println(format.toString())
}
```

```text title="Output"
0A:0F
0xFF
BytesHexFormat(
    bytesPerLine = 2147483647,
    bytesPerGroup = 2147483647,
    groupSeparator = "  ",
    byteSeparator = ":",
    bytePrefix = "",
    byteSuffix = ""
)
NumberHexFormat(
    prefix = "0x",
    suffix = "",
    removeLeadingZeros = true,
    minLength = 1
)
HexFormat(
    upperCase = true,
    bytes = BytesHexFormat(
        bytesPerLine = 2147483647,
        bytesPerGroup = 2147483647,
        groupSeparator = "  ",
        byteSeparator = ":",
        bytePrefix = "",
        byteSuffix = ""
    ),
    number = NumberHexFormat(
        prefix = "0x",
        suffix = "",
        removeLeadingZeros = true,
        minLength = 1
    )
)
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
