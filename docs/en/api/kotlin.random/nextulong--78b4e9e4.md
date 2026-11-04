# nextULong

`kotlin.random` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Gets the next random `ULong` from the random number generator.

Generates a `ULong` random value uniformly distributed between `ULong.MIN_VALUE` and `ULong.MAX_VALUE` (inclusive).

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun Random.nextULong(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L61)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public fun Random.nextULong(until: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L69)

Gets the next random `ULong` from the random number generator less than the specified `until` bound.

Generates a `ULong` random value uniformly distributed between `0` (inclusive) and the specified `until` bound (exclusive).

@throws IllegalArgumentException if `until` is zero.

### 3. Common

```kotlin
@SinceKotlin("1.5")
public fun Random.nextULong(from: ULong, until: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L79)

Gets the next random `ULong` from the random number generator in the specified range.

Generates a `ULong` random value uniformly distributed between the specified `from` (inclusive) and `until` (exclusive) bounds.

@throws IllegalArgumentException if `from` is greater than or equal to `until`.

### 4. Common

```kotlin
@SinceKotlin("1.5")
public fun Random.nextULong(range: ULongRange): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L97)

Gets the next random `ULong` from the random number generator in the specified `range`.

Generates a `ULong` random value uniformly distributed in the specified `range`:
from `range.start` inclusive to `range.endInclusive` inclusive.

@throws IllegalArgumentException if `range` is empty.

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
import kotlin.random.*

fun main() {
    val source = Random(42)
    val result = source.`nextULong`()
    println(result)
}
```

```text title="Output"
4174779793377534016
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
