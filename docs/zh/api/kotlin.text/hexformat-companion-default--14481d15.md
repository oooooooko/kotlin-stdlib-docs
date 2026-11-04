# HexFormat.Companion.Default

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

默认十六进制格式选项。

此 `HexFormat` 实例对所有格式选项采用默认值 。

格式化函数对字节数组和数值值使用小写十六进制数字(`0-9`,`a-f`),具体来说,`upperCase`被设定为`false`。

没有使用线条分隔符、 组分隔符、 字节分隔符、 字节前缀或字节后缀
当格式化或分析字节数组时。 具体地说:
* `bytes.bytesPerLine``BytesHexFormat.bytesPerLine`设为`Int.MAX_VALUE`。
* `bytes.bytesPerGroup``BytesHexFormat.bytesPerGroup`设为`Int.MAX_VALUE`。
  * `bytes.byteSeparator``BytesHexFormat.byteSeparator`, `bytes.bytePrefix``BytesHexFormat.bytePrefix`,
`bytes.byteSuffix``BytesHexFormat.byteSuffix`是空字符串。

未使用前缀或后缀,前缀零不会从十六进制表示式中删除
格式化或解析数值时。 具体地说:
  * `number.prefix``NumberHexFormat.prefix`和`number.suffix``NumberHexFormat.suffix`空字符串。
* `number.removeLeadingZeros``NumberHexFormat.removeLeadingZeros`设为`false`。

??? note "查看英文原文"

    The default hexadecimal format options.
    
    This `HexFormat` instance adopts default values for all format options.
    
    Formatting functions use lower-case hexadecimal digits (`0-9`, `a-f`) for both byte arrays and
    numeric values. Specifically, `upperCase` is set to `false`.
    
    No line separator, group separator, byte separator, byte prefix, or byte suffix is used
    when formatting or parsing byte arrays. Specifically:
      * `bytes.bytesPerLine``BytesHexFormat.bytesPerLine` is set to `Int.MAX_VALUE`.
      * `bytes.bytesPerGroup``BytesHexFormat.bytesPerGroup` is set to `Int.MAX_VALUE`.
      * `bytes.byteSeparator``BytesHexFormat.byteSeparator`, `bytes.bytePrefix``BytesHexFormat.bytePrefix`,
      and `bytes.byteSuffix``BytesHexFormat.byteSuffix` are empty strings.
    
    No prefix or suffix is used, and leading zeros are not removed from the hexadecimal representation
    when formatting or parsing numeric values. Specifically:
      * `number.prefix``NumberHexFormat.prefix` and `number.suffix``NumberHexFormat.suffix` are empty strings.
      * `number.removeLeadingZeros``NumberHexFormat.removeLeadingZeros` is set to `false`.

## 声明与重载

### 1. Common

```kotlin
public val Default: HexFormat
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L769)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.text.*

fun main() {
    val source = kotlin.text.HexFormat.Companion
    val result = source.`Default`
    println(result)
}
```

```text title="输出"
HexFormat(
    upperCase = false,
    bytes = BytesHexFormat(
        bytesPerLine = 2147483647,
        bytesPerGroup = 2147483647,
        groupSeparator = "  ",
        byteSeparator = "",
        bytePrefix = "",
        byteSuffix = ""
    ),
    number = NumberHexFormat(
        prefix = "",
        suffix = "",
        removeLeadingZeros = false,
        minLength = 1
    )
)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
