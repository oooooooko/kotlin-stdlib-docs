# AtomicIntArray.compareAndExchangeAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Atomically stores the `new value``newValue` into the element of this `AtomicIntArray` at the given `index`
if the current value equals the `expected value``expectedValue` and returns the old value of the element in any case.

Comparison of values is done by value.

@throws IndexOutOfBoundsException if the `index` is out of bounds of this array.

@sample samples.concurrent.atomics.AtomicIntArray.compareAndExchangeAt

## Declarations and overloads

### 1. Common

```kotlin
public fun compareAndExchangeAt(index: Int, expectedValue: Int, newValue: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L98)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicIntArray(intArrayOf(1, 2, 3))
    // Current value of a[1] is 2, it is equal to the expected value 2 ->
    // compareAndExchangeAt succeeds, stores the new value 7 to a[1] and returns the old value 2.
    println(a.compareAndExchangeAt(index = 1, expectedValue = 2, newValue = 7))
    println(a.loadAt(1))
    println(a.toString())

    // Current value of a[2] is 3, it is not equal to the expected value 4 ->
    // compareAndExchangeAt fails, does not store the new value to a[2] and returns the current value 3.
    println(a.compareAndExchangeAt(index = 2, expectedValue = 4, newValue = 25))
    println(a.loadAt(2))
    println(a.toString())
}
```

```text title="Output"
2
7
[1, 7, 3]
3
3
[1, 7, 3]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L75)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
