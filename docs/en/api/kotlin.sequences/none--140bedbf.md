# none

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if the sequence has no elements.

The operation is _terminal_.

@sample samples.collections.Collections.Aggregates.none

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Sequence<T>.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L2579)

### 2. Common

```kotlin
public inline fun <T> Sequence<T>.none(predicate: (T) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L2590)

Returns `true` if no elements match the given `predicate`.

The operation is _terminal_.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val emptyList = emptyList<Int>()
    println(emptyList.none())

    val nonEmptyList = listOf("one", "two", "three")
    println(nonEmptyList.none())
}
```

```text title="Output"
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L997)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val isEven: (Int) -> Boolean = { it % 2 == 0 }
    val zeroToTen = 0..10
    println(zeroToTen.none { isEven(it) })
    println(zeroToTen.none(isEven))

    val odds = zeroToTen.map { it * 2 + 1 }
    println(odds.none { isEven(it) })

    val emptyList = emptyList<Int>()
    println(emptyList.none { true })
}
```

```text title="Output"
false
false
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1006)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
