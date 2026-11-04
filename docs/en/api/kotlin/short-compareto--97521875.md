# Short.compareTo

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Compares this value with the specified value for order.
Returns zero if this value is equal to the specified other value, a negative number if it's less than other,
or a positive number if it's greater than other.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public operator fun compareTo(other: Byte): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L408)

### 2. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public override operator fun compareTo(other: Short): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L416)

### 3. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public operator fun compareTo(other: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L424)

### 4. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public operator fun compareTo(other: Long): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L432)

### 5. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public operator fun compareTo(other: Float): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L440)

### 6. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public operator fun compareTo(other: Double): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L448)

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
    val source = 5.toShort()
    val result = source.`compareTo`(2.toByte())
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
