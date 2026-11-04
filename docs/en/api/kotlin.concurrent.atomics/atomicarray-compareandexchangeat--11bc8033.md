# AtomicArray.compareAndExchangeAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Atomically stores the `new value``newValue` into the element of this `AtomicArray` at the given `index`
if the current value equals the `expected value``expectedValue` and returns the old value of the element in any case.

Comparison of values is done by reference.

@throws IndexOutOfBoundsException if the `index` is out of bounds of this array.

@sample samples.concurrent.atomics.AtomicArray.compareAndExchangeAt

## Declarations and overloads

### 1. Common

```kotlin
public fun compareAndExchangeAt(index: Int, expectedValue: T, newValue: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L630)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicArray(arrayOf("aaa", "bbb", "ccc"))
    // Current value of a[1] is "bbb, it is equal to the expected value "bbb" ->
    // compareAndExchangeAt succeeds, stores the new value "kkk" to a[1] and returns the old value "bbb".
    println(a.compareAndExchangeAt(index = 1, expectedValue = "bbb", newValue = "kkk"))
    println(a.loadAt(1))
    println(a.toString())

    // Current value of a[2] is "ccc", it is not equal to the expected value "aaa" ->
    // compareAndExchangeAt fails, does not store the new value to a[2] and returns the current value "ccc".
    println(a.compareAndExchangeAt(index = 2, expectedValue = "aaa", newValue = "jjj"))
    println(a.loadAt(2))
    println(a.toString())
}
```

```text title="Output"
bbb
kkk
[aaa, kkk, ccc]
ccc
ccc
[aaa, kkk, ccc]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L407)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
