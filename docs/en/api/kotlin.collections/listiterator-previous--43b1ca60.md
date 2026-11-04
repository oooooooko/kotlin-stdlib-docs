# ListIterator.previous

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the previous element in the iteration and moves the cursor position backwards.

@throws NoSuchElementException if the iteration has no previous element.

## Declarations and overloads

### 1. Common

```kotlin
public fun previous(): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Iterator.kt#L55)

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

        assertFailsWith<NoSuchElementException> {
            listOf(1, 2, 3).asReversed().listIterator().previous()
        }
        assertFailsWith<NoSuchElementException> {
            mutableListOf(1, 2, 3).asReversed().listIterator().previous()
        }
    
}
```

```text title="Output"

```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/ReversedViewsTest.kt#L330)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
