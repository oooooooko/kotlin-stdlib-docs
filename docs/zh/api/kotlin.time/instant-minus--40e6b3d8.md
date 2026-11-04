# Instant.minus

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个瞬时,即从此时减去指定的`duration`。

如果`duration`是正数,则返回的瞬时比此时早。如果`duration`是负数,则返回的瞬时晚于此时。

如果结果超过 `Instant` 的边界,则将返回值固定在`Instant`的边界上。

**`Duration.Companion.days`是24小时的倍数,但在一些时区,由于时钟的变换,有些日数可能更短或更长。考虑在算术操作中使用`kotlinx-datetime`,将时区过渡考虑在内。

@sample 样本的采样时间。

??? note "查看英文原文"

    Returns an instant that is the result of subtracting the specified `duration` from this instant.
    
    If the `duration` is positive, the returned instant is earlier than this instant.
    If the `duration` is negative, the returned instant is later than this instant.
    
    The return value is clamped to the boundaries of `Instant` if the result exceeds them.
    
    **Pitfall**: `Duration.Companion.days` are multiples of 24 hours, but in some time zones,
    some days can be shorter or longer because clocks are shifted.
    Consider using `kotlinx-datetime` for arithmetic operations that take time zone transitions into account.
    
    @sample samples.time.Instants.minusDuration

## 声明与重载

### 1. Common

```kotlin
public operator fun minus(duration: Duration): Instant
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L196)

### 2. Common

```kotlin
public operator fun minus(other: Instant): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L212)

返回`Duration`, 即`other`和`this`之间的两秒间。

如果返回的时间比另一个晚,则返回的时间为正数,如果返回的时间比另一个早,则返回的时间为负数。

其结果从未被夹住, 但请注意, 对于相距甚远的瞬时, 返回的值可能由于精确度的丧失而不确切地代表它们之间的持续时间 。

请注意,`Instant`值的来源(特别是`Clock`)不能保证相互同步,甚至不能保证单声波同步,因此,即使另一个瞬时比这个时晚,或者相反,这一操作的结果也可能是负的。 为了测量时间间隔,请考虑使用 `TimeSource.Monotonic` 。

@sample 样本的采样时间

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Finding a moment that's earlier than the starting point by the given amount of real time
    val instant = Instant.fromEpochSeconds(7 * 60 * 60, nanosecondAdjustment = 123_456_789)
    val fiveHoursEarlier = instant - 5.hours
    println(fiveHoursEarlier.epochSeconds == 2 * 60 * 60L)
    println(fiveHoursEarlier.nanosecondsOfSecond == 123_456_789)
}
```

```text title="输出"
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L74)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Finding the difference between two instants in terms of elapsed time
    val instant1 = Instant.fromEpochSeconds(0) // The Unix epoch start.
    val instant2 = Instant.fromEpochSeconds(7 * 60 * 60) // 7 hours since the Unix epoch.
    val elapsedTime = instant1 - instant2 // The duration between instant1 and instant2.
    println(elapsedTime == (-7).hours)
}
```

```text title="输出"
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L83)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
