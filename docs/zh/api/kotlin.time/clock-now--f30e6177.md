# Clock.now

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 `Instant` 。

稍后拨打`now`,但不能保证返回更大的`Instant`。
特别是,对于`Clock.System`,完全预期相反的情况,
必须考虑到这一点。
详情请见 `System` 文档。

尽管`Instant`被界定为按UTC-SLS时间尺度,即以具体方式处理跳秒,但不能保证`now`以任何具体方式处理跳秒。

请注意,`Instant`支持纳米第二精确度,而返回的`Instant`的实际精确度取决于`Clock`执行的解决。

@sample 样本. 时间. 时. 时. 系统 @sample 样本. 时. 时. 时. 依赖性

??? note "查看英文原文"

    Returns the `Instant` corresponding to the current time, according to this clock.
    
    Calling `now` later is not guaranteed to return a larger `Instant`.
    In particular, for `Clock.System`, the opposite is completely expected,
    and it must be taken into account.
    See the `System` documentation for details.
    
    Even though `Instant` is defined to be on the UTC-SLS time scale, which enforces a specific way of handling
    leap seconds, `now` is not guaranteed to handle leap seconds in any specific way.
    
    Note that while `Instant` supports nanosecond precision,
    the actual precision of the returned `Instant` depends on the resolution of the `Clock` implementation.
    
    @sample samples.time.Clocks.system
    @sample samples.time.Clocks.dependencyInjection

## 声明与重载

### 1. Common

```kotlin
public fun now(): Instant
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Clock.kt#L21)

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
