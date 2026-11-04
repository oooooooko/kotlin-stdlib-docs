# takeLowestOneBit

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a number having a single bit set in the position of the least significant set bit of this `Int` number,
or zero, if this number is zero.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun Int.takeLowestOneBit(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L35)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun Long.takeLowestOneBit(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L95)

Returns a number having a single bit set in the position of the least significant set bit of this `Long` number,
or zero, if this number is zero.

### 3. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun Byte.takeLowestOneBit(): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L157)

Returns a number having a single bit set in the position of the least significant set bit of this `Byte` number,
or zero, if this number is zero.

### 4. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun Short.takeLowestOneBit(): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L224)

Returns a number having a single bit set in the position of the least significant set bit of this `Short` number,
or zero, if this number is zero.

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UInt.takeLowestOneBit(): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L38)

Returns a number having a single bit set in the position of the least significant set bit of this `UInt` number,
or zero, if this number is zero.

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun ULong.takeLowestOneBit(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L105)

Returns a number having a single bit set in the position of the least significant set bit of this `ULong` number,
or zero, if this number is zero.

### 7. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UByte.takeLowestOneBit(): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L170)

Returns a number having a single bit set in the position of the least significant set bit of this `UByte` number,
or zero, if this number is zero.

### 8. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UShort.takeLowestOneBit(): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L236)

Returns a number having a single bit set in the position of the least significant set bit of this `UShort` number,
or zero, if this number is zero.

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
    val source = 5
    val result = source.`takeLowestOneBit`()
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
