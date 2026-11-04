# Instant.epochSeconds

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

时间从`1970-01-01T00:00:00Z`号时钟 开始 倒数到`Long`秒

以纳米秒表示的`nanosecondsOfSecond`属性返回四舍五入秒数和实际秒数之间的差额。

请注意,这个数字不包括自这个时代以来 所增加或删除的跳秒。

@see 来自Epoch seconds @sample 样本.时间。 Instants. ofcents and Nano seconds occ seconds @sample 样本.时间。 Instants. from Epoch seconds properies.

??? note "查看英文原文"

    The number of seconds from the epoch instant `1970-01-01T00:00:00Z` rounded down to a `Long` number.
    
    The difference between the rounded number of seconds and the actual number of seconds
    is returned by `nanosecondsOfSecond` property expressed in nanoseconds.
    
    Note that this number doesn't include leap seconds added or removed since the epoch.
    
    @see fromEpochSeconds
    @sample samples.time.Instants.epochSecondsAndNanosecondsOfSecond
    @sample samples.time.Instants.fromEpochSecondsProperties

## 声明与重载

### 1. Common

```kotlin
public val epochSeconds: Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L108)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    val currentInstant = Clock.System.now()
    // The number of whole seconds that have passed since the Unix epoch.
    println(currentInstant.epochSeconds)
    // The number of nanoseconds that passed since the start of the second.
    println(currentInstant.nanosecondsOfSecond)
}
```

```text title="输出"
1793758576
426344000
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L17)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // When nanosecondAdjustment is within the range `0..999_999_999`,
    // epochSeconds and nanosecondsOfSecond hold the exact values provided.
    val instant1 = Instant.fromEpochSeconds(999_999, nanosecondAdjustment = 123_456_789)
    println(instant1.epochSeconds)
    println(instant1.nanosecondsOfSecond)

    // When nanosecondAdjustment exceeds `999_999_999`, the excess contributes to whole seconds,
    // increasing epochSeconds. The remainder forms the new value of nanosecondsOfSecond.
    val instant2 = Instant.fromEpochSeconds(1_000_000, nanosecondAdjustment = 100_123_456_789)
    println(instant2.epochSeconds)
    println(instant2.nanosecondsOfSecond)

    // When nanosecondAdjustment is negative, epochSeconds is decreased
    // to offset the negative nanoseconds and ensure nanosecondsOfSecond remains non-negative.
    val instant3 = Instant.fromEpochSeconds(1_000_000, nanosecondAdjustment = -100_876_543_211)
    println(instant3.epochSeconds)
    println(instant3.nanosecondsOfSecond)
}
```

```text title="输出"
999999
123456789
1000100
123456789
999899
123456789
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L26)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
