# TimeMark.hasNotPassedNow

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns false if this time mark has not passed according to the time source from which this mark was taken.

Note that the value returned by this function can change on subsequent invocations.
If the time source is monotonic, it can change only from `true` to `false`, namely, when the time mark becomes behind the current point of the time source.

## Declarations and overloads

### 1. Common

```kotlin
public fun hasNotPassedNow(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L188)

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
import kotlin.time.*

fun main() {
    val source = TimeSource.Monotonic.markNow()
    val result = source.`hasNotPassedNow`()
    println(result)
}
```

```text title="Output"
false
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
