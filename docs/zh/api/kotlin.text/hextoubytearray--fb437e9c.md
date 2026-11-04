# hexToUByteArray

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用指定的 `format` 来从此字符串中提取字节数组 。

字符串必须符合 `format` 定义的结构。 注意, `format` 实例只有 `HexFormat.bytes` 属性影响字节数组的解析 。

对于`HexFormat.bytes`属性中定义的十六进制数字和元素(前缀、后缀、分隔符),分解方式不区分情况,此外,任何字符序列都被视为有效的线性分隔符,CRLF、LF和CR。

现有格式选项及其对分析的影响详情请查阅`HexFormat.BytesHexFormat`。

@param 格式为 `HexFormat` 用于解析, 默认为 `HexFormat.Default` 。 @return 字节数组从此字符串中解析 。

@throws 非法设备例外,如果该字符串不符合指定的 `format` 。

@sample 样本. text. HexFormats. Extensions.hex ToByte 箭头

??? note "查看英文原文"

    Parses a byte array from this string using the specified `format`.
    
    The string must conform to the structure defined by the `format`.
    Note that only the `HexFormat.bytes` property of the `format` instance affects the parsing of a byte array.
    
    Parsing is performed in a case-insensitive manner for both the hexadecimal digits and the elements
    (prefix, suffix, separators) defined in the `HexFormat.bytes` property. Additionally, any of the
    char sequences CRLF, LF and CR is considered a valid line separator.
    
    Refer to `HexFormat.BytesHexFormat` for details about the available format options and their impact on parsing.
    
    @param format the `HexFormat` to use for parsing, `HexFormat.Default` by default.
    @return the byte array parsed from this string.
    
    @throws IllegalArgumentException if this string does not conform to the specified `format`.
    
    @sample samples.text.HexFormats.Extensions.hexToByteArray

## 声明与重载

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@ExperimentalUnsignedTypes
@InlineOnly
public inline fun String.hexToUByteArray(format: HexFormat = HexFormat.Default): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L74)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val expectedData = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte(), 0x5C, 0x0E)

    // Using the default format
    println("de2d02c05c0e".hexToByteArray().contentEquals(expectedData))

    // Parsing is case-insensitive
    println("DE2D02C05C0E".hexToByteArray().contentEquals(expectedData))

    // Using a custom format
    val format = HexFormat {
        bytes {
            bytesPerLine = 4
            byteSeparator = " " // One space
            bytePrefix = "0x"
        }
    }
    println("0xDE 0x2D 0x02 0xC0\n0x5C 0x0E".hexToByteArray(format).contentEquals(expectedData))

    // Parsing unsigned bytes results in the unsigned versions of the same bytes
    val expectedUnsignedData = expectedData.toUByteArray()
    println("de2d02c05c0e".hexToUByteArray().contentEquals(expectedUnsignedData))

    // Parsing fails if the input string does not conform to the specified format.
    // In this case, there is no line separator after the fourth formatted byte.
    assertFailsWith<IllegalArgumentException> {
        "0xDE 0x2D 0x02 0xC0 0x5C 0x0E".hexToByteArray(format)
    }
}
```

```text title="输出"
true
true
true
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L391)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
