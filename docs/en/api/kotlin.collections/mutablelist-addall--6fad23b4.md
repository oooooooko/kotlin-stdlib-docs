# MutableList.addAll

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Adds all of the elements of the specified collection to the end of this list.

The elements are appended in the order they appear in the `elements` collection.

@return `true` if the list was changed as the result of the operation.

@sample samples.collections.Collections.Lists.addAll

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
    override fun addAll(elements: Collection<E>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L329)

### 2. Common

```kotlin
@IgnorableReturnValue
    public fun addAll(index: Int, elements: Collection<E>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L341)

Inserts all of the elements of the specified collection `elements` into this list at the specified `index`.

The elements are inserted in the order they appear in the `elements` collection.

All elements that initially were stored at indices `index .. index + size - 1` are shifted `elements.size` positions to the end.

If `index` is equal to `size`, `elements` will be appended to the list.

@return `true` if the list was changed as the result of the operation.

@throws IndexOutOfBoundsException if `index` less than zero or greater than `size` of this list.

@sample samples.collections.Collections.Lists.addAllAt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')
    println(list.addAll(listOf('a', 'b', 'c')))
    println(list)
}
```

```text title="Output"
true
[a, b, c, a, b, c]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L354)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')

    list.addAll(1, listOf('x', 'y', 'z'))
    println(list)

    list.addAll(6, listOf('h', 'i'))
    println(list)

    assertFailsWith<IndexOutOfBoundsException> { list.addAll(100500, listOf('z')) }
}
```

```text title="Output"
[a, x, y, z, b, c]
[a, x, y, z, b, c, h, i]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L361)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
