# Byte.rem

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Calculates the remainder of truncating division of this value (dividend) by the other value (divisor).

The result is either zero or has the same sign as the _dividend_ and has the absolute value less than the absolute value of the divisor.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Byte): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L182)

### 2. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Short): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L191)

### 3. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L200)

### 4. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L209)

### 5. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L218)

### 6. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L227)

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
import kotlin.*

fun main() {
    val source = 5.toByte()
    val result = source.`rem`(2.toByte())
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
