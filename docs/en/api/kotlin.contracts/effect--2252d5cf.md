# Effect

`kotlin.contracts` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Effect interfaces are produced by the contract DSL, not instantiated as ordinary objects. Contracts guide smart casts and initialization analysis; they do not enforce the function's promises at runtime.

## Declarations and overloads

### 1. Common

```kotlin
@ContractsDsl
@ExperimentalContracts
@SinceKotlin("1.3")
public interface Effect
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/Effect.kt#L10)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.contracts.*
fun isText(value: Any?): Boolean {
    contract { returns(true) implies (value is String) }
    return value is String
}
fun requireText(value: Any?) {
    contract { returns() implies (value is String) }
    require(value is String)
}
fun textOrNull(value: Any?): String? {
    contract { returnsNotNull() implies (value is String) }
    return value as? String
}
inline fun once(block: () -> Unit) {
    contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE) }
    block()
}
fun main() {
    val value: Any? = "Kotlin"
    if (isText(value)) println(value.length)
    requireText(value)
    println(value.length)
    val result = textOrNull(value)
    println(result)
    val initialized: Int
    once { initialized = 42 }
    println(initialized)
}
```

```text title="Output"
6
6
Kotlin
42
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
