# HexFormat.bytes

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定用于格式化和分析字节数组的十六进制格式。

此属性定义字节数组如何格式化为十六进制字符串,从字符串到字节数组的反向分析。 `ByteArray.toHexString` 用于格式化,`String.hexToByteArray` 用于解析。这些函数也可以用于 `UByteArray` 。

有关可用格式选项、其对格式化和分析结果的影响及其默认设置的细节,请查阅`BytesHexFormat`。

??? note "查看英文原文"

    Specifies the hexadecimal format used for formatting and parsing byte arrays.
    
    This property defines how byte arrays are formatted into hexadecimal strings and parsed back from strings into
    byte arrays. It is utilized by `ByteArray.toHexString` for formatting and `String.hexToByteArray` for parsing.
    These functions are available for `UByteArray` as well.
    
    Refer to `BytesHexFormat` for details about the available format options, their impact on formatting and
    parsing results, and their default settings.

## 声明与重载

### 1. Common

```kotlin
public val bytes: BytesHexFormat
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L55)

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
