# TestTimeSource.read

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

`TestTimeSource.read` is a protected time-mark hook. Deprecated `Instant.now()` throws `NotImplementedError` in 2.4.21; this example catches it. Use `Clock.System.now()` in new code.

## Declarations and overloads

### 1. Common

```kotlin
override fun read(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L171)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
1970-01-01T00:00:00Z
25ms
true
true
Instant.now: An operation is not implemented.
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
