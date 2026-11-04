# ArrayList

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A dynamic array implementation of `MutableList`.

This class stores elements contiguously in memory using an internal array that automatically
grows as needed. It fully implements the `MutableList` contract, providing all standard list
operations including indexed access, iteration, and modification. As an implementation of
`RandomAccess`, it provides fast indexed access to elements.

## Performance characteristics

`ArrayList` provides efficient implementation for common operations:

- **Indexed access** (`get`, `set`): O(1) constant time
- **Appending to the end** (`add`): O(1) [amortized](https://en.wikipedia.org/wiki/Amortized_analysis)
  constant time. When the internal array is full, it must be resized, which takes O(n) time to copy
  all existing elements to a new, larger array. However, these resize operations become less frequent
  as the list grows, making the average cost per appending constant over many operations.
- **Removing from the end** (`removeLast`, `removeAt``(size - 1)`): O(1) constant time
- **Inserting or removing at a position** (`add` with index, `removeAt`): O(n) linear time,
  as elements after the position must be shifted
- **Search operations** (`contains`, `indexOf`, `lastIndexOf`): O(n) linear time
- **Iteration**: O(n) linear time

Note: On the JS target, these time-complexity guarantees may not hold due to the underlying
JavaScript engine implementation.

## Usage guidelines

To optimize performance and memory usage:

- If the number of elements is known in advance, use the constructor with initial capacity
  to avoid multiple reallocations as the list grows.
- Use `ensureCapacity` before adding many elements to pre-allocate sufficient storage.
- Prefer `addAll` over multiple individual `add` calls when adding multiple elements.
- Call `trimToSize` after all elements have been added to reduce memory consumption if no further
  growth is expected.

## Thread safety

`ArrayList` is not thread-safe. If multiple threads access an instance concurrently and at least
one thread modifies it, external synchronization is required.

@param E the type of elements contained in the list.

## Declarations and overloads

### 1. Common

```kotlin
public expect class ArrayList<E> : MutableList<E>, RandomAccess
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/ArrayList.kt#L8)

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
    val value = arrayListOf(1, 2, 3)
    println(value)
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
