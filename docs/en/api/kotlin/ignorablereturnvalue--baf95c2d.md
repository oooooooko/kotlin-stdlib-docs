# IgnorableReturnValue

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Expresses that calls of the annotated function are ignorable.
Ignorable calls would not trigger a warning from Kotlin's return value checker, even if they are not used.

This annotation only makes sense when used together with the 'Return value checker' feature.
Placing it without enabling the corresponding feature would result in a compiler error.

Please note that this feature is currently experimental and this annotation may be changed without further notice
or deprecation cycle. This, in particular, concerns annotation's target list.

## Declarations and overloads

### 1. Common

```kotlin
@Target(AnnotationTarget.FUNCTION)
@MustBeDocumented
@SinceKotlin("2.2")
public annotation class IgnorableReturnValue
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/ReturnValue.kt#L8)

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
    val value = kotlin.IgnorableReturnValue()
    println(value)
}
```

```text title="Output"
@kotlin.IgnorableReturnValue()
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
