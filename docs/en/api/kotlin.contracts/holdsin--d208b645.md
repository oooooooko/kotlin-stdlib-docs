# HoldsIn

`kotlin.contracts` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Describes a situation when a provided condition is guaranteed to be true in the body of a functional parameter.

@see ContractBuilder.holdsIn

## Declarations and overloads

### 1. Common

```kotlin
@ContractsDsl
@ExperimentalContracts
@ExperimentalExtendedContracts
@SinceKotlin("2.2")
public interface HoldsIn : Effect
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/Effect.kt#L97)

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
