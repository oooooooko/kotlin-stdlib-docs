# MutableList.removeAt

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Removes an element at the specified `index` from the list.

All elements placed after `index` are shifted 1 position left.

@return the element that has been removed.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than or equal to `size` of this list.

@sample samples.collections.Collections.Lists.removeAt

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun removeAt(index: Int): E
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L392)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')

    list.removeAt(1)
    println(list)

    list.removeAt(0)
    println(list)

    assertFailsWith<IndexOutOfBoundsException> { list.removeAt(1) }
}
```

```text title="Output"
[a, c]
[c]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L398)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
