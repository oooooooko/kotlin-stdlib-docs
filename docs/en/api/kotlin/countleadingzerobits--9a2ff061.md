# countLeadingZeroBits

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Counts the number of consecutive most significant bits that are zero in the binary representation of this `Int` number.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun Int.countLeadingZeroBits(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L16)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun Long.countLeadingZeroBits(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L76)

Counts the number of consecutive most significant bits that are zero in the binary representation of this `Long` number.

### 3. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun Byte.countLeadingZeroBits(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L135)

Counts the number of consecutive most significant bits that are zero in the binary representation of this `Byte` number.

### 4. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun Short.countLeadingZeroBits(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Numbers.kt#L201)

Counts the number of consecutive most significant bits that are zero in the binary representation of this `Short` number.

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UInt.countLeadingZeroBits(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L16)

Counts the number of consecutive most significant bits that are zero in the binary representation of this `UInt` number.

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun ULong.countLeadingZeroBits(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L83)

Counts the number of consecutive most significant bits that are zero in the binary representation of this `ULong` number.

### 7. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UByte.countLeadingZeroBits(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L148)

Counts the number of consecutive most significant bits that are zero in the binary representation of this `UByte` number.

### 8. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun UShort.countLeadingZeroBits(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UNumbers.kt#L214)

Counts the number of consecutive most significant bits that are zero in the binary representation of this `UShort` number.

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
    val result = source.`countLeadingZeroBits`()
    println(result)
}
```

```text title="Output"
29
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
