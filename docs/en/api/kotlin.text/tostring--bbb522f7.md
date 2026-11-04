# toString

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a string representation of this `Byte` value in the specified `radix`.

@throws IllegalArgumentException when `radix` is not a valid radix for number to string conversion.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Byte.toString(radix: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L650)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Short.toString(radix: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L658)

Returns a string representation of this `Short` value in the specified `radix`.

@throws IllegalArgumentException when `radix` is not a valid radix for number to string conversion.

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Int.toString(radix: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L666)

Returns a string representation of this `Int` value in the specified `radix`.

@throws IllegalArgumentException when `radix` is not a valid radix for number to string conversion.

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Long.toString(radix: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L674)

Returns a string representation of this `Long` value in the specified `radix`.

@throws IllegalArgumentException when `radix` is not a valid radix for number to string conversion.

### 5. Common

```kotlin
@SinceKotlin("1.5")
//@kotlin.internal.InlineOnly
public /*inline*/ fun UByte.toString(radix: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L10)

### 6. Common

```kotlin
@SinceKotlin("1.5")
//@kotlin.internal.InlineOnly
public /*inline*/ fun UShort.toString(radix: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L19)

Returns a string representation of this `Short` value in the specified `radix`.

@throws IllegalArgumentException when `radix` is not a valid radix for number to string conversion.

### 7. Common

```kotlin
@SinceKotlin("1.5")
//@kotlin.internal.InlineOnly
public /*inline*/ fun UInt.toString(radix: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L29)

Returns a string representation of this `Int` value in the specified `radix`.

@throws IllegalArgumentException when `radix` is not a valid radix for number to string conversion.

### 8. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.toString(radix: Int): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L38)

Returns a string representation of this `Long` value in the specified `radix`.

@throws IllegalArgumentException when `radix` is not a valid radix for number to string conversion.

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
import kotlin.text.*

fun main() {
    val source = 5.toByte()
    val result = source.`toString`(2)
    println(result)
}
```

```text title="Output"
101
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
