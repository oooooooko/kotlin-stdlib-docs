# Collection.contains

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Checks if the specified element is contained in this collection.

@sample samples.collections.Collections.Collections.collectionContains

## Declarations and overloads

### 1. Common

```kotlin
public operator fun contains(element: @UnsafeVariance E): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L78)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val collection: Collection<Int> = listOf(1, 2, 3)

    println(1 in collection)
    println(4 in collection)

    // Ref does not override equals, so instances compared by reference
    class Ref<T>(val value: T)

    val r0 = Ref(42)
    val refCollection: Collection<Ref<Int>> = listOf(r0)

    println(r0 in refCollection)
    // Ref(42) is a new instance
    println(Ref(42) in refCollection)
}
```

```text title="Output"
true
false
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L107)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
