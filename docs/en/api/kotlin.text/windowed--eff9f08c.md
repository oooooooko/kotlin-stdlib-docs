# windowed

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list of snapshots of the window of the given `size`
sliding along this char sequence with the given `step`, where each
snapshot is a string.

Several last strings may have fewer characters than the given `size`.

Both `size` and `step` must be positive and can be greater than the number of elements in this char sequence.
@param size the number of elements to take in each window
@param step the number of elements to move the window forward by on an each step, by default 1
@param partialWindows controls whether or not to keep partial windows in the end if any,
by default `false` which means partial windows won't be preserved

@sample samples.collections.Sequences.Transformations.takeWindows

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun CharSequence.windowed(size: Int, step: Int = 1, partialWindows: Boolean = false): List<String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2414)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public fun <R> CharSequence.windowed(size: Int, step: Int = 1, partialWindows: Boolean = false, transform: (CharSequence) -> R): List<R>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2434)

Returns a list of results of applying the given `transform` function to
an each char sequence representing a view over the window of the given `size`
sliding along this char sequence with the given `step`.

Note that the char sequence passed to the `transform` function is ephemeral and is valid only inside that function.
You should not store it or allow it to escape in some way, unless you made a snapshot of it.
Several last char sequences may have fewer characters than the given `size`.

Both `size` and `step` must be positive and can be greater than the number of elements in this char sequence.
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
import kotlin.text.*

fun main() {
    val source = "kotlin"
    val result = source.`windowed`(2)
    println(result)
}
```

```text title="Output"
[ko, ot, tl, li, in]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
