# Duration.Companion.days

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a `Duration` equal to this `Int` number of days.

Note that a day in this conversion always represents exactly 24 hours.
This is different from calendar days which may be longer or shorter
than 24 hours when a daylight saving transition happens on that day.

@sample samples.time.Durations.fromDays

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Int.days: Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L246)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Long.days: Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L258)

Returns a `Duration` equal to this `Long` number of days.

Note that a day in this conversion always represents exactly 24 hours.
This is different from calendar days which may be longer or shorter
than 24 hours when a daylight saving transition happens on that day.

@sample samples.time.Durations.fromDays

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Double.days: Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L270)

Returns a `Duration` equal to this `Double` number of days.

Depending on its magnitude, the value is rounded to an integer number of nanoseconds or milliseconds.

Note that a day in this conversion always represents exactly 24 hours.
This is different from calendar days which may be longer or shorter
than 24 hours when a daylight saving transition happens on that day.

@throws IllegalArgumentException if this `Double` value is `NaN`.
@sample samples.time.Durations.fromDays

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
    println(366.days)
    println(0.5.days)

    // Large values can be converted to an infinite duration
    println(100_000_000_000.days)

    assertFailsWith<IllegalArgumentException> { Double.NaN.days }
}
```

```text title="Output"
366d
12h
Infinity
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L161)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
