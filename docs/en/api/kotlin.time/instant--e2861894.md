# Instant

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A moment in time.

A point in time must be uniquely identified in a way that is independent of a time zone.
For example, `1970-01-01, 00:00:00` does not represent a moment in time since this would happen at different times
in different time zones: someone in Tokyo would think it is already `1970-01-01` several hours earlier than someone
in Berlin would. To represent such entities, use the `LocalDateTime` from `kotlinx-datetime`.
In contrast, "the moment the clocks in London first showed 00:00 on Jan 1, 2000" is a specific moment
in time, as is "1970-01-01, 00:00:00 UTC+0", so it can be represented as an `Instant`.

`Instant` uses the UTC-SLS (smeared leap second) time scale. This time scale doesn't contain instants
corresponding to leap seconds, but instead "smears" positive and negative leap seconds among the last 1000 seconds
of the day when a leap second happens.

### Obtaining the current moment

The `Clock` interface is the primary way to obtain the current moment:

```
val clock: Clock = Clock.System
val instant = clock.now()
```

The `Clock.System` implementation uses the platform-specific system clock to obtain the current moment.
Note that this clock is not guaranteed to be monotonic, and the user or the system may adjust it at any time,
so it should not be used for measuring time intervals.
For that, consider using `TimeSource.Monotonic` and `TimeMark` instead of `Clock.System` and `Instant`.

### Arithmetic operations

The `plus` and `minus` operators can be used to add `Duration`s to and subtract them from an `Instant`:

```
Clock.System.now() + 5.seconds // 5 seconds from now
```

Also, there is a `minus` operator that returns the `Duration` representing the difference between two instants:

```
val kotlinRelease = Instant.parse("2016-02-15T12:00:00+03:00")
val kotlinStableDuration = Clock.System.now() - kotlinRelease
```

### Platform specifics

On the JVM, there are `Instant.toJavaInstant()` and `java.time.Instant.toKotlinInstant()`
extension functions to convert between `kotlin.time` and `java.time` objects used for the same purpose.
Likewise, on JS, there are `Instant.toJSDate()` and `Date.toKotlinInstant()` extension functions.

For technical reasons, converting `Instant` to and from Foundation's `NSDate` is provided in
`kotlinx-datetime` via `Instant.toNSDate()` and `NSDate.toKotlinInstant()` extension functions.
These functions might become available in `kotlin.time` in the future.

### Construction, serialization, and deserialization

`fromEpochSeconds` can be used to construct an instant from the number of seconds since
`1970-01-01T00:00:00Z` (the Unix epoch).
`epochSeconds` and `nanosecondsOfSecond` can be used to obtain the number of seconds and nanoseconds since the epoch.

```
val instant = Instant.fromEpochSeconds(1709898983, 123456789)
instant.epochSeconds // 1709898983
instant.nanosecondsOfSecond // 123456789
```

`fromEpochMilliseconds` allows constructing an instant from the number of milliseconds since the epoch.
`toEpochMilliseconds` can be used to obtain the number of milliseconds since the epoch.
Note that `Instant` supports nanosecond precision, so converting to milliseconds is a lossy operation.

```
val instant1 = Instant.fromEpochSeconds(1709898983, 123456789)
instant1.nanosecondsOfSecond // 123456789
val milliseconds = instant1.toEpochMilliseconds() // 1709898983123
val instant2 = Instant.fromEpochMilliseconds(milliseconds)
instant2.nanosecondsOfSecond // 123000000
```

`parse` and `toString` methods can be used to obtain an `Instant` from and convert it to a string in the
[ISO 8601 extended format](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations),
which includes a time zone designator.

```
val instant = Instant.parse("2023-01-02T22:35:01+01:00")
instant.toString() // 2023-01-02T21:35:01Z
```

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.3")
@WasExperimental(ExperimentalTime::class)
public class Instant internal constructor(
    /**
     * The number of seconds from the epoch instant `1970-01-01T00:00:00Z` rounded down to a [Long] number.
     *
     * The difference between the rounded number of seconds and the actual number of seconds
     * is returned by [nanosecondsOfSecond] property expressed in nanoseconds.
     *
     * Note that this number doesn't include leap seconds added or removed since the epoch.
     *
     * @see fromEpochSeconds
     * @sample samples.time.Instants.epochSecondsAndNanosecondsOfSecond
     * @sample samples.time.Instants.fromEpochSecondsProperties
     */
    public val epochSeconds: Long,
    /**
     * The number of nanoseconds by which this instant is later than [epochSeconds] from the epoch instant.
     *
     * The value is always non-negative and lies in the range `0..999_999_999`.
     *
     * @see fromEpochSeconds
     * @sample samples.time.Instants.epochSecondsAndNanosecondsOfSecond
     * @sample samples.time.Instants.fromEpochSecondsProperties
     */
    public val nanosecondsOfSecond: Int
) : Comparable<Instant>, Serializable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L19)

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
    val value = Instant.fromEpochMilliseconds(0)
    println(value)
}
```

```text title="Output"
1970-01-01T00:00:00Z
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
