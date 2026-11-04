# TimeSource.Monotonic

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

平台上最精确的时间来源。

当目标平台上有单声波时间源时,此时间源返回其读数, 并使用非声波时间源。

此时间源的`markNow`函数返回专门值 `ValueTimeMark`, 即嵌入值分类, 包嵌平台上依赖时间读取值 。

??? note "查看英文原文"

    The most precise time source available in the platform.
    
    This time source returns its readings from a source of monotonic time when it is available in a target platform,
    and resorts to a non-monotonic time source otherwise.
    
    The function `markNow` of this time source returns the specialized `ValueTimeMark` that is an inline value class
    wrapping a platform-dependent time reading value.

## 声明与重载

### 1. Common

```kotlin
public object Monotonic : TimeSource.WithComparableMarks
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L42)

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
    val value = kotlin.time.TimeSource.Monotonic
    println(value)
}
```

```text title="输出"
TimeSource(System.nanoTime())
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
