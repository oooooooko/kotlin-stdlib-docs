# readlnOrNull

`kotlin.io` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

读取标准输入流的一行输入并返回,或者如果在拨打 `readlnOrNull` 时EOF 已经到达,则返回 `null` 。

LF或CRLF被视为线终止者。 线终止者不包括在返回的字符串中。

目前,Kotlin/JS和Kotlin/WasmJS都不支持这一功能,并投`UnsupportedOperationException`。

??? note "查看英文原文"

    Reads a line of input from the standard input stream and returns it,
    or return `null` if EOF has already been reached when `readlnOrNull` is called.
    
    LF or CRLF is treated as the line terminator. Line terminator is not included in the returned string.
    
    Currently this function is not supported in Kotlin/JS and in Kotlin/WasmJS, and throws `UnsupportedOperationException`.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
public expect fun readlnOrNull(): String?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/ioH.kt#L29)

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
import kotlin.io.*

fun main() {
    val result = `readlnOrNull`()
    println(result)
}
```

```text title="输出"
null
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
