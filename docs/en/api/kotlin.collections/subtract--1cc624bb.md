# subtract

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a set containing all elements that are contained by this array and not contained by the specified collection.

The returned set preserves the element iteration order of the original array.

The returned set uses structural equality (`==`) to distinguish elements, meaning there will be no two
structurally equal, but otherwise different elements in it.

## Declarations and overloads

### 1. Common

```kotlin
public infix fun <T> Array<out T>.subtract(other: Iterable<T>): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13783)

### 2. Common

```kotlin
public infix fun ByteArray.subtract(other: Iterable<Byte>): Set<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13802)

### 3. Common

```kotlin
public infix fun ShortArray.subtract(other: Iterable<Short>): Set<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13816)

### 4. Common

```kotlin
public infix fun IntArray.subtract(other: Iterable<Int>): Set<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13830)

### 5. Common

```kotlin
public infix fun LongArray.subtract(other: Iterable<Long>): Set<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13844)

### 6. Common

```kotlin
public infix fun FloatArray.subtract(other: Iterable<Float>): Set<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13858)

### 7. Common

```kotlin
public infix fun DoubleArray.subtract(other: Iterable<Double>): Set<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13872)

### 8. Common

```kotlin
public infix fun BooleanArray.subtract(other: Iterable<Boolean>): Set<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13886)

### 9. Common

```kotlin
public infix fun CharArray.subtract(other: Iterable<Char>): Set<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13900)

### 10. Common

```kotlin
public infix fun <T> Iterable<T>.subtract(other: Iterable<T>): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1886)

Returns a set containing all elements that are contained by this collection and not contained by the specified collection.

The returned set preserves the element iteration order of the original collection.

The returned set uses structural equality (`==`) to distinguish elements, meaning there will be no two
structurally equal, but otherwise different elements in it.

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
    val result = source.`subtract`(listOf(1, 2, 3))
    println(result)
}
```

```text title="Output"
[]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
