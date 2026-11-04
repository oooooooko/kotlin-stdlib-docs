# HexFormat.Companion.UpperCase

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

配置了十六进制格式选项, 以使用大写十六进制数字 。

此 `HexFormat` 实例对所有格式选项采用默认值, 除了 `upperCase`,
设定为 `true`。 因此,格式化功能将使用大写十六进制数字
(`0-9`, `A-F`) 用于字节数组和数值。

在所有其他方面,这一格式与`Default`格式相同。

??? note "查看英文原文"

    The hexadecimal format options configured to use upper-case hexadecimal digits.
    
    This `HexFormat` instance adopts default values for all format options, except for `upperCase`,
    which is set to `true`. As a result, formatting functions will use upper-case hexadecimal digits
    (`0-9`, `A-F`) for both byte arrays and numeric values.
    
    In all other aspects, this format is identical to the `Default` format.

## 声明与重载

### 1. Common

```kotlin
public val UpperCase: HexFormat
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L795)

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
    val result = source.`UpperCase`
    println(result)
}
```

```text title="输出"
HexFormat(
    upperCase = true,
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
