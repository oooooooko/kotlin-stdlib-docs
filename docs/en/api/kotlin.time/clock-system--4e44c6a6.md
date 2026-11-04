# Clock.System

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The `Clock` instance that queries the platform-specific system clock as its source of time knowledge.

Successive calls to `now` will not necessarily return increasing `Instant` values, and when they do,
these increases will not necessarily correspond to the elapsed time.

For example, when using `Clock.System`, the following could happen:
- `now` returns `2023-01-02T22:35:01Z`.
- The system queries the Internet and recognizes that its clock needs adjusting.
- `now` returns `2023-01-02T22:32:05Z`.

When you need predictable intervals between successive measurements, consider using `TimeSource.Monotonic`.

For improved testability, you should avoid using `Clock.System` directly in the implementation
and pass a `Clock` explicitly instead. For example:

@sample samples.time.Clocks.system
@sample samples.time.Clocks.dependencyInjection

## Declarations and overloads

### 1. Common

```kotlin
public object System : Clock
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Clock.kt#L40)

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
