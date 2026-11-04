# HexFormat

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

表示十六进制格式选项,用于格式化和分析字节数组和数字整数值,既有签名的,也有未签名的。

此类的例子被传递到格式化和解析函数, 并指定如何进行格式化和解析。 `bytes` 属性的选项仅在格式化和解析字节数组时才适用, 而 `number` 属性在格式化和解析数字值时适用。 `upperCase` 选项影响两个部分。

此类不可更改, 无法直接创建或配置。 要创建新格式, 请使用 `HexFormat { }` 构建器功能, 并在括号内配置选项 。 例如, 使用 `val format = HexFormat { upperCase = true }` 来启用大写格式 。

类的同伴对象提供了两个预设实例:`Default`和 `UpperCase` 。 `Default` 例的选项设定为 `upperCase` ,`false`, `bytes` 和 `number` ,其默认值设定为 `BytesHexFormat` 和 `NumberHexFormat` 。`UpperCase`例的选项设定为`upperCase`,`true`, `bytes` 和 `number` 的选项设定为默认值。

@sample 样本. 文本. HexFormats. HexFormatClass. hexFormatBruilder Function 样本. text. HexFormats. HexFormatClass.hexFormatBruiter Function 样本

@see 位元数阵列.toHexString @see 字符串.hexTo ByteArray @see 内插到 HexString @see 字符串.hexToInt

??? note "查看英文原文"

    Represents hexadecimal format options for formatting and parsing byte arrays and integer numeric values,
    both signed and unsigned.
    
    An instance of this class is passed to formatting and parsing functions and specifies how formatting and parsing
    should be conducted. The options of the `bytes` property apply only when formatting and parsing byte arrays,
    while the `number` property applies when formatting and parsing numeric values. The `upperCase` option affects both.
    
    This class is immutable and cannot be created or configured directly. To create a new format, use the
    `HexFormat { }` builder function and configure the options inside the braces. For example, use
    `val format = HexFormat { upperCase = true }` to enable upper-case formatting.
    
    Two predefined instances are provided by this class's companion object: `Default` and `UpperCase`.
    The `Default` instance has the `upperCase` option set to `false`, and the options of `bytes` and `number` properties
    set to their default values as specified in `BytesHexFormat` and `NumberHexFormat`, respectively.
    The `UpperCase` instance has the `upperCase` option set to `true`, and the options of `bytes` and `number` properties
    set to their default values.
    
    @sample samples.text.HexFormats.HexFormatClass.hexFormatBuilderFunction
    
    @see ByteArray.toHexString
    @see String.hexToByteArray
    @see Int.toHexString
    @see String.hexToInt

## 声明与重载

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public class HexFormat internal constructor(
    /**
     * Specifies whether upper-case hexadecimal digits should be used for formatting, `false` by default.
     *
     * When this option is set to `true`, formatting functions will use upper-case hexadecimal digits (`0-9`, `A-F`)
     * to create the hexadecimal representation of the values being formatted. Otherwise, lower-case hexadecimal digits
     * (`0-9`, `a-f`) will be used.
     *
     * This option affects the formatting results for both byte arrays and numeric values. However, it **has no effect
     * on parsing**, which is always performed in a case-insensitive manner.
     *
     * Note: This option **affects only the case of hexadecimal digits** and does not influence other elements like
     * [BytesHexFormat.bytePrefix] or [NumberHexFormat.suffix].
     *
     * @sample samples.text.HexFormats.HexFormatClass.upperCase
     */
    public val upperCase: Boolean,

    /**
     * Specifies the hexadecimal format used for formatting and parsing byte arrays.
     *
     * This property defines how byte arrays are formatted into hexadecimal strings and parsed back from strings into
     * byte arrays. It is utilized by [ByteArray.toHexString] for formatting and [String.hexToByteArray] for parsing.
     * These functions are available for [UByteArray] as well.
     *
     * Refer to [BytesHexFormat] for details about the available format options, their impact on formatting and
     * parsing results, and their default settings.
     */
    public val bytes: BytesHexFormat,

    /**
     * Specifies the hexadecimal format used for formatting and parsing numeric values.
     *
     * This property defines how numeric values are formatted into hexadecimal strings and parsed back from strings
     * into numeric values. It is utilized by functions like [Int.toHexString] for formatting and [String.hexToInt] for
     * parsing. These functions are available for all integer numeric types.
     *
     * Refer to [NumberHexFormat] for details about the available format options, their impact on formatting and
     * parsing results, and their default settings.
     */
    public val number: NumberHexFormat
)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L10)

### 2. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun HexFormat(builderAction: HexFormat.Builder.() -> Unit): HexFormat
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L812)

使用指定的 `builderAction` 配置格式选项,以构建新的 `HexFormat` 并返回由此生成的格式。

生成的格式可以被传递到格式化和解析函数, 以决定格式化和解析的进行方式。 例如, `val format = HexFormat { number.prefix = "0x" }` 创建了一个新的 `HexFormat` 并指定给 `format` 变量。 当此 `format` 被传递到数字格式化函数时, 生成的字符串将包括 `"0x"` 作为正在格式化的数值的十六进制表示的前缀。 例如, 拨打 `58.toHexString(format)` 将产生 `"0x0000003a"` 。

配置格式选项详情请查阅`HexFormat.Builder`, 配置格式选项的相关信息请查阅`HexFormat`, 配置格式选项如何影响格式和分析结果, 请查看`HexFormat`。

作为`builderAction`号的接收器提供的建筑商只有在该函数中有效。使用该函数之外,可以产生一种未指明的行为。

@param 构建器动作 函数配置 `HexFormat.Builder` 接收器的格式选项。 @return 一个新实例 `HexFormat` , 由 `builderAction` 所配置 。

@sample 样本. 文本. HexFormats. HexFormatClass. hexFormatBruilder Function 样本. text. HexFormats. HexFormatClass.hexFormatBruiter Function 样本

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Specifying format options for numeric values.
    println(58.toHexString(HexFormat { number.removeLeadingZeros = true }))
    println("0x3a".hexToInt(HexFormat { number.prefix = "0x" }))

    // Specifying format options for byte arrays.
    val macAddressFormat = HexFormat {
        upperCase = true
        bytes {
            bytesPerGroup = 2
            groupSeparator = "."
        }
    }
    val macAddressBytes = byteArrayOf(0x00, 0x1b, 0x63, 0x84.toByte(), 0x45, 0xe6.toByte())
    println(macAddressBytes.toHexString(macAddressFormat))
    println("001B.6384.45E6".hexToByteArray(macAddressFormat).contentEquals(macAddressBytes))

    // Creating a format that defines options for both byte arrays and numeric values.
    val customHexFormat = HexFormat {
        upperCase = true
        number {
            removeLeadingZeros = true
            prefix = "0x"
        }
        bytes {
            bytesPerGroup = 2
            groupSeparator = "."
        }
    }
    // Formatting numeric values utilizes the `upperCase` and `number` options.
    println(58.toHexString(customHexFormat))
    // Formatting byte arrays utilizes the `upperCase` and `bytes` options.
    println(macAddressBytes.toHexString(customHexFormat))
}
```

```text title="输出"
3a
58
001B.6384.45E6
true
0x3A
001B.6384.45E6
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L15)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
