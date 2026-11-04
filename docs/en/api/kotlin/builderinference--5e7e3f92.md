# BuilderInference

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

This is a compatibility example. Modern Kotlin enables builder inference automatically when needed; the annotation is deprecated.

## Declarations and overloads

### 1. Common

```kotlin
@Target(VALUE_PARAMETER, FUNCTION, PROPERTY)
@Retention(AnnotationRetention.BINARY)
@SinceKotlin("1.3")
@ExperimentalTypeInference
@Deprecated("BuilderInference annotation must not be used anymore. Builder inference is enabled automatically for builder calls if needed.")
@DeprecatedSinceKotlin(warningSince = "2.0", errorSince = "2.5", hiddenSince = "2.6")
public annotation class BuilderInference
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/Inference.kt#L11)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun <T> collect(@BuilderInference block: MutableList<T>.() -> Unit): List<T> = mutableListOf<T>().apply(block)
fun main() { val values = collect { add("Kotlin"); add("stdlib") }; println(values) }
```

```text title="Output"
[Kotlin, stdlib]
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
