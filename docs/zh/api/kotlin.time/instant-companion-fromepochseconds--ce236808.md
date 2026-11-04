# Instant.Companion.fromEpochSeconds

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回`Instant`,也就是`1970-01-01T00:00:00Z` 秒数 从`1970-01-01T00:00:00Z`时起的`epochSeconds`秒数 和`nanosecondAdjustment`纳米秒数的`nanosecondAdjustment`秒数。

`nanosecondAdjustment` 描述给定的瞬间比仅 `epochSeconds` 定义的时数要晚多少纳米秒。 为了方便和灵活起见, `fromEpochSeconds` 接受 `nanosecondAdjustment` 值, 范围在 `Instant.nanosecondsOfSecond` 范围之外。 负 `nanosecondAdjustment` 意味着给定的时数会比 仅 `epochSeconds` 定义的时数要早, 超过一秒的值将会促成结果的秒数 。

例如,如果`nanosecondAdjustment`是`-1`,则由此得出的`Instant`将比`nanosecondAdjustment`是`0`早`1`纳米秒,如果是`1_000_000_000`,则`Instant`将是`1`第二。

如果结果超过 `Instant` 的边界,则将返回值固定在`Instant`的边界上,无论如何,保证`DISTANT_PAST`至`DISTANT_FUTURE`的秒数可以代表。

`fromEpochMilliseconds`对于输入数据只有毫秒精确度时,则具有类似的功能。

@see 瞬间 瞬间 瞬间 瞬间 秒数 秒数 秒数 秒数 八万万003 样本数 时间. Instants. from Epoch seconds @sample 样本数.时间. instants. from Epoch seconds properies.time. instants. from Epoch seconds properies. intots.

??? note "查看英文原文"

    Returns an `Instant` that is the `epochSeconds` number of seconds from the epoch instant `1970-01-01T00:00:00Z`
    and the `nanosecondAdjustment` number of nanoseconds.
    
    `nanosecondAdjustment` describes how many nanoseconds the given instant is later than the one defined by just `epochSeconds`.
    For convenience and flexibility, `fromEpochSeconds` accepts `nanosecondAdjustment` values outside
    of `Instant.nanosecondsOfSecond` range. Negative `nanosecondAdjustment` means that the given instant will be earlier than
    the one defined by just `epochSeconds`, and values greater than a second will contribute to the resulting number of seconds.
    
    For example, if `nanosecondAdjustment` is `-1`, the resulting `Instant` will be `1` nanosecond earlier than
    if `nanosecondAdjustment` was `0`, and if it is `1_000_000_000`, the resulting `Instant` will be `1` second later.
    
    The return value is clamped to the boundaries of `Instant` if the result exceeds them.
    In any case, it is guaranteed that instants between `DISTANT_PAST` and `DISTANT_FUTURE` can be represented.
    
    `fromEpochMilliseconds` is a similar function for when input data only has millisecond precision.
    
    @see Instant.epochSeconds
    @see Instant.nanosecondsOfSecond
    @sample samples.time.Instants.fromEpochSeconds
    @sample samples.time.Instants.fromEpochSecondsProperties

## 声明与重载

### 1. Common

```kotlin
public fun fromEpochSeconds(epochSeconds: Long, nanosecondAdjustment: Long = 0): Instant
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L297)

### 2. Common

```kotlin
public fun fromEpochSeconds(epochSeconds: Long, nanosecondAdjustment: Int): Instant
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L333)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Creating an Instant representing the Unix epoch.
    val unixEpochInstant = Instant.fromEpochSeconds(0)
    // Creating an Instant from a specific number of milliseconds and nanoseconds since the Unix epoch.
    val instant = Instant.fromEpochSeconds(999_999_999, nanosecondAdjustment = 999_999_999)

    // The string representation of the constructed instants.
    println(unixEpochInstant)
    println(instant)

    // Creating an Instant with negative nanosecondAdjustment
    val earlierInstant = Instant.fromEpochSeconds(999_999_999, nanosecondAdjustment = -999_999_999)
    println(earlierInstant)
    println(earlierInstant < instant)

    // Creating an Instant with nanosecondAdjustment > 1s
    val laterInstant = Instant.fromEpochSeconds(999_999_999, nanosecondAdjustment = 1_999_999_999)
    println(laterInstant)
    println(laterInstant > instant)
}
```

```text title="输出"
1970-01-01T00:00:00Z
2001-09-09T01:46:39.999999999Z
2001-09-09T01:46:38.000000001Z
true
2001-09-09T01:46:40.999999999Z
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L132)

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
