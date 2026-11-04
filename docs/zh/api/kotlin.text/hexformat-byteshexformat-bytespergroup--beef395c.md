# HexFormat.BytesHexFormat.bytesPerGroup

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

每组最多字节数, 每行`Int.MAX_VALUE`, 默认数 。

每行的字节数由`bytesPerLine`选项决定。

格式化时,每行将分成每组中 `bytesPerGroup` 字节的组,但最后一组除外,最后一组在一行中,如果该行中字节数不均匀地除以此值,则该组的字节数可能较少。每行中的相近组数将除以 `groupSeparator` 。请注意,如果该值大于或等于一行中字节数,则该字节不会分成若干组。

当解析时,输入字符串中的每行必须分成 `bytesPerGroup` 字节的组,但最后一组除外,最后一组的行可能较少。每行内的相邻组必须除以 `groupSeparator` 。分隔符的解析方式不区分大小写。

@sample 样本. text. HexFormats. yte 阵列. byteesPer Group

??? note "查看英文原文"

    The maximum number of bytes per group in a line, `Int.MAX_VALUE` by default.
    
    The number of bytes in each line is determined by the `bytesPerLine` option.
    
    When formatting, each line is split into groups with `bytesPerGroup` bytes in each group, except for the
    last group in a line, which may have fewer bytes if the number of bytes in the line does not divide evenly
    by this value. Adjacent groups within each line are separated by `groupSeparator`. Note that if this value
    is greater than or equal to the number of bytes in a line, the bytes are not split into groups.
    
    When parsing, each line in the input string must be split into groups of `bytesPerGroup` bytes, except for
    the last group in a line, which may have fewer bytes. Adjacent groups within each line must be separated by
    `groupSeparator`. The parsing of the separator is performed in a case-insensitive manner.
    
    @sample samples.text.HexFormats.ByteArrays.bytesPerGroup

## 声明与重载

### 1. Common

```kotlin
public val bytesPerGroup: Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L169)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val data = ByteArray(7) { it.toByte() }

    // By default, both bytesPerLine and bytesPerGroup are set to Int.MAX_VALUE, which exceeds data.size.
    // Hence, all bytes are formatted as a single line and a single group.
    println(data.toHexString())
    println("00010203040506".hexToByteArray().contentEquals(data))

    // Setting bytesPerGroup to 2 with the default group separator, which is two spaces.
    val twoPerGroupFormat = HexFormat {
        bytes.bytesPerGroup = 2
    }
    println(data.toHexString(twoPerGroupFormat))
    println("0001  0203  0405  06".hexToByteArray(twoPerGroupFormat).contentEquals(data))

    // Specifying a custom group separator, a dot in this case.
    val dotGroupSeparatorFormat = HexFormat {
        bytes {
            bytesPerGroup = 2
            groupSeparator = "."
        }
    }
    println(data.toHexString(dotGroupSeparatorFormat))
    println("0001.0203.0405.06".hexToByteArray(dotGroupSeparatorFormat).contentEquals(data))

    // If bytesPerLine is less than or equal to bytesPerGroup, each line is treated as a single group,
    // hence no group separator is used.
    val lessBytesPerLineFormat = HexFormat {
        bytes {
            bytesPerLine = 3
            bytesPerGroup = 4
            groupSeparator = "|"
        }
    }
    println(data.toHexString(lessBytesPerLineFormat))
    println("000102\n030405\n06".hexToByteArray(lessBytesPerLineFormat).contentEquals(data))

    // When bytesPerLine is greater than bytesPerGroup, each line is split into multiple groups.
    val moreBytesPerLineFormat = HexFormat {
        bytes {
            bytesPerLine = 5
            bytesPerGroup = 2
            groupSeparator = "."
        }
    }
    println(data.toHexString(moreBytesPerLineFormat))
    println("0001.0203.04\n0506".hexToByteArray(moreBytesPerLineFormat).contentEquals(data))

    // Parsing fails due to incorrect group separator.
    assertFailsWith<IllegalArgumentException> {
        "0001  0203  04\n0506".hexToByteArray(moreBytesPerLineFormat)
    }
}
```

```text title="输出"
00010203040506
true
0001  0203  0405  06
true
0001.0203.0405.06
true
000102
030405
06
true
0001.0203.04
0506
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L104)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
