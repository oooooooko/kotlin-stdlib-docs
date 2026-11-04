# HashSet.constructor

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a new empty `HashSet`.

## Declarations and overloads

### 1. Common

```kotlin
public constructor()
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashSet.kt#L81)

### 2. Common

```kotlin
public constructor(initialCapacity: Int)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashSet.kt#L86)

Creates a new empty `HashSet` with the specified initial capacity.

Capacity is the maximum number of elements the set is able to store in the current internal data structure.
When the set gets full by a certain default load factor, its capacity is expanded,
which usually leads to rebuild of the internal data structure.

@param initialCapacity the initial capacity of the created set.
  Note that the argument is just a hint for the implementation and can be ignored.

@throws IllegalArgumentException if `initialCapacity` is negative.

### 3. Common

```kotlin
public constructor(initialCapacity: Int, loadFactor: Float)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashSet.kt#L100)

Creates a new empty `HashSet` with the specified initial capacity and load factor.

Capacity is the maximum number of elements the set is able to store in the current internal data structure.
Load factor is the measure of how full the set is allowed to get in relation to
its capacity before the capacity is expanded, which usually leads to rebuild of the internal data structure.

@param initialCapacity the initial capacity of the created set.
  Note that the argument is just a hint for the implementation and can be ignored.
@param loadFactor the load factor of the created set.
  Note that the argument is just a hint for the implementation and can be ignored.

@throws IllegalArgumentException if `initialCapacity` is negative or `loadFactor` is non-positive.

### 4. Common

```kotlin
public constructor(elements: Collection<E>)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashSet.kt#L116)

Creates a new `HashSet` filled with the elements of the specified collection.

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
    val value = hashSetOf(1, 2, 3)
    println(value)
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
