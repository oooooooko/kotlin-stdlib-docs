# toDuration

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

a `Duration` 返回等于指定 `unit` 中的 `Int` 个数。

@sample 样本 时间 剂量 到 日产

??? note "查看英文原文"

    Returns a `Duration` equal to this `Int` number of the specified `unit`.
    
    @sample samples.time.Durations.toDurationInt

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
public fun Int.toDuration(unit: DurationUnit): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L965)

### 2. Common

```kotlin
@SinceKotlin("1.6")
public fun Long.toDuration(unit: DurationUnit): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L978)

a `Duration` 返回等于指定 `unit` 中的 `Long` 个数。

@sample 样本 时间 剂量 到 水下Long

### 3. Common

```kotlin
@SinceKotlin("1.6")
public fun Double.toDuration(unit: DurationUnit): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L998)

a `Duration` 返回等于指定 `unit` 中的 `Double` 个数。

值根据数值大小四舍五入到毫秒或毫秒的整数。

@throws 非法设备除外,如果这个`Double`值为 `NaN` 。

@sample 样本.时间. 剂量. 至剂量多用途

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    println(100.toDuration(DurationUnit.MILLISECONDS))
    println(60.toDuration(DurationUnit.SECONDS))
}
```

```text title="输出"
100ms
1m
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L255)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    println(1_000_000_000L.toDuration(DurationUnit.NANOSECONDS))
    println(Long.MAX_VALUE.toDuration(DurationUnit.DAYS))
}
```

```text title="输出"
1s
Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L261)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    println(1.5.toDuration(DurationUnit.HOURS))
    println(0.001.toDuration(DurationUnit.SECONDS))
}
```

```text title="输出"
1h 30m
1ms
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L267)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
