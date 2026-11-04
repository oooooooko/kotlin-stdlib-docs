# windowed

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a sequence of snapshots of the window of the given `size`
sliding along this sequence with the given `step`, where each
snapshot is a list.

Several last lists may have fewer elements than the given `size`.

Both `size` and `step` must be positive and can be greater than the number of elements in this sequence.
@param size the number of elements to take in each window
@param step the number of elements to move the window forward by on an each step, by default 1
@param partialWindows controls whether or not to keep partial windows in the end if any,
by default `false` which means partial windows won't be preserved

@sample samples.collections.Sequences.Transformations.takeWindows

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun <T> Sequence<T>.windowed(size: Int, step: Int = 1, partialWindows: Boolean = false): Sequence<List<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3203)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public fun <T, R> Sequence<T>.windowed(size: Int, step: Int = 1, partialWindows: Boolean = false, transform: (List<T>) -> R): Sequence<R>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3223)

Returns a sequence of results of applying the given `transform` function to
an each list representing a view over the window of the given `size`
sliding along this sequence with the given `step`.

Note that the list passed to the `transform` function is ephemeral and is valid only inside that function.
You should not store it or allow it to escape in some way, unless you made a snapshot of it.
Several last lists may have fewer elements than the given `size`.

Both `size` and `step` must be positive and can be greater than the number of elements in this sequence.
@param size the number of elements to take in each window
@param step the number of elements to move the window forward by on an each step, by default 1
@param partialWindows controls whether or not to keep partial windows in the end if any,
by default `false` which means partial windows won't be preserved

@sample samples.collections.Sequences.Transformations.averageWindows

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
    val source = sequenceOf(1, 2, 3)
    val result = source.`windowed`(2)
    println(result.toList())
}
```

```text title="Output"
[[1, 2], [2, 3]]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
