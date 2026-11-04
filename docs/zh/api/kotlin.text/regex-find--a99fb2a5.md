# Regex.find

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 `input` 中正则表达式的第一个匹配,从指定的 `startIndex` 开始。

@param 启动 Index 索引 以默认 0 开始搜索 。 不得小于零,且不超过`input.length()`
@return举例说,`MatchResult`如果找到匹配, 或`null`否则。
@throws 指数外溢值,但`startIndex`小于零或大于`input`字符序列长度的除外。
@sample 样本. text. regexprises. finded

??? note "查看英文原文"

    Returns the first match of a regular expression in the `input`, beginning at the specified `startIndex`.
    
    @param startIndex An index to start search with, by default 0. Must be not less than zero and not greater than `input.length()`
    @return An instance of `MatchResult` if match was found or `null` otherwise.
    @throws IndexOutOfBoundsException if `startIndex` is less than zero or greater than the length of the `input` char sequence.
    @sample samples.text.Regexps.find

## 声明与重载

### 1. Common

```kotlin
public fun find(input: CharSequence, startIndex: Int = 0): MatchResult?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L122)

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
    val result = source.`find`("AQID")
    println(result)
}
```

```text title="输出"
null
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
