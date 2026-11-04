# HashSet

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A hash table implementation of `MutableSet`.

This class stores unique elements using a hash table data structure that provides fast lookups
and ensures no duplicate elements are stored. It fully implements the `MutableSet` contract,
providing all standard Set operations including lookup, insertion, and removal.

## Null elements

`HashSet` accepts `null` as an element. Since elements are unique, at most one `null` element
can exist in the set.

## Element's hash code and equality contracts

`HashSet` relies on the `Any.hashCode` and `Any.equals` functions of elements to organize and locate them.
Elements are considered equal if their `Any.equals` function returns `true`, and elements that are equal
must have the same `Any.hashCode` value. Violating this contract can lead to incorrect behavior, such as
duplicate elements being stored or elements becoming unreachable.

The `Any.hashCode` and `Any.equals` functions should be consistent and immutable during the lifetime
of the element objects. Modifying an element in a way that changes its hash code or equality
after it has been added to a `HashSet` may lead to the element becoming unreachable.

## Performance characteristics

The performance characteristics below assume that the `Any.hashCode` function of elements distributes
them uniformly across the hash table, minimizing collisions. A poor hash function that causes
many collisions can degrade performance.

`HashSet` provides efficient implementation for common operations:

- **Lookup** (`contains`): O(1) time
- **Insertion and removal** (`add`, `remove`): O(1) time
- **Iteration**: O(n) time

## Iteration order

`HashSet` does not guarantee any particular order for iteration over its elements.
The iteration order is unpredictable and may change when the set is rehashed (when elements are
added or removed and the internal capacity is adjusted). Do not rely on any specific iteration order.

If a predictable iteration order is required, consider using `LinkedHashSet`, which maintains
insertion order.

## Usage guidelines

`HashSet` uses an internal data structure with a finite *capacity* - the maximum number of elements
it can store before needing to grow. As elements are added, the set tracks its *load factor*, which is
the ratio of the number of elements to the current capacity. When this ratio exceeds a certain threshold,
the set automatically increases its capacity and performs *rehashing* - rebuilding the internal data
structure to redistribute elements. Rehashing is a relatively expensive operation that temporarily impacts
performance. When creating a `HashSet`, you can optionally provide values for the initial capacity and
load factor threshold. Note that these parameters are just hints for the implementation and can be ignored.

To optimize performance and memory usage:

- If the number of elements is known in advance, use the constructor with initial capacity
  to avoid multiple rehashing operations as the set grows.
- Choose an appropriate load factor when creating the set. A lower load factor reduces collision
  probability but uses more memory, while a higher load factor saves memory but may increase
  lookup time. The default load factor typically provides a good balance.
- Ensure element objects have well-distributed `Any.hashCode` implementations to minimize collisions
  and maintain good performance.
- Prefer `addAll` over multiple individual `add` calls when adding multiple elements.

## Thread safety

`HashSet` is not thread-safe. If multiple threads access an instance concurrently and at least
one thread modifies it, external synchronization is required.

@param E the type of elements contained in the set. The mutable set is invariant in its element type.

## Declarations and overloads

### 1. Common

```kotlin
public expect class HashSet<E> : MutableSet<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashSet.kt#L8)

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
