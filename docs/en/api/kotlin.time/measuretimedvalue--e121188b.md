# measureTimedValue

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Executes the given function `block` and returns an instance of `TimedValue` class, containing both
the result of the function execution and the duration of the elapsed time interval.

The elapsed time is measured with `TimeSource.Monotonic` which is the most precise
available time source on the platform.

@sample samples.time.MeasureTime.measureTimedValueSample

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalTime::class)
public inline fun <T> measureTimedValue(block: () -> T): TimedValue<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/measureTime.kt#L79)

### 2. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalTime::class)
public inline fun <T> TimeSource.measureTimedValue(block: () -> T): TimedValue<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/measureTime.kt#L98)

Executes the given function `block` and returns an instance of `TimedValue` class, containing both
the result of function execution and the duration of the elapsed time interval.

The elapsed time is measured with the specified `this` `TimeSource` instance.

@sample samples.time.MeasureTime.explicitMeasureTimedValueSample

### 3. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalTime::class)
public inline fun <T> TimeSource.Monotonic.measureTimedValue(block: () -> T): TimedValue<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/measureTime.kt#L118)

Executes the given function `block` and returns an instance of `TimedValue` class, containing both
the result of function execution and the duration of the elapsed time interval.

The elapsed time is measured with the specified `this` `TimeSource.Monotonic` instance.
The explicit instance allows using non-boxed version of `TimeSource.Monotonic.ValueTimeMark`
and, optionally, be more explicit about the intent.

@sample samples.time.MeasureTime.monotonicMeasureTimedValueSample

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.time.*

fun main() {
    val result = `measureTimedValue`({ 42 })
    println(result)
}
```

```text title="Output"
TimedValue(value=42, duration=385.417us)
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
