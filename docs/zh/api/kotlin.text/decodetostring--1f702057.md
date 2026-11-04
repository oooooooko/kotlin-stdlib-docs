# decodeToString

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在此数组中解码一个字节的字符串, 以 UTF-8 编码 。

替换的查尔`\uFFFD`,替换的字节序列是错误的。

??? note "查看英文原文"

    Decodes a string from the bytes in UTF-8 encoding in this array.
    
    Malformed byte sequences are replaced by the replacement char `\uFFFD`.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun ByteArray.decodeToString(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L322)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun ByteArray.decodeToString(
    startIndex: Int = 0,
    endIndex: Int = this.size,
    throwOnInvalidSequence: Boolean = false
): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L330)

在此数组或其子排列中解码此数组中的 UTF-8 编码字节字串的字符串。

@param 开始 Index 显示要解码的子序列的起始(包括) 0 默认值 。 @param endIndex 显示要解码的子序列的结尾(不包括) 。 @param 丢弃 OnInvalidSquartice 指定了对错误的字节序列实施例外, 或替换为 char `\uFFFD` 。

@throws 指数外在除外,如果`startIndex` 低于0或 `endIndex` 大于此阵列的大小。 @throws 非法证明除外,如果 `startIndex` 大于 `endIndex` . @throws 字符编码除外,如果字节阵列包含不正确的 UTF-8 字节序列, `throwOnInvalidSequence` 是真实的。

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
    val source = byteArrayOf(1, 2, 3)
    val result = source.`decodeToString`()
    println(result)
}
```

```text title="输出"

```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
