# lastIndexOfAny

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在此字符序列中查找所指定的 `chars` 中任何一次最后发生的索引,从指定的 `startIndex` 开始,可选择忽略此选项。

@param 开头 Index 字符索引 。 搜索向下向后向到字符串的起始处 。 @param 忽略Case `true` , 以忽略字符在匹配字符时的字符 。 默认为 `false` 。 @return 。 上次匹配字符的索引为 8,0000006 或 - 1, 如果找不到 `chars` , 则从 8,0000006 或 - 1 。

??? note "查看英文原文"

    Finds the index of the last occurrence of any of the specified `chars` in this char sequence,
    starting from the specified `startIndex` and optionally ignoring the case.
    
    @param startIndex The index of character to start searching at. The search proceeds backward toward the beginning of the string.
    @param ignoreCase `true` to ignore character case when matching a character. By default `false`.
    @return An index of the last occurrence of matched character from `chars` or -1 if none of `chars` are found.

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.lastIndexOfAny(chars: CharArray, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L990)

### 2. Common

```kotlin
public fun CharSequence.lastIndexOfAny(strings: Collection<String>, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1106)

在此字符序列中查找所指定的 `strings` 中任何一次最后发生的索引,从指定的 `startIndex` 开始,可选择忽略此选项。

为了避免在`strings` 字符串中字符共的模糊结果, 这种方法从此字符串的结尾开始, 在每个位置上都发现 `strings` 中的第一个元素与该字符串相同 。

@param 开头 Index 字符索引 。 搜索向下向下向弦起始处进行 。 @param 忽略Case `true` , 以忽略字符串匹配时的字符 。 默认为 `false` 。 @return 。 默认为 `strings` 。 @return 是一个匹配字符串最后一次出现的索引, 从 8,0000006 或 - 1 , 如果找不到 `strings` 。

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
    val source = "kotlin"
    val result = source.`lastIndexOfAny`(charArrayOf('a', 'b', 'c'))
    println(result)
}
```

```text title="输出"
-1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
