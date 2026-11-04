# Target

`kotlin.annotation` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

This meta-annotation indicates the kinds of code elements which are possible targets of an annotation.

If the target meta-annotation is not present on an annotation declaration, the annotation is applicable to the following elements:
`CLASS`, `PROPERTY`, `FIELD`, `LOCAL_VARIABLE`, `VALUE_PARAMETER`, `CONSTRUCTOR`, `FUNCTION`, `PROPERTY_GETTER`, `PROPERTY_SETTER`.

@property allowedTargets list of allowed annotation targets

## Declarations and overloads

### 1. Common

```kotlin
@Target(AnnotationTarget.ANNOTATION_CLASS)
@MustBeDocumented
public annotation class Target(vararg val allowedTargets: AnnotationTarget)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotation/Annotations.kt#L63)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.annotation.*

fun main() {
    val value = kotlin.annotation.Target(kotlin.annotation.AnnotationTarget.ANNOTATION_CLASS)
    println(value)
}
```

```text title="Output"
@kotlin.annotation.Target(allowedTargets=[ANNOTATION_CLASS])
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
