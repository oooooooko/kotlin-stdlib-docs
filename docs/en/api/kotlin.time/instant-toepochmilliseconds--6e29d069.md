# Instant.toEpochMilliseconds

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the number of milliseconds from the epoch instant `1970-01-01T00:00:00Z`.

Any fractional part of a millisecond is rounded toward zero to the whole number of milliseconds.

If the result does not fit in `Long`,
returns `Long.MAX_VALUE` for a positive result or `Long.MIN_VALUE` for a negative result.

@see fromEpochMilliseconds
@sample samples.time.Instants.toEpochMilliseconds

## Declarations and overloads

### 1. Common

```kotlin
public fun toEpochMilliseconds(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L137)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    val currentInstant = Clock.System.now()
    // The number of whole milliseconds that have passed since the Unix epoch.
    println(currentInstant.toEpochMilliseconds())

    // When an Instant is created with fromEpochMilliseconds,
    // toEpochMilliseconds will return the exact value provided.
    val instant1 = Instant.fromEpochMilliseconds(0)
    println(instant1.toEpochMilliseconds())
    val instant2 = Instant.fromEpochMilliseconds(1_000_000_000_123)
    println(instant2.toEpochMilliseconds())

    // Any fractional part of a millisecond is rounded toward zero to the whole number of milliseconds.
    val instant3 = Instant.fromEpochSeconds(1_000_000_000, nanosecondAdjustment = 123_999_999)
    println(instant3.toEpochMilliseconds())
}
```

```text title="Output"
1793758576454
0
1000000000123
1000000000123
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L47)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
