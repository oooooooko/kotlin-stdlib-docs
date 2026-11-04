# Deprecated

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Marks the annotated declaration as deprecated.

A deprecated API element is not recommended to use, typically because it's being phased out or a better alternative exists.

To help removing deprecated API gradually, the property `level` could be used.
Usually a gradual phase-out goes through the "warning", then "error", then "hidden" or "removed" stages:
- First and by default, `DeprecationLevel.WARNING` is used to notify API consumers, but not to break their compilation or runtime usages.
- Then, some time later the deprecation level is raised to `DeprecationLevel.ERROR`, so that no new Kotlin code can be compiled
  using the deprecated API.
- Finally, the API is either removed entirely, or hidden (`DeprecationLevel.HIDDEN`) from code,
so its usages look like unresolved references, while the API remains in the compiled code
preserving binary compatibility with previously compiled code.

@property message The message explaining the deprecation and recommending an alternative API to use.
@property replaceWith If present, specifies a code fragment which should be used as a replacement for
 the deprecated API usage.
@property level Specifies how the deprecated element usages are reported in code.
 See the `DeprecationLevel` enum for the possible values.

## Declarations and overloads

### 1. Common

```kotlin
@Target(CLASS, FUNCTION, PROPERTY, ANNOTATION_CLASS, CONSTRUCTOR, PROPERTY_SETTER, PROPERTY_GETTER, TYPEALIAS)
@MustBeDocumented
public annotation class Deprecated(
    val message: String,
    val replaceWith: ReplaceWith = ReplaceWith(""),
    val level: DeprecationLevel = DeprecationLevel.WARNING
)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L14)

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
    val value = kotlin.Deprecated("o")
    println(value)
}
```

```text title="Output"
@kotlin.Deprecated(message=o, replaceWith=@kotlin.ReplaceWith(expression=, imports=[]), level=WARNING)
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
