# asReversed

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a reversed read-only view of the original List.
All changes made in the original list will be reflected in the reversed one.
@sample samples.collections.ReversedViews.asReversedList

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> List<T>.asReversed(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/ReversedViews.kt#L72)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("asReversedMutable")
public fun <T> MutableList<T>.asReversed(): MutableList<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/ReversedViews.kt#L79)

Returns a reversed mutable view of the original mutable List.
All changes made in the original list will be reflected in the reversed one and vice versa.
@sample samples.collections.ReversedViews.asReversedMutableList

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val original = mutableListOf('a', 'b', 'c', 'd', 'e')
    val originalReadOnly = original as List<Char>
    val reversed = originalReadOnly.asReversed()

    println(original)
    println(reversed)

    // changing the original list affects its reversed view
    original.add('f')
    println(original)
    println(reversed)

    original[original.lastIndex] = 'z'
    println(original)
    println(reversed)
}
```

```text title="Output"
[a, b, c, d, e]
[e, d, c, b, a]
[a, b, c, d, e, f]
[f, e, d, c, b, a]
[a, b, c, d, e, z]
[z, e, d, c, b, a]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/reversedViews.kt#L22)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val original = mutableListOf(1, 2, 3, 4, 5)
    val reversed = original.asReversed()

    println(original)
    println(reversed)

    // changing the reversed view affects the original list
    reversed.add(0)
    println(original)
    println(reversed)

    // changing the original list affects its reversed view
    original[2] = -original[2]
    println(original)
    println(reversed)
}
```

```text title="Output"
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
[0, 1, 2, 3, 4, 5]
[5, 4, 3, 2, 1, 0]
[0, 1, -2, 3, 4, 5]
[5, 4, 3, -2, 1, 0]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/reversedViews.kt#L41)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
