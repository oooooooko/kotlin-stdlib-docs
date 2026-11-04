# DeprecatedSinceKotlin

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Marks the annotated declaration as deprecated. In contrast to `Deprecated`, severity of the reported diagnostic is not a constant value,
but differs depending on the API version of the usage (the value of the `-api-version` argument when compiling the module where
the usage is located). If the API version is greater or equal than `hiddenSince`, the declaration will not be accessible from the code
(as if it was deprecated with level `DeprecationLevel.HIDDEN`), otherwise if the API version is greater or equal than `errorSince`,
the usage will be marked as an error (as with `DeprecationLevel.ERROR`), otherwise if the API version is greater or equal
than `warningSince`, the usage will be marked as a warning (as with `DeprecationLevel.WARNING`), otherwise the annotation is ignored.

@property warningSince The version, since which this deprecation should be reported as a warning.
@property errorSince The version, since which this deprecation should be reported as a error.
@property hiddenSince The version, since which the annotated declaration should not be available in code.

## Declarations and overloads

### 1. Common

```kotlin
@Target(CLASS, FUNCTION, PROPERTY, ANNOTATION_CLASS, CONSTRUCTOR, PROPERTY_SETTER, PROPERTY_GETTER, TYPEALIAS)
@MustBeDocumented
@SinceKotlin("1.4")
public annotation class DeprecatedSinceKotlin(
    val warningSince: String = "",
    val errorSince: String = "",
    val hiddenSince: String = ""
)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L42)

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
import kotlin.*

fun main() {
    val value = kotlin.DeprecatedSinceKotlin()
    println(value)
}
```

```text title="Output"
@kotlin.DeprecatedSinceKotlin(warningSince=, errorSince=, hiddenSince=)
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
