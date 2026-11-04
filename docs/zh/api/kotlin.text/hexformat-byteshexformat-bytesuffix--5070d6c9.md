# HexFormat.BytesHexFormat.byteSuffix

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

紧随每个字节的两位数十六进制表示的字符串。

格式化时, 此字符串用作每个字节十六进制表示法的后缀 。

当分析时, 每一字节的十六进制表示必须用此字符串来补足。 此后缀的解析方式对大小写不敏感 。

@sample 样本. 文本. HexFormats. Byte 阵列. byte 后缀

??? note "查看英文原文"

    The string that immediately follows the two-digit hexadecimal representation of each byte.
    
    When formatting, this string is used as a suffix for the hexadecimal representation of each byte.
    
    When parsing, the hexadecimal representation of each byte must be suffixed by this string.
    The parsing of this suffix is performed in a case-insensitive manner.
    
    @sample samples.text.HexFormats.ByteArrays.byteSuffix

## 声明与重载

### 1. Common

```kotlin
public val byteSuffix: String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L228)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val data = ByteArray(4) { it.toByte() }

    // By default, the byteSuffix is an empty string, so bytes are formatted without any suffix.
    println(data.toHexString())
    println("00010203".hexToByteArray().contentEquals(data))

    // Specifying a custom byte suffix, a semicolon in this case, to follow each byte.
    val byteSuffixFormat = HexFormat {
        bytes.byteSuffix = ";"
    }
    println(data.toHexString(byteSuffixFormat))
    println("00;01;02;03;".hexToByteArray(byteSuffixFormat).contentEquals(data))

    // Parsing fails due to incorrect byte suffix.
    // In this case, the input string is lacking the necessary byte suffixes.
    assertFailsWith<IllegalArgumentException> {
        "00010203".hexToByteArray(byteSuffixFormat)
    }
}
```

```text title="输出"
00010203
true
00;01;02;03;
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L212)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
