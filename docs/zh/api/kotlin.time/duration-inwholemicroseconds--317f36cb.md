# Duration.inWholeMicroseconds

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

以 `Long` 微秒计值的这一持续时间值。

时间长度小于一微秒的部分成为结果的一小部分,然后被缩短(四舍五入为零)。

如果结果不等于 `Long` 的范围之内, 它会被强制到这个范围内: - `Long.MIN_VALUE` 如果它小于`Long.MIN_VALUE`, 则返回`Long.MIN_VALUE`, 如果它大于`Long.MAX_VALUE`, 则返回`Long.MAX_VALUE`。

无限期限值根据符号的符号转换为 `Long.MAX_VALUE` 或 `Long.MIN_VALUE` 。

@sample 样本 时间、剂量、全细胞

??? note "查看英文原文"

    The value of this duration expressed as a `Long` number of microseconds.
    
    The part of this duration that is smaller than a microsecond
    becomes a fractional part of the result and then is truncated (rounded towards zero).
    
    If the result doesn't fit in the range of `Long` type, it is coerced into that range:
    - `Long.MIN_VALUE` is returned if it's less than `Long.MIN_VALUE`,
    - `Long.MAX_VALUE` is returned if it's greater than `Long.MAX_VALUE`.
    
    An infinite duration value is converted either to `Long.MAX_VALUE` or `Long.MIN_VALUE` depending on its sign.
    
    @sample samples.time.Durations.inWholeMicroseconds

## 声明与重载

### 1. Common

```kotlin
public val inWholeMicroseconds: Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L777)

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
    println(25_900.nanoseconds.inWholeMicroseconds)

    println(1_000_000_000.days.inWholeMicroseconds == Long.MAX_VALUE)
    println((-Duration.INFINITE).inWholeMicroseconds == Long.MIN_VALUE)
}
```

```text title="输出"
25
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L180)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
