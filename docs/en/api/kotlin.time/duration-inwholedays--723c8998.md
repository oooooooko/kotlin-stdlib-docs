# Duration.inWholeDays

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The value of this duration expressed as a `Long` number of days.

The part of this duration that is smaller than a day
becomes a fractional part of the result and then is truncated (rounded towards zero).

Note that a day in this conversion always represents exactly 24 hours.
This is different from calendar days which may be longer or shorter
than 24 hours when a daylight saving transition happens on that day.

An infinite duration value is converted either to `Long.MAX_VALUE` or `Long.MIN_VALUE` depending on its sign.

@sample samples.time.Durations.inWholeDays

## Declarations and overloads

### 1. Common

```kotlin
public val inWholeDays: Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L706)

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
    println(23.5.hours.inWholeDays)
    println(48.hours.inWholeDays)

    println((-Duration.INFINITE).inWholeDays == Long.MIN_VALUE)
}
```

```text title="Output"
0
2
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L219)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
