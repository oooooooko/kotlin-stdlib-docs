# Set

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A generic unordered collection of unique elements. The interface allows checking if an element is contained by it
and iterating over all elements. Complex operations are built upon this functionality
and provided in form of `kotlin.collections` extension functions.

It is implementation-specific how `Set` defines element's uniqueness. If not stated otherwise, `Set` implementations are usually
distinguishing elements using `Any.equals`. However, it is not the only way to distinguish elements, and some implementations may use
referential equality or compare elements by some of their properties. It is recommended to explicitly specify how a class
implementing `Set` distinguish elements.

Methods in this interface support only read-only access to the set;
read/write access is supported through the `MutableSet` interface.

Unlike `List`, `Set` does not guarantee any particular order for iteration. However, particular implementations
are free to have fixed iteration order, like "smaller", in some sense, elements are visited prior to "larger". In this case,
it is recommended to explicitly document ordering guarantees for the `Set` implementation.

Unlike `Collection` implementations, `Set` implementations must override `Any.toString`, `Any.equals` and `Any.hashCode` functions
and provide implementations such that:
- `Set.toString` should return a string containing string representation of contained elements in iteration order.
- `Set.equals` should consider two sets equal if and only if they contain the same number of elements and each element
  from one set is contained in another set. Unlike some other `equals` implementations, `Set.equals`
  should consider two sets equal even if they are instances of different classes; the only requirement here is that both sets have
  to implement `Set` interface.
- `Set.hashCode` should be computed as a sum of elements' hash codes using the following algorithm:
  ```kotlin
  var hashCode: Int = 0
  for (element in this) hashCode += element.hashCode()
  ```

@param E the type of elements contained in the set. The set is covariant in its element type.

## Declarations and overloads

### 1. Common

```kotlin
public expect interface Set<out E> : Collection<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L426)

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
    val value = linkedSetOf(1, 2, 3)
    println(value)
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
