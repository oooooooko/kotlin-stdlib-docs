# Duration.toInt

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the value of this duration expressed as an `Int` number of the specified `unit`.

The part of this duration that is smaller than the specified unit
becomes a fractional part of the result and then is truncated (rounded towards zero).

If the result doesn't fit in the range of `Int` type, it is coerced into that range:
- `Int.MIN_VALUE` is returned if it's less than `Int.MIN_VALUE`,
- `Int.MAX_VALUE` is returned if it's greater than `Int.MAX_VALUE`.

An infinite duration value is converted either to `Int.MAX_VALUE` or `Int.MIN_VALUE` depending on its sign.

@sample samples.time.Durations.toIntUnits

## Declarations and overloads

### 1. Common

```kotlin
public fun toInt(unit: DurationUnit): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L688)

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
    println(2900.milliseconds.toInt(DurationUnit.SECONDS))
    println(3.hours.toInt(DurationUnit.MINUTES))

    println(1.minutes.toInt(DurationUnit.NANOSECONDS) == Int.MAX_VALUE)
    println((-Duration.INFINITE).toInt(DurationUnit.DAYS) == Int.MIN_VALUE)
}
```

```text title="Output"
2
180
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/durations.kt#L227)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
