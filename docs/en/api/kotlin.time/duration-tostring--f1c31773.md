# Duration.toString

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a string representation of this duration value
expressed as a combination of numeric components, each in its own unit.

Each component is a number followed by the unit abbreviated name: `d`, `h`, `m`, `s`:
`5h`, `1d 12h`, `1h 0m 30.340s`.
The last component, usually seconds, can be a number with a fractional part.

If the duration is less than a second, it is represented as a single number
with one of sub-second units: `ms` (milliseconds), `us` (microseconds), or `ns` (nanoseconds):
`140.884ms`, `500us`, `24ns`.

A negative duration is prefixed with `-` sign and, if it consists of multiple components, surrounded with parentheses:
`-12m` and `-(1h 30m)`.

Special cases:
 - an infinite duration is formatted as `"Infinity"` or `"-Infinity"` without a unit.

It's recommended to use `toIsoString` that uses more strict ISO-8601 format instead of this `toString`
when you want to convert a duration to a string in cases of serialization, interchange, etc.

@sample samples.time.Durations.toStringDefault

## Declarations and overloads

### 1. Common

```kotlin
override fun toString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L816)

### 2. Common

```kotlin
public fun toString(unit: DurationUnit, decimals: Int = 0): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L898)

Returns a string representation of this duration value expressed in the given `unit`
and formatted with the specified `decimals` number of digits after decimal point.

Special cases:
 - an infinite duration is formatted as `"Infinity"` or `"-Infinity"` without a unit.

@param decimals the number of digits after decimal point to show. The value must be non-negative.
No more than 12 decimals will be shown, even if a larger number is requested.

@return the value of duration in the specified `unit` followed by that unit abbreviated name: `d`, `h`, `m`, `s`, `ms`, `us`, or `ns`.

@throws IllegalArgumentException if `decimals` is less than zero.

@sample samples.time.Durations.toStringDecimals

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    println(45.days)
    println(1.5.days)
    println(1230.minutes)
    println(920.minutes)
    println(1.546.seconds)
    println(25.12.milliseconds)
}
```

```text title="Output"
45d
1d 12h
20h 30m
15h 20m
1.546s
25.12ms
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L34)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    println(1230.minutes.toString(DurationUnit.DAYS, 2))
    println(1230.minutes.toString(DurationUnit.HOURS, 2))
    println(1230.minutes.toString(DurationUnit.MINUTES))
    println(1230.minutes.toString(DurationUnit.SECONDS))
}
```

```text title="Output"
0.85d
20.50h
1230m
73800s
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L44)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
