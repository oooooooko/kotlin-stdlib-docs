# Float.toShort

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

These direct conversions are deprecated. This compatibility example suppresses deprecation errors; explicitly convert to `Int` first in new code.

## Declarations and overloads

### 1. Common

```kotlin
@Deprecated("Unclear conversion. To achieve the same result convert to Int explicitly and then to Short.", ReplaceWith("toInt().toShort()"))
    @DeprecatedSinceKotlin(warningSince = "1.3", errorSince = "1.5")
    @kotlin.internal.IntrinsicConstEvaluation
    public override fun toShort(): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1862)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() { val value = 65.5f; println(value.toChar()); println(value.toByte()); println(value.toShort()); println(value.toInt().toChar()) }
```

```text title="Output"
A
65
65
A
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
