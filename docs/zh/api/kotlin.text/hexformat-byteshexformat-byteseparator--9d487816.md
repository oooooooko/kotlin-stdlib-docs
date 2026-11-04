# HexFormat.BytesHexFormat.byteSeparator

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

用于在组内分隔相邻字节的字符串 。

每个组的字节数由 `bytesPerGroup` 选项决定。

格式化时,每个组内相邻的字节会由此字符串分隔。

当分析时, 每一组内相邻的字节必须用此字符串分隔 。 此分隔符的解析是以不区分大小写的方式进行的 。

@sample 样本. text. HexFormats. 双面阵列. byte 分隔器

??? note "查看英文原文"

    The string used to separate adjacent bytes within a group.
    
    The number of bytes in each group is determined by the `bytesPerGroup` option.
    
    When formatting, adjacent bytes within each group are separated by this string.
    
    When parsing, adjacent bytes within each group must be separated by this string
    The parsing of this separator is performed in a case-insensitive manner.
    
    @sample samples.text.HexFormats.ByteArrays.byteSeparator

## 声明与重载

### 1. Common

```kotlin
public val byteSeparator: String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L202)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val data = ByteArray(7) { it.toByte() }

    // By default, the byteSeparator is an empty string, hence all bytes are concatenated without any separator.
    println(data.toHexString())
    println("00010203040506".hexToByteArray().contentEquals(data))

    // Specifying a custom byte separator, a colon in this case.
    val colonByteSeparatorFormat = HexFormat { bytes.byteSeparator = ":" }
    println(data.toHexString(colonByteSeparatorFormat))
    println("00:01:02:03:04:05:06".hexToByteArray(colonByteSeparatorFormat).contentEquals(data))

    // Only adjacent bytes within a group are separated by the byteSeparator.
    val groupFormat = HexFormat {
        bytes.bytesPerGroup = 3
        bytes.byteSeparator = ":"
    }
    println(data.toHexString(groupFormat))
    println("00:01:02  03:04:05  06".hexToByteArray(groupFormat).contentEquals(data))

    // Parsing fails due to incorrect byte separator.
    // In this case, the input string is lacking the necessary byte separators within groups.
    assertFailsWith<IllegalArgumentException> {
        "000102  030405  06".hexToByteArray(groupFormat)
    }
}
```

```text title="输出"
00010203040506
true
00:01:02:03:04:05:06
true
00:01:02  03:04:05  06
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L159)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
