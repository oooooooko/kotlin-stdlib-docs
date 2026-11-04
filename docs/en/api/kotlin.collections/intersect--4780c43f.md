# intersect

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a set containing elements of this array that are also contained in the specified `other` array.

The returned set preserves the element iteration order of the original array.

The returned set uses structural equality (`==`) to distinguish elements, meaning there will be no two
structurally equal, but otherwise different elements in it.

To get a set containing all elements that are contained at least in one of these collections use `union`.

## Declarations and overloads

### 1. Common

```kotlin
public infix fun <T> Array<out T>.intersect(other: Iterable<T>): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13634)

### 2. Common

```kotlin
public infix fun ByteArray.intersect(other: Iterable<Byte>): Set<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13655)

### 3. Common

```kotlin
public infix fun ShortArray.intersect(other: Iterable<Short>): Set<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13671)

### 4. Common

```kotlin
public infix fun IntArray.intersect(other: Iterable<Int>): Set<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13687)

### 5. Common

```kotlin
public infix fun LongArray.intersect(other: Iterable<Long>): Set<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13703)

### 6. Common

```kotlin
public infix fun FloatArray.intersect(other: Iterable<Float>): Set<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13719)

### 7. Common

```kotlin
public infix fun DoubleArray.intersect(other: Iterable<Double>): Set<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13735)

### 8. Common

```kotlin
public infix fun BooleanArray.intersect(other: Iterable<Boolean>): Set<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13751)

### 9. Common

```kotlin
public infix fun CharArray.intersect(other: Iterable<Char>): Set<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13767)

### 10. Common

```kotlin
public infix fun <T> Iterable<T>.intersect(other: Iterable<T>): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1865)

Returns a set containing elements of this collection that are also contained in the specified `other` collection.

The returned set preserves the element iteration order of the original collection.

The returned set uses structural equality (`==`) to distinguish elements, meaning there will be no two
structurally equal, but otherwise different elements in it.

To get a set containing all elements that are contained at least in one of these collections use `union`.

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
    val result = source.`intersect`(listOf(1, 2, 3))
    println(result)
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
