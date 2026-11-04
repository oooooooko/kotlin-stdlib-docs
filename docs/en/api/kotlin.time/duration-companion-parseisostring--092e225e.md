# Duration.Companion.parseIsoString

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses a string that represents a duration in a restricted ISO-8601 composite representation
and returns the parsed `Duration` value.
Composite representation is a relaxed version of ISO-8601 duration format that supports
negative durations and negative values of individual components.

The following restrictions are imposed:

- The only allowed non-time designator is days (`D`). `Y` (years), `W` (weeks), and `M` (months) are not supported.
- Day is considered to be exactly 24 hours (24-hour clock time scale).
- Alternative week-based representation ``"P"``number``"W"`` is not supported.

@throws IllegalArgumentException if the string doesn't represent a duration in ISO-8601 format.
@sample samples.time.Durations.parseIsoString

## Declarations and overloads

### 1. Common

```kotlin
public fun parseIsoString(value: String): Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L304)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*
import kotlin.time.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    val isoFormatString = "PT1H30M"
    val defaultFormatString = "1h 30m"

    println(Duration.parseIsoString(isoFormatString))
    assertFails { Duration.parseIsoString(defaultFormatString) }
    println(Duration.parseIsoStringOrNull(defaultFormatString))
}
```

```text title="Output"
1h 30m
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L66)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
