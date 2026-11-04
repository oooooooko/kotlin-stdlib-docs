# Regex.findAll

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 `input` 字符串内正则表达式的所有发生序列, 以指定的 `startIndex` 开始 。

@throws 指数外溢值,如果 `startIndex` 低于零或大于 `input` 字符序列的长度,则除外。

@sample 样本. text. regexpex. finded all

??? note "查看英文原文"

    Returns a sequence of all occurrences of a regular expression within the `input` string, beginning at the specified `startIndex`.
    
    @throws IndexOutOfBoundsException if `startIndex` is less than zero or greater than the length of the `input` char sequence.
    
    @sample samples.text.Regexps.findAll

## 声明与重载

### 1. Common

```kotlin
public fun findAll(input: CharSequence, startIndex: Int = 0): Sequence<MatchResult>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L132)

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
    val result = source.`findAll`("AQID")
    println(result.toList())
}
```

```text title="输出"
[]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
