# maxWith

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the first element having the largest value according to the provided `comparator`.

@throws NoSuchElementException if the array is empty.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun <T> Array<out T>.maxWith(comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18977)

### 2. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun ByteArray.maxWith(comparator: Comparator<in Byte>): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18995)

### 3. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun ShortArray.maxWith(comparator: Comparator<in Short>): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19013)

### 4. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun IntArray.maxWith(comparator: Comparator<in Int>): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19031)

### 5. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun LongArray.maxWith(comparator: Comparator<in Long>): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19049)

### 6. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun FloatArray.maxWith(comparator: Comparator<in Float>): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19067)

### 7. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun DoubleArray.maxWith(comparator: Comparator<in Double>): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19085)

### 8. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun BooleanArray.maxWith(comparator: Comparator<in Boolean>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19103)

### 9. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun CharArray.maxWith(comparator: Comparator<in Char>): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19121)

### 10. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun <T> Iterable<T>.maxWith(comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2602)

Returns the first element having the largest value according to the provided `comparator`.

@throws NoSuchElementException if the collection is empty.

### 11. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <K, V> Map<out K, V>.maxWith(comparator: Comparator<in Map.Entry<K, V>>): Map.Entry<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L400)

Returns the first entry having the largest value according to the provided `comparator`.

@throws NoSuchElementException if the map is empty.

### 12. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UIntArray.maxWith(comparator: Comparator<in UInt>): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8247)

### 13. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun ULongArray.maxWith(comparator: Comparator<in ULong>): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8266)

### 14. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UByteArray.maxWith(comparator: Comparator<in UByte>): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8285)

### 15. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UShortArray.maxWith(comparator: Comparator<in UShort>): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8304)

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
import kotlin.collections.*

fun main() {
    val source = arrayOf(1, 2, 3)
    val result = source.`maxWith`(naturalOrder())
    println(result)
}
```

```text title="Output"
3
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
