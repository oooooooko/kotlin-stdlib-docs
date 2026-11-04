# ComparableTimeMark.minus

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回`other`时间标记与`this`时间标记之间的时间间隔。

如果时间标记距离彼此遥远,结果不等于 `Duration` 类型,或者如果一个时间标记无限遥远,或者如果`this`和`other`时间标记在时间尺度的对面是无限遥远的,则返回的时间长度可以是无限的。

在同一时间尺度的同一侧,两个无限遥远的时间标记被认为是相等的,它们之间的时间长度为 `Duration.ZERO` 。

请注意,另一个时间标记必须从与此相同的时间源获取。

@throws 非法辩护,如果从不同时间来源获得时间标记,则例外。

??? note "查看英文原文"

    Returns the duration elapsed between the `other` time mark and `this` time mark.
    
    The returned duration can be infinite if the time marks are far away from each other and
    the result doesn't fit into `Duration` type,
    or if one time mark is infinitely distant, or if both `this` and `other` time marks
    lie infinitely distant on the opposite sides of the time scale.
    
    Two infinitely distant time marks on the same side of the time scale are considered equal and
    the duration between them is `Duration.ZERO`.
    
    Note that the other time mark must be obtained from the same time source as this one.
    
    @throws IllegalArgumentException if time marks were obtained from different time sources.

## 声明与重载

### 1. Common

```kotlin
public open override operator fun minus(duration: Duration): ComparableTimeMark
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L204)

### 2. Common

```kotlin
public operator fun minus(other: ComparableTimeMark): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L206)

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
import kotlin.time.*

fun main() {
    val source = TimeSource.Monotonic.markNow()
    val result = source.`minus`(2.seconds)
    println(result)
}
```

```text title="输出"
ValueTimeMark(reading=-1999987959)
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
