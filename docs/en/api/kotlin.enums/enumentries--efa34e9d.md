# EnumEntries

`kotlin.enums` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A specialized immutable implementation of `List` interface that
contains all enum entries of the specified enum type `E`.
`EnumEntries` contains all enum entries in the order they are declared in the source code,
consistently with the corresponding `Enum.ordinal` values.

An instance of this interface can be obtained from `EnumClass.entries` property or with `enumEntries` function.

#### Implementation note
All basic operations, such as `get`, `contains` and `indexOf`, are executed in constant time and are likely to be
faster than regular `ArrayList<E>` counterparts.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public sealed interface EnumEntries<E : Enum<E>> : List<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/enums/EnumEntries.kt#L14)

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
import kotlin.enums.*

enum class Demo { FIRST, SECOND }

fun main() {
    val value = Demo.entries
    println(value)
}
```

```text title="Output"
[FIRST, SECOND]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
