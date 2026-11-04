# TimeMark.elapsedNow

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the amount of time passed from this mark measured with the time source from which this mark was taken.

Note that the value returned by this function can change on subsequent invocations.

The value returned by this function may be infinitely large (in terms of `Duration.isInfinite`).

Depending on monotonicity guarantees of a `TimeSource` from which a `TimeMark` was obtained,
subsequence calls may return non-increasing (or even negative) `Duration` values.
Consult with a documentation of a particular `TimeSource` implementation for more details about
monotonicity guarantees.

@throws IllegalArgumentException an implementation may throw if calculating the elapsed time involves
adding a positive infinite duration to an infinitely distant past time mark or
a negative infinite duration to an infinitely distant future time mark.

## Declarations and overloads

### 1. Common

```kotlin
public abstract fun elapsedNow(): Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L135)

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
    val source = TimeSource.Monotonic.markNow()
    val result = source.`elapsedNow`()
    println(result)
}
```

```text title="Output"
231.916us
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
