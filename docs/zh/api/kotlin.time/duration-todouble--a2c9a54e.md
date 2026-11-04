# Duration.toDouble

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回指定 `unit` 的`Double` 值。

当结果不能精确代表`Double`的号码时,操作可能涉及四舍五入。

无限期限值根据符号的符号转换为 `Double.POSITIVE_INFINITY` 或 `Double.NEGATIVE_INFINITY` 。

@sample 样本.时间. 剂量. 至四分单位

??? note "查看英文原文"

    Returns the value of this duration expressed as a `Double` number of the specified `unit`.
    
    The operation may involve rounding when the result cannot be represented exactly with a `Double` number.
    
    An infinite duration value is converted either to `Double.POSITIVE_INFINITY` or `Double.NEGATIVE_INFINITY` depending on its sign.
    
    @sample samples.time.Durations.toDoubleUnits

## 声明与重载

### 1. Common

```kotlin
public fun toDouble(unit: DurationUnit): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L646)

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
    println(2900.milliseconds.toDouble(DurationUnit.SECONDS))
    println(1.seconds.toDouble(DurationUnit.MINUTES))

    println(Duration.INFINITE.toDouble(DurationUnit.SECONDS))
}
```

```text title="输出"
2.9
0.016666666666666666
Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L247)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
