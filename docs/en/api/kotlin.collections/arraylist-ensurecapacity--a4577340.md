# ArrayList.ensureCapacity

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Ensures that the capacity of this list is at least equal to the specified `minCapacity`.

If the current capacity is less than the `minCapacity`, a new backing storage is allocated with greater capacity.
Otherwise, this method takes no action and simply returns.

This operation can be used to minimize the number of incremental reallocations when the eventual size
of the list is known in advance, improving performance when adding many elements.

On the JS target, this method has no effect due to the internal JS implementation.

@param minCapacity the desired minimum capacity.

@sample samples.collections.Collections.Lists.ArrayList.ensureCapacity

## Declarations and overloads

### 1. Common

```kotlin
public fun ensureCapacity(minCapacity: Int)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/ArrayList.kt#L93)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // Suppose we have an existing list with unknown current capacity
    val list = arrayListOf(1, 2, 3, 4, 5)

    // When we know in advance that we'll add many elements,
    // we can pre-allocate capacity to avoid multiple reallocations
    val elementsToAdd = 1000
    list.ensureCapacity(list.size + elementsToAdd)

    // Now adding elements won't trigger internal array resizing
    // until we exceed the ensured capacity
    for (i in 1..elementsToAdd) {
        list.add(i)
    }

    println(list.size)
    println(list.first())
    println(list.last())
}
```

```text title="Output"
1005
1
1000
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L540)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
