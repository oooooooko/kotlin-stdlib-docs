# MutableListIterator.set

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Replaces the last element returned by `next` or `previous` with the specified element `element`.

@throws IllegalStateException if neither `next` nor `previous` has not been called yet,
or the most recent `next` or `previous` call has already been followed by a `remove` or `add` call.

## Declarations and overloads

### 1. Common

```kotlin
public fun set(element: T): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Iterator.kt#L96)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

private fun Iterator<*>.seekEnd() {
    while (hasNext()) {
        next()
    }
}

fun main() {

        val original = mutableListOf(2, 3, 4)
        val iter = original.asReversed().listIterator()

        while (iter.hasNext()) {
            val v = iter.next()
            iter.set(v * v)
        }

        println(original)
    
}
```

```text title="Output"
[4, 9, 16]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/ReversedViewsTest.kt#L256)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
