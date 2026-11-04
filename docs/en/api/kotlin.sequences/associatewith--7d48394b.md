# associateWith

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a `Map` where keys are elements from the given sequence and values are
produced by the `valueSelector` function applied to each element.

If any two elements are equal, the last one gets added to the map.

The returned map preserves the entry iteration order of the original sequence.

The operation is _terminal_.

@sample samples.collections.Collections.Transformations.associateWith

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
public inline fun <K, V> Sequence<K>.associateWith(valueSelector: (K) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L931)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val words = listOf("a", "abc", "ab", "def", "abcd")
    val withLength = words.associateWith { it.length }
    println(withLength.keys)
    println(withLength.values)
}
```

```text title="Output"
[a, abc, ab, def, abcd]
[1, 3, 2, 3, 4]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L794)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
