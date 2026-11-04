# Collection

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A generic collection of elements. The interface allows iterating over contained elements
and checking whether something is contained within the collection. Complex operations are built upon this
functionality and provided in form of `kotlin.collections` extension functions.

Functions in this interface support only read-only access to the collection;
read/write access is supported through the `MutableCollection` interface.

`Collection` is a top-level interface for objects aggregating multiple different homogenous elements. Other more specific interfaces,
like `List`, `Set`, and `Map` extend `Collection` to provide more specific guarantees on how elements are stored and accessed, as well
as provide richer functionality.

`Collection` implementation may have different guarantees on the order and uniqueness of contained elements,
for example, elements contained in a `List` are ordered and could contain duplicates, while elements contained in
a `Set` may not contain duplicates and there is no particular order imposed on them.

`Collection.contains` behavior is implementation-specific, but usually, it uses `Any.equals` to compare elements
for equality.

`Collection` does not impose any requirements for `toString`, `equals` and `hashCode` functions
and implementations are free to inherit a default behavior.
More specialized interfaces extending `Collection` (like `List`, `Set` and `Map`) may impose stricter requirements.

@param E the type of elements contained in the collection. The collection is covariant in its element type.

## Declarations and overloads

### 1. Common

```kotlin
public expect interface Collection<out E> : Iterable<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L33)

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
    val value = listOf(1, 2, 3)
    println(value)
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
