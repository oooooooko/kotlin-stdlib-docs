# MutableList.subList

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a view of the portion of this list between the specified `fromIndex` (inclusive) and `toIndex` (exclusive).
The returned list is backed by this list, so changes in the returned list are reflected in this list, and vice versa.

Structural changes in the base list make the behavior of the view unspecified.

@throws IndexOutOfBoundsException if `fromIndex` less than zero or `toIndex` greater than `size` of this list.
@throws IllegalArgumentException of `fromIndex` is greater than `toIndex`.

@sample samples.collections.Collections.Lists.subList

## Declarations and overloads

### 1. Common

```kotlin
override fun subList(fromIndex: Int, toIndex: Int): MutableList<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L412)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf(1, 2, 3, 4, 5)
    println(list.subList(2, 4))

    val mutableList = mutableListOf(1, 2, 3, 4, 5)
    val subList = mutableList.subList(2, 4)
    println(subList)

    mutableList[3] = -1
    println(subList)

    assertFailsWith<IndexOutOfBoundsException> { list.subList(0, 100) }
}
```

```text title="Output"
[3, 4]
[3, 4]
[3, -1]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L430)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
