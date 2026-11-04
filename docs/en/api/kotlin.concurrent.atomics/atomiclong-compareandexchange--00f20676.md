# AtomicLong.compareAndExchange

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Atomically stores the given `new value``newValue` into this `AtomicLong` if the current value equals the `expected value``expectedValue`
and returns the old value in any case.

Comparison of values is done by value.

@sample samples.concurrent.atomics.AtomicLong.compareAndExchange

## Declarations and overloads

### 1. Common

```kotlin
public fun compareAndExchange(expectedValue: Long, newValue: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L287)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicLong(7)
    // Current value 7 is equal to the expected value 7 ->
    // compareAndExchange succeeds, stores the new value 10 and returns the old value 7.
    println(a.compareAndExchange(7, 10))
    println(a.load())

    // Current value 10 is not equal to the expected value 2 ->
    // compareAndExchange fails, does not store the new value and returns the current value 10.
    println(a.compareAndExchange(2, 12))
    println(a.load())
}
```

```text title="Output"
7
10
10
10
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L192)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
