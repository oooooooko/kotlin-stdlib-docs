# HexFormat.NumberHexFormat.Builder.suffix

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

定义正在构建的格式的 `NumberHexFormat.suffix`, 默认为空字符串 。

字符串中不得包含线性种子( LF) 和 运输返回( CR) 字符 。

格式选项如何影响格式化和分析结果,详见`NumberHexFormat.suffix`。

@throws 非法设备除外,如果为该属性指定了含有LF或CR字符的字符串。

@sample 样本. 文本. HexFormats. 编号. 后缀

??? note "查看英文原文"

    Defines `NumberHexFormat.suffix` of the format being built, empty string by default.
    
    The string must not contain line feed (LF) and carriage return (CR) characters.
    
    Refer to `NumberHexFormat.suffix` for details about how the format option affects
    the formatting and parsing results.
    
    @throws IllegalArgumentException if a string containing LF or CR character is assigned to this property.
    
    @sample samples.text.HexFormats.Numbers.suffix

## 声明与重载

### 1. Common

```kotlin
public var suffix: String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L568)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    // By default, `suffix` is an empty string
    println(0x3a.toHexString())
    println("0000003a".hexToInt())

    val suffixFormat = HexFormat { number.suffix = "h" }

    // `suffix` is placed after the hex representation
    println(0x3a.toHexString(suffixFormat))
    println("0000003ah".hexToByte(suffixFormat))

    // Parsing `suffix` is conducted in a case-insensitive manner
    println("0000003aH".hexToInt(suffixFormat))

    // Parsing fails if the input string does not end with the specified suffix.
    assertFailsWith<IllegalArgumentException> {
        "0000003a".hexToInt(suffixFormat)
    }
}
```

```text title="输出"
0000003a
58
0000003ah
58
58
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L274)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
