# Duration.toIsoString

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回基于 ISO-8601 的字符串表示此持续时间。

返回的数值以`PThHmMs.fS`格式显示,`h`、`m`、`s`是这一时期的整数组成部分(见`toComponents`)。
`f`是第二组的一部分 视数值的圆圆大小而定,可使用其中任意一种格式化的分部分
0,3,6,或9位数小数数。

无限期限为 `"PT9999999999999H"` ,大于科特林任何可能的有限期限。

返回字符串开头的符号 `-` 显示负时长,例如 `"-PT5M30S"` 。

@sample 样本 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点 地点

??? note "查看英文原文"

    Returns an ISO-8601 based string representation of this duration.
    
    The returned value is presented in the format `PThHmMs.fS`, where `h`, `m`, `s` are the integer components of this duration (see `toComponents`)
    and `f` is a fractional part of second. Depending on the roundness of the value the fractional part can be formatted with either
    0, 3, 6, or 9 decimal digits.
    
    The infinite duration is represented as `"PT9999999999999H"` which is larger than any possible finite duration in Kotlin.
    
    Negative durations are indicated with the sign `-` in the beginning of the returned string, for example, `"-PT5M30S"`.
    
    @sample samples.time.Durations.toIsoString

## 声明与重载

### 1. Common

```kotlin
public fun toIsoString(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L922)

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
    println(25.nanoseconds.toIsoString())
    println(120.3.milliseconds.toIsoString())
    println(30.5.seconds.toIsoString())
    println(30.5.minutes.toIsoString())
    println(86420.seconds.toIsoString())
    println(2.days.toIsoString())
    println(Duration.ZERO.toIsoString())
    println(Duration.INFINITE.toIsoString())
}
```

```text title="输出"
PT0.000000025S
PT0.120300S
PT30.500S
PT30M30S
PT24H0M20S
PT48H
PT0S
PT9999999999999H
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L22)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
