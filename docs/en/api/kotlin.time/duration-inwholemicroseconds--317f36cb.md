# Duration.inWholeMicroseconds

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The value of this duration expressed as a `Long` number of microseconds.

The part of this duration that is smaller than a microsecond
becomes a fractional part of the result and then is truncated (rounded towards zero).

If the result doesn't fit in the range of `Long` type, it is coerced into that range:
- `Long.MIN_VALUE` is returned if it's less than `Long.MIN_VALUE`,
- `Long.MAX_VALUE` is returned if it's greater than `Long.MAX_VALUE`.

An infinite duration value is converted either to `Long.MAX_VALUE` or `Long.MIN_VALUE` depending on its sign.

@sample samples.time.Durations.inWholeMicroseconds

## Declarations and overloads

### 1. Common

```kotlin
public val inWholeMicroseconds: Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L777)

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
    println(25_900.nanoseconds.inWholeMicroseconds)

    println(1_000_000_000.days.inWholeMicroseconds == Long.MAX_VALUE)
    println((-Duration.INFINITE).inWholeMicroseconds == Long.MIN_VALUE)
}
```

```text title="Output"
25
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L180)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
