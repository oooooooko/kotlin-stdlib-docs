# Duration.toString

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个字符串表示此持续时间值,以数字组成部分组合表示,每个组成部分都以自己的单位表示。

每个组成部分后面是单位名称缩写号: `d` , `h` , `m` , `s` :`5h`,`1d 12h`, `1h 0m 30.340s` 。最后一部分通常为几秒,但有几分部分。

如果持续时间少于一秒钟,则以一个数字表示
具有以下二分单元之一:`ms`(毫秒)、`us`(微秒)或`ns`(毫秒):
`140.884ms`,`500us`,`24ns`。

负时段前有 `-` 号标记,如果由多个部件组成,则括号围起来:`-12m`和`-(1h 30m)`。

特殊情况: - 无期限为 `"Infinity"` 或 `"-Infinity"` ,无单位。

推荐使用 `toIsoString` , 使用更严格的ISO-8601格式, 而不是这个 `toString` 格式, 在序列化、交换等情况下, 您想要将一个时间段转换为字符串 。

@sample样本 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 : 时间 :

??? note "查看英文原文"

    Returns a string representation of this duration value
    expressed as a combination of numeric components, each in its own unit.
    
    Each component is a number followed by the unit abbreviated name: `d`, `h`, `m`, `s`:
    `5h`, `1d 12h`, `1h 0m 30.340s`.
    The last component, usually seconds, can be a number with a fractional part.
    
    If the duration is less than a second, it is represented as a single number
    with one of sub-second units: `ms` (milliseconds), `us` (microseconds), or `ns` (nanoseconds):
    `140.884ms`, `500us`, `24ns`.
    
    A negative duration is prefixed with `-` sign and, if it consists of multiple components, surrounded with parentheses:
    `-12m` and `-(1h 30m)`.
    
    Special cases:
     - an infinite duration is formatted as `"Infinity"` or `"-Infinity"` without a unit.
    
    It's recommended to use `toIsoString` that uses more strict ISO-8601 format instead of this `toString`
    when you want to convert a duration to a string in cases of serialization, interchange, etc.
    
    @sample samples.time.Durations.toStringDefault

## 声明与重载

### 1. Common

```kotlin
override fun toString(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L816)

### 2. Common

```kotlin
public fun toString(unit: DurationUnit, decimals: Int = 0): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L898)

返回给定的 `unit` 中表达的、且格式化为小数点后指定的 `decimals` 位数的字符串表示值。

特殊情况: - 无期限为 `"Infinity"` 或 `"-Infinity"` ,无单位。

以小数点后的数字表示@param小数。 数值必须是非负值。 将显示的小数点数不超过12小数, 即使要求的数字更大 。

@return , 长度值在指定的 `unit` , 之后是该单位的缩写名称: `d` , `h` , `h` , `m` , `s`, `ms` , `ms` , `us`, `us` , 或 `ns` 。

@throws 非法设备,如果`decimals`低于0,则不在此列。

@sample 样本 时间 剂量 到12: 10

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
    println(45.days)
    println(1.5.days)
    println(1230.minutes)
    println(920.minutes)
    println(1.546.seconds)
    println(25.12.milliseconds)
}
```

```text title="输出"
45d
1d 12h
20h 30m
15h 20m
1.546s
25.12ms
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L34)

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
    println(1230.minutes.toString(DurationUnit.DAYS, 2))
    println(1230.minutes.toString(DurationUnit.HOURS, 2))
    println(1230.minutes.toString(DurationUnit.MINUTES))
    println(1230.minutes.toString(DurationUnit.SECONDS))
}
```

```text title="输出"
0.85d
20.50h
1230m
73800s
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L44)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
