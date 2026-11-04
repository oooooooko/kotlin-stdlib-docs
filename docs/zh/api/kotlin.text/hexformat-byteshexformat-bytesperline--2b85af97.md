# HexFormat.BytesHexFormat.bytesPerLine

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

每行最多字节数, 默认为`Int.MAX_VALUE` 。

格式化时, 字节会以每行`bytesPerLine`字节的行分隔成行, 但最后一行除外, 如果字节总数不能平均地除以此值, 则最后一行的字节会更少。 相邻的行会通过线状种子字符 `'\n'` . 分隔。 请注意, 如果此值大于或等于字节数组的大小, 则整个数组会以单行格式格式, 没有换行符 。

当解析时, 输入字符串必须相应地拆分为行, 每行中各有 `bytesPerLine` 字节, 但最后一行除外, 最后一行的字节可能较少。 任何字符序列 CRLF、 LF或 CR 都被视为有效的线条分隔符 。

@sample 样本.text.HexFormats. bytees yte 阵列. byteesPerLine

??? note "查看英文原文"

    The maximum number of bytes per line, `Int.MAX_VALUE` by default.
    
    When formatting, bytes are split into lines with `bytesPerLine` bytes in each line, except for the last
    line, which may have fewer bytes if the total number of bytes does not divide evenly by this value. Adjacent
    lines are separated by the line feed (LF) character `'\n'`. Note that if this value is greater than or equal
    to the size of the byte array, the entire array will be formatted as a single line without any line breaks.
    
    When parsing, the input string must be split into lines accordingly, with `bytesPerLine` bytes in each line,
    except for the last line, which may have fewer bytes. Any of the char sequences CRLF, LF, or CR
    is considered a valid line separator.
    
    @sample samples.text.HexFormats.ByteArrays.bytesPerLine

## 声明与重载

### 1. Common

```kotlin
public val bytesPerLine: Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L153)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val data = ByteArray(7) { it.toByte() }

    // By default, bytesPerLine is set to Int.MAX_VALUE, which exceeds data.size.
    // Therefore, all bytes are formatted as a single line without any line breaks.
    println(data.toHexString())
    println("00010203040506".hexToByteArray().contentEquals(data))

    // Setting bytesPerLine to 3 splits the output into 3 lines with 3, 3, and 1 bytes, respectively.
    // Each line is separated by a line feed (LF) character.
    val threePerLineFormat = HexFormat {
        bytes.bytesPerLine = 3
    }
    println(data.toHexString(threePerLineFormat))

    // When parsing, any of the line separators CRLF, LF, and CR are accepted.
    println("000102\n030405\r\n06".hexToByteArray(threePerLineFormat).contentEquals(data))

    // Parsing fails if the input string does not conform to specified format.
    // In this case, lines do not consist of the expected number of bytes.
    assertFailsWith<IllegalArgumentException> {
        "0001\n0203\n0405\n06".hexToByteArray(threePerLineFormat)
    }
}
```

```text title="输出"
00010203040506
true
000102
030405
06
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L78)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
