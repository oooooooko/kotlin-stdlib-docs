# Duration.Companion.parseOrNull

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

剖析一个代表一个持续时间的字符串, 并返回已解析的 `Duration` 值, 如果字符串不代表任何支持格式中的持续时间, 则返回 `null` 。

接受下列格式:

- 限制的ISO-8601 期限复合表示式,例如`P1DT2H3M4.058S`,见`toIsoString`和`parseIsoString`。
- 以默认的`Duration.toString`和`toString`在特定单位中返回的字符串格式,
例如,`10s`、`1h 30m`或`-(1h 30m)`。
@sample样本 时间. 时间. 光度. parse

??? note "查看英文原文"

    Parses a string that represents a duration and returns the parsed `Duration` value,
    or `null` if the string doesn't represent a duration in any of the supported formats.
    
    The following formats are accepted:
    
    - Restricted ISO-8601 duration composite representation, e.g. `P1DT2H3M4.058S`, see `toIsoString` and `parseIsoString`.
    - The format of string returned by the default `Duration.toString` and `toString` in a specific unit,
      e.g. `10s`, `1h 30m` or `-(1h 30m)`.
      @sample samples.time.Durations.parse

## 声明与重载

### 1. Common

```kotlin
public fun parseOrNull(value: String): Duration?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L325)

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
    val singleUnitFormatString = "1.5h"
    val invalidFormatString = "1 hour 30 minutes"

    println(Duration.parse(isoFormatString))
    println(Duration.parse(defaultFormatString))
    println(Duration.parse(singleUnitFormatString))
    assertFails { Duration.parse(invalidFormatString) }
    println(Duration.parseOrNull(invalidFormatString))
}
```

```text title="输出"
1h 30m
1h 30m
1h 30m
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L52)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
