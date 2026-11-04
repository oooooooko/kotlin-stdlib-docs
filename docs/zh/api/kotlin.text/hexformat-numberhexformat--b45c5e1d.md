# HexFormat.NumberHexFormat

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

表示用于格式化和解析数值的十六进制格式选项。

这些选项被`Int.toHexString` 等功能用于格式化, 并被`String.hexToInt` 用于解析。 对所有整数数字类型都可用格式化和解析功能。

格式化时,结果由`prefix`字符串组成,该数字值的十六进制表示法,
和`suffix`字符串。 绘制每块四位元块的图示,计算出一个数值的十六进制表示法
的二进制表示法,以相应的十六进制位数开始,从最重要的位数开始。
`upperCase` 选项确定十六进制位数的大小( `A-F` 或 `a-f`) 。
如果`removeLeadingZeros`为`true`,而十六进制代表值大于`minLength`,则前零
将删除,直到长度与 `minLength` 匹配。 但是,如果`minLength`超过十六进制长度
代表的开始, `removeLeadingZeros` 被忽略, 零被加入到代表的开始
达到指定的 `minLength`。

例如,`Int`值 `58`(32比特长`00000000000000000000000000111010`)的二进制表示法
转换为十六进制表示 `0000003a` 或 `0000003A`,视`upperCase`而定。
将`removeLeadingZeros`设为`true`,将缩短为`3a`。 但是,如果`minLength`设为`6`,则删除
一旦长度缩小为`00003a`, 引导零停止 。 将`minLength`设为`12`
`00000000003a`, 此处`removeLeadingZeros`选项因最低长度要求而被忽略。

要将一个数值格式化为特定长度的十六进制字符串,首先将该数值转换为
合适的位数大小 。 例如,要将 `Int` 值格式化为四位数十六进制字符串,将数值转换为
在十六进制格式化之前使用 `toShort()`。 获得最多4位数的四位数,但无前导零位数,
将`removeLeadingZeros`附加设为`true`。

当分析时,输入字符串必须从 `prefix` 开始,最后以 `suffix` 结束。 须至少包含
中间一个十六进制数字 如果十六进制位数数超过该类型的能力
根据其位数大小,分析出的超大前位数必须是零。 `prefix`、`suffix`和
以不区分大小写的方式进行十六进制位数。 `removeLeadingZeros` 和 `minLength` 选项
分析时忽略。

此类不可更改, 无法直接创建或配置 。 要创建新格式, 请使用 `HexFormat { }` 构建器功能, 并配置括号内 `number` 属性的选项 。 例如, 使用 `val format = HexFormat { number.prefix = "0x" }` 设置 `prefix` 。 `number` 属性属于 `NumberHexFormat.Builder` 型, 其选项可以配置, 并符合此类的选项 。

@sample 样本. text. HexFormats. 编号. number HexFormats

??? note "查看英文原文"

    Represents hexadecimal format options for formatting and parsing numeric values.
    
    These options are utilized by functions like `Int.toHexString` for formatting and `String.hexToInt` for parsing.
    The formatting and parsing functions are available for all integer numeric types.
    
    When formatting, the result consists of a `prefix` string, the hexadecimal representation of the numeric value,
    and a `suffix` string. The hexadecimal representation of a value is calculated by mapping each four-bit chunk
    of its binary representation to the corresponding hexadecimal digit, starting with the most significant bits.
    The `upperCase` option determines the case (`A-F` or `a-f`) of the hexadecimal digits.
    If `removeLeadingZeros` is `true` and the hexadecimal representation is longer than `minLength`, leading zeros
    are removed until the length matches `minLength`. However, if `minLength` exceeds the length of the hexadecimal
    representation, `removeLeadingZeros` is ignored, and zeros are added to the start of the representation to
    achieve the specified `minLength`.
    
    For example, the binary representation of the `Int` value `58` (32-bit long `00000000000000000000000000111010`)
    converts to the hexadecimal representation `0000003a` or `0000003A`, depending on `upperCase`.
    With `removeLeadingZeros` set to `true`, it shortens to `3a`. However, if `minLength` is set to `6`, the removal of
    leading zeros stops once the length is reduced to `00003a`. Setting `minLength` to `12` results in
    `00000000003a`, where the `removeLeadingZeros` option is ignored due to the minimum length requirement.
    
    To format a value into a hexadecimal string of a particular length, start by converting the value to a type with
    the suitable bit size. For instance, to format an `Int` value into a 4-digit hexadecimal string, convert the value
    using `toShort()` before hexadecimal formatting. To obtain a maximum of 4 digits without leading zeros,
    additionally set `removeLeadingZeros` to `true`.
    
    When parsing, the input string must start with the `prefix` and end with the `suffix`. It must contain at least
    one hexadecimal digit between them. If the number of hexadecimal digits exceeds the capacity of the type being
    parsed, based on its bit size, the excess leading digits must be zeros. Parsing of the `prefix`, `suffix`, and
    hexadecimal digits is performed in a case-insensitive manner. The `removeLeadingZeros` and `minLength` options
    are ignored during parsing.
    
    This class is immutable and cannot be created or configured directly. To create a new format, use the
    `HexFormat { }` builder function and configure the options of the `number` property inside the braces. For
    example, use `val format = HexFormat { number.prefix = "0x" }` to set the `prefix`. The `number` property is of
    type `NumberHexFormat.Builder`, whose options are configurable and correspond to the options of this class.
    
    @sample samples.text.HexFormats.Numbers.numberHexFormat

## 声明与重载

### 1. Common

```kotlin
public class NumberHexFormat internal constructor(
        /**
         * The string that immediately precedes the hexadecimal representation of a numeric value,
         * empty string by default.
         *
         * When formatting, this string is placed before the hexadecimal representation.
         * When parsing, the string being parsed must start with this string.
         * The parsing of this prefix is performed in a case-insensitive manner.
         *
         * @sample samples.text.HexFormats.Numbers.prefix
         */
        public val prefix: String,

        /**
         * The string that immediately succeeds the hexadecimal representation of a numeric value,
         * empty string by default.
         *
         * When formatting, this string is placed after the hexadecimal representation.
         * When parsing, the string being parsed must end with this string.
         * The parsing of this suffix is performed in a case-insensitive manner.
         *
         * @sample samples.text.HexFormats.Numbers.suffix
         */
        public val suffix: String,

        /**
         * Specifies whether to remove leading zeros in the hexadecimal representation of a numeric value,
         * `false` by default.
         *
         * The hexadecimal representation of a value is calculated by mapping each four-bit chunk of its binary
         * representation to the corresponding hexadecimal digit, starting with the most significant bits.
         *
         * When formatting, if this option is `true` and the length of the hexadecimal representation exceeds
         * [minLength], leading zeros are removed until the length matches [minLength]. If the length
         * does not exceed [minLength], this option has no effect on the formatting result.
         *
         * When parsing, this option is ignored.
         *
         * @sample samples.text.HexFormats.Numbers.removeLeadingZeros
         */
        public val removeLeadingZeros: Boolean,

        /**
         * Specifies the minimum number of hexadecimal digits to be used in the representation of a numeric value,
         * `1` by default.
         *
         * The hexadecimal representation of a value is calculated by mapping each four-bit chunk of its binary
         * representation to the corresponding hexadecimal digit, starting with the most significant bits.
         *
         * When formatting:
         *   - If this option is less than the length of the hexadecimal representation:
         *       - If [removeLeadingZeros] is `true`, leading zeros are removed until the length matches [minLength].
         *       - If [removeLeadingZeros] is `false`, the representation remains unchanged, as no leading zeros are removed.
         *   - If this option is greater than the length of the hexadecimal representation, the
         *     representation is padded with zeros at the start to reach the specified [minLength].
         *   - If this option matches the length of the hexadecimal representation, the representation remains unchanged.
         *
         * When parsing, this option is ignored. However, there must be at least one hexadecimal digit in the input
         * string. If the number of hexadecimal digits exceeds the capacity of the type being parsed, based on its bit
         * size, the excess leading digits must be zeros.
         *
         * @sample samples.text.HexFormats.Numbers.minLength
         */
        @SinceKotlin("2.0")
        public val minLength: Int
    )
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L406)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val numberHexFormat = HexFormat {
        upperCase = true
        number {
            removeLeadingZeros = true
            minLength = 4
            prefix = "0x"
        }
    }

    println(0x3a.toHexString(numberHexFormat))
    println("0x003A".hexToInt(numberHexFormat))
    // Parsing is case-insensitive
    println("0X003a".hexToInt(numberHexFormat))
}
```

```text title="输出"
0x003A
58
58
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L236)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
