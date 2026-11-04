# AtomicArray.compareAndSetAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Atomically stores the `new value``newValue` into the element of this `AtomicArray` at the given `index`
if the current value equals the `expected value``expectedValue`.
Returns true if the operation was successful and false only if the current value of the element was not equal to the expected value.

This operation has so-called strong semantics,
meaning that it returns false if and only if current and expected values are not equal.

Comparison of values is done by reference.

@throws IndexOutOfBoundsException if the `index` is out of bounds of this array.

@sample samples.concurrent.atomics.AtomicArray.compareAndSetAt

## Declarations and overloads

### 1. Common

```kotlin
public fun compareAndSetAt(index: Int, expectedValue: T, newValue: T): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L614)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicArray(arrayOf("aaa", "bbb", "ccc"))
    // Current value of a[1] is "bbb", it is equal to the expected value "bbb" -> compareAndSetAt succeeds.
    println(a.compareAndSetAt(index = 1, expectedValue = "bbb", newValue = "kkk"))
    println(a.loadAt(1))
    println(a.toString())

    // Current value of a[2] is "ccc", it is not equal to the expected value "aaa" -> compareAndSetAt fails.
    println(a.compareAndSetAt(index = 2, expectedValue = "aaa", newValue = "jjj"))
    println(a.loadAt(2))
    println(a.toString())
}
```

```text title="Output"
true
kkk
[aaa, kkk, ccc]
false
ccc
[aaa, kkk, ccc]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L393)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
