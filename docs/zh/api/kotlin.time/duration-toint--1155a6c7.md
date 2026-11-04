# Duration.toInt

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回指定 `unit` 的`Int` 值。

超过指定单位的这一段持续时间,成为结果的一小部分,然后被缩短(四舍五入为零)。

如果结果不等于 `Int` 的范围之内, 它会被强制到这个范围内: - `Int.MIN_VALUE` 如果它小于`Int.MIN_VALUE`, 则返回`Int.MIN_VALUE`, 如果它大于`Int.MAX_VALUE`, 则返回`Int.MAX_VALUE`。

无限期限值根据符号的符号转换为 `Int.MAX_VALUE` 或 `Int.MIN_VALUE` 。

@sample 样本 时间 剂量 到单位

??? note "查看英文原文"

    Returns the value of this duration expressed as an `Int` number of the specified `unit`.
    
    The part of this duration that is smaller than the specified unit
    becomes a fractional part of the result and then is truncated (rounded towards zero).
    
    If the result doesn't fit in the range of `Int` type, it is coerced into that range:
    - `Int.MIN_VALUE` is returned if it's less than `Int.MIN_VALUE`,
    - `Int.MAX_VALUE` is returned if it's greater than `Int.MAX_VALUE`.
    
    An infinite duration value is converted either to `Int.MAX_VALUE` or `Int.MIN_VALUE` depending on its sign.
    
    @sample samples.time.Durations.toIntUnits

## 声明与重载

### 1. Common

```kotlin
public fun toInt(unit: DurationUnit): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L688)

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
    println(2900.milliseconds.toInt(DurationUnit.SECONDS))
    println(3.hours.toInt(DurationUnit.MINUTES))

    println(1.minutes.toInt(DurationUnit.NANOSECONDS) == Int.MAX_VALUE)
    println((-Duration.INFINITE).toInt(DurationUnit.DAYS) == Int.MIN_VALUE)
}
```

```text title="输出"
2
180
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L227)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
