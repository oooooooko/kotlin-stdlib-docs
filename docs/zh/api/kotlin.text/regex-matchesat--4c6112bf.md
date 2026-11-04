# Regex.matchesAt

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查正则表达式是否与指定的 `input` 字符序列中与指定的 `index` 字符序列完全匹配的一部分。

与 `matches` 函数不同, 它不需要匹配 以至 `input` 结束 。

@throws 指数外溢值,如果 `index` 低于零或大于 `input` 字符序列的长度。 @sample 样本.text.regexpexs.matchesAt,则例外。

??? note "查看英文原文"

    Checks if a regular expression matches a part of the specified `input` char sequence
    exactly at the specified `index`.
    
    Unlike `matches` function, it doesn't require the match to span to the end of `input`.
    
    @throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of the `input` char sequence.
    @sample samples.text.Regexps.matchesAt

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.7")
    @WasExperimental(ExperimentalStdlibApi::class)
    public fun matchesAt(input: CharSequence, index: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L53)

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
    val source = Regex("[a-z]+")
    val result = source.`matchesAt`("AQID", 0)
    println(result)
}
```

```text title="输出"
false
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
