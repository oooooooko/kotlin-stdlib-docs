# Duration.toComponents

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Splits this duration into days, hours, minutes, seconds, and nanoseconds and executes the given `action` with these components.
The result of `action` is returned as the result of this function.

- `nanoseconds` represents the whole number of nanoseconds in this duration, and its absolute value is less than 1_000_000_000;
- `seconds` represents the whole number of seconds in this duration, and its absolute value is less than 60;
- `minutes` represents the whole number of minutes in this duration, and its absolute value is less than 60;
- `hours` represents the whole number of hours in this duration, and its absolute value is less than 24;
- `days` represents the whole number of days in this duration.

Note that a day in this conversion always represents exactly 24 hours.
This is different from calendar days which may be longer or shorter
than 24 hours when a daylight saving transition happens on that day.

  Infinite durations are represented as either `Long.MAX_VALUE` days, or `Long.MIN_VALUE` days (depending on the sign of infinity),
  and zeroes in the lower components.

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T> toComponents(action: (days: Long, hours: Int, minutes: Int, seconds: Int, nanoseconds: Int) -> T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L553)

### 2. Common

```kotlin
public inline fun <T> toComponents(action: (hours: Long, minutes: Int, seconds: Int, nanoseconds: Int) -> T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L575)

Splits this duration into hours, minutes, seconds, and nanoseconds and executes the given `action` with these components.
The result of `action` is returned as the result of this function.

- `nanoseconds` represents the whole number of nanoseconds in this duration, and its absolute value is less than 1_000_000_000;
- `seconds` represents the whole number of seconds in this duration, and its absolute value is less than 60;
- `minutes` represents the whole number of minutes in this duration, and its absolute value is less than 60;
- `hours` represents the whole number of hours in this duration.

  Infinite durations are represented as either `Long.MAX_VALUE` hours, or `Long.MIN_VALUE` hours (depending on the sign of infinity),
  and zeroes in the lower components.

### 3. Common

```kotlin
public inline fun <T> toComponents(action: (minutes: Long, seconds: Int, nanoseconds: Int) -> T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L592)

Splits this duration into minutes, seconds, and nanoseconds and executes the given `action` with these components.
The result of `action` is returned as the result of this function.

- `nanoseconds` represents the whole number of nanoseconds in this duration, and its absolute value is less than 1_000_000_000;
- `seconds` represents the whole number of seconds in this duration, and its absolute value is less than 60;
- `minutes` represents the whole number of minutes in this duration.

  Infinite durations are represented as either `Long.MAX_VALUE` minutes, or `Long.MIN_VALUE` minutes (depending on the sign of infinity),
  and zeroes in the lower components.

### 4. Common

```kotlin
public inline fun <T> toComponents(action: (seconds: Long, nanoseconds: Int) -> T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L608)

Splits this duration into seconds, and nanoseconds and executes the given `action` with these components.
The result of `action` is returned as the result of this function.

- `nanoseconds` represents the whole number of nanoseconds in this duration, and its absolute value is less than 1_000_000_000;
- `seconds` represents the whole number of seconds in this duration.

  Infinite durations are represented as either `Long.MAX_VALUE` seconds, or `Long.MIN_VALUE` seconds (depending on the sign of infinity),
  and zero nanoseconds.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.math.nextDown
import kotlin.math.pow
import kotlin.test.*
import kotlin.time.*
import kotlin.random.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds

private val units = DurationUnit.entries

fun main() {

        (36.hours + 90.minutes + 90.seconds + 1500.milliseconds).run {
            toComponents { days, hours, minutes, seconds, nanoseconds ->
                println(days)
                println(hours)
                println(minutes)
                println(seconds)
                println(nanoseconds)
            }
        }
    
}
```

```text title="Output"
1
13
31
31
500000000
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/time/DurationTest.kt#L282)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
