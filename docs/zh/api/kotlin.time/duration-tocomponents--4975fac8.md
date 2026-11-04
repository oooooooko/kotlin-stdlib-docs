# Duration.toComponents

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将这一时间段分为天数、小时、分钟、秒、纳米秒,并用这些组件执行给定的`action`。由于此函数的结果,`action`的结果被返回。

`nanoseconds`代表整个期间的纳米秒数,其绝对值低于1 000_000_000; - `seconds`代表整个期间的秒数,其绝对值低于60; - `minutes`代表整个期间的分钟数,其绝对值低于60; - `hours`代表整个期间的小时数,其绝对值低于24; - `days`代表整个期间的天数。

请注意, 转换中的一天总是 24 小时。 这与日历日不同, 当白天发生日光节省过渡时, 日历日可能长于或短于 24 小时 。

无限期的期间为 `Long.MAX_VALUE` 天或 `Long.MIN_VALUE` 天(取决于无限的标志),低级部分为零。

??? note "查看英文原文"

    Splits this duration into days, hours, minutes, seconds, and nanoseconds and executes the given `action` with these components.
    The result of `action` is returned as the result of this function.
    
    - `nanoseconds` represents the whole number of nanoseconds in this duration, and its absolute value is less than 1_000_000_000;
    - `seconds` represents the whole number of seconds in this duration, and its absolute value is less than 60;
    - `minutes` represents the whole number of minutes in this duration, and its absolute value is less than 60;
    - `hours` represents the whole number of hours in this duration, and its absolute value is less than 24;
    - `days` represents the whole number of days in this duration.
    
    Note that a day in this conversion always represents exactly 24 hours.
    This is different from calendar days which may be longer or shorter
    than 24 hours when a daylight saving transition happens on that day.
    
      Infinite durations are represented as either `Long.MAX_VALUE` days, or `Long.MIN_VALUE` days (depending on the sign of infinity),
      and zeroes in the lower components.

## 声明与重载

### 1. Common

```kotlin
public inline fun <T> toComponents(action: (days: Long, hours: Int, minutes: Int, seconds: Int, nanoseconds: Int) -> T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L553)

### 2. Common

```kotlin
public inline fun <T> toComponents(action: (hours: Long, minutes: Int, seconds: Int, nanoseconds: Int) -> T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L575)

将这一时间段分割为小时、分钟、秒、纳米秒,并用这些组件执行给定的`action`。由于此函数的结果,`action`的结果被返回。

`nanoseconds`代表整个期间的纳米秒数,其绝对值低于1 000_000_000; - `seconds`代表整个期间的秒数,其绝对值低于60; - `minutes`代表整个期间的分钟数,其绝对值低于60; - `hours`代表整个期间的小时数。

无限期的时数为 `Long.MAX_VALUE` 小时或 `Long.MIN_VALUE` 小时(视无限的标志而定),低级部分为零。

### 3. Common

```kotlin
public inline fun <T> toComponents(action: (minutes: Long, seconds: Int, nanoseconds: Int) -> T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L592)

将这一持续时间分割为分钟、秒和纳米秒,并用这些组件执行给定的`action`。由于此函数的结果,`action`的结果被返回。

- `nanoseconds`代表整个纳米秒,其绝对值低于1 000_000_000; - `seconds`代表整个秒,其绝对值低于60; - `minutes`代表整个分钟。

无限期的会期为 `Long.MAX_VALUE` 分钟或 `Long.MIN_VALUE` 分钟(视无限的标志而定),低级部分为零。

### 4. Common

```kotlin
public inline fun <T> toComponents(action: (seconds: Long, nanoseconds: Int) -> T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L608)

将此持续时间分割为秒, 纳米秒并用这些组件执行给定的 `action` 。 `action` 的结果会因此函数而返回 。

- `nanoseconds`代表整个纳米秒的这一时间段,其绝对值低于1 000_000_000_000; - `seconds`代表整个时间段的秒数。

无限持续时间代表为 `Long.MAX_VALUE` 秒或`Long.MIN_VALUE`秒(取决于无限的标志),零纳米秒。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.math.nextDown
import kotlin.math.pow
import kotlin.test.*
import kotlin.time.*
import kotlin.random.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds

private val units = DurationUnit.entries

fun main() {

        (36.hours + 90.minutes + 90.seconds + 1500.milliseconds).run {
            toComponents { days, hours, minutes, seconds, nanoseconds ->
                println(days)
                println(hours)
                println(minutes)
                println(seconds)
                println(nanoseconds)
            }
        }
    
}
```

```text title="输出"
1
13
31
31
500000000
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/time/DurationTest.kt#L282)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
