# ReplaceWith

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Specifies a code fragment that can be used to replace a deprecated function, property or class. Tools such
as IDEs can automatically apply the replacements specified through this annotation.

@property expression The replacement expression. It is interpreted in the context
  of the symbol being used, and can reference members of enclosing classes etc.
  For function calls, the replacement expression may contain argument names of the deprecated function,
  which will be substituted with actual parameters used in the call being updated. The imports used in the file
  containing the deprecated function or property are NOT accessible; if the replacement expression refers
  on any of those imports, they need to be specified explicitly in the `imports` parameter.
@property imports The qualified names that need to be imported in order for the references in the
  replacement expression to be resolved correctly.

## Declarations and overloads

### 1. Common

```kotlin
@Target()
@Retention(BINARY)
@MustBeDocumented
public annotation class ReplaceWith(val expression: String, vararg val imports: String)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L63)

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
    val value = kotlin.ReplaceWith("o", "o")
    println(value)
}
```

```text title="Output"
@kotlin.ReplaceWith(expression=o, imports=[o])
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
