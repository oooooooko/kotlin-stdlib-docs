# MutableList

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A generic ordered collection of elements that supports adding, replacing and removing elements, as well as
iterating over contained elements, accessing them by an index and checking if a collection contains a particular value.

If a particular use case does not require list's modification,
a read-only counterpart, `List` could be used instead.

`MutableList` extends `List` contract with functions allowing to add, replace and remove elements.

Unlike `List`, iterators returned by `iterator` and `listIterator` allow modifying the list during iteration.
A view returned by `subList` also allows modifications of the underlying list.

Until stated otherwise, `MutableList` implementations are not thread-safe and their modification without
explicit synchronization may result in data corruption, loss, and runtime errors.

@param E the type of elements contained in the list. The mutable list is invariant in its element type.

## Declarations and overloads

### 1. Common

```kotlin
public expect interface MutableList<E> : List<E>, MutableCollection<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L296)

### 2. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public inline fun <T> MutableList(size: Int, init: (index: Int) -> T): MutableList<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L155)

Creates a new mutable list with the specified `size`, where each element is calculated by calling the specified
`init` function.

The function `init` is called for each list element sequentially starting from the first one.
It should return the value for a list element given its index.

@sample samples.collections.Collections.Lists.mutableListFromInitializer

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = MutableList(3) { index -> 'A' + index }
    println(list)

    list.clear()
    println(list)
}
```

```text title="Output"
[A, B, C]
[]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L233)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
