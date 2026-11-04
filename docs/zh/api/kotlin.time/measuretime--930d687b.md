# measureTime

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

执行给定的函数 `block`, 并返回已过时间间隔的长度 。

时间的长短用`TimeSource.Monotonic`测量,这是平台上最精确的可用时间来源。

@sample 样本 时间 测量时间 测量时间抽样

??? note "查看英文原文"

    Executes the given function `block` and returns the duration of the elapsed time interval.
    
    The elapsed time is measured with `TimeSource.Monotonic` which is the most precise
    available time source on the platform.
    
    @sample samples.time.MeasureTime.measureTimeSample

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalTime::class)
public inline fun measureTime(block: () -> Unit): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/measureTime.kt#L10)

### 2. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalTime::class)
public inline fun TimeSource.measureTime(block: () -> Unit): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/measureTime.kt#L28)

执行给定的函数 `block`, 并返回已过时间间隔的长度 。

时间长短用规定的 `this` `TimeSource` 实例来测量。

@sample 样本 时间 测量时间 清晰测量时间抽样

### 3. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalTime::class)
public inline fun TimeSource.Monotonic.measureTime(block: () -> Unit): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/measureTime.kt#L47)

执行给定的函数 `block`, 并返回已过时间间隔的长度 。

时间的长短用指定的 `this` `TimeSource.Monotonic` 实例来测量。 明确实例允许使用非框版的 `TimeSource.Monotonic.ValueTimeMark` , 并且可以选择, 更明确地表达意图 。

@sample 样本 时间 计量时间 调制测量时间

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
    val result = `measureTime`({ println("called") })
    println(result)
}
```

```text title="输出"
called
492.917us
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
