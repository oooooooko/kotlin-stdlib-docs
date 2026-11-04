# HexFormat.BytesHexFormat.Builder.groupSeparator

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

定义正在构建的格式的 `BytesHexFormat.groupSeparator` , 默认情况下两个空格字符( `"  "` ) 。

有关该格式选项如何影响格式化和分析结果的细节,请查阅`BytesHexFormat.groupSeparator`。

@sample 样本. text. HexFormats. yte 阵列. byteesPer Group

??? note "查看英文原文"

    Defines `BytesHexFormat.groupSeparator` of the format being built, two space characters (`"  "`) by default.
    
    Refer to `BytesHexFormat.groupSeparator` for details about how this format option affects
    the formatting and parsing results.
    
    @sample samples.text.HexFormats.ByteArrays.bytesPerGroup

## 声明与重载

### 1. Common

```kotlin
public var groupSeparator: String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L322)

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
