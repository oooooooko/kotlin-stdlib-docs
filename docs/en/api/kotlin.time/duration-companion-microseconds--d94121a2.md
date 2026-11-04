# Duration.Companion.microseconds

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a `Duration` equal to this `Int` number of microseconds.

@sample samples.time.Durations.fromMicroseconds

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Int.microseconds: Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L106)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Long.microseconds: Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L114)

Returns a `Duration` equal to this `Long` number of microseconds.

@sample samples.time.Durations.fromMicroseconds

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
        public inline val Double.microseconds: Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L122)

Returns a `Duration` equal to this `Double` number of microseconds.

Depending on its magnitude, the value is rounded to an integer number of nanoseconds or milliseconds.

@throws IllegalArgumentException if this `Double` value is `NaN`.
@sample samples.time.Durations.fromMicroseconds

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*
import kotlin.time.*
import kotlin.time.Duration.Companion.days
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.minutes
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    println(15.microseconds)

    // Large values can be accurately represented only with millisecond precision
    println(9000000000000_775_807.microseconds)

    // Fractional part is rounded to the nearest integer nanosecond value
    println(999.0004.microseconds)
    println(999.0009.microseconds)

    assertFailsWith<IllegalArgumentException> { Double.NaN.microseconds }
}
```

```text title="Output"
15us
104166666d 16h 0m 0.775s
999us
999.001us
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L90)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
