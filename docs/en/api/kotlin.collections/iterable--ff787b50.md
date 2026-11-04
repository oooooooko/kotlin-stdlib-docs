# Iterable

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Classes that inherit from this interface can be represented as a sequence of elements that can
be iterated over.
@param T the type of element being iterated over. The iterator is covariant in its element type.

## Declarations and overloads

### 1. Common

```kotlin
public expect interface Iterable<out T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L9)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Iterable(crossinline iterator: () -> Iterator<T>): Iterable<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Iterables.kt#L10)

Given an `iterator` function constructs an `Iterable` instance that returns values through the `Iterator`
provided by that function.
@sample samples.collections.Iterables.Building.iterable

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val iterable = Iterable {
        iterator {
            yield(42)
            yieldAll(1..5 step 2)
        }
    }
    val result = iterable.mapIndexed { index, value -> "$index: $value" }
    println(result)

    // can be iterated many times
    repeat(2) {
        val sum = iterable.sum()
        println(sum)
    }
}
```

```text title="Output"
[0: 42, 1: 1, 2: 3, 3: 5]
51
51
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L26)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
