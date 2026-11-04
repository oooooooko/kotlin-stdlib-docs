# HexFormat.NumberHexFormat.Builder.removeLeadingZeros

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

定义了正在构建的格式的 `NumberHexFormat.removeLeadingZeros` , 默认情况下为 `false` 。

格式选项如何影响格式化和分析结果,详见`NumberHexFormat.removeLeadingZeros`。

@sample 样本. 文本. HexFormats. 数字. 移动 列车零号

??? note "查看英文原文"

    Defines `NumberHexFormat.removeLeadingZeros` of the format being built, `false` by default.
    
    Refer to `NumberHexFormat.removeLeadingZeros` for details about how the format option affects
    the formatting and parsing results.
    
    @sample samples.text.HexFormats.Numbers.removeLeadingZeros

## 声明与重载

### 1. Common

```kotlin
public var removeLeadingZeros: Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L587)

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
