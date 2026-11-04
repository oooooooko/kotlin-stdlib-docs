# Instant.minus

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an instant that is the result of subtracting the specified `duration` from this instant.

If the `duration` is positive, the returned instant is earlier than this instant.
If the `duration` is negative, the returned instant is later than this instant.

The return value is clamped to the boundaries of `Instant` if the result exceeds them.

**Pitfall**: `Duration.Companion.days` are multiples of 24 hours, but in some time zones,
some days can be shorter or longer because clocks are shifted.
Consider using `kotlinx-datetime` for arithmetic operations that take time zone transitions into account.

@sample samples.time.Instants.minusDuration

## Declarations and overloads

### 1. Common

```kotlin
public operator fun minus(duration: Duration): Instant
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L196)

### 2. Common

```kotlin
public operator fun minus(other: Instant): Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L212)

Returns the `Duration` between two instants: `other` and `this`.

The duration returned is positive if this instant is later than the other,
and negative if this instant is earlier than the other.

The result is never clamped, but note that for instants that are far apart,
the value returned may represent the duration between them inexactly due to the loss of precision.

Note that sources of `Instant` values (in particular, `Clock`) are not guaranteed to be in sync with each other
or even monotonic, so the result of this operation may be negative even if the other instant was observed later
than this one, or vice versa.
For measuring time intervals, consider using `TimeSource.Monotonic`.

@sample samples.time.Instants.minusInstant

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Finding a moment that's earlier than the starting point by the given amount of real time
    val instant = Instant.fromEpochSeconds(7 * 60 * 60, nanosecondAdjustment = 123_456_789)
    val fiveHoursEarlier = instant - 5.hours
    println(fiveHoursEarlier.epochSeconds == 2 * 60 * 60L)
    println(fiveHoursEarlier.nanosecondsOfSecond == 123_456_789)
}
```

```text title="Output"
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L74)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Finding the difference between two instants in terms of elapsed time
    val instant1 = Instant.fromEpochSeconds(0) // The Unix epoch start.
    val instant2 = Instant.fromEpochSeconds(7 * 60 * 60) // 7 hours since the Unix epoch.
    val elapsedTime = instant1 - instant2 // The duration between instant1 and instant2.
    println(elapsedTime == (-7).hours)
}
```

```text title="Output"
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L83)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
