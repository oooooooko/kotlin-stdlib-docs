# asSequence

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a `Sequence` instance that wraps the original array returning its elements when being iterated.

@sample samples.collections.Sequences.Building.sequenceFromArray

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.asSequence(): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27612)

### 2. Common

```kotlin
public fun ByteArray.asSequence(): Sequence<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27622)

### 3. Common

```kotlin
public fun ShortArray.asSequence(): Sequence<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27632)

### 4. Common

```kotlin
public fun IntArray.asSequence(): Sequence<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27642)

### 5. Common

```kotlin
public fun LongArray.asSequence(): Sequence<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27652)

### 6. Common

```kotlin
public fun FloatArray.asSequence(): Sequence<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27662)

### 7. Common

```kotlin
public fun DoubleArray.asSequence(): Sequence<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27672)

### 8. Common

```kotlin
public fun BooleanArray.asSequence(): Sequence<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27682)

### 9. Common

```kotlin
public fun CharArray.asSequence(): Sequence<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27692)

### 10. Common

```kotlin
public fun <T> Iterable<T>.asSequence(): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3966)

Creates a `Sequence` instance that wraps the original collection returning its elements when being iterated.

@sample samples.collections.Sequences.Building.sequenceFromCollection

### 11. Common

```kotlin
public fun <K, V> Map<out K, V>.asSequence(): Sequence<Map.Entry<K, V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L667)

Creates a `Sequence` instance that wraps the original map returning its entries when being iterated.

@sample samples.collections.Sequences.Building.sequenceFromMap

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
    val result = source.`asSequence`()
    println(result.toList())
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
