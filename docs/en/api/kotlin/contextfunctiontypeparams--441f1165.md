# ContextFunctionTypeParams

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Signifies that the annotated functional type has the prefix of size `count` for context receivers.
Thus, `@ContextFunctionTypeParams(2) @ExtensionFunctionType Function4<String, Int, Double, Byte, Unit>` is a normalized representation of
`context(String, Int) Double.(Byte) -> Unit`.

Just the same as @ExtensionFunctionType, this annotation is not assumed to be used in source code, preferring the explicit function type
syntax, like in the example above.

There's no need in any additional opt-in limitations because this annotation might only be referenced by users
who turned on an experimental `-Xcontext-receivers` compiler flag, for which there are no backward/forward compatibilities guarantees.

## Declarations and overloads

### 1. Common

```kotlin
@Target(TYPE)
@MustBeDocumented
@SinceKotlin("1.7")
public annotation class ContextFunctionTypeParams(val count: Int)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L102)

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
    val value = kotlin.ContextFunctionTypeParams(2)
    println(value)
}
```

```text title="Output"
@kotlin.ContextFunctionTypeParams(count=2)
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
