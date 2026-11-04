# unzip

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a pair of lists, where
*first* list is built from the first values of each pair from this array,
*second* list is built from the second values of each pair from this array.
@sample samples.collections.Arrays.Transformations.unzipArray

## Declarations and overloads

### 1. Common

```kotlin
public fun <T, R> Array<out Pair<T, R>>.unzip(): Pair<List<T>, List<R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Arrays.kt#L37)

### 2. Common

```kotlin
public fun <T, R> Iterable<Pair<T, R>>.unzip(): Pair<List<T>, List<R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Iterables.kt#L54)

Returns a pair of lists, where
*first* list is built from the first values of each pair from this collection,
*second* list is built from the second values of each pair from this collection.
@sample samples.collections.Iterables.Operations.unzipIterable

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf(1 to 'a', 2 to 'b', 3 to 'c')
    println(list.unzip())
}
```

```text title="Output"
([1, 2, 3], [a, b, c])
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L54)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
