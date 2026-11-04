# HexFormat.upperCase

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定是否应该使用大写十六进制数字来格式化,默认情况下为 `false` 。

当此选项设定为 `true` 时,格式化函数将使用大写十六进制数字( `0-9`, `A-F`)来创建正格式化的数值的十六进制表示。 否则, 将使用小写十六进制数字( `0-9`, `a-f`) 。

此选项影响字节数组和数值的格式化结果。 但是, ** ** 对分析** 没有任何影响, 分析总是以不区分大小写的方式进行 。

注:本选项** 仅影响十六进制数字** 的情况,不影响其他要素,如`BytesHexFormat.bytePrefix`或`NumberHexFormat.suffix`。

@sample 样本.text.HexFormats.HexFormatclass.upperCase 样本

??? note "查看英文原文"

    Specifies whether upper-case hexadecimal digits should be used for formatting, `false` by default.
    
    When this option is set to `true`, formatting functions will use upper-case hexadecimal digits (`0-9`, `A-F`)
    to create the hexadecimal representation of the values being formatted. Otherwise, lower-case hexadecimal digits
    (`0-9`, `a-f`) will be used.
    
    This option affects the formatting results for both byte arrays and numeric values. However, it **has no effect
    on parsing**, which is always performed in a case-insensitive manner.
    
    Note: This option **affects only the case of hexadecimal digits** and does not influence other elements like
    `BytesHexFormat.bytePrefix` or `NumberHexFormat.suffix`.
    
    @sample samples.text.HexFormats.HexFormatClass.upperCase

## 声明与重载

### 1. Common

```kotlin
public val upperCase: Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L38)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // By default, upperCase is set to false, so lower-case hexadecimal digits are used when formatting.
    println(58.toHexString())
    println(58.toHexString(HexFormat.Default))

    // Setting upperCase to true changes the hexadecimal digits to upper-case.
    println(58.toHexString(HexFormat { upperCase = true }))
    println(58.toHexString(HexFormat.UpperCase))

    // The upperCase option affects only the case of hexadecimal digits.
    val format = HexFormat {
        upperCase = true
        number.prefix = "0x"
    }
    println(58.toHexString(format))

    // The upperCase option also affects how byte arrays are formatted.
    println(byteArrayOf(0x1b, 0xe6.toByte()).toHexString(format))

    // The upperCase option does not affect parsing; parsing is always case-insensitive.
    println("0x0000003a".hexToInt(format))
    println("1BE6".hexToByteArray(format).contentEquals(byteArrayOf(0x1b, 0xe6.toByte())))
}
```

```text title="输出"
0000003a
0000003a
0000003A
0000003A
0x0000003A
1BE6
58
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L51)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
