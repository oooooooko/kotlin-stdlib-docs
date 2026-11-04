# Duration

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents the amount of time one instant of time is away from another instant.

A negative duration is possible in a situation when the second instant is earlier than the first one.

The type can store duration values up to ±146 years with nanosecond precision,
and up to ±146 million years with millisecond precision.
If a duration-returning operation provided in `kotlin.time` produces a duration value that doesn't fit into the above range,
the returned `Duration` is infinite.

An infinite duration value `Duration.INFINITE` can be used to represent infinite timeouts.

To construct a duration use either the extension function `toDuration`,
or the extension properties `hours`, `minutes`, `seconds`, and so on,
available on `Int`, `Long`, and `Double` numeric types.

To get the value of this duration expressed in a particular `duration units``DurationUnit`
use the functions `toInt`, `toLong`, and `toDouble`
or the properties `inWholeHours`, `inWholeMinutes`, `inWholeSeconds`, `inWholeNanoseconds`, and so on.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.6")
@JvmInline
public value class Duration
// A temporary workaround for KT-81995, the constructor has to be private once the issue is resolved.
@Deprecated("Don't call this constructor directly.", level = DeprecationLevel.ERROR)
internal constructor(private val rawValue: Long) :
    Comparable<Duration>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L12)

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
    val value = 2.seconds
    println(value)
}
```

```text title="Output"
2s
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
