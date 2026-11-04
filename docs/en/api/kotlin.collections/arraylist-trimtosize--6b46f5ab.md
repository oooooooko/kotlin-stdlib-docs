# ArrayList.trimToSize

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Attempts to reduce the storage used for this list.

If the backing storage of this list is larger than necessary to hold its current elements,
then it may be resized to become more space efficient.
This operation can help reduce memory consumption when the list is not expected to grow further.

On the JS target, this method has no effect due to the internal JS implementation.

@sample samples.collections.Collections.Lists.ArrayList.trimToSize

## Declarations and overloads

### 1. Common

```kotlin
public fun trimToSize()
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/ArrayList.kt#L80)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = ArrayList<Int>(1000)
    // Add only a few elements
    list.addAll(listOf(1, 2, 3))
    println(list)

    // The list has capacity for 1000 elements, but only 3 are used.
    // trimToSize() can help reduce memory usage by resizing the backing storage
    // to fit the actual number of elements.
    list.trimToSize()

    // The list content remains the same
    println(list)
    println(list.size)
}
```

```text title="Output"
[1, 2, 3]
[1, 2, 3]
3
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L523)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
