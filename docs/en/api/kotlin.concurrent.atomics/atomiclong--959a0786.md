# AtomicLong

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A `Long` value that may be updated atomically.

Platform-specific implementation details:

When targeting the Native backend, `AtomicLong` stores a volatile `Long` variable and atomically updates it.
For additional details about atomicity guarantees for reads and writes see `kotlin.concurrent.Volatile`.

When targeting the JVM, instances of `AtomicLong` are represented by
[java.util.concurrent.atomic.AtomicLong](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicLong.html).
For details about guarantees of volatile accesses and updates of atomics refer to The Java Language Specification (17.4 Memory Model).

For JS and Wasm `AtomicLong` is implemented trivially and is not thread-safe since these platforms do not support multi-threading.

@constructor Creates a new `AtomicLong` initialized with the specified value.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public expect class AtomicLong public constructor(value: Long)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L234)

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
import kotlin.concurrent.atomics.*

fun main() {
    val value = kotlin.concurrent.atomics.AtomicLong(1L)
    println(value)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
