# Clock.now

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the `Instant` corresponding to the current time, according to this clock.

Calling `now` later is not guaranteed to return a larger `Instant`.
In particular, for `Clock.System`, the opposite is completely expected,
and it must be taken into account.
See the `System` documentation for details.

Even though `Instant` is defined to be on the UTC-SLS time scale, which enforces a specific way of handling
leap seconds, `now` is not guaranteed to handle leap seconds in any specific way.

Note that while `Instant` supports nanosecond precision,
the actual precision of the returned `Instant` depends on the resolution of the `Clock` implementation.

@sample samples.time.Clocks.system
@sample samples.time.Clocks.dependencyInjection

## Declarations and overloads

### 1. Common

```kotlin
public fun now(): Instant
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Clock.kt#L21)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds



fun main() {
    // The current instant according to the system clock.
    val currentInstant = Clock.System.now()
    // The number of whole milliseconds that have passed since the Unix epoch.
    println(currentInstant.toEpochMilliseconds())
}
```

```text title="Output"
1793758575430
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/clocks.kt#L13)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds



fun main() {
    fun formatCurrentTime(clock: Clock): String =
        clock.now().toString()

    // In the production code:
    val currentTimeInProduction = formatCurrentTime(Clock.System)
    // Testing this value is tricky because it changes all the time.
    println(currentTimeInProduction)

    // In the test code:
    val testClock = object : Clock {
        override fun now(): Instant = Instant.parse("2023-01-02T22:35:01Z")
    }
    // Then, one can write a completely deterministic test:
    val currentTimeForTests = formatCurrentTime(testClock)
    println(currentTimeForTests)
}
```

```text title="Output"
2026-11-04T02:16:15.469505Z
2023-01-02T22:35:01Z
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/clocks.kt#L21)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
