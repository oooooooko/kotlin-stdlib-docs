# Instant.toString

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Converts this instant to the ISO 8601 string representation, for example, `2023-01-02T23:40:57.120Z`.

The representation uses the UTC-SLS time scale instead of UTC.
In practice, this means that leap second handling will not be readjusted to the UTC.
Leap seconds will not be added or skipped, so it is impossible to acquire a string
where the component for seconds is 60, and for any day, it's possible to observe 23:59:59.

@see parse
@sample samples.time.Instants.toStringSample

## Declarations and overloads

### 1. Common

```kotlin
public override fun toString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L256)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // The string representation of the current instant in ISO 8601 format.
    val currentInstant = Clock.System.now()
    println(currentInstant.toString())
    // The string representation of the Unix epoch.
    val unixEpochInstant = Instant.fromEpochSeconds(0)
    println(unixEpochInstant.toString())
    // The string representation of an instant.
    val instant = Instant.fromEpochMilliseconds(1_000_000_000_123)
    println(instant.toString())
}
```

```text title="Output"
2026-11-04T02:16:16.622229Z
1970-01-01T00:00:00Z
2001-09-09T01:46:40.123Z
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L103)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
