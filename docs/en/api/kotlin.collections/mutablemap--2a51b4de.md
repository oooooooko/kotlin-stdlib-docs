# MutableMap

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A collection that holds pairs of objects (keys and values) and supports retrieving
the value corresponding to each key, as well as adding new, removing or updating existing pairs.

Map keys are unique; the map holds only one value for each key. In contrast, the same value can be associated with several unique keys.

If a particular use case does not require map's modification, a read-only counterpart, `Map` could be used instead.

`MutableMap` extends `Map` contract with functions allowing to add, remove and update mapping between keys and values.

Unlike `Map`, `keys`, `values` and `entries` collections are all mutable, and changes in them update the map.

Until stated otherwise, `MutableMap` implementations are not thread-safe and their modification without
explicit synchronization may result in data corruption, loss, and runtime errors.

@param K the type of map keys. The map is invariant in its key type.
@param V the type of map values. The mutable map is invariant in its value type.

## Declarations and overloads

### 1. Common

```kotlin
public expect interface MutableMap<K, V> : Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L654)

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
    val value = linkedMapOf("a" to 1, "b" to 2)
    println(value)
}
```

```text title="Output"
{a=1, b=2}
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
