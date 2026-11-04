# IntroducedAt

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The version belongs to the library being published, not Kotlin itself. Annotated parameters need defaults; the compiler emits old signatures for binary compatibility.

## Declarations and overloads

### 1. Common

```kotlin
@Target(AnnotationTarget.VALUE_PARAMETER)
@MustBeDocumented
@SinceKotlin("2.3")
@ExperimentalVersionOverloading
public annotation class IntroducedAt(val version: String)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/VersionOverloads.kt#L24)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun greeting(name: String, @IntroducedAt("1.1") punctuation: String = "!"): String = "Hello, $name$punctuation"
fun main() { println(greeting("Kotlin")); println(greeting("Kotlin", "?")) }
```

```text title="Output"
Hello, Kotlin!
Hello, Kotlin?
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
