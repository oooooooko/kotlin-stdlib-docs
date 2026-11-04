# updateAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Atomically updates the element of this `AtomicIntArray` at the given index using the `transform` function.

`transform` may be invoked more than once to recompute a result.
That may happen, for example,
when an integer value at the specified index was concurrently updated while `transform` was applied,
or due to a spurious compare-and-set failure.
The latter is implementation-specific, and it should not be relied upon.

On platforms that do no support multi-threading (JS and Wasm), this operation has a trivial implementation
and `transform` will be invoked exactly once.

It's recommended to keep `transform` fast and free of side effects.

@throws IndexOutOfBoundsException if the `index` is out of bounds of this array.

@sample samples.concurrent.atomics.AtomicIntArray.updateAt

## Declarations and overloads

### 1. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun AtomicIntArray.updateAt(index: Int, transform: (Int) -> Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L195)

### 2. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun AtomicLongArray.updateAt(index: Int, transform: (Long) -> Long): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L464)

Atomically updates the element of this `AtomicLongArray` at the given index using the `transform` function.

`transform` may be invoked more than once to recompute a result.
That may happen, for example,
when a long value at the specified index was concurrently updated while `transform` was applied,
or due to a spurious compare-and-set failure.
The latter is implementation-specific, and it should not be relied upon.

On platforms that do no support multi-threading (JS and Wasm), this operation has a trivial implementation
and `transform` will be invoked exactly once.

It's recommended to keep `transform` fast and free of side effects.

@throws IndexOutOfBoundsException if the `index` is out of bounds of this array.

@sample samples.concurrent.atomics.AtomicLongArray.updateAt

### 3. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun <T> AtomicArray<T>.updateAt(index: Int, transform: (T) -> T): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L681)

Atomically updates the element of this `AtomicArray` at the given index using the `transform` function.

`transform` may be invoked more than once to recompute a result.
That may happen, for example,
when a reference at the specified index was concurrently updated while `transform` was applied,
or due to a spurious compare-and-set failure.
The latter is implementation-specific, and it should not be relied upon.

On platforms that do no support multi-threading (JS and Wasm), this operation has a trivial implementation
and `transform` will be invoked exactly once.

It's recommended to keep `transform` fast and free of side effects.

@throws IndexOutOfBoundsException if the `index` is out of bounds of this array.

@sample samples.concurrent.atomics.AtomicArray.updateAt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicIntArray(intArrayOf(1, 2, 3))
    a.updateAt(1) { currentValue -> currentValue * 10 }
    println(a.toString())

    // The index is out of array bounds
    assertFailsWith<IndexOutOfBoundsException> { a.updateAt(10) { it } }
}
```

```text title="Output"
[1, 20, 3]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L141)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicLongArray(longArrayOf(1L, 2L, 3L))
    a.updateAt(1) { currentValue -> currentValue * 10L }
    println(a.toString())

    // The index is out of array bounds
    assertFailsWith<IndexOutOfBoundsException> { a.updateAt(10) { it } }
}
```

```text title="Output"
[1, 20, 3]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L303)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicArray(arrayOf("hello", "concurrent", "world"))
    a.updateAt(1) { currentValue -> currentValue.uppercase() }
    println(a.toString())

    // The index is out of array bounds
    assertFailsWith<IndexOutOfBoundsException> { a.updateAt(10) { it } }
}
```

```text title="Output"
[hello, CONCURRENT, world]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L423)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
