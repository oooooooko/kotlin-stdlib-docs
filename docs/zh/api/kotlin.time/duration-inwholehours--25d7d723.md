# Duration.inWholeHours

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

这一持续时间的价值以`Long`小时计。

时间小于1小时的部分成为结果的一小部分,然后被缩短(四舍五入为零)。

无限期限值根据符号的符号转换为 `Long.MAX_VALUE` 或 `Long.MIN_VALUE` 。

@sample 样本 时间 剂量 全身

??? note "查看英文原文"

    The value of this duration expressed as a `Long` number of hours.
    
    The part of this duration that is smaller than an hour
    becomes a fractional part of the result and then is truncated (rounded towards zero).
    
    An infinite duration value is converted either to `Long.MAX_VALUE` or `Long.MIN_VALUE` depending on its sign.
    
    @sample samples.time.Durations.inWholeHours

## 声明与重载

### 1. Common

```kotlin
public val inWholeHours: Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L723)

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
    println(59.minutes.inWholeHours)
    println(120.minutes.inWholeHours)

    println((-Duration.INFINITE).inWholeHours == Long.MIN_VALUE)
}
```

```text title="输出"
0
2
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L210)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
