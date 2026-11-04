# toUShort

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Converts this `Byte` value to `UShort`.

If this value is positive, the resulting `UShort` value represents the same numerical value as this `Byte`.

The least significant 8 bits of the resulting `UShort` value are the same as the bits of this `Byte` value,
whereas the most significant 8 bits are filled with the sign bit of this value.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.toUShort(): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L413)

### 2. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.toUShort(): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L425)

Converts this `Short` value to `UShort`.

If this value is positive, the resulting `UShort` value represents the same numerical value as this `Short`.

The resulting `UShort` value has the same binary representation as this `Short` value.

### 3. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.toUShort(): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L436)

Converts this `Int` value to `UShort`.

If this value is positive and less than or equals to `UShort.MAX_VALUE`, the resulting `UShort` value represents
the same numerical value as this `Int`.

The resulting `UShort` value is represented by the least significant 16 bits of this `Int` value.

### 4. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.toUShort(): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L448)

Converts this `Long` value to `UShort`.

If this value is positive and less than or equals to `UShort.MAX_VALUE`, the resulting `UShort` value represents
the same numerical value as this `Long`.

The resulting `UShort` value is represented by the least significant 16 bits of this `Long` value.

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
    val result = source.`toUShort`()
    println(result)
}
```

```text title="Output"
5
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
