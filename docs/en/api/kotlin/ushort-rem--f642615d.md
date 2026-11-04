# UShort.rem

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Calculates the remainder of truncating division of this value (dividend) by the other value (divisor).

The result is always less than the divisor.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline operator fun rem(other: UByte): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L145)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline operator fun rem(other: UShort): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L153)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline operator fun rem(other: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L161)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline operator fun rem(other: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L169)

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
    val source = 5.toUShort()
    val result = source.`rem`(2.toUByte())
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
