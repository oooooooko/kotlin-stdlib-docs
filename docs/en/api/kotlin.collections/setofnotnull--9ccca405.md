# setOfNotNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new read-only set either with single given element, if it is not null, or empty set if the element is null.
The returned set is serializable (JVM).
@sample samples.collections.Collections.Sets.setOfNotNull

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Any> setOfNotNull(element: T?): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L103)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Any> setOfNotNull(vararg elements: T?): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L111)

Returns a new read-only set only with those given elements, that are not null.
Elements of the set are iterated in the order they were specified.
The returned set is serializable (JVM).
@sample samples.collections.Collections.Sets.setOfNotNull

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val empty = setOfNotNull<Any>(null)
    println(empty)

    val singleton = setOfNotNull(42)
    println(singleton)

    val set = setOfNotNull(1, null, 2, null, 3)
    println(set)
}
```

```text title="Output"
[]
[42]
[1, 2, 3]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L629)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
