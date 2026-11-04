# asIterable

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates an `Iterable` instance that wraps the original array returning its elements when being iterated.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.asIterable(): Iterable<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27540)

### 2. Common

```kotlin
public fun ByteArray.asIterable(): Iterable<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27548)

### 3. Common

```kotlin
public fun ShortArray.asIterable(): Iterable<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27556)

### 4. Common

```kotlin
public fun IntArray.asIterable(): Iterable<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27564)

### 5. Common

```kotlin
public fun LongArray.asIterable(): Iterable<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27572)

### 6. Common

```kotlin
public fun FloatArray.asIterable(): Iterable<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27580)

### 7. Common

```kotlin
public fun DoubleArray.asIterable(): Iterable<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27588)

### 8. Common

```kotlin
public fun BooleanArray.asIterable(): Iterable<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27596)

### 9. Common

```kotlin
public fun CharArray.asIterable(): Iterable<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27604)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Iterable<T>.asIterable(): Iterable<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3958)

Returns this collection as an `Iterable`.

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.asIterable(): Iterable<Map.Entry<K, V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L659)

Creates an `Iterable` instance that wraps the original map returning its entries when being iterated.

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
    val result = source.`asIterable`()
    println(result)
}
```

```text title="Output"
kotlin.collections.ArraysKt___ArraysKt$asIterable$$inlined$Iterable$1@14ae5a5
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
