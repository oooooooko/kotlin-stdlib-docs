# sum

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the sum of all elements in the sequence.

The operation is _terminal_.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.jvm.JvmName("sumOfByte")
public fun Sequence<Byte>.sum(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3464)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("sumOfShort")
public fun Sequence<Short>.sum(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3478)

### 3. Common

```kotlin
@kotlin.jvm.JvmName("sumOfInt")
public fun Sequence<Int>.sum(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3492)

### 4. Common

```kotlin
@kotlin.jvm.JvmName("sumOfLong")
public fun Sequence<Long>.sum(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3506)

### 5. Common

```kotlin
@kotlin.jvm.JvmName("sumOfFloat")
public fun Sequence<Float>.sum(): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3520)

### 6. Common

```kotlin
@kotlin.jvm.JvmName("sumOfDouble")
public fun Sequence<Double>.sum(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3534)

### 7. Common

```kotlin
@kotlin.jvm.JvmName("sumOfUInt")
@SinceKotlin("1.5")
public fun Sequence<UInt>.sum(): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_USequences.kt#L20)

### 8. Common

```kotlin
@kotlin.jvm.JvmName("sumOfULong")
@SinceKotlin("1.5")
public fun Sequence<ULong>.sum(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_USequences.kt#L35)

### 9. Common

```kotlin
@kotlin.jvm.JvmName("sumOfUByte")
@SinceKotlin("1.5")
public fun Sequence<UByte>.sum(): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_USequences.kt#L50)

### 10. Common

```kotlin
@kotlin.jvm.JvmName("sumOfUShort")
@SinceKotlin("1.5")
public fun Sequence<UShort>.sum(): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_USequences.kt#L65)

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
import kotlin.sequences.*

fun main() {
    val source = sequenceOf(1, 2, 3)
    val result = source.`sum`()
    println(result)
}
```

```text title="Output"
6
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
