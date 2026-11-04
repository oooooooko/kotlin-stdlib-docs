# hexToUInt

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用指定的 `format` , 从此字符串中提取 `UInt` 值 。

字符串必须符合 `format` 定义的结构。 注意, `format` 实例只有 `HexFormat.number` 属性影响数值的解析。

输入字符串必须从前缀开始, 结尾必须是 `HexFormat.number` 属性中定义的后缀 。
还必须含有它们之间至少一个十六进制数字。 如果十六进制位数数
超过八,超额前列数字必须是零。 这确保了《公约》所代表的价值
十六进制位数符合32位`UInt`。
剖析是以不区分情况的方式进行的,包括十六进制数字、前缀和后缀。

现有格式选项及其对分析的影响详情请查阅`HexFormat.NumberHexFormat`。

@param 格式为 `HexFormat` 用于解析, 默认为 `HexFormat.Default` 。 @return 值是 `UInt` 值, 从此字符串中解析 。

@throws 非法配置除外,如果该字符串不符合指定的 `format` ,或者如果十六进制数字代表的数值与`UInt`不相容。

@sample 样本. text. HexFormats. Extensitions. hexToInt 样本. 文本. exformats. Extentions. hexToInt 样本

??? note "查看英文原文"

    Parses an `UInt` value from this string using the specified `format`.
    
    The string must conform to the structure defined by the `format`.
    Note that only the `HexFormat.number` property of the `format` instance affects the parsing of a numeric value.
    
    The input string must start with the prefix and end with the suffix defined in the `HexFormat.number` property.
    It must also contain at least one hexadecimal digit between them. If the number of hexadecimal digits
    exceeds eight, the excess leading digits must be zeros. This ensures that the value represented by the
    hexadecimal digits fits into a 32-bit `UInt`.
    Parsing is performed in a case-insensitive manner, including for the hexadecimal digits, prefix, and suffix.
    
    Refer to `HexFormat.NumberHexFormat` for details about the available format options and their impact on parsing.
    
    @param format the `HexFormat` to use for parsing, `HexFormat.Default` by default.
    @return the `UInt` value parsed from this string.
    
    @throws IllegalArgumentException if this string does not conform to the specified `format`, or if the hexadecimal
      digits represent a value that does not fit into an `UInt`.
    
    @sample samples.text.HexFormats.Extensions.hexToInt

## 声明与重载

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun String.hexToUInt(format: HexFormat = HexFormat.Default): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L235)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    // Using the default format
    println("3a".hexToInt())

    // Parsing is case-insensitive
    println("3A".hexToInt())

    // Up to 8 hexadecimal digits can fit into an Int
    println("ffffffff".hexToInt())

    // Excess leading hexadecimal digits must be zeros
    println("00ffffffff".hexToInt())
    assertFailsWith<IllegalArgumentException> { "0100000000".hexToInt() }

    // Parsing an UInt results in the unsigned version of the same value
    // In this case, (-1).toUInt() = UInt.MAX_VALUE
    println("ffffffff".hexToULong())

    // Using a custom format
    val format = HexFormat { number.prefix = "0x" }
    println("0x3A".hexToInt(format))

    // Parsing fails if the input string does not conform to the specified format.
    // In this case, the prefix is not present.
    assertFailsWith<IllegalArgumentException> { "3A".hexToInt(format) }
}
```

```text title="输出"
58
58
-1
-1
4294967295
58
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L551)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
