# ComparableTimeMark.minus

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the duration elapsed between the `other` time mark and `this` time mark.

The returned duration can be infinite if the time marks are far away from each other and
the result doesn't fit into `Duration` type,
or if one time mark is infinitely distant, or if both `this` and `other` time marks
lie infinitely distant on the opposite sides of the time scale.

Two infinitely distant time marks on the same side of the time scale are considered equal and
the duration between them is `Duration.ZERO`.

Note that the other time mark must be obtained from the same time source as this one.

@throws IllegalArgumentException if time marks were obtained from different time sources.

## Declarations and overloads

### 1. Common

```kotlin
public open override operator fun minus(duration: Duration): ComparableTimeMark
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L204)

### 2. Common

```kotlin
public operator fun minus(other: ComparableTimeMark): Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L206)

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
    val result = source.`minus`(2.seconds)
    println(result)
}
```

```text title="Output"
ValueTimeMark(reading=-1999987959)
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
