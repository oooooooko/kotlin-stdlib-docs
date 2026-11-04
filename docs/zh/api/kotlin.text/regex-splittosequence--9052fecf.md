# Regex.splitToSequence

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将 `input` 字符序列拆分为串序列, 围绕此正则表达式的匹配 。

生成序列的最后一个元素对应于在上次匹配(或者在没有匹配的情况下在 `input` 字符序列的起始点)之后开始的 `input` 结束的`input`次序列。 这意味着如果 `input` 中不包含与 8,0000005 常规表达式匹配的子序列, 则该序列将包含一个与整个8,00000006 序列相对应的单个元素。 它还意味着对于以 `this` 常规表达式匹配结束的字符序列, 其产生的序列将用空字符串结束 。

@param 限制 非负值, 指定字符串可分割为最大子字符串数。 默认为零, 表示没有设定限制 。 @sample 样本. text. regexpts. plit. plit.

??? note "查看英文原文"

    Splits the `input` CharSequence to a sequence of strings around matches of this regular expression.
    
    The last element of the resulting sequence corresponds to an `input` subsequence starting right
    after the last match (or at the beginning of `input` char sequence if there were no matches)
    and ending at the end of `input`. That implies that if `input` does not contain subsequences
    matching `this` regular expression, the resulting sequence will contain a single element
    corresponding to the whole `input` sequence.
    It also implies that for char sequences ending with a `this` regular expression match,
    the resulting sequence will end with an empty string.
    
    @param limit Non-negative value specifying the maximum number of substrings the string can be split to.
    Zero by default means no limit is set.
    @sample samples.text.Regexps.splitToSequence

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
    public fun splitToSequence(input: CharSequence, limit: Int = 0): Sequence<String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L159)

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
    val result = source.`splitToSequence`("AQID")
    println(result.toList())
}
```

```text title="输出"
[AQID]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
