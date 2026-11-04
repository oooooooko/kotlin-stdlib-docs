# HexFormat.NumberHexFormat.removeLeadingZeros

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定是否删除数字值的十六进制表示式中前导零,默认为 `false` 。

数值的十六进制表示法是将其二进制表示法的每个四位元块绘制成相应的十六进制数字,从最重要的位数开始计算。

当格式化时,如果此选项为`true`, 且十六进制代表符长度超过`minLength`, 则在长度匹配 `minLength` 之前删除前导零。 如果长度不超过 `minLength` , 此选项对格式化结果没有影响 。

当进行分析时, 此选项将被忽略 。

@sample 样本. 文本. HexFormats. 数字. 移动 列车零号

??? note "查看英文原文"

    Specifies whether to remove leading zeros in the hexadecimal representation of a numeric value,
    `false` by default.
    
    The hexadecimal representation of a value is calculated by mapping each four-bit chunk of its binary
    representation to the corresponding hexadecimal digit, starting with the most significant bits.
    
    When formatting, if this option is `true` and the length of the hexadecimal representation exceeds
    `minLength`, leading zeros are removed until the length matches `minLength`. If the length
    does not exceed `minLength`, this option has no effect on the formatting result.
    
    When parsing, this option is ignored.
    
    @sample samples.text.HexFormats.Numbers.removeLeadingZeros

## 声明与重载

### 1. Common

```kotlin
public val removeLeadingZeros: Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L470)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // By default, removeLeadingZeroes is `false`
    println(0x3a.toHexString())

    val removeLeadingZerosFormat = HexFormat { number.removeLeadingZeros = true }

    // If there are no leading zeros, removeLeadingZeroes has no effect
    println(0x3a.toByte().toHexString(removeLeadingZerosFormat))

    // The leading zeros in the hex representation are removed until minLength is reached.
    // By default, minLength is 1.
    println(0x3a.toHexString(removeLeadingZerosFormat))
    println(0.toHexString(removeLeadingZerosFormat))

    // Here minLength is set to 6.
    val shorterLengthFormat = HexFormat {
        number.removeLeadingZeros = true
        number.minLength = 6
    }
    println(0x3a.toHexString(shorterLengthFormat))

    // When minLength is longer than the hex representation, the hex representation is padded with zeros.
    // removeLeadingZeros is ignored in this case.
    val longerLengthFormat = HexFormat {
        number.removeLeadingZeros = true
        number.minLength = 12
    }
    println(0x3a.toHexString(longerLengthFormat))

    // When parsing, removeLeadingZeros is ignored
    println("0000003a".hexToInt(removeLeadingZerosFormat))
}
```

```text title="输出"
0000003a
3a
3a
0
00003a
00000000003a
58
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L295)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
