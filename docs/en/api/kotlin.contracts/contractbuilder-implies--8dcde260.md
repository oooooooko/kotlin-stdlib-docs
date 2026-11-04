# ContractBuilder.implies

`kotlin.contracts` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Specifies the effect that will be observed if the condition passed as a receiver argument holds.

Only `ReturnsNotNull` effect is supported for now.

Note: the receiver can accept only a subset of boolean expressions,
where a function parameter or receiver (`this`) undergoes
- null-checks (`== null`, `!= null`);
- instance-checks (`is`, `!is`);

## Declarations and overloads

### 1. Common

```kotlin
@ExperimentalExtendedContracts
    @ContractsDsl
    @SinceKotlin("2.2") // Technically 2.2.20
    public infix fun Boolean.implies(value: ReturnsNotNull)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/ContractBuilder.kt#L99)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.contracts.*
fun textOrNull(value: Any?): String? {
    contract { (value is String) implies returnsNotNull() }
    return value as? String
}
fun main() { println(textOrNull("Kotlin")); println(textOrNull(42)) }
```

```text title="Output"
Kotlin
null
```

Compiler options: `-Xallow-condition-implies-returns-contracts`

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
