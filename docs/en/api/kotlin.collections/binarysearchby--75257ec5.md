# binarySearchBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Searches this list or its range for an element having the key returned by the specified `selector` function
equal to the provided `key` value using the binary search algorithm.
The list is expected to be sorted into ascending order according to the Comparable natural ordering of keys of its elements.
otherwise the result is undefined.

If the list contains multiple elements with the specified `key`, there is no guarantee which one will be found.

`null` value is considered to be less than any non-null value.

@return the index of the element with the specified `key`, if it is contained in the list within the specified range;
otherwise, the inverted insertion point `(-insertion point - 1)`.
The insertion point is defined as the index at which the element should be inserted,
so that the list (or the specified subrange of list) still remains sorted.
@sample samples.collections.Collections.Lists.binarySearchByKey

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, K : Comparable<K>> List<T>.binarySearchBy(
    key: K?,
    fromIndex: Int = 0,
    toIndex: Int = size,
    crossinline selector: (T) -> K?
): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L388)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Box(val value: Int)

    val numbers = listOf(1, 3, 7, 10, 12)
    val boxes = numbers.map { Box(it) }
    println(boxes.binarySearchBy(10) { it.value })
}
```

```text title="Output"
3
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L307)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
