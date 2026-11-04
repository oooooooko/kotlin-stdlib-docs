# Instant.Companion.DISTANT_PAST

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

An instant value that is far in the past.

`isDistantPast` returns true for this value and all earlier ones.

@sample samples.time.Instants.isDistantPast

## Declarations and overloads

### 1. Common

```kotlin
public val DISTANT_PAST: Instant // -100001-12-31T23:59:59.999999999Z
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L417)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Checking if an instant is so far in the past that it's probably irrelevant.
    val tenThousandYearsBC = Instant.parse("-10000-01-01T00:00:00Z")
    println(tenThousandYearsBC.isDistantPast)

    // Instant.DISTANT_PAST is the latest instant that is considered far in the past.
    println(Instant.DISTANT_PAST)
    println(Instant.DISTANT_PAST.isDistantPast)

    // All instants earlier than Instant.DISTANT_PAST are considered to be far in the past.
    val earlierThanDistantPast = Instant.DISTANT_PAST - 1.nanoseconds
    println(earlierThanDistantPast)
    println(earlierThanDistantPast.isDistantPast)

    // All instants later than Instant.DISTANT_PAST are not considered to be far in the past.
    val laterThanDistantPast = Instant.DISTANT_PAST + 1.nanoseconds
    println(laterThanDistantPast)
    println(laterThanDistantPast.isDistantPast)
}
```

```text title="Output"
false
-100001-12-31T23:59:59.999999999Z
true
-100001-12-31T23:59:59.999999998Z
true
-100000-01-01T00:00:00Z
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L183)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
