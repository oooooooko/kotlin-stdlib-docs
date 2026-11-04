# TimeSource.Monotonic.ValueTimeMark.elapsedNow

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the amount of time passed from this mark measured with the time source from which this mark was taken.

Note that the value returned by this function can change on subsequent invocations.

The value returned by this function may be infinitely large (in terms of `Duration.isInfinite`).

@throws IllegalArgumentException an implementation may throw if calculating the elapsed time involves
adding a positive infinite duration to an infinitely distant past time mark or
a negative infinite duration to an infinitely distant future time mark.

## Declarations and overloads

### 1. Common

```kotlin
override fun elapsedNow(): Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L71)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*
import kotlin.time.*
import kotlin.time.Duration.Companion.nanoseconds



fun main() {

        val baseMark = TimeSource.Monotonic.markNow()
        val longDuration = Long.MAX_VALUE.nanoseconds

        val pastMark = baseMark - longDuration
        val infiniteFutureMark1 = pastMark + longDuration * 3

        println(infiniteFutureMark1.elapsedNow())
    
}
```

```text title="Output"
-Infinity
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/jvm/test/time/TimeMarkJVMTest.kt#L19)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
