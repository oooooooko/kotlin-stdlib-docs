# partition

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Splits the original sequence into a pair of lists,
where *first* list contains elements for which `predicate` yielded `true`,
while *second* list contains elements for which `predicate` yielded `false`.

The operation is _terminal_.

@sample samples.collections.Sequences.Transformations.partition

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T> Sequence<T>.partition(predicate: (T) -> Boolean): Pair<List<T>, List<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3126)

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
    val result = source.`partition`({ it.toString().length > 0 })
    println(result)
}
```

```text title="Output"
([1, 2, 3], [])
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
