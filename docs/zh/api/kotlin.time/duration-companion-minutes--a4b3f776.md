# Duration.Companion.minutes

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

a `Duration` 返回等于此 `Int`分钟。

@sample 样本 时间 剂量 来自米诺特斯

??? note "查看英文原文"

    Returns a `Duration` equal to this `Int` number of minutes.
    
    @sample samples.time.Durations.fromMinutes

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Int.minutes: Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L190)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Long.minutes: Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L198)

a `Duration` 返回等于此 `Long`分钟。

@sample 样本 时间 剂量 来自米诺特斯

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Double.minutes: Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L206)

a `Duration` 返回等于此 `Double`分钟。

值根据数值大小四舍五入到毫秒或毫秒的整数。

@throws 非法设备,如果`Double`值为`NaN`,则例外。 @sample 样本.time. durations. fromminutes.

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
    println(61.minutes)
    println(0.5.minutes)

    // Large values can be converted to an infinite duration
    println(90_000_000_000_000.minutes)

    assertFailsWith<IllegalArgumentException> { Double.NaN.minutes }
}
```

```text title="输出"
1h 1m
30s
Infinity
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L139)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
