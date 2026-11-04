# Clock.System

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

`Clock`例,查询特定平台的系统时钟作为时间知识的来源。

连续拨打`now`不一定会回升`Instant`的值,当呼唤回`Instant`的值,这些增加不一定与过去的时间相符。

例如,使用`Clock.System`时,可以出现以下情况: - `now`返回`2023-01-02T22:35:01Z`。 - 该系统查询互联网,并承认其时钟需要调整。 - `now` 返回`2023-01-02T22:32:05Z`。

当您需要连续测量之间的可预测间隔时,请考虑使用 `TimeSource.Monotonic` 。

为提高测试能力,您应避免直接使用 `Clock.System` 来实施,而是明确通过`Clock`,例如:

@sample 样本. 时间. 时. 时. 系统 @sample 样本. 时. 时. 时. 依赖性

??? note "查看英文原文"

    The `Clock` instance that queries the platform-specific system clock as its source of time knowledge.
    
    Successive calls to `now` will not necessarily return increasing `Instant` values, and when they do,
    these increases will not necessarily correspond to the elapsed time.
    
    For example, when using `Clock.System`, the following could happen:
    - `now` returns `2023-01-02T22:35:01Z`.
    - The system queries the Internet and recognizes that its clock needs adjusting.
    - `now` returns `2023-01-02T22:32:05Z`.
    
    When you need predictable intervals between successive measurements, consider using `TimeSource.Monotonic`.
    
    For improved testability, you should avoid using `Clock.System` directly in the implementation
    and pass a `Clock` explicitly instead. For example:
    
    @sample samples.time.Clocks.system
    @sample samples.time.Clocks.dependencyInjection

## 声明与重载

### 1. Common

```kotlin
public object System : Clock
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Clock.kt#L40)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds



fun main() {
    // The current instant according to the system clock.
    val currentInstant = Clock.System.now()
    // The number of whole milliseconds that have passed since the Unix epoch.
    println(currentInstant.toEpochMilliseconds())
}
```

```text title="输出"
1793758575430
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/clocks.kt#L13)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds



fun main() {
    fun formatCurrentTime(clock: Clock): String =
        clock.now().toString()

    // In the production code:
    val currentTimeInProduction = formatCurrentTime(Clock.System)
    // Testing this value is tricky because it changes all the time.
    println(currentTimeInProduction)

    // In the test code:
    val testClock = object : Clock {
        override fun now(): Instant = Instant.parse("2023-01-02T22:35:01Z")
    }
    // Then, one can write a completely deterministic test:
    val currentTimeForTests = formatCurrentTime(testClock)
    println(currentTimeForTests)
}
```

```text title="输出"
2026-11-04T02:16:15.469505Z
2023-01-02T22:35:01Z
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/clocks.kt#L21)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
