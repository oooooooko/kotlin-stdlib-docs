# Duration.Companion.parseIsoString

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

分解一个字符串, 代表限制的 ISO-8601 复合表示法中的一段持续时间, 并返回所解析的 `Duration` 值。 复合表示法是ISO-8601 持续时间格式的宽松版本, 支持单个部件的负持续时间和负值 。

施加下列限制:

- 唯一允许的非时间代号是天数(`D`),`Y`(年份)、`W`(星期)和`M`(月)不支持。
- 白天被认为是24小时(24小时24小时)的准确时间。
- 每周制备选代表制`"P"``number``"W"``不支持。

@throws 非法参数 不包括如果字符串不代表ISO-8601格式的长度 。 @sample 样本。 时间。 时间 。 时间 。 时间 。 参数 。 parseIsoString

??? note "查看英文原文"

    Parses a string that represents a duration in a restricted ISO-8601 composite representation
    and returns the parsed `Duration` value.
    Composite representation is a relaxed version of ISO-8601 duration format that supports
    negative durations and negative values of individual components.
    
    The following restrictions are imposed:
    
    - The only allowed non-time designator is days (`D`). `Y` (years), `W` (weeks), and `M` (months) are not supported.
    - Day is considered to be exactly 24 hours (24-hour clock time scale).
    - Alternative week-based representation ``"P"``number``"W"`` is not supported.
    
    @throws IllegalArgumentException if the string doesn't represent a duration in ISO-8601 format.
    @sample samples.time.Durations.parseIsoString

## 声明与重载

### 1. Common

```kotlin
public fun parseIsoString(value: String): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L304)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*
import kotlin.time.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    val isoFormatString = "PT1H30M"
    val defaultFormatString = "1h 30m"

    println(Duration.parseIsoString(isoFormatString))
    assertFails { Duration.parseIsoString(defaultFormatString) }
    println(Duration.parseIsoStringOrNull(defaultFormatString))
}
```

```text title="输出"
1h 30m
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L66)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
