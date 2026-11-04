# Duration.Companion.seconds

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回`Duration` 等于这`Int`秒数。

@sample 样本 时间 剂量 来自中学生

??? note "查看英文原文"

    Returns a `Duration` equal to this `Int` number of seconds.
    
    @sample samples.time.Durations.fromSeconds

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Int.seconds: Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L162)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Long.seconds: Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L170)

返回`Duration` 等于这`Long`秒数。

@sample 样本 时间 剂量 来自中学生

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Double.seconds: Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L178)

返回`Duration` 等于这`Double`秒数。

值根据数值大小四舍五入到毫秒或毫秒的整数。

@throws 非法设备除外,如果这个`Double`值是`NaN`。 @sample 样本. 时间. 时间. 剂量. 来自第二代的 时间 。

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
    println(61.seconds)
    println(0.5.seconds)

    // Large values can be converted to an infinite duration
    println(9_000_000_000_000_000.seconds)

    // Fractional part is rounded to the nearest integer nanosecond value
    println(2.000_000_000_4.seconds)
    println(2.000_000_000_9.seconds)
    // Or to the nearest integer millisecond value
    println(9_000_000_000_000.001_5.seconds)

    assertFailsWith<IllegalArgumentException> { Double.NaN.seconds }
}
```

```text title="输出"
1m 1s
500ms
Infinity
2s
2.000000001s
104166666d 16h 0m 0.002s
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L122)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
