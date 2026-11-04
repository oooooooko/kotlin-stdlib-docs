# sortWith

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Sorts the array in-place according to the order specified by the given `comparator`.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

## Declarations and overloads

### 1. Common

```kotlin
public expect fun <T> Array<out T>.sortWith(comparator: Comparator<in T>): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9981)

### 2. Common

```kotlin
public expect fun <T> Array<out T>.sortWith(comparator: Comparator<in T>, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9988)

Sorts a range in the array in-place with the given `comparator`.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

@param fromIndex the start of the range (inclusive) to sort, 0 by default.
@param toIndex the end of the range (exclusive) to sort, size of this array by default.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 3. Common

```kotlin
public expect fun <T> MutableList<T>.sortWith(comparator: Comparator<in T>): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/CollectionsH.kt#L60)

Sorts elements in the list in-place according to the order specified with `comparator`.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortMutableListWith

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // non-comparable class
    class Person(val firstName: String, val lastName: String) {
        override fun toString(): String = "$firstName $lastName"
    }

    val people = mutableListOf(
        Person("Ragnar", "Lodbrok"),
        Person("Bjorn", "Ironside"),
        Person("Sweyn", "Forkbeard")
    )

    people.sortWith(compareByDescending { it.firstName })

    // after sorting
    println(people.joinToString())
}
```

```text title="Output"
Sweyn Forkbeard, Ragnar Lodbrok, Bjorn Ironside
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1397)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
