# binarySearch

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Searches this list or its range for the provided `element` using the binary search algorithm.
The list is expected to be sorted into ascending order according to the Comparable natural ordering of its elements,
otherwise the result is undefined.

If the list contains multiple elements equal to the specified `element`, there is no guarantee which one will be found.

`null` value is considered to be less than any non-null value.

@return the index of the element, if it is contained in the list within the specified range;
otherwise, the inverted insertion point `(-insertion point - 1)`.
The insertion point is defined as the index at which the element should be inserted,
so that the list (or the specified subrange of list) still remains sorted.
@sample samples.collections.Collections.Lists.binarySearchOnComparable
@sample samples.collections.Collections.Lists.binarySearchWithBoundaries

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Comparable<T>> List<T?>.binarySearch(element: T?, fromIndex: Int = 0, toIndex: Int = size): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L315)

### 2. Common

```kotlin
public fun <T> List<T>.binarySearch(element: T, comparator: Comparator<in T>, fromIndex: Int = 0, toIndex: Int = size): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L352)

Searches this list or its range for the provided `element` using the binary search algorithm.
The list is expected to be sorted into ascending order according to the specified `comparator`,
otherwise the result is undefined.

If the list contains multiple elements equal to the specified `element`, there is no guarantee which one will be found.

`null` value is considered to be less than any non-null value.

@return the index of the element, if it is contained in the list within the specified range;
otherwise, the inverted insertion point `(-insertion point - 1)`.
The insertion point is defined as the index at which the element should be inserted,
so that the list (or the specified subrange of list) still remains sorted according to the specified `comparator`.
@sample samples.collections.Collections.Lists.binarySearchWithComparator

### 3. Common

```kotlin
public fun <T> List<T>.binarySearch(fromIndex: Int = 0, toIndex: Int = size, comparison: (T) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L417)

Searches this list or its range for an element for which the given `comparison` function returns zero using the binary search algorithm.

The list is expected to be sorted so that the signs of the `comparison` function's return values ascend on the list elements,
i.e. negative values come before zero and zeroes come before positive values.
Otherwise, the result is undefined.

If the list contains multiple elements for which `comparison` returns zero, there is no guarantee which one will be found.

@param comparison function that returns zero when called on the list element being searched.
On the elements coming before the target element, the function must return negative values;
on the elements coming after the target element, the function must return positive values.

@return the index of the found element, if it is contained in the list within the specified range;
otherwise, the inverted insertion point `(-insertion point - 1)`.
The insertion point is defined as the index at which the element should be inserted,
so that the list (or the specified subrange of list) still remains sorted.
@sample samples.collections.Collections.Lists.binarySearchWithComparisonFunction

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = mutableListOf('a', 'b', 'c', 'd', 'e')
    println(list.binarySearch('d'))

    list.remove('d')

    val invertedInsertionPoint = list.binarySearch('d')
    val actualInsertionPoint = -(invertedInsertionPoint + 1)
    println(actualInsertionPoint)

    list.add(actualInsertionPoint, 'd')
    println(list)
}
```

```text title="Output"
3
3
[a, b, c, d, e]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L274)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf('a', 'b', 'c', 'd', 'e')
    println(list.binarySearch('d'))

    // element is out of range from the left
    println(list.binarySearch('b', fromIndex = 2) < 0)

    // element is out of range from the right
    println(list.binarySearch('d', toIndex = 2) < 0)
}
```

```text title="Output"
3
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L289)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val colors = listOf("Blue", "green", "ORANGE", "Red", "yellow")
    println(colors.binarySearch("RED", String.CASE_INSENSITIVE_ORDER))
}
```

```text title="Output"
3
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L301)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Box(val value: String)

    val values = listOf("A", "ant", "binding", "Box", "cell")
    val boxes = values.map { Box(it) }

    val valueToFind = "box"
    // `boxes` list is sorted according to the following comparison function
    val index = boxes.binarySearch { String.CASE_INSENSITIVE_ORDER.compare(it.value, valueToFind) }

    if (index >= 0) {
        println("Value at $index is ${boxes[index]}")
    } else {
        println("Box with value=$valueToFind was not found")
    }
}
```

```text title="Output"
Value at 3 is Box(value=Box)
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L316)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
