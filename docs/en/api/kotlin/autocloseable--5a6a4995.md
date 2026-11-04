# AutoCloseable

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A resource that can be closed or released.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.0")
@WasExperimental(ExperimentalStdlibApi::class)
public expect interface AutoCloseable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/AutoCloseable.kt#L11)

### 2. Common

```kotlin
@SinceKotlin("2.0")
@kotlin.internal.InlineOnly
public expect inline fun AutoCloseable(crossinline closeAction: () -> Unit): AutoCloseable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/AutoCloseable.kt#L34)

Returns an `AutoCloseable` instance that executes the specified `closeAction`
upon invocation of its ``close()```AutoCloseable.close` function.

This function allows specifying custom cleanup actions for resources.

Note that each invocation of the `close()` function on the returned `AutoCloseable` instance executes the `closeAction`.
Therefore, implementers are strongly recommended to make the `closeAction` idempotent, or to prevent multiple invocations.

Example:

```kotlin
val autoCloseable = AutoCloseable {
    // Cleanup action, e.g., closing a file or releasing a network connection
    Logger.log("Releasing the network connection.")
    networkConnection.release()
}

// Now you can pass the autoCloseable to a function or use it directly.
autoCloseable.use {
    // Use the connection, which will be automatically released when this scope finishes.
    val content = networkConnection.readContent()
    Logger.log("Network connection content: $content")
}
```

@See AutoCloseable.use

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
import kotlin.*

fun main() {
    val value = AutoCloseable { println("closed") }
    println(value)
}
```

```text title="Output"
ExampleKt$$Lambda$1/0x000000e001000a08@7344699f
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
