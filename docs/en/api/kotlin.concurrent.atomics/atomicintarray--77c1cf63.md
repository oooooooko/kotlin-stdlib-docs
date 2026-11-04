# AtomicIntArray

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

An array of ints in which elements may be updated atomically.

Platform-specific implementation details:

When targeting the Native backend, `AtomicIntArray` stores an `IntArray` and atomically updates it's elements.
For additional details about atomicity guarantees for reads and writes see `kotlin.concurrent.Volatile`.

When targeting the JVM, instances of `AtomicIntArray` are represented by
[java.util.concurrent.atomic.AtomicIntegerArray](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicIntegerArray.html).
For details about guarantees of volatile accesses and updates of atomics refer to The Java Language Specification (17.4 Memory Model).

For JS and Wasm `AtomicIntArray` is implemented trivially and is not thread-safe since these platforms do not support multi-threading.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public expect class AtomicIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L15)

### 2. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public inline fun AtomicIntArray(size: Int, init: (Int) -> Int): AtomicIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L136)

Creates a new `AtomicIntArray` of the given `size`, where each element is initialized by calling the given `init` function.

The function `init` is called for each array element sequentially starting from the first one.
It should return the value for an array element given its index.

@throws RuntimeException if the specified `size` is negative.

@sample samples.concurrent.atomics.AtomicIntArray.initCons

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicIntArray(3) { it * 10 }
    println(a.toString())
}
```

```text title="Output"
[0, 10, 20]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L27)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
