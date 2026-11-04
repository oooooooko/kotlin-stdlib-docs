# distinct

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a sequence containing only distinct elements from the given sequence.

Among equal elements of the given sequence, only the first one will be present in the resulting sequence.
The elements in the resulting sequence are in the same order as they were in the source sequence.

The operation is _intermediate_ and _stateful_.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Sequence<T>.distinct(): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1368)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf('a', 'A', 'b', 'B', 'A', 'a')
    println(list.distinct())
    println(list.distinctBy { it.uppercaseChar() })
}
```

```text title="Output"
[a, A, b, B]
[a, b]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L819)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
