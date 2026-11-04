# Instant.compareTo

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Compares `this` instant with the `other` instant.

Returns zero if this instant represents the same moment as the other (meaning they are equal to one another),
a negative number if this instant is earlier than the other,
and a positive number if this instant is later than the other.

@sample samples.time.Instants.compareToSample

## Declarations and overloads

### 1. Common

```kotlin
public override operator fun compareTo(other: Instant): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L232)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    val instant1 = Instant.parse("1970-01-01T00:00:00Z") // The Unix epoch.
    val instant2 = Instant.parse("2025-01-06T13:36:44Z")
    val instant3 = Instant.fromEpochSeconds(0) // The Unix epoch.

    println(instant1 < instant2)
    println(instant3 > instant1)
    println(instant3 == instant1)
}
```

```text title="Output"
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L92)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
