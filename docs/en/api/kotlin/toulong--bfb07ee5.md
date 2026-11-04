# toULong

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Converts this `Byte` value to `ULong`.

If this value is positive, the resulting `ULong` value represents the same numerical value as this `Byte`.

The least significant 8 bits of the resulting `ULong` value are the same as the bits of this `Byte` value,
whereas the most significant 56 bits are filled with the sign bit of this value.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.toULong(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L439)

### 2. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.toULong(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L451)

Converts this `Short` value to `ULong`.

If this value is positive, the resulting `ULong` value represents the same numerical value as this `Short`.

The least significant 16 bits of the resulting `ULong` value are the same as the bits of this `Short` value,
whereas the most significant 48 bits are filled with the sign bit of this value.

### 3. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.toULong(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L463)

Converts this `Int` value to `ULong`.

If this value is positive, the resulting `ULong` value represents the same numerical value as this `Int`.

The least significant 32 bits of the resulting `ULong` value are the same as the bits of this `Int` value,
whereas the most significant 32 bits are filled with the sign bit of this value.

### 4. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.toULong(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L475)

Converts this `Long` value to `ULong`.

If this value is positive, the resulting `ULong` value represents the same numerical value as this `Long`.

The resulting `ULong` value has the same binary representation as this `Long` value.

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Float.toULong(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L487)

Converts this `Float` value to `ULong`.

The fractional part, if any, is rounded down towards zero.
Returns zero if this `Float` value is negative or `NaN`, `ULong.MAX_VALUE` if it's bigger than `ULong.MAX_VALUE`.

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Double.toULong(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L497)

Converts this `Double` value to `ULong`.

The fractional part, if any, is rounded down towards zero.
Returns zero if this `Double` value is negative or `NaN`, `ULong.MAX_VALUE` if it's bigger than `ULong.MAX_VALUE`.

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
    val result = source.`toULong`()
    println(result)
}
```

```text title="Output"
5
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
