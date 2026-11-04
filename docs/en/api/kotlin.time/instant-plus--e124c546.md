# Instant.plus

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an instant that is the result of adding the specified `duration` to this instant.

If the `duration` is positive, the returned instant is later than this instant.
If the `duration` is negative, the returned instant is earlier than this instant.

The return value is clamped to the boundaries of `Instant` if the result exceeds them.

**Pitfall**: `Duration.Companion.days` are multiples of 24 hours, but in some time zones,
some days can be shorter or longer because clocks are shifted.
Consider using `kotlinx-datetime` for arithmetic operations that take time zone transitions into account.

@sample samples.time.Instants.plusDuration

## Declarations and overloads

### 1. Common

```kotlin
public operator fun plus(duration: Duration): Instant
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L170)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Finding a moment that's later than the starting point by the given amount of real time
    val instant = Instant.fromEpochSeconds(7 * 60 * 60, nanosecondAdjustment = 123_456_789)
    val fiveHoursLater = instant + 5.hours
    println(fiveHoursLater.epochSeconds == 12 * 60 * 60L)
    println(fiveHoursLater.nanosecondsOfSecond == 123_456_789)
}
```

```text title="Output"
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L65)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
