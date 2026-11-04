# sorted

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Comparable<T>> Array<out T>.sorted(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7492)

### 2. Common

```kotlin
public fun ByteArray.sorted(): List<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7503)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 3. Common

```kotlin
public fun ShortArray.sorted(): List<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7512)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 4. Common

```kotlin
public fun IntArray.sorted(): List<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7521)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 5. Common

```kotlin
public fun LongArray.sorted(): List<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7530)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 6. Common

```kotlin
public fun FloatArray.sorted(): List<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7539)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 7. Common

```kotlin
public fun DoubleArray.sorted(): List<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7548)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 8. Common

```kotlin
public fun CharArray.sorted(): List<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7557)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 9. Common

```kotlin
public fun <T : Comparable<T>> Iterable<T>.sorted(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1204)

Returns a list of all elements sorted according to their natural sort order.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

### 10. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sorted(): List<UInt>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3591)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sorted(): List<ULong>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3602)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sorted(): List<UByte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3613)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sorted(): List<UShort>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3624)

Returns a list of all elements sorted according to their natural sort order.

Use `sortedArray` if you need to get the result in an array.

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
    val result = source.`sorted`()
    println(result)
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
