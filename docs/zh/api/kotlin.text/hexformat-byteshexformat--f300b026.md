# HexFormat.BytesHexFormat

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

表示用于格式化和分析字节数组的十六进制格式选项。

这些选项分别由 `ByteArray.toHexString` 和`String.hexToByteArray`功能用于格式化和分类,格式化和分类功能也可用`UByteArray`。

在格式化字节数组时,可以假定以下步骤:1. 字节在每行中以 `bytesPerLine` 字节分成行,但最后一行除外,最后一行可能少字节。 2. 每行各分为各组以`bytesPerGroup`字节组成的组,但最后一组则少字节。 3. 所有字节都转换成其两位数的十六进制表示法,每字节前加`bytePrefix`字节,后加 `byteSuffix` .。 4. 每个组内相近格式化的字节除以`byteSeparator`。 5. 每行内相近组则以`groupSeparator`字节分隔。 6. 相近各行按线种子字符 `'\n'` 分隔。

例如,考虑以下片段:```kotlin
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
```鉴于`byteArray`和`format`,收益的格式如下:
1. 国家 8字节被分成6字节的行。 第一行包含`0, 1, 2, 3, 4, 5`,
第二行(和最后一行)包含`6, 7`。
2. 目标 然后将每一行分为4字节的组。 第一行分为两类:`0, 1, 2, 3`和`4, 5`;
第二行组成一组:`6, 7`。
3. 3 个 每个字节转换为十六进制表示法, 以 `"0x"` 预设, 并用空字符串来后缀 。
4. 4个 每个组内的字节用一个空间`" "`分隔。
5. 5 点 每行内的组由垂直条形字符`"|"`分隔。
6. 国家 线条用LF字符`'\n'`分隔。

`byteArray.toHexString(format)` 电话将产生`"0x00 0x01 0x02 0x03|0x04 0x05\n0x06 0x07"`,并印刷到控制台产出:```
0x00 0x01 0x02 0x03|0x04 0x05
0x06 0x07
```

当解析时, 输入字符串必须符合这些选项指定的格式 。 但是, 解析略为宽松, 允许使用任何字符序列 CRLF、 LF或 CR 来作为线分隔符 。 此外, 解析`groupSeparator`、 `byteSeparator`、 `bytePrefix`、 `bytePrefix`、 `byteSuffix`、 `byteSuffix` 和 十六进制数字时, 以不区分大小写的方式进行 。

此类不可更改, 无法直接创建或配置 。 要创建新格式, 请使用 `HexFormat { }` 构建器功能, 并配置括号内 `bytes` 属性的选项 。 例如, 使用 `val format = HexFormat { bytes.bytesPerLine = 16 }` 设置 `bytesPerLine` 。 `bytes` 属性属于 `BytesHexFormat.Builder` 型, 其选项可以配置, 并符合此类的选项 。

??? note "查看英文原文"

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

## 声明与重载

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

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L92)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

```text title="输出"
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

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
