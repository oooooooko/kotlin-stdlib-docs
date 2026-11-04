# HexFormat.NumberHexFormat.Builder

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

提供API 用于建造`NumberHexFormat`。

此类为`NumberHexFormat`的[builder](https://en.wikipedia.org/wiki/Builder_pattern), 并且
当使用 `HexFormat { }` 构建器创建新格式时, 用作 `number` 属性的类型
函数。 此类中的每一选项与 `NumberHexFormat` 中的选项对应,并在
后生成格式。 例如,使用 `val format = HexFormat { number.removeLeadingZeros = true }`设置
`NumberHexFormat.removeLeadingZeros` 号 如何配置 详细 , 请参考 `NumberHexFormat`
格式格式选项会影响格式化和分析结果。

@sample 样本. text. HexFormats. 编号. number HexFormats

??? note "查看英文原文"

    Provides an API for building a `NumberHexFormat`.
    
    This class is a [builder](https://en.wikipedia.org/wiki/Builder_pattern) for `NumberHexFormat`, and
    serves as the type of the `number` property when creating a new format using the `HexFormat { }` builder
    function. Each option in this class corresponds to an option in `NumberHexFormat` and defines it in the
    resulting format. For example, use `val format = HexFormat { number.removeLeadingZeros = true }` to set
    `NumberHexFormat.removeLeadingZeros`. Refer to `NumberHexFormat` for details about how the configured
    format options affect formatting and parsing results.
    
    @sample samples.text.HexFormats.Numbers.numberHexFormat

## 声明与重载

### 1. Common

```kotlin
public class Builder internal constructor()
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L536)

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
