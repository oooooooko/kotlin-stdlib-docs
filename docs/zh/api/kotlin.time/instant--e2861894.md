# Instant

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

时间的一瞬间

时间点必须被指定为与时区无关的独特点。 例如, `1970-01-01, 00:00:00` 并不代表时间时刻, 因为这在不同的时间会发生在不同的时区: 东京的人会认为它比柏林的人提前几个小时已经存在 `1970-01-01` 。 要代表这些实体, 请使用 `kotlinx-datetime` 的 `LocalDateTime` 。 相反, “ 伦敦的时钟首次显示2000 年 月 1 日 00 00 00 时 时, 与 “ 1970-01- 01, 00: 00: 00 UTC+0 ” 一样, 时间是特定的时刻 。 因此, 它可以被代表为 `Instant` 时 。

`Instant` 使用UTC- SLS( 擦除跳跃第二) 时间尺度。 这个时间尺度不包含与跳秒相对应的速率, 而是在跳跃第二时的一天最后1000秒中“ 擦拭” 的正负跳秒 。

获得当前

`Clock` 接口是目前取得以下信息的主要途径:

```
val clock: Clock = Clock.System
val instant = clock.now()
```

`Clock.System`执行程序使用平台特定系统时钟来获取当前时间。 请注意, 无法保证这个时钟是单声道, 用户或系统可以随时调整它, 因此不应用于测量时间间隔 。 为此, 考虑使用 `TimeSource.Monotonic` 和 `TimeMark` 而不是 `Clock.System` 和 `Instant` 。

亚氏体

`plus` 和 `minus` 操作员可用来在 `Instant` 中增加`Duration`,并从`Instant`中减去:

```
Clock.System.now() + 5.seconds // 5 seconds from now
```

还有一个 `minus` 操作员 返回`Duration` 代表两秒之间的差数

```
val kotlinRelease = Instant.parse("2016-02-15T12:00:00+03:00")
val kotlinStableDuration = Clock.System.now() - kotlinRelease
```

平台特定

在联合核查团,有 `Instant.toJavaInstant()` 和 `java.time.Instant.toKotlinInstant()` 的延伸功能,用于将用于同一目的的物体从`kotlin.time`和 `java.time` 转换为`kotlin.time`和`java.time`,在联署材料上,也有`Instant.toJSDate()`和`Date.toKotlinInstant()`的延伸功能。

由于技术原因,`Instant`转换成或从基金会`NSDate`转换成或从Found Found Founds的`NSDate`的功能载于
经由`Instant.toNSDate()`和`NSDate.toKotlinInstant()`的`kotlinx-datetime`扩展功能。
这些功能将来可能在`kotlin.time`中提供。

建造、序列和分解

`fromEpochSeconds` 可用来从`1970-01-01T00:00:00Z`(Unixeeoch)以来的秒数中制造一个瞬间。 `epochSeconds`和`nanosecondsOfSecond`可用来获取自该时代以来的秒数和纳米秒数。

```
val instant = Instant.fromEpochSeconds(1709898983, 123456789)
instant.epochSeconds // 1709898983
instant.nanosecondsOfSecond // 123456789
```

`fromEpochMilliseconds` 允许从自此时起的毫秒数中抽出一秒。 `toEpochMilliseconds` 可用于获取自此时起的毫秒数。 请注意, `Instant` 支持纳米二分精确度, 因此转换为毫秒是一个损失操作 。

```
val instant1 = Instant.fromEpochSeconds(1709898983, 123456789)
instant1.nanosecondsOfSecond // 123456789
val milliseconds = instant1.toEpochMilliseconds() // 1709898983123
val instant2 = Instant.fromEpochMilliseconds(milliseconds)
instant2.nanosecondsOfSecond // 123000000
```

`parse`和 `toString` 方法可用来从[ISO 8601 扩展格式](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations),)中获取`Instant`,并将其转换成字符串,其中包括一个时区代号。

```
val instant = Instant.parse("2023-01-02T22:35:01+01:00")
instant.toString() // 2023-01-02T21:35:01Z
```

??? note "查看英文原文"

    A moment in time.
    
    A point in time must be uniquely identified in a way that is independent of a time zone.
    For example, `1970-01-01, 00:00:00` does not represent a moment in time since this would happen at different times
    in different time zones: someone in Tokyo would think it is already `1970-01-01` several hours earlier than someone
    in Berlin would. To represent such entities, use the `LocalDateTime` from `kotlinx-datetime`.
    In contrast, "the moment the clocks in London first showed 00:00 on Jan 1, 2000" is a specific moment
    in time, as is "1970-01-01, 00:00:00 UTC+0", so it can be represented as an `Instant`.
    
    `Instant` uses the UTC-SLS (smeared leap second) time scale. This time scale doesn't contain instants
    corresponding to leap seconds, but instead "smears" positive and negative leap seconds among the last 1000 seconds
    of the day when a leap second happens.
    
    ### Obtaining the current moment
    
    The `Clock` interface is the primary way to obtain the current moment:
    
    ```
    val clock: Clock = Clock.System
    val instant = clock.now()
    ```
    
    The `Clock.System` implementation uses the platform-specific system clock to obtain the current moment.
    Note that this clock is not guaranteed to be monotonic, and the user or the system may adjust it at any time,
    so it should not be used for measuring time intervals.
    For that, consider using `TimeSource.Monotonic` and `TimeMark` instead of `Clock.System` and `Instant`.
    
    ### Arithmetic operations
    
    The `plus` and `minus` operators can be used to add `Duration`s to and subtract them from an `Instant`:
    
    ```
    Clock.System.now() + 5.seconds // 5 seconds from now
    ```
    
    Also, there is a `minus` operator that returns the `Duration` representing the difference between two instants:
    
    ```
    val kotlinRelease = Instant.parse("2016-02-15T12:00:00+03:00")
    val kotlinStableDuration = Clock.System.now() - kotlinRelease
    ```
    
    ### Platform specifics
    
    On the JVM, there are `Instant.toJavaInstant()` and `java.time.Instant.toKotlinInstant()`
    extension functions to convert between `kotlin.time` and `java.time` objects used for the same purpose.
    Likewise, on JS, there are `Instant.toJSDate()` and `Date.toKotlinInstant()` extension functions.
    
    For technical reasons, converting `Instant` to and from Foundation's `NSDate` is provided in
    `kotlinx-datetime` via `Instant.toNSDate()` and `NSDate.toKotlinInstant()` extension functions.
    These functions might become available in `kotlin.time` in the future.
    
    ### Construction, serialization, and deserialization
    
    `fromEpochSeconds` can be used to construct an instant from the number of seconds since
    `1970-01-01T00:00:00Z` (the Unix epoch).
    `epochSeconds` and `nanosecondsOfSecond` can be used to obtain the number of seconds and nanoseconds since the epoch.
    
    ```
    val instant = Instant.fromEpochSeconds(1709898983, 123456789)
    instant.epochSeconds // 1709898983
    instant.nanosecondsOfSecond // 123456789
    ```
    
    `fromEpochMilliseconds` allows constructing an instant from the number of milliseconds since the epoch.
    `toEpochMilliseconds` can be used to obtain the number of milliseconds since the epoch.
    Note that `Instant` supports nanosecond precision, so converting to milliseconds is a lossy operation.
    
    ```
    val instant1 = Instant.fromEpochSeconds(1709898983, 123456789)
    instant1.nanosecondsOfSecond // 123456789
    val milliseconds = instant1.toEpochMilliseconds() // 1709898983123
    val instant2 = Instant.fromEpochMilliseconds(milliseconds)
    instant2.nanosecondsOfSecond // 123000000
    ```
    
    `parse` and `toString` methods can be used to obtain an `Instant` from and convert it to a string in the
    [ISO 8601 extended format](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations),
    which includes a time zone designator.
    
    ```
    val instant = Instant.parse("2023-01-02T22:35:01+01:00")
    instant.toString() // 2023-01-02T21:35:01Z
    ```

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.3")
@WasExperimental(ExperimentalTime::class)
public class Instant internal constructor(
    /**
     * The number of seconds from the epoch instant `1970-01-01T00:00:00Z` rounded down to a [Long] number.
     *
     * The difference between the rounded number of seconds and the actual number of seconds
     * is returned by [nanosecondsOfSecond] property expressed in nanoseconds.
     *
     * Note that this number doesn't include leap seconds added or removed since the epoch.
     *
     * @see fromEpochSeconds
     * @sample samples.time.Instants.epochSecondsAndNanosecondsOfSecond
     * @sample samples.time.Instants.fromEpochSecondsProperties
     */
    public val epochSeconds: Long,
    /**
     * The number of nanoseconds by which this instant is later than [epochSeconds] from the epoch instant.
     *
     * The value is always non-negative and lies in the range `0..999_999_999`.
     *
     * @see fromEpochSeconds
     * @sample samples.time.Instants.epochSecondsAndNanosecondsOfSecond
     * @sample samples.time.Instants.fromEpochSecondsProperties
     */
    public val nanosecondsOfSecond: Int
) : Comparable<Instant>, Serializable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L19)

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
    val value = Instant.fromEpochMilliseconds(0)
    println(value)
}
```

```text title="输出"
1970-01-01T00:00:00Z
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
