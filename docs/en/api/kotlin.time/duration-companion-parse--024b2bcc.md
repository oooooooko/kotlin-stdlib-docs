# Duration.Companion.parse

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses a string that represents a duration and returns the parsed `Duration` value.

The following formats are accepted:

- ISO-8601 Duration format, e.g. `P1DT2H3M4.058S`, see `toIsoString` and `parseIsoString`.
- The format of string returned by the default `Duration.toString` and `toString` in a specific unit,
  e.g. `10s`, `1h 30m` or `-(1h 30m)`.

@throws IllegalArgumentException if the string doesn't represent a duration in any of the supported formats.
@sample samples.time.Durations.parse

## Declarations and overloads

### 1. Common

```kotlin
public fun parse(value: String): Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L286)

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
    val singleUnitFormatString = "1.5h"
    val invalidFormatString = "1 hour 30 minutes"

    println(Duration.parse(isoFormatString))
    println(Duration.parse(defaultFormatString))
    println(Duration.parse(singleUnitFormatString))
    assertFails { Duration.parse(invalidFormatString) }
    println(Duration.parseOrNull(invalidFormatString))
}
```

```text title="Output"
1h 30m
1h 30m
1h 30m
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L52)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
