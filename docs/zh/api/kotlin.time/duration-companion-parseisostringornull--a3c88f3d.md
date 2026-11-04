# Duration.Companion.parseIsoStringOrNull

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

分解一个在 ISO-8601 限制的复合表示式中代表一个持续时间的字符串, 如果字符串不代表以 `parseIsoString` 可接受的格式表示的长度, 则返回已解析的 `Duration` 值或 `null` 。

@sample 样本 时间 剂量 分

??? note "查看英文原文"

    Parses a string that represents a duration in restricted ISO-8601 composite representation
    and returns the parsed `Duration` value or `null` if the string doesn't represent a duration in the format
    acceptable by `parseIsoString`.
    
    @sample samples.time.Durations.parseIsoString

## 声明与重载

### 1. Common

```kotlin
public fun parseIsoStringOrNull(value: String): Duration?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L339)

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
