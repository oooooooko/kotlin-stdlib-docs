# KType.arguments

`kotlin.reflect` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Type arguments passed for the parameters of the classifier in this type.
For example, in the type `Array<out Number>` the only type argument is `out Number`.

In case this type is based on an inner class, the returned list contains the type arguments provided for the innermost class first,
then its outer class, and so on.
For example, in the type `Outer<A, B>.Inner<C, D>` the returned list is ``C, D, A, B``.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
    public val arguments: List<KTypeProjection>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KType.kt#L24)

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
    val source = typeOf<List<String>>()
    val result = source.`arguments`
    println(result)
}
```

```text title="Output"
[kotlin.String]
```

This example requires `kotlin-reflect:2.4.21`.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
