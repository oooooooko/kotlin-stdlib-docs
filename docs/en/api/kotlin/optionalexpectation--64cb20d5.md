# OptionalExpectation

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

This minimal multiplatform compilation puts `common.kt` in the common source set. The optional annotation is erased without an actual implementation; the common function still works.

## Declarations and overloads

### 1. Common

```kotlin
@Target(ANNOTATION_CLASS)
@Retention(AnnotationRetention.BINARY)
@ExperimentalMultiplatform
public annotation class OptionalExpectation
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/Multiplatform.kt#L37)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() { println(taggedValue()) }
```

```text title="Output"
common annotation, no actual required
```

```kotlin title="common.kt"
@file:OptIn(kotlin.ExperimentalMultiplatform::class)
@OptionalExpectation
expect annotation class OptionalTrace()
@OptionalTrace
fun taggedValue(): String = "common annotation, no actual required"
```

Compiler options: `-Xmulti-platform` `-Xcommon-sources={common.kt}`

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
