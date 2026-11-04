# Instant.Companion.parse

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses an ISO 8601 string that represents an instant (for example, `2020-08-30T18:43:00Z`).

Guaranteed to parse all strings that `Instant.toString` produces.

Examples of instants in the ISO 8601 format:
- `2020-08-30T18:43:00Z`
- `2020-08-30T18:43:00.50Z`
- `2020-08-30T18:43:00.123456789Z`
- `2020-08-30T18:40:00+03:00`
- `2020-08-30T18:40:00+03:30:20`
* `2020-01-01T23:59:59.123456789+01`
* `+12020-01-31T23:59:59Z`

See ISO-8601-1:2019, 5.4.2.1b), excluding the format without the offset.

The string is considered to represent time on the UTC-SLS time scale instead of UTC.
In practice, this means that, even if there is a leap second on the given day, it will not affect how the
time is parsed, even if it's in the last 1000 seconds of the day.
Instead, even if there is a negative leap second on the given day, 23:59:59 is still considered a valid time.
23:59:60 is invalid on UTC-SLS, so parsing it will fail.

@throws IllegalArgumentException if the text cannot be parsed or the boundaries of `Instant` are exceeded.

@see Instant.parseOrNull for a version of this function that returns `null` on failure.
@see Instant.toString for formatting.
@sample samples.time.Instants.parsing

## Declarations and overloads

### 1. Common

```kotlin
public fun parse(input: CharSequence): Instant
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L358)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Parsing a string that represents the Unix epoch.
    val unixEpochInstant = Instant.parse("1970-01-01T00:00:00Z")
    println(unixEpochInstant.epochSeconds)

    // Parsing an ISO 8601 string with a time zone offset.
    val instant = Instant.parse("2020-08-30T18:40:00+03:00")
    // Instants are presented in the UTC time zone when converted to string.
    println(instant.toString())
}
```

```text title="Output"
0
2020-08-30T15:40:00Z
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L154)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
