# rotateRight

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Rotates the binary representation of this `Int` number right by the specified `bitCount` number of bits.
The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.

Rotating the number right by a negative bit count is the same as rotating it left by the negated bit count:
`number.rotateRight(-n) == number.rotateLeft(n)`

Rotating by a multiple of `Int.SIZE_BITS` (32) returns the same number, or more generally
`number.rotateRight(n) == number.rotateRight(n % 32)`

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.6")
public expect fun Int.rotateRight(bitCount: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L56)

### 2. Common

```kotlin
@SinceKotlin("1.6")
public expect fun Long.rotateRight(bitCount: Int): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L115)

Rotates the binary representation of this `Long` number right by the specified `bitCount` number of bits.
The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.

Rotating the number right by a negative bit count is the same as rotating it left by the negated bit count:
`number.rotateRight(-n) == number.rotateLeft(n)`

Rotating by a multiple of `Long.SIZE_BITS` (64) returns the same number, or more generally
`number.rotateRight(n) == number.rotateRight(n % 64)`

### 3. Common

```kotlin
@SinceKotlin("1.6")
public fun Byte.rotateRight(bitCount: Int): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L180)

Rotates the binary representation of this `Byte` number right by the specified `bitCount` number of bits.
The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.

Rotating the number right by a negative bit count is the same as rotating it left by the negated bit count:
`number.rotateRight(-n) == number.rotateLeft(n)`

Rotating by a multiple of `Byte.SIZE_BITS` (8) returns the same number, or more generally
`number.rotateRight(n) == number.rotateRight(n % 8)`

### 4. Common

```kotlin
@SinceKotlin("1.6")
public fun Short.rotateRight(bitCount: Int): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L247)

Rotates the binary representation of this `Short` number right by the specified `bitCount` number of bits.
The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.

Rotating the number right by a negative bit count is the same as rotating it left by the negated bit count:
`number.rotateRight(-n) == number.rotateLeft(n)`

Rotating by a multiple of `Short.SIZE_BITS` (16) returns the same number, or more generally
`number.rotateRight(n) == number.rotateRight(n % 16)`

### 5. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun UInt.rotateRight(bitCount: Int): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L61)

Rotates the binary representation of this `UInt` number right by the specified `bitCount` number of bits.
The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.

Rotating the number right by a negative bit count is the same as rotating it left by the negated bit count:
`number.rotateRight(-n) == number.rotateLeft(n)`

Rotating by a multiple of `UInt.SIZE_BITS` (32) returns the same number, or more generally
`number.rotateRight(n) == number.rotateRight(n % 32)`

### 6. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun ULong.rotateRight(bitCount: Int): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L127)

Rotates the binary representation of this `ULong` number right by the specified `bitCount` number of bits.
The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.

Rotating the number right by a negative bit count is the same as rotating it left by the negated bit count:
`number.rotateRight(-n) == number.rotateLeft(n)`

Rotating by a multiple of `ULong.SIZE_BITS` (64) returns the same number, or more generally
`number.rotateRight(n) == number.rotateRight(n % 64)`

### 7. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun UByte.rotateRight(bitCount: Int): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L193)

Rotates the binary representation of this `UByte` number right by the specified `bitCount` number of bits.
The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.

Rotating the number right by a negative bit count is the same as rotating it left by the negated bit count:
`number.rotateRight(-n) == number.rotateLeft(n)`

Rotating by a multiple of `UByte.SIZE_BITS` (8) returns the same number, or more generally
`number.rotateRight(n) == number.rotateRight(n % 8)`

### 8. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun UShort.rotateRight(bitCount: Int): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L259)

Rotates the binary representation of this `UShort` number right by the specified `bitCount` number of bits.
The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.

Rotating the number right by a negative bit count is the same as rotating it left by the negated bit count:
`number.rotateRight(-n) == number.rotateLeft(n)`

Rotating by a multiple of `UShort.SIZE_BITS` (16) returns the same number, or more generally
`number.rotateRight(n) == number.rotateRight(n % 16)`

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
    val result = source.`rotateRight`(2)
    println(result)
}
```

```text title="Output"
1073741825
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
