# Regex.matchAt

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

尝试匹配正则表达式, 精确匹配于 `input` 字符序列中指定的 `index` 。

与 `matchEntire` 函数不同, 它不需要匹配 以至 `input` 结束 。

@return 例 `MatchResult` 如果输入与8`Regex` 匹配, 则在指定的`index` 或 `null` 中进行。 @throws 索引外溢值除以`index` 低于0或大于 `input` 字符序列长度。 @sample 样本。 text. regexp. matchAt

??? note "查看英文原文"

    Attempts to match a regular expression exactly at the specified `index` in the `input` char sequence.
    
    Unlike `matchEntire` function, it doesn't require the match to span to the end of `input`.
    
    @return An instance of `MatchResult` if the input matches this `Regex` at the specified `index` or `null` otherwise.
    @throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of the `input` char sequence.
    @sample samples.text.Regexps.matchAt

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.7")
    public fun matchAt(input: CharSequence, index: Int): MatchResult?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L41)

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
    val result = source.`matchAt`("AQID", 0)
    println(result)
}
```

```text title="输出"
null
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
