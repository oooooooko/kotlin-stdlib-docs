# Instant.toEpochMilliseconds

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回从时速 `1970-01-01T00:00:00Z` 返回毫秒数。

毫秒的任何部分均四舍五入为零,整秒数为毫秒数。

如果结果不符合`Long`,则返回`Long.MAX_VALUE`,结果正数,返回`Long.MAX_VALUE`,结果负数,返回`Long.MIN_VALUE`。

@see,来自Epoch-Millin秒 @sample 样本.时间。

??? note "查看英文原文"

    Returns the number of milliseconds from the epoch instant `1970-01-01T00:00:00Z`.
    
    Any fractional part of a millisecond is rounded toward zero to the whole number of milliseconds.
    
    If the result does not fit in `Long`,
    returns `Long.MAX_VALUE` for a positive result or `Long.MIN_VALUE` for a negative result.
    
    @see fromEpochMilliseconds
    @sample samples.time.Instants.toEpochMilliseconds

## 声明与重载

### 1. Common

```kotlin
public fun toEpochMilliseconds(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L137)

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
    // The number of whole milliseconds that have passed since the Unix epoch.
    println(currentInstant.toEpochMilliseconds())

    // When an Instant is created with fromEpochMilliseconds,
    // toEpochMilliseconds will return the exact value provided.
    val instant1 = Instant.fromEpochMilliseconds(0)
    println(instant1.toEpochMilliseconds())
    val instant2 = Instant.fromEpochMilliseconds(1_000_000_000_123)
    println(instant2.toEpochMilliseconds())

    // Any fractional part of a millisecond is rounded toward zero to the whole number of milliseconds.
    val instant3 = Instant.fromEpochSeconds(1_000_000_000, nanosecondAdjustment = 123_999_999)
    println(instant3.toEpochMilliseconds())
}
```

```text title="输出"
1793758576454
0
1000000000123
1000000000123
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L47)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
