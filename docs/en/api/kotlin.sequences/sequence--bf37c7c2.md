# sequence

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Builds a `Sequence` lazily yielding values one by one.

If the consuming code stops iterating the sequence before it's completed,
the remainder of the computation will not run at all.
In particular, it means that `finally` blocks may be left unexecuted:

```
val sequenceOfOne = sequence {
    try {
        yield(1)
        // no code after the `yield(1)` line will be executed!
    } finally {
        println("This line will not run")
    }
}
// only get the first element, do not attempt evaluating the rest of them
println(sequenceOfOne.first())
```

@see kotlin.sequences.generateSequence

@sample samples.collections.Sequences.Building.buildSequenceYieldAll
@sample samples.collections.Sequences.Building.buildFibonacciSequence

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@Suppress("DEPRECATION")
public fun <T> sequence(@BuilderInference block: suspend SequenceScope<T>.() -> Unit): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L16)

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
    val result = `sequence`({ yield(1); yield(2) })
    println(result.toList())
}
```

```text title="Output"
[1, 2]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
