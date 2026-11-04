# flatten

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a single list of all elements from all arrays in the given array.
@sample samples.collections.Arrays.Transformations.flattenArray

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out Array<out T>>.flatten(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Arrays.kt#L15)

### 2. Common

```kotlin
public fun <T> Iterable<Iterable<T>>.flatten(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Iterables.kt#L42)

Returns a single list of all elements from all collections in the given collection.
@sample samples.collections.Iterables.Operations.flattenIterable

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val deepList = listOf(listOf(1), listOf(2, 3), listOf(4, 5, 6))
    println(deepList.flatten())
}
```

```text title="Output"
[1, 2, 3, 4, 5, 6]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L48)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
