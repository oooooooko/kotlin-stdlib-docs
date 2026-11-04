# setOf

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new read-only set with the given elements.
Elements of the set are iterated in the order they were specified.
The returned set is serializable (JVM).
@sample samples.collections.Collections.Sets.readOnlySet

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> setOf(vararg elements: T): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L38)

### 2. Common

```kotlin
@SinceKotlin("1.9")
public expect fun <T> setOf(element: T): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L46)

Returns a new read-only set containing only the specified object `element`.

The returned set is serializable (JVM).

@sample samples.collections.Collections.Sets.singletonReadOnlySet

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> setOf(): Set<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L56)

Returns an empty read-only set.  The returned set is serializable (JVM).
@sample samples.collections.Collections.Sets.emptyReadOnlySet

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set1 = setOf(1, 2, 3)
    val set2 = setOf(3, 2, 1)

    // setOf preserves the iteration order of elements
    println(set1)
    println(set2)

    // but the sets with the same elements are equal no matter of order
    println(set1 == set2)
}
```

```text title="Output"
[1, 2, 3]
[3, 2, 1]
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L578)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set = setOf('a')
    println(set)
    println(set.size)
}
```

```text title="Output"
[a]
1
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L591)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set = setOf<String>()
    println(set.isEmpty())

    // another way to create an empty set,
    // type parameter is inferred from the expected type
    val other: Set<Int> = emptySet()

    println(set == other)
    println(set)
}
```

```text title="Output"
true
true
[]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L565)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
