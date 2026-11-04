# removeAll

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Removes all of this collection's elements that are also contained in the specified collection.

Allows to overcome type-safety restriction of `removeAll` that requires to pass a collection of type `Collection<E>`.

@return `true` if any of the specified elements was removed from the collection, `false` if the collection was not modified.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <@kotlin.internal.OnlyInputTypes T> MutableCollection<out T>.removeAll(elements: Collection<T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L24)

### 2. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.removeAll(elements: Iterable<T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L155)

Removes all elements from this `MutableCollection` that are also contained in the given `elements` collection.

### 3. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.removeAll(elements: Sequence<T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L163)

Removes all elements from this `MutableCollection` that are also contained in the given `elements` sequence.

### 4. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.removeAll(elements: Array<out T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L172)

Removes all elements from this `MutableCollection` that are also contained in the given `elements` array.

### 5. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableIterable<T>.removeAll(predicate: (T) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L219)

Removes all elements from this `MutableIterable` that match the given `predicate`.

@return `true` if any element was removed from this collection, or `false` when no elements were removed and collection was not modified.

### 6. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableList<T>.removeAll(predicate: (T) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L284)

Removes all elements from this `MutableList` that match the given `predicate`.

@return `true` if any element was removed from this collection, or `false` when no elements were removed and collection was not modified.

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
    val result = source.`removeAll`(listOf(1, 2, 3))
    println(result)
}
```

```text title="Output"
true
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
