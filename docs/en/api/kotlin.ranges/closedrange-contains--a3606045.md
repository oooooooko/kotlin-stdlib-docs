# ClosedRange.contains

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Checks whether the specified `value` belongs to the range.

A value belongs to the closed range if it is greater than or equal to the `start` bound and less than or equal to the `endInclusive` bound.

@sample samples.ranges.Ranges.closedRangeContains

## Declarations and overloads

### 1. Common

```kotlin
public operator fun contains(value: T): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Range.kt#L25)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val range = 1..10
    println(5 in range)
    // Both lower and upper bounds are contained within the range
    println(1 in range)
    println(10 in range)
    // Values lying outside bounds are not contained within the range
    println(0 in range)
    println(11 in range)

    val stringRange = "AA".."ZZ"
    println("AA" in stringRange)
    println("AB" in stringRange)
    println("ZZ" in stringRange)
    // Note that "contains" relies on "compareTo" implementation, so in some cases results may not be intuitive.
    // Here, "AAA" is lexicographically greater than "AA", but lower than "ZZ", thus the range contains it.
    println("AAA" in stringRange)
}
```

```text title="Output"
true
true
true
false
false
true
true
true
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L140)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
