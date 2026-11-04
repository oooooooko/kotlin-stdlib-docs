# groupBy

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Groups elements of the original sequence by the key returned by the given `keySelector` function
applied to each element and returns a map where each group key is associated with a list of corresponding elements.

The returned map preserves the entry iteration order of the keys produced from the original sequence.

The operation is _terminal_.

@sample samples.collections.Collections.Transformations.groupBy

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, K> Sequence<T>.groupBy(keySelector: (T) -> K): Map<K, List<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1169)

### 2. Common

```kotlin
public inline fun <T, K, V> Sequence<T>.groupBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1183)

Groups values returned by the `valueTransform` function applied to each element of the original sequence
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original sequence.

The operation is _terminal_.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val words = listOf("a", "abc", "ab", "def", "abcd")
    val byLength = words.groupBy { it.length }

    println(byLength.keys)
    println(byLength.values)

    val mutableByLength: MutableMap<Int, MutableList<String>> = words.groupByTo(mutableMapOf()) { it.length }
    // same content as in byLength map, but the map is mutable
    println(mutableByLength == byLength)
}
```

```text title="Output"
[1, 3, 2, 4]
[[a], [abc, def], [ab], [abcd]]
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L826)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val nameToTeam = listOf("Alice" to "Marketing", "Bob" to "Sales", "Carol" to "Marketing")
    val namesByTeam = nameToTeam.groupBy({ it.second }, { it.first })
    println(namesByTeam)

    val mutableNamesByTeam = nameToTeam.groupByTo(HashMap(), { it.second }, { it.first })
    // same content as in namesByTeam map, but the map is mutable
    println(mutableNamesByTeam == namesByTeam)
}
```

```text title="Output"
{Marketing=[Alice, Carol], Sales=[Bob]}
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L839)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
