# MutableCollection

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A generic collection of elements that supports iterating, adding and removing elements, as well as checking if the
collection contains some elements. Complex operations are built upon this
functionality and provided in form of `kotlin.collections` extension functions.

If a particular use case does not require collection's modification,
a read-only counterpart, `Collection` could be used instead.

`MutableCollection` extends `Collection` contract with functions allowing to add or remove elements.

`MutableCollection` is a top-level interface for mutable objects aggregating multiple different homogenous elements.
Other more specific interfaces, like `MutableList`, `MutableSet`, and `MutableMap` extend `MutableCollection` to provide
more specific guarantees on how elements are stored, accessed and modified, as well as provide richer functionality.

Unlike `Collection`, an iterator returned by `iterator` allows removing elements during iteration.

Until stated otherwise, `MutableCollection` implementations are not thread-safe and their modification without
explicit synchronization may result in data corruption, loss, and runtime errors.

@param E the type of elements contained in the collection. The mutable collection is invariant in its element type.

## Declarations and overloads

### 1. Common

```kotlin
public expect interface MutableCollection<E> : Collection<E>, MutableIterable<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L96)

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
    val value = mutableListOf(1, 2, 3)
    println(value)
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
