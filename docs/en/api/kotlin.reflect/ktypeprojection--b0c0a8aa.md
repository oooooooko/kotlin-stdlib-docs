# KTypeProjection

`kotlin.reflect` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents a type projection. Type projection is usually the argument to another type in a type usage.
For example, in the type `Array<out Number>`, `out Number` is the covariant projection of the type represented by the class `Number`.

Type projection is either the star projection, or an entity consisting of a specific type plus optional variance.

See the [Kotlin language documentation](https://kotlinlang.org/docs/reference/generics.html#type-projections)
for more information.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
public data class KTypeProjection constructor(
    /**
     * The use-site variance specified in the projection, or `null` if this is a star projection.
     */
    public val variance: KVariance?,
    /**
     * The type specified in the projection, or `null` if this is a star projection.
     */
    public val type: KType?
)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KTypeProjection.kt#L15)

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
import kotlin.reflect.*

fun main() {
    val value = kotlin.reflect.KTypeProjection(kotlin.reflect.KVariance.IN, typeOf<List<String>>())
    println(value)
}
```

```text title="Output"
in kotlin.collections.List<kotlin.String>
```

This example requires `kotlin-reflect:2.4.21`.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
