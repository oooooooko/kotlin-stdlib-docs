# decrementAndFetchAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Atomically decrements the element of this `AtomicIntArray` at the given `index` by one and returns the new value of the element.

@throws IndexOutOfBoundsException if the `index` is out of bounds of this array.

@sample samples.concurrent.atomics.AtomicIntArray.decrementAndFetchAt

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public fun AtomicIntArray.decrementAndFetchAt(index: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L173)

### 2. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public fun AtomicLongArray.decrementAndFetchAt(index: Int): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L442)

Atomically decrements the element of this `AtomicLongArray` at the given `index` by one and returns the new value of the element.

@throws IndexOutOfBoundsException if the `index` is out of bounds of this array.

@sample samples.concurrent.atomics.AtomicLongArray.decrementAndFetchAt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicIntArray(intArrayOf(1, 2, 3))
    println(a.decrementAndFetchAt(1))
    println(a.loadAt(1))
    println(a.toString())
}
```

```text title="Output"
1
1
[1, 1, 3]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L133)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicLongArray(longArrayOf(1, 2, 3))
    println(a.decrementAndFetchAt(1))
    println(a.loadAt(1))
    println(a.toString())
}
```

```text title="Output"
1
1
[1, 1, 3]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L295)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
