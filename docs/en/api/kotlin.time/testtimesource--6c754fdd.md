# TestTimeSource

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A time source that has programmatically updatable readings. It is useful as a predictable source of time in tests.

The current reading value can be advanced by the specified duration amount with the operator `plusAssign`:

```
val timeSource = TestTimeSource()
timeSource += 10.seconds
```

Time marks returned by this time source can be compared for difference with other time marks
obtained from the same time source.

Implementation note: the current reading value is stored as a `Long` number of nanoseconds,
thus it's capable to represent a time range of approximately ±292 years.
Should the reading value overflow as the result of `plusAssign` operation, an `IllegalStateException` is thrown.

@sample samples.time.MeasureTime.explicitMeasureTimeSample
@sample samples.time.MeasureTime.explicitMeasureTimedValueSample

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalTime::class)
public class TestTimeSource : AbstractLongTimeSource(unit = DurationUnit.NANOSECONDS)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L142)

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
    val value = kotlin.time.TestTimeSource()
    println(value)
}
```

```text title="Output"
kotlin.time.TestTimeSource@452b3a41
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
