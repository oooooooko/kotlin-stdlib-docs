# MatchGroup

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

代表 `Regex` `MatchResult`中单个捕捉组的结果。

特定平台上的Not`MatchGroup`也可以提供`range`输入中显示群体匹配发生的位置。具体平台的详情请参见`MatchGroup`的文档。

@property 值 被俘团体的价值

??? note "查看英文原文"

    Represents the results from a single capturing group within a `MatchResult` of `Regex`.
    
    Note `MatchGroup` on particular platforms can also provide the `range` in the input
    where the group match has happened.
    See the docs of `MatchGroup` for the specific platform for details.
    
    @property value The value of captured group.

## 声明与重载

### 1. Common

```kotlin
public expect class MatchGroup
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L198)

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
    val value = MatchGroup("hello", 0..4)
    println(value)
}
```

```text title="输出"
MatchGroup(value=hello, range=0..4)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
