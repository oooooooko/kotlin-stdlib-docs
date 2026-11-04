# ContractBuilder.holdsIn

`kotlin.contracts` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Specifies the condition, passed as a receiver argument, that is guaranteed to be true in the body of a function parameter `lambda`.

Note: the receiver accepts only a restricted boolean expression representing the condition, where the expression may include
only the boolean parameter of the function defining the contract, or its negation.

## Declarations and overloads

### 1. Common

```kotlin
@ExperimentalExtendedContracts
    @ContractsDsl
    @SinceKotlin("2.2") // Technically 2.2.20
    public infix fun <R> Boolean.holdsIn(lambda: Function<R>): HoldsIn
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/ContractBuilder.kt#L114)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.contracts.*
inline fun whenEnabled(enabled: Boolean, block: () -> Unit) {
    contract { enabled holdsIn block; callsInPlace(block, InvocationKind.AT_MOST_ONCE) }
    if (enabled) block()
}
fun main() { val enabled = true; whenEnabled(enabled) { println("enabled=$enabled") } }
```

```text title="Output"
enabled=true
```

Compiler options: `-Xallow-holdsin-contract`

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
