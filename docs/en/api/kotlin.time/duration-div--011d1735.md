# Duration.div

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a duration whose value is this duration value divided by the given `scale` number.

@throws IllegalArgumentException if the operation results in an undefined value for the given arguments,
e.g. when dividing zero duration by zero.

## Declarations and overloads

### 1. Common

```kotlin
public operator fun div(scale: Int): Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L462)

### 2. Common

```kotlin
public operator fun div(scale: Double): Duration
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L492)

Returns a duration whose value is this duration value divided by the given `scale` number.

@throws IllegalArgumentException if the operation results in an undefined value for the given arguments,
e.g. when dividing an infinite duration by infinity or zero duration by zero.

### 3. Common

```kotlin
public operator fun div(other: Duration): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L509)

Returns a number that is the ratio of this and `other` duration values.

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
    val source = 2.seconds
    val result = source.`div`(2)
    println(result)
}
```

```text title="Output"
1s
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
