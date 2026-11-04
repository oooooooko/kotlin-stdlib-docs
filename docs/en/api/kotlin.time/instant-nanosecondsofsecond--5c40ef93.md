# Instant.nanosecondsOfSecond

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The number of nanoseconds by which this instant is later than `epochSeconds` from the epoch instant.

The value is always non-negative and lies in the range `0..999_999_999`.

@see fromEpochSeconds
@sample samples.time.Instants.epochSecondsAndNanosecondsOfSecond
@sample samples.time.Instants.fromEpochSecondsProperties

## Declarations and overloads

### 1. Common

```kotlin
public val nanosecondsOfSecond: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L121)

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
    // The number of whole seconds that have passed since the Unix epoch.
    println(currentInstant.epochSeconds)
    // The number of nanoseconds that passed since the start of the second.
    println(currentInstant.nanosecondsOfSecond)
}
```

```text title="Output"
1793758576
426344000
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L17)

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
