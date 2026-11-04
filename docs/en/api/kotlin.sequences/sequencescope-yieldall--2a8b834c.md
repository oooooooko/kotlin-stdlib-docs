# SequenceScope.yieldAll

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Yields all values from the `iterator` to the `Iterator` being built
and suspends until all these values are iterated and the next one is requested.

The sequence of values returned by the given iterator can be potentially infinite.

@sample samples.collections.Sequences.Building.buildSequenceYieldAll

## Declarations and overloads

### 1. Common

```kotlin
public abstract suspend fun yieldAll(iterator: Iterator<T>)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L99)

### 2. Common

```kotlin
public suspend fun yieldAll(elements: Iterable<T>)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L109)

Yields a collections of values to the `Iterator` being built
and suspends until all these values are iterated and the next one is requested.

@sample samples.collections.Sequences.Building.buildSequenceYieldAll

### 3. Common

```kotlin
public suspend fun yieldAll(sequence: Sequence<T>): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L120)

Yields potentially infinite sequence of values  to the `Iterator` being built
and suspends until all these values are iterated and the next one is requested.

The sequence can be potentially infinite.

@sample samples.collections.Sequences.Building.buildSequenceYieldAll

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*



fun main() {

        val result = sequence<Int> {
            yieldAll(listOf())
        }
        println(result.toList())
    
}
```

```text title="Output"
[]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/SequenceBuilderTest.kt#L220)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
