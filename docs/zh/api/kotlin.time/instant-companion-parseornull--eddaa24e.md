# Instant.Companion.parseOrNull

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

剖析代表瞬时的 ISO 8601 字符串( 例如 `2020-08-30T18:43:00Z`) , 如果无法解析字符串或超过 `Instant` 的边界, 则返回 `null` 。

保证分析所有`Instant.toString`生产的所有线条

ISO 8601 格式的当量实例: - `2020-08-30T18:43:00Z`- `2020-08-30T18:43:00.50Z` - `2020-08-30T18:43:00.123456789Z` - `2020-08-30T18:43:00.123456789Z` - `2020-08-30T18:40:00+03:00` - `2020-08-30T18:40:00+03:00` - `2020-08-30T18:40:00+03:30:20` * `2020-01-01T23:59:59.123456789+01` * `2020-01-01T23:59:59.123456789+01` * `+12020-01-31T23:59:59Z`

见ISO-8601-11:2019,5.4.2.1b),不包括没有冲抵的格式。

字符串被视为代表UTC- SLS时间尺度上的时间, 而不是UTC。 实际上, 这意味着, 即使在给定日期有跳秒, 也不会影响时间的切换方式, 即使是在给定日期的最后1000秒。 相反, 即使给定日期有负跳秒, 23: 59: 59 仍然被视为有效时间 。 23: 59: 60 在 UTC- SLS 中无效, 如此区分它就会失败 。

@see 用于此函数版本的切换, 将失败作为例外 。 @see 用于格式化 @sample 样本的刻度到 String 。 Instants.parse Ornull

??? note "查看英文原文"

    Parses an ISO 8601 string that represents an instant (for example, `2020-08-30T18:43:00Z`),
    or returns `null` if the string cannot be parsed or the boundaries of `Instant` are exceeded.
    
    Guaranteed to parse all strings that `Instant.toString` produces.
    
    Examples of instants in the ISO 8601 format:
    - `2020-08-30T18:43:00Z`
    - `2020-08-30T18:43:00.50Z`
    - `2020-08-30T18:43:00.123456789Z`
    - `2020-08-30T18:40:00+03:00`
    - `2020-08-30T18:40:00+03:30:20`
    * `2020-01-01T23:59:59.123456789+01`
    * `+12020-01-31T23:59:59Z`
    
    See ISO-8601-1:2019, 5.4.2.1b), excluding the format without the offset.
    
    The string is considered to represent time on the UTC-SLS time scale instead of UTC.
    In practice, this means that, even if there is a leap second on the given day, it will not affect how the
    time is parsed, even if it's in the last 1000 seconds of the day.
    Instead, even if there is a negative leap second on the given day, 23:59:59 is still considered a valid time.
    23:59:60 is invalid on UTC-SLS, so parsing it will fail.
    
    @see Instant.parse for a version of this function that throws an exception on failure.
    @see Instant.toString for formatting.
    @sample samples.time.Instants.parseOrNull

## 声明与重载

### 1. Common

```kotlin
public fun parseOrNull(input: CharSequence): Instant?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L388)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Parsing a string that represents the Unix epoch.
    val unixEpochInstant = Instant.parseOrNull("1970-01-01T00:00:00Z")
    println(unixEpochInstant?.epochSeconds)

    // Parsing an ISO 8601 string with a time zone offset.
    val instant = Instant.parseOrNull("2020-08-30T18:40:00+03:00")
    // Instants are presented in the UTC time zone when converted to string.
    println(instant.toString())

    // Failing to parse an invalid string returns null.
    println(Instant.parseOrNull("Ten o'clock today"))
    println(Instant.parseOrNull("2020-08-32T15:40:00Z"))
    println(Instant.parseOrNull("+10000000000000-08-01T15:40:00Z"))
}
```

```text title="输出"
0
2020-08-30T15:40:00Z
null
null
null
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L166)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
