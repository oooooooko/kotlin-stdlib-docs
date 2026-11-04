# UIntProgression.Companion.fromClosedRange

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates UIntProgression within the specified bounds of a closed range.

The progression starts with the `rangeStart` value and goes toward the `rangeEnd` value not excluding it, with the specified `step`.
In order to go backwards the `step` must be negative.

`step` must be greater than `Int.MIN_VALUE` and not equal to zero.

## Declarations and overloads

### 1. Common

```kotlin
public fun fromClosedRange(rangeStart: UInt, rangeEnd: UInt, step: Int): UIntProgression
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UIntRange.kt#L106)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.ranges.*

fun main() {
    val source = kotlin.ranges.UIntProgression.Companion
    val result = source.`fromClosedRange`(2u, 2u, 2)
    println(result)
}
```

```text title="Output"
2..2 step 2
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
