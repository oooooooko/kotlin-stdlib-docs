# DoubleIterator

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

An iterator over a sequence of values of type `Double`.

This is a substitute for `Iterator<Double>` that provides a specialized version of `next(): T` method: `nextDouble(): Double`
and has a special handling by the compiler to avoid platform-specific boxing conversions as a performance optimization.

In the following example:

```kotlin
class DoubleContainer(private val data: DoubleArray) {

    // DoubleIterator instead of Iterator<Double> in the signature
    operator fun iterator(): DoubleIterator = object : DoubleIterator() {
        private var idx = 0

        override fun nextDouble(): Double {
            if (!hasNext()) throw NoSuchElementException()
            return data`idx++`
        }

        override fun hasNext(): Boolean = idx < data.size
    }
}

for (element in DoubleContainer(doubleArrayOf(1.0, 2.0, 3.0))) {
    ... handle element ...
}
```
No boxing conversion is performed during the for-loop iteration.
Note that the iterator itself will still be allocated.

## Declarations and overloads

### 1. Common

```kotlin
public abstract class DoubleIterator : Iterator<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/PrimitiveIterators.kt#L264)

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
import kotlin.collections.*

fun main() {
    val value = doubleArrayOf(1.0, 2.0, 3.0).iterator()
    println(value.next())
}
```

```text title="Output"
1.0
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
