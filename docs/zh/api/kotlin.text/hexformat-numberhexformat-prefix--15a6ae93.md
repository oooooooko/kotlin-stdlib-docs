# HexFormat.NumberHexFormat.prefix

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

紧接在数字值十六进制表示之前的字符串,默认为空字符串。

格式化时, 此字符串会被置于十六进制表示式之前。 当分析时, 正在分析的字符串必须从此字符串开始。 此前缀的解析是以不区分大小写的方式进行的 。

@sample 样本. text. HexFormats. 编号. 前缀

??? note "查看英文原文"

    The string that immediately precedes the hexadecimal representation of a numeric value,
    empty string by default.
    
    When formatting, this string is placed before the hexadecimal representation.
    When parsing, the string being parsed must start with this string.
    The parsing of this prefix is performed in a case-insensitive manner.
    
    @sample samples.text.HexFormats.Numbers.prefix

## 声明与重载

### 1. Common

```kotlin
public val prefix: String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L446)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    // By default, `prefix` is an empty string.
    println(0x3a.toHexString())
    println("0000003a".hexToInt())

    val prefixFormat = HexFormat { number.prefix = "0x" }

    // `prefix` is placed before the hex representation.
    println(0x3a.toHexString(prefixFormat))
    println("0x0000003a".hexToInt(prefixFormat))

    // Parsing `prefix` is conducted in a case-insensitive manner.
    println("0X0000003a".hexToInt(prefixFormat))

    // Parsing fails if the input string does not start with the specified prefix.
    assertFailsWith<IllegalArgumentException> {
        "0000003a".hexToInt(prefixFormat)
    }
}
```

```text title="输出"
0000003a
58
0x0000003a
58
58
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L253)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
