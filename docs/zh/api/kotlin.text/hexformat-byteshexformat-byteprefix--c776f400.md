# HexFormat.BytesHexFormat.bytePrefix

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

紧接在两位数的字节十六进制表示数之前的字符串。

格式化时, 此字符串用作每个字节十六进制表示的前缀 。

当分析时, 每一字节的十六进制表示必须用此字符串前缀。 此前缀的解析方式对大小写不敏感 。

@sample 样本. 文本. HexFormats. Byte 阵列. byte Prefix

??? note "查看英文原文"

    The string that immediately precedes the two-digit hexadecimal representation of each byte.
    
    When formatting, this string is used as a prefix for the hexadecimal representation of each byte.
    
    When parsing, the hexadecimal representation of each byte must be prefixed by this string.
    The parsing of this prefix is performed in a case-insensitive manner.
    
    @sample samples.text.HexFormats.ByteArrays.bytePrefix

## 声明与重载

### 1. Common

```kotlin
public val bytePrefix: String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L216)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val data = ByteArray(4) { it.toByte() }

    // By default, the bytePrefix is an empty string, so bytes are formatted without any prefix.
    println(data.toHexString())
    println("00010203".hexToByteArray().contentEquals(data))

    // Specifying a custom byte prefix, "0x" in this case, to precede each byte.
    // A space is used as a byte separator for clarity in the output.
    val bytePrefixFormat = HexFormat {
        bytes.bytePrefix = "0x"
        bytes.byteSeparator = " "
    }
    println(data.toHexString(bytePrefixFormat))
    println("0x00 0x01 0x02 0x03".hexToByteArray(bytePrefixFormat).contentEquals(data))

    // Parsing fails due to incorrect byte prefix.
    // In this case, the input string is lacking the necessary byte prefixes.
    assertFailsWith<IllegalArgumentException> {
        "00 01 02 03".hexToByteArray(bytePrefixFormat)
    }
}
```

```text title="输出"
00010203
true
0x00 0x01 0x02 0x03
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L187)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
