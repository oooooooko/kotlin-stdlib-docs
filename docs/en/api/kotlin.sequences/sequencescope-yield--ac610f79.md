# SequenceScope.yield

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Yields a value to the `Iterator` being built and suspends
until the next value is requested.

@sample samples.collections.Sequences.Building.buildSequenceYieldAll
@sample samples.collections.Sequences.Building.buildFibonacciSequence

## Declarations and overloads

### 1. Common

```kotlin
public abstract suspend fun yield(value: T)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L90)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*



fun main() {

        val result = sequence {
            yieldAll(listOf(1, 2, 3))
            yield(4)
        }
        println(result.toList())
    
}
```

```text title="Output"
[1, 2, 3, 4]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/SequenceBuilderTest.kt#L186)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
