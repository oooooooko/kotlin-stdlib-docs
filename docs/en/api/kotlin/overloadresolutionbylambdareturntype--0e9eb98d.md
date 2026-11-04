# OverloadResolutionByLambdaReturnType

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Enables overload selection based on the type of the value returned from lambda argument.

When two or more function overloads have otherwise the same parameter lists that differ only in the return type
of a functional parameter, this annotation enables overload selection by the type of the value returned from
the lambda function passed to this functional parameter.

Example:
```
@OverloadResolutionByLambdaReturnType
fun create(intProducer: () -> Int): Int

fun create(doubleProducer: () -> Double): Double

val newValue = create { 3.14 }
```

The annotation being applied to one of overloads allows to resolve this ambiguity by analyzing what value is returned
from the lambda function.

This annotation is also used to discriminate the annotated overloads in case if overload selection still cannot
choose one of them even taking in account the result of lambda parameter analysis. In that case a warning is reported.

Note: this annotation is experimental, see `ExperimentalTypeInference` on how to opt-in for it.

## Declarations and overloads

### 1. Common

```kotlin
@Target(FUNCTION)
@Retention(AnnotationRetention.BINARY)
@SinceKotlin("1.4")
@ExperimentalTypeInference
public annotation class OverloadResolutionByLambdaReturnType
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/Inference.kt#L42)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


@OverloadResolutionByLambdaReturnType
fun choose(block: () -> Int, marker: Int = 0): String = "Int: ${block()}"
@OverloadResolutionByLambdaReturnType
fun choose(block: () -> String, marker: String = ""): String = "String: ${block()}"
fun main() { println(choose({ 42 })); println(choose({ "Kotlin" })) }
```

```text title="Output"
Int: 42
String: Kotlin
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
