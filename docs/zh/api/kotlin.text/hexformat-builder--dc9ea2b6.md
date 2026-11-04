# HexFormat.Builder

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

提供API 用于建造`HexFormat`。

此类为`HexFormat`的[builder](https://en.wikipedia.org/wiki/Builder_pattern), 并且
充当用于此定义中的 ambda 表达式的接收器类型`HexFormat { }`创建
新格式。 此类中的每一选项与 `HexFormat` 中的选项对应, 并定义它, 产生
格式。 例如,使用 `val format = HexFormat { bytes.byteSeparator = ":" }`设置
`HexFormat.bytes` 属性的 `BytesHexFormat.byteSeparator` 选项 。

有关配置格式选项如何影响格式化和分析结果的细节,请查看`HexFormat`。

@sample 样本. 文本. HexFormats. HexFormatClass. hexFormatBruilder Function 样本. text. HexFormats. HexFormatClass.hexFormatBruiter Function 样本

??? note "查看英文原文"

    Provides an API for building a `HexFormat`.
    
    This class is a [builder](https://en.wikipedia.org/wiki/Builder_pattern) for `HexFormat`, and
    serves as the receiver type of the lambda expression used in the `HexFormat { }` builder function to create a
    new format. Each option in this class corresponds to an option in `HexFormat` and defines it in the resulting
    format. For example, use `val format = HexFormat { bytes.byteSeparator = ":" }` to set
    `BytesHexFormat.byteSeparator` option of the `HexFormat.bytes` property.
    
    Refer to `HexFormat` for details about how the configured format options affect formatting and parsing results.
    
    @sample samples.text.HexFormats.HexFormatClass.hexFormatBuilderFunction

## 声明与重载

### 1. Common

```kotlin
public class Builder @PublishedApi internal constructor()
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L632)

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
