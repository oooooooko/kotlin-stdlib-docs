# List.listIterator

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list iterator over the elements in this list (in proper sequence).

If the list needs to be iterated starting from a specific index,
a `listIterator` overload accepting the `Int` parameter could be used instead
of using this function and manually iterating until the required index is reached.

@sample samples.collections.Collections.Lists.listIterator

## Declarations and overloads

### 1. Common

```kotlin
public fun listIterator(): ListIterator<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L261)

### 2. Common

```kotlin
public fun listIterator(index: Int): ListIterator<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L272)

Returns a list iterator over the elements in this list (in proper sequence), starting at the specified `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than `size` of this list.
@sample samples.collections.Collections.Lists.listIteratorWithIndex

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf('a', 'b')
    val iterator = list.listIterator()

    // "Cursor" is at the beginning of the list,
    // so there is no previous element, only a next one
    println(iterator.hasPrevious())
    println(iterator.hasNext())

    // Let's scan the list in a forward direction
    println(iterator.next())
    println(iterator.next())

    // Cursor is past the end of the list,
    // so there is no next element, only a previous one
    println(iterator.hasPrevious())
    println(iterator.hasNext())

    // Let's scan the list backwards, starting from the end
    println(iterator.previous())
    println(iterator.previous())

    // We ran out of elements
    assertFailsWith<NoSuchElementException> { iterator.previous() }

    // Empty list has an empty iterator
    val emptyListIterator = emptyList<String>().listIterator()
    println(emptyListIterator.hasNext())
    println(emptyListIterator.hasPrevious())
}
```

```text title="Output"
false
true
a
b
true
false
b
a
false
false
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L461)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf('a', 'b', 'c')

    // The iterator will scan elements starting from 'c' (the element at the index = 2)
    val sublistIterator = list.listIterator(index = 2)
    // However, previous elements are also accessible
    println(sublistIterator.hasPrevious())
    // One step forward
    println(sublistIterator.next())
    // Two steps backward
    println(sublistIterator.previous())
    println(sublistIterator.previous())

    // If the index is equal to the length of the list,
    // the iterator's "cursor" will point past the last element and only previous elements
    // will be accessible
    val pastLastIterator = list.listIterator(index = 3)
    println(pastLastIterator.hasPrevious())
    println(pastLastIterator.hasNext())
    println(pastLastIterator.previous())
    println(pastLastIterator.previous())

    // It's an error to use indices outside of list bounds
    assertFailsWith<IndexOutOfBoundsException> { list.listIterator(-1) }
    assertFailsWith<IndexOutOfBoundsException> { list.listIterator(list.size + 1) }
}
```

```text title="Output"
true
c
c
b
true
false
c
b
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L493)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
