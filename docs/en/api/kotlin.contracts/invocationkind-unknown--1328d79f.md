# InvocationKind.UNKNOWN

`kotlin.contracts` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A function parameter is called in place, but it's unknown how many times it can be called.

## Declarations and overloads

### 1. Common

```kotlin
// @sample samples.contracts.callsInPlaceUnknownContract
    @ContractsDsl UNKNOWN
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/ContractBuilder.kt#L190)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.contracts.*
inline fun invokeBlock(enabled: Boolean, block: () -> Unit) {
    contract { callsInPlace(block, InvocationKind.UNKNOWN) }
    repeat(if (enabled) 3 else 0) { block() }
}
fun main() { var count = 0; invokeBlock(true) { count++ }; println(count) }
```

```text title="Output"
3
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
