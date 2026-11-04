# asClock

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建`Clock`, 使用 `time mark at the moment of creation` `TimeSource.markNow` 确定 `far` `TimeMark.elapsedNow` `current moment``Clock.now` 如何来自 `origin` 。

这个时钟在创建时存储了 `TimeMark` , 因此反复从相同的`TimeSource`中创建`Clock`, 如果增加 `TimeSource` 的时间, 则产生 `Instant` 。 要同步不同的 8,00000006, 请使用 `origin` 参数 。

@sample 样本 时间 时间 时间 来源时间 时间 来源 时间 时间 时间 时间 时间 时间 时间 时间 来源 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 来源 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间 时间

??? note "查看英文原文"

    Creates a `Clock` that uses the `time mark at the moment of creation``TimeSource.markNow` to determine how `far``TimeMark.elapsedNow`
    the `current moment``Clock.now` is from the `origin`.
    
    This clock stores the `TimeMark` at the moment of creation, so repeatedly creating `Clock`s from the same `TimeSource` results
    in different `Instant`s iff the time of the `TimeSource` was increased. To sync different `Clock`s, use the `origin`
    parameter.
    
    @sample samples.time.Clocks.timeSourceAsClock

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.3")
@WasExperimental(ExperimentalTime::class)
@kotlin.jvm.JvmName("fromTimeSource")
public fun TimeSource.asClock(origin: Instant): Clock
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Clocks.kt#L8)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Creating a TimeSource
    // When testing a Clock in combination of kotlinx-coroutines-test, use the testTimeSource of the TestDispatcher.
    val timeSource = TestTimeSource()
    // Creating a clock by setting the specified origin
    val clock = timeSource.asClock(origin = Instant.parse("2023-01-02T22:00:00Z"))

    println(clock.now())

    // Advancing time in the timeSource
    timeSource += 10.seconds

    println(clock.now())
}
```

```text title="输出"
2023-01-02T22:00:00Z
2023-01-02T22:00:10Z
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/clocks.kt#L40)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
