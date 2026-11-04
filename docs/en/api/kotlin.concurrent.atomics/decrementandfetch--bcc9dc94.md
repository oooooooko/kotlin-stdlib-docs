# decrementAndFetch

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Atomically decrements the current value of this `AtomicInt` by one and returns the new value.

@sample samples.concurrent.atomics.AtomicInt.decrementAndFetch

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public fun AtomicInt.decrementAndFetch(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L136)

### 2. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public fun AtomicLong.decrementAndFetch(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L355)

Atomically decrements the current value of this `AtomicLong` by one and returns the new value.

@sample samples.concurrent.atomics.AtomicLong.decrementAndFetch

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicInt(7)
    println(a.decrementAndFetch())
    println(a.load())
}
```

```text title="Output"
6
6
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L112)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicLong(7)
    println(a.decrementAndFetch())
    println(a.load())
}
```

```text title="Output"
6
6
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L257)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
