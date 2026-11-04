# sortedWith

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list of all elements sorted according to the specified `comparator`.

Use `sortedArrayWith` if you need to get the result in an array.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.sortedWith(comparator: Comparator<in T>): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8032)

### 2. Common

```kotlin
public fun ByteArray.sortedWith(comparator: Comparator<in Byte>): List<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8043)

Returns a list of all elements sorted according to the specified `comparator`.

### 3. Common

```kotlin
public fun ShortArray.sortedWith(comparator: Comparator<in Short>): List<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8050)

Returns a list of all elements sorted according to the specified `comparator`.

### 4. Common

```kotlin
public fun IntArray.sortedWith(comparator: Comparator<in Int>): List<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8057)

Returns a list of all elements sorted according to the specified `comparator`.

### 5. Common

```kotlin
public fun LongArray.sortedWith(comparator: Comparator<in Long>): List<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8064)

Returns a list of all elements sorted according to the specified `comparator`.

### 6. Common

```kotlin
public fun FloatArray.sortedWith(comparator: Comparator<in Float>): List<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8071)

Returns a list of all elements sorted according to the specified `comparator`.

### 7. Common

```kotlin
public fun DoubleArray.sortedWith(comparator: Comparator<in Double>): List<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8078)

Returns a list of all elements sorted according to the specified `comparator`.

### 8. Common

```kotlin
public fun BooleanArray.sortedWith(comparator: Comparator<in Boolean>): List<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8085)

Returns a list of all elements sorted according to the specified `comparator`.

### 9. Common

```kotlin
public fun CharArray.sortedWith(comparator: Comparator<in Char>): List<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8092)

Returns a list of all elements sorted according to the specified `comparator`.

### 10. Common

```kotlin
public fun <T> Iterable<T>.sortedWith(comparator: Comparator<in T>): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1251)

Returns a list of all elements sorted according to the specified `comparator`.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

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
    val result = source.`sortedWith`(naturalOrder())
    println(result)
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
