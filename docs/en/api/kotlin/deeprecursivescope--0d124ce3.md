# DeepRecursiveScope

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Use `callRecursive` inside the scope. Direct `invoke` is forbidden; the suppressed legacy call demonstrates its exception for migration.

## Declarations and overloads

### 1. Common

```kotlin
@RestrictsSuspension
@SinceKotlin("1.7")
@WasExperimental(ExperimentalStdlibApi::class)
public sealed class DeepRecursiveScope<T, R>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/DeepRecursive.kt#L85)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val sum = DeepRecursiveFunction<Int, Int> { n -> if (n == 0) 0 else n + callRecursive(n - 1) }
    println(sum(100))
    lateinit var invalid: DeepRecursiveFunction<Int, Int>
    invalid = DeepRecursiveFunction { n -> invalid(n) }
    try { invalid(1) } catch (error: UnsupportedOperationException) { println(error.message) }
}
```

```text title="Output"
5050
Should not be called from DeepRecursiveScope
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
