# HexFormat.BytesHexFormat.Builder

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

提供API 用于建造`BytesHexFormat`。

此类为`BytesHexFormat`的[builder](https://en.wikipedia.org/wiki/Builder_pattern), 并且
当使用 `HexFormat { }` 构建器创建新格式时, 用作 `bytes` 属性的类型
函数。 此类中的每一选项与 `BytesHexFormat` 中的选项对应,并在
后生成格式。 例如,使用 `val format = HexFormat { bytes.byteSeparator = true }`设置
`BytesHexFormat.byteSeparator` 号 如何配置 详细 , 请参考 `BytesHexFormat`
格式格式选项会影响格式化和分析结果。

??? note "查看英文原文"

    Provides an API for building a `BytesHexFormat`.
    
    This class is a [builder](https://en.wikipedia.org/wiki/Builder_pattern) for `BytesHexFormat`, and
    serves as the type of the `bytes` property when creating a new format using the `HexFormat { }` builder
    function. Each option in this class corresponds to an option in `BytesHexFormat` and defines it in the
    resulting format. For example, use `val format = HexFormat { bytes.byteSeparator = true }` to set
    `BytesHexFormat.byteSeparator`. Refer to `BytesHexFormat` for details about how the configured
    format options affect formatting and parsing results.

## 声明与重载

### 1. Common

```kotlin
public class Builder internal constructor()
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L273)

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
