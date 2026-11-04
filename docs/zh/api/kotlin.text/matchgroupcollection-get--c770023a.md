# MatchGroupCollection.get

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回指定 `index` 的组。

@return举例说,`MatchGroup`如果该组与指定`index`匹配或匹配`null`否则。

组合从 1 索引到正则表达式中的组数。一个有索引 0 的组与整个匹配对应。

??? note "查看英文原文"

    Returns a group with the specified `index`.
    
    @return An instance of `MatchGroup` if the group with the specified `index` was matched or `null` otherwise.
    
    Groups are indexed from 1 to the count of groups in the regular expression. A group with the index 0
    corresponds to the entire match.

## 声明与重载

### 1. Common

```kotlin
public operator fun get(index: Int): MatchGroup?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/regex/MatchResult.kt#L20)

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
    val source = Regex("([a-z]+)").find("hello")!!.groups
    val result = source.`get`(0)
    println(result)
}
```

```text title="输出"
MatchGroup(value=hello, range=0..4)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
