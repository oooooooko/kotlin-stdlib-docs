# TimeMark.plus

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a time mark on the same time source that is ahead of this time mark by the specified `duration`.

The returned time mark is more _late_ when the `duration` is positive, and more _early_ when the `duration` is negative.

If the time mark is adjusted too far in the past or in the future, it may saturate to an infinitely distant time mark.
In that case, `elapsedNow` will return an infinite duration elapsed from such infinitely distant mark.

@throws IllegalArgumentException an implementation may throw if a positive infinite duration is added to an infinitely distant past time mark or
a negative infinite duration is added to an infinitely distant future time mark.

## Declarations and overloads

### 1. Common

```kotlin
public operator fun plus(duration: Duration): TimeMark
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L153)

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
    val result = source.`plus`(2.seconds)
    println(result)
}
```

```text title="Output"
ValueTimeMark(reading=2000003666)
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
