# Duration.toIsoString

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an ISO-8601 based string representation of this duration.

The returned value is presented in the format `PThHmMs.fS`, where `h`, `m`, `s` are the integer components of this duration (see `toComponents`)
and `f` is a fractional part of second. Depending on the roundness of the value the fractional part can be formatted with either
0, 3, 6, or 9 decimal digits.

The infinite duration is represented as `"PT9999999999999H"` which is larger than any possible finite duration in Kotlin.

Negative durations are indicated with the sign `-` in the beginning of the returned string, for example, `"-PT5M30S"`.

@sample samples.time.Durations.toIsoString

## Declarations and overloads

### 1. Common

```kotlin
public fun toIsoString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L922)

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
    println(25.nanoseconds.toIsoString())
    println(120.3.milliseconds.toIsoString())
    println(30.5.seconds.toIsoString())
    println(30.5.minutes.toIsoString())
    println(86420.seconds.toIsoString())
    println(2.days.toIsoString())
    println(Duration.ZERO.toIsoString())
    println(Duration.INFINITE.toIsoString())
}
```

```text title="Output"
PT0.000000025S
PT0.120300S
PT30.500S
PT30M30S
PT24H0M20S
PT48H
PT0S
PT9999999999999H
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L22)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
