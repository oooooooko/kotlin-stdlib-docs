# isDistantFuture

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns true if the instant is `Instant.DISTANT_FUTURE` or later.

@sample samples.time.Instants.isDistantFuture

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.3")
@WasExperimental(ExperimentalTime::class)
@kotlin.internal.InlineOnly
public inline val Instant.isDistantFuture: Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L453)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Checking if an instant is so far in the future that it's probably irrelevant.
    val yearTenThousand = Instant.parse("+10000-01-01T00:00:00Z")
    println(yearTenThousand.isDistantFuture)

    // Instant.DISTANT_FUTURE is the earliest instant that is considered far in the future.
    println(Instant.DISTANT_FUTURE)
    println(Instant.DISTANT_FUTURE.isDistantFuture)

    // All instants later than Instant.DISTANT_FUTURE are considered to be far in the future.
    val laterThanDistantFuture = Instant.DISTANT_FUTURE + 1.nanoseconds
    println(laterThanDistantFuture)
    println(laterThanDistantFuture.isDistantFuture)

    // All instants earlier than Instant.DISTANT_FUTURE are not considered to be far in the future.
    val earlierThanDistantFuture = Instant.DISTANT_FUTURE - 1.nanoseconds
    println(earlierThanDistantFuture)
    println(earlierThanDistantFuture.isDistantFuture)
}
```

```text title="Output"
false
+100000-01-01T00:00:00Z
true
+100000-01-01T00:00:00.000000001Z
true
+99999-12-31T23:59:59.999999999Z
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L204)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
