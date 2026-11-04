# sequenceOf

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a sequence that returns the specified values.

@sample samples.collections.Sequences.Building.sequenceOfValues

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> sequenceOf(vararg elements: T): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L33)

### 2. Common

```kotlin
@SinceKotlin("2.2")
public fun <T> sequenceOf(element: T): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L40)

Creates a `Sequence` that contains a single given element.

@param element the single element to be contained in the resulting sequence.
@return a sequence containing only the specified `element`.
@sample samples.collections.Sequences.Building.sequenceOfSingleValue

### 3. Common

```kotlin
@SinceKotlin("2.2")
@InlineOnly
public inline fun <T> sequenceOf(): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L62)

Creates an empty `Sequence`.

@return an empty sequence.
@sample samples.collections.Sequences.Building.sequenceOfEmpty

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
    val result = `sequenceOf`(1)
    println(result.toList())
}
```

```text title="Output"
[1]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
