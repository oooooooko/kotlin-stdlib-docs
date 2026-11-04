# listOfNotNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new read-only list either of single given element, if it is not null, or empty list if the element is null. The returned list is serializable (JVM).
@sample samples.collections.Collections.Lists.listOfNotNull

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Any> listOfNotNull(element: T?): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L130)

### 2. Common

```kotlin
public fun <T : Any> listOfNotNull(vararg elements: T?): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L136)

Returns a new read-only list only of those given elements, that are not null.  The returned list is serializable (JVM).
@sample samples.collections.Collections.Lists.listOfNotNull

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val empty = listOfNotNull<Any>(null)
    println(empty)

    val singleton = listOfNotNull(42)
    println(singleton)

    val list = listOfNotNull(1, null, 2, null, 3)
    println(list)
}
```

```text title="Output"
[]
[42]
[1, 2, 3]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L215)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
