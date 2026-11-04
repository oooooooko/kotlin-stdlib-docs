# MutableList.add

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Adds the specified element to the end of this list.

@return `true` because the list is always modified as the result of this operation.

@sample samples.collections.Collections.Lists.add

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
    override fun add(element: E): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L315)

### 2. Common

```kotlin
public fun add(index: Int, element: E): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L379)

Inserts an element into the list at the specified `index`.

All elements that had indices `index .. index + size - 1` are shifted 1 position right.

If `index` is equal to `size`, `element` will be appended to this list.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than `size` of this list.

@sample samples.collections.Collections.Lists.addAt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')
    println(list.add('c'))
    println(list)
}
```

```text title="Output"
true
[a, b, c, c]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L334)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')

    list.add(1, 'c')
    println(list)

    list.add(4, 'a')
    println(list)

    assertFailsWith<IndexOutOfBoundsException> { list.add(100500, 'a') }
}
```

```text title="Output"
[a, c, b, c]
[a, c, b, c, a]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L341)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
