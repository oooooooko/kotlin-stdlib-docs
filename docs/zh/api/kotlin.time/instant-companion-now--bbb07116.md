# Instant.Companion.now

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

`TestTimeSource.read` 是由时间标记间接使用的受保护钩子。`Instant.now()` 已弃用，2.4.21 中的实现会抛出 `NotImplementedError`；本例捕获该异常，新代码使用 `Clock.System.now()`。

## 声明与重载

### 1. Common

```kotlin
@Deprecated("Use Clock.System.now() instead", ReplaceWith("Clock.System.now()", "kotlin.time.Clock"), level = DeprecationLevel.ERROR)
        public fun now(): Instant
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L274)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.time.*
import kotlin.time.Duration.Companion.milliseconds
fun main() {
    val clock: Clock = object : Clock { override fun now(): Instant = Instant.fromEpochMilliseconds(0) }
    println(clock.now())
    val source: TimeSource.WithComparableMarks = TestTimeSource()
    val mark = source.markNow()
    (source as TestTimeSource) += 25.milliseconds
    println(mark.elapsedNow())
    val monotonic: TimeSource = TimeSource.Monotonic
    val valueMark: TimeSource.Monotonic.ValueTimeMark = TimeSource.Monotonic.markNow()
    println(valueMark.hasPassedNow())
    println(monotonic.markNow().hasPassedNow())
    try { println(Instant.now()) } catch (error: NotImplementedError) { println("Instant.now: ${error.message}") }
}
```

```text title="输出"
1970-01-01T00:00:00Z
25ms
true
true
Instant.now: An operation is not implemented.
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
