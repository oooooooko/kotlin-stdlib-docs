# asClock

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a `Clock` that uses the `time mark at the moment of creation``TimeSource.markNow` to determine how `far``TimeMark.elapsedNow`
the `current moment``Clock.now` is from the `origin`.

This clock stores the `TimeMark` at the moment of creation, so repeatedly creating `Clock`s from the same `TimeSource` results
in different `Instant`s iff the time of the `TimeSource` was increased. To sync different `Clock`s, use the `origin`
parameter.

@sample samples.time.Clocks.timeSourceAsClock

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.3")
@WasExperimental(ExperimentalTime::class)
@kotlin.jvm.JvmName("fromTimeSource")
public fun TimeSource.asClock(origin: Instant): Clock
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Clocks.kt#L8)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
2023-01-02T22:00:00Z
2023-01-02T22:00:10Z
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/clocks.kt#L40)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
