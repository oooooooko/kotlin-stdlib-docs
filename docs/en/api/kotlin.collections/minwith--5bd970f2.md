# minWith

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the first element having the smallest value according to the provided `comparator`.

@throws NoSuchElementException if the array is empty.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun <T> Array<out T>.minWith(comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21949)

### 2. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun ByteArray.minWith(comparator: Comparator<in Byte>): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21967)

### 3. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun ShortArray.minWith(comparator: Comparator<in Short>): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21985)

### 4. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun IntArray.minWith(comparator: Comparator<in Int>): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22003)

### 5. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun LongArray.minWith(comparator: Comparator<in Long>): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22021)

### 6. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun FloatArray.minWith(comparator: Comparator<in Float>): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22039)

### 7. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun DoubleArray.minWith(comparator: Comparator<in Double>): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22057)

### 8. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun BooleanArray.minWith(comparator: Comparator<in Boolean>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22075)

### 9. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun CharArray.minWith(comparator: Comparator<in Char>): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22093)

### 10. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun <T> Iterable<T>.minWith(comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3026)

Returns the first element having the smallest value according to the provided `comparator`.

@throws NoSuchElementException if the collection is empty.

### 11. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <K, V> Map<out K, V>.minWith(comparator: Comparator<in Map.Entry<K, V>>): Map.Entry<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L598)

Returns the first entry having the smallest value according to the provided `comparator`.

@throws NoSuchElementException if the map is empty.

### 12. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UIntArray.minWith(comparator: Comparator<in UInt>): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9607)

### 13. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun ULongArray.minWith(comparator: Comparator<in ULong>): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9626)

### 14. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UByteArray.minWith(comparator: Comparator<in UByte>): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9645)

### 15. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UShortArray.minWith(comparator: Comparator<in UShort>): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9664)

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
    val result = source.`minWith`(naturalOrder())
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
