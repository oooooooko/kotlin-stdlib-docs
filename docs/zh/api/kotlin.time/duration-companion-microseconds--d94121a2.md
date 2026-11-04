# Duration.Companion.microseconds

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个`Duration`等于此`Int`微秒数。

@sample 样本 时间 剂量 来自米克罗秒

??? note "查看英文原文"

    Returns a `Duration` equal to this `Int` number of microseconds.
    
    @sample samples.time.Durations.fromMicroseconds

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Int.microseconds: Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L106)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Long.microseconds: Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L114)

返回一个`Duration`等于此`Long`微秒数。

@sample 样本 时间 剂量 来自米克罗秒

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Double.microseconds: Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L122)

返回一个`Duration`等于此`Double`微秒数。

值根据数值大小四舍五入到毫秒或毫秒的整数。

@throws 非法设备,如果`Double`值为`NaN`,则例外。 @sample 样本.时间。 来自米克龙的剂量。

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
    println(15.microseconds)

    // Large values can be accurately represented only with millisecond precision
    println(9000000000000_775_807.microseconds)

    // Fractional part is rounded to the nearest integer nanosecond value
    println(999.0004.microseconds)
    println(999.0009.microseconds)

    assertFailsWith<IllegalArgumentException> { Double.NaN.microseconds }
}
```

```text title="输出"
15us
104166666d 16h 0m 0.775s
999us
999.001us
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L90)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
