# MutableCollection.retainAll

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Retains only the elements in this collection that are contained in the specified collection.

@return `true` if any element was removed from the collection, `false` if the collection was not modified.

@sample samples.collections.Collections.Collections.retainAll

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun retainAll(elements: Collection<E>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L169)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val collection: MutableCollection<Char> = mutableSetOf('a', 'b', 'c')

    // Nothing was removed
    println(collection.retainAll(listOf('a', 'b', 'c')))
    println(collection)

    println(collection.retainAll(listOf('a', 'e', 'i', 'o')))
    println(collection)
}
```

```text title="Output"
false
[a, b, c]
true
[a]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L125)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
