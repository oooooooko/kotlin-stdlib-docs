# updateAndFetch

`kotlin.concurrent.atomics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Atomically updates the value of this `AtomicInt` with the value obtained by calling the `transform` function on the current value
and returns the new value.

`transform` may be invoked more than once to recompute a result.
That may happen, for example, when this atomic integer value was concurrently updated while `transform` was applied,
or due to a spurious compare-and-set failure.
The latter is implementation-specific, and it should not be relied upon.

On platforms that do no support multi-threading (JS and Wasm), this operation has a trivial implementation
and `transform` will be invoked exactly once.

It's recommended to keep `transform` fast and free of side effects.

@sample samples.concurrent.atomics.AtomicInt.updateAndFetch

## Declarations and overloads

### 1. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun AtomicInt.updateAndFetch(transform: (Int) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L207)

### 2. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun AtomicLong.updateAndFetch(transform: (Long) -> Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L426)

Atomically updates the value of this `AtomicLong` with the value obtained by calling the `transform` function on the current value
and returns the new value.

That may happen, for example, when this atomic long value was concurrently updated while `transform` was applied,
or due to a spurious compare-and-set failure.
The latter is implementation-specific, and it should not be relied upon.

On platforms that do no support multi-threading (JS and Wasm), this operation has a trivial implementation
and `transform` will be invoked exactly once.

It's recommended to keep `transform` fast and free of side effects.

@sample samples.concurrent.atomics.AtomicLong.updateAndFetch

### 3. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun <T> AtomicReference<T>.updateAndFetch(transform: (T) -> T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L644)

Atomically updates the value of this `AtomicReference` with the value obtained by calling the `transform` function on the current value
and returns the new value.

`transform` may be invoked more than once to recompute a result.
That may happen, for example, when this atomic reference was concurrently updated while `transform` was applied,
or due to a spurious compare-and-set failure.
The latter is implementation-specific, and it should not be relied upon.

On platforms that do no support multi-threading (JS and Wasm), this operation has a trivial implementation
and `transform` will be invoked exactly once.

It's recommended to keep `transform` fast and free of side effects.

@sample samples.concurrent.atomics.AtomicReference.updateAndFetch

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicInt(7)
    val updatedValue = a.updateAndFetch { currentValue ->
        when (currentValue % 2) {
            0 -> currentValue / 2
            else -> 3 * currentValue + 1
        }
    }
    println(updatedValue)
    println(a.load())
}
```

```text title="Output"
22
22
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L131)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicLong(7L)
    val updatedValue = a.updateAndFetch { currentValue ->
        when (currentValue % 2) {
            0L -> currentValue / 2
            else -> 3 * currentValue + 1
        }
    }
    println(updatedValue)
    println(a.load())
}
```

```text title="Output"
22
22
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L277)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    data class Wallet(val owner: String, val balance: Long)

    val a = AtomicReference(Wallet("Kodee", 100_00L))
    val updatedWallet = a.updateAndFetch { wallet ->
        wallet.copy(balance = wallet.balance + 1_00) // Kodee got a buck!
    }
    println(updatedWallet)
    println(a.load())
}
```

```text title="Output"
Wallet(owner=Kodee, balance=10100)
Wallet(owner=Kodee, balance=10100)
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L412)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
