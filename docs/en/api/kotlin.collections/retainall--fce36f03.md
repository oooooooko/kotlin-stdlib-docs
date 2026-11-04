# retainAll

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Retains only the elements in this collection that are contained in the specified collection.

Allows to overcome type-safety restriction of `retainAll` that requires to pass a collection of type `Collection<E>`.

@return `true` if any element was removed from the collection, `false` if the collection was not modified.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <@kotlin.internal.OnlyInputTypes T> MutableCollection<out T>.retainAll(elements: Collection<T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L36)

### 2. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.retainAll(elements: Iterable<T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L180)

Retains only elements of this `MutableCollection` that are contained in the given `elements` collection.

### 3. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.retainAll(elements: Array<out T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L188)

Retains only elements of this `MutableCollection` that are contained in the given `elements` array.

### 4. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.retainAll(elements: Sequence<T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L199)

Retains only elements of this `MutableCollection` that are contained in the given `elements` sequence.

### 5. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableIterable<T>.retainAll(predicate: (T) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L227)

Retains only elements of this `MutableIterable` that match the given `predicate`.

@return `true` if any element was removed from this collection, or `false` when all elements were retained and collection was not modified.

### 6. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableList<T>.retainAll(predicate: (T) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L292)

Retains only elements of this `MutableList` that match the given `predicate`.

@return `true` if any element was removed from this collection, or `false` when all elements were retained and collection was not modified.

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
    val source = mutableListOf(1, 2, 3)
    val result = source.`retainAll`(listOf(1, 2, 3))
    println(result)
}
```

```text title="Output"
false
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
