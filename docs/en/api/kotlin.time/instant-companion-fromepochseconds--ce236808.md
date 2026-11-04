# Instant.Companion.fromEpochSeconds

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an `Instant` that is the `epochSeconds` number of seconds from the epoch instant `1970-01-01T00:00:00Z`
and the `nanosecondAdjustment` number of nanoseconds.

`nanosecondAdjustment` describes how many nanoseconds the given instant is later than the one defined by just `epochSeconds`.
For convenience and flexibility, `fromEpochSeconds` accepts `nanosecondAdjustment` values outside
of `Instant.nanosecondsOfSecond` range. Negative `nanosecondAdjustment` means that the given instant will be earlier than
the one defined by just `epochSeconds`, and values greater than a second will contribute to the resulting number of seconds.

For example, if `nanosecondAdjustment` is `-1`, the resulting `Instant` will be `1` nanosecond earlier than
if `nanosecondAdjustment` was `0`, and if it is `1_000_000_000`, the resulting `Instant` will be `1` second later.

The return value is clamped to the boundaries of `Instant` if the result exceeds them.
In any case, it is guaranteed that instants between `DISTANT_PAST` and `DISTANT_FUTURE` can be represented.

`fromEpochMilliseconds` is a similar function for when input data only has millisecond precision.

@see Instant.epochSeconds
@see Instant.nanosecondsOfSecond
@sample samples.time.Instants.fromEpochSeconds
@sample samples.time.Instants.fromEpochSecondsProperties

## Declarations and overloads

### 1. Common

```kotlin
public fun fromEpochSeconds(epochSeconds: Long, nanosecondAdjustment: Long = 0): Instant
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L297)

### 2. Common

```kotlin
public fun fromEpochSeconds(epochSeconds: Long, nanosecondAdjustment: Int): Instant
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L333)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Creating an Instant representing the Unix epoch.
    val unixEpochInstant = Instant.fromEpochSeconds(0)
    // Creating an Instant from a specific number of milliseconds and nanoseconds since the Unix epoch.
    val instant = Instant.fromEpochSeconds(999_999_999, nanosecondAdjustment = 999_999_999)

    // The string representation of the constructed instants.
    println(unixEpochInstant)
    println(instant)

    // Creating an Instant with negative nanosecondAdjustment
    val earlierInstant = Instant.fromEpochSeconds(999_999_999, nanosecondAdjustment = -999_999_999)
    println(earlierInstant)
    println(earlierInstant < instant)

    // Creating an Instant with nanosecondAdjustment > 1s
    val laterInstant = Instant.fromEpochSeconds(999_999_999, nanosecondAdjustment = 1_999_999_999)
    println(laterInstant)
    println(laterInstant > instant)
}
```

```text title="Output"
1970-01-01T00:00:00Z
2001-09-09T01:46:39.999999999Z
2001-09-09T01:46:38.000000001Z
true
2001-09-09T01:46:40.999999999Z
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L132)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // When nanosecondAdjustment is within the range `0..999_999_999`,
    // epochSeconds and nanosecondsOfSecond hold the exact values provided.
    val instant1 = Instant.fromEpochSeconds(999_999, nanosecondAdjustment = 123_456_789)
    println(instant1.epochSeconds)
    println(instant1.nanosecondsOfSecond)

    // When nanosecondAdjustment exceeds `999_999_999`, the excess contributes to whole seconds,
    // increasing epochSeconds. The remainder forms the new value of nanosecondsOfSecond.
    val instant2 = Instant.fromEpochSeconds(1_000_000, nanosecondAdjustment = 100_123_456_789)
    println(instant2.epochSeconds)
    println(instant2.nanosecondsOfSecond)

    // When nanosecondAdjustment is negative, epochSeconds is decreased
    // to offset the negative nanoseconds and ensure nanosecondsOfSecond remains non-negative.
    val instant3 = Instant.fromEpochSeconds(1_000_000, nanosecondAdjustment = -100_876_543_211)
    println(instant3.epochSeconds)
    println(instant3.nanosecondsOfSecond)
}
```

```text title="Output"
999999
123456789
1000100
123456789
999899
123456789
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L26)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
