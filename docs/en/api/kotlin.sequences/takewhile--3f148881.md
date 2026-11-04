# takeWhile

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a sequence containing first elements satisfying the given `predicate`.

The operation is _intermediate_ and _stateless_.

@sample samples.collections.Collections.Transformations.take

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Sequence<T>.takeWhile(predicate: (T) -> Boolean): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L575)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val chars = ('a'..'z').toList()
    println(chars.take(3))
    println(chars.takeWhile { it < 'f' })
    println(chars.takeLast(2))
    println(chars.takeLastWhile { it > 'w' })
}
```

```text title="Output"
[a, b, c]
[a, b, c, d, e]
[y, z]
[x, y, z]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L911)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
