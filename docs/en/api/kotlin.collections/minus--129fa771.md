# minus

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list containing all elements of the original collection without the first occurrence of the given `element`.

## Declarations and overloads

### 1. Common

```kotlin
public operator fun <T> Iterable<T>.minus(element: T): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3578)

### 2. Common

```kotlin
public operator fun <T> Iterable<T>.minus(elements: Array<out T>): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3587)

Returns a list containing all elements of the original collection except the elements contained in the given `elements` array.

### 3. Common

```kotlin
public operator fun <T> Iterable<T>.minus(elements: Iterable<T>): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3595)

Returns a list containing all elements of the original collection except the elements contained in the given `elements` collection.

### 4. Common

```kotlin
public operator fun <T> Iterable<T>.minus(elements: Sequence<T>): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3605)

Returns a list containing all elements of the original collection except the elements contained in the given `elements` sequence.

### 5. Common

```kotlin
public operator fun <T> Set<T>.minus(element: T): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sets.kt#L22)

Returns a set containing all elements of the original set except the given `element`.

The returned set preserves the element iteration order of the original set.

### 6. Common

```kotlin
public operator fun <T> Set<T>.minus(elements: Array<out T>): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sets.kt#L33)

Returns a set containing all elements of the original set except the elements contained in the given `elements` array.

The returned set preserves the element iteration order of the original set.

### 7. Common

```kotlin
public operator fun <T> Set<T>.minus(elements: Iterable<T>): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sets.kt#L44)

Returns a set containing all elements of the original set except the elements contained in the given `elements` collection.

The returned set preserves the element iteration order of the original set.

### 8. Common

```kotlin
public operator fun <T> Set<T>.minus(elements: Sequence<T>): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sets.kt#L60)

Returns a set containing all elements of the original set except the elements contained in the given `elements` sequence.

The returned set preserves the element iteration order of the original set.

### 9. Common

```kotlin
@SinceKotlin("1.1")
public operator fun <K, V> Map<out K, V>.minus(key: K): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L885)

Returns a map containing all entries of the original map except the entry with the given `key`.

The returned map preserves the entry iteration order of the original map.

### 10. Common

```kotlin
@SinceKotlin("1.1")
public operator fun <K, V> Map<out K, V>.minus(keys: Iterable<K>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L894)

Returns a map containing all entries of the original map except those entries
the keys of which are contained in the given `keys` collection.

The returned map preserves the entry iteration order of the original map.

### 11. Common

```kotlin
@SinceKotlin("1.1")
public operator fun <K, V> Map<out K, V>.minus(keys: Array<out K>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L904)

Returns a map containing all entries of the original map except those entries
the keys of which are contained in the given `keys` array.

The returned map preserves the entry iteration order of the original map.

### 12. Common

```kotlin
@SinceKotlin("1.1")
public operator fun <K, V> Map<out K, V>.minus(keys: Sequence<K>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L914)

Returns a map containing all entries of the original map except those entries
the keys of which are contained in the given `keys` sequence.

The returned map preserves the entry iteration order of the original map.

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
    val source = listOf(1, 2, 3)
    val result = source.`minus`(1)
    println(result)
}
```

```text title="Output"
[2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
