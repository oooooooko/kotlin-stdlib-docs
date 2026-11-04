# Sequence

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A sequence that returns values through its iterator. The values are evaluated lazily, and the sequence
is potentially infinite.

Sequences can be iterated multiple times, however some sequence implementations might constrain themselves
to be iterated only once. That is mentioned specifically in their documentation (e.g. `generateSequence` overload).
The latter sequences throw an exception on an attempt to iterate them the second time.

Sequence operations, like `Sequence.map`, `Sequence.filter` etc, generally preserve that property of a sequence, and
again it's documented for an operation if it doesn't.

@param T the type of elements in the sequence.

## Declarations and overloads

### 1. Common

```kotlin
public interface Sequence<out T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequence.kt#L8)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Sequence(crossinline iterator: () -> Iterator<T>): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L14)

Given an `iterator` function constructs a `Sequence` that returns values through the `Iterator`
provided by that function.
The values are evaluated lazily, and the sequence is potentially infinite.

@sample samples.collections.Sequences.Building.sequenceFromIterator

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.sequences.*

fun main() {
    val value = sequenceOf(1, 2, 3)
    println(value)
}
```

```text title="Output"
kotlin.collections.ArraysKt___ArraysKt$asSequence$$inlined$Sequence$1@511d50c0
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
