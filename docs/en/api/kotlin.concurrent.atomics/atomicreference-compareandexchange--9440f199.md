# AtomicReference.compareAndExchange

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Atomically stores the given `new value``newValue` into this `AtomicReference` if the current value equals the `expected value``expectedValue`
and returns the old value in any case.

Comparison of values is done by reference.

@sample samples.concurrent.atomics.AtomicReference.compareAndExchange

## Declarations and overloads

### 1. Common

```kotlin
public fun compareAndExchange(expectedValue: T, newValue: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L575)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicReference("aaa")
    // Current value "aaa" is equal to the expected value "aaa" ->
    // compareAndExchange succeeds, stores the new value "bbb" and returns the old value "aaa".
    println(a.compareAndExchange("aaa", "bbb"))
    println(a.load())

    // Current value "bbb" is not equal to the expected value "aaa" ->
    // compareAndExchange fails, does not store the new value and returns the current value "bbb".
    println(a.compareAndExchange("aaa", "kkk"))
    println(a.load())
}
```

```text title="Output"
aaa
bbb
bbb
bbb
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L387)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
