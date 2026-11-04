# KType.isMarkedNullable

`kotlin.reflect` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

`true` if this type was marked nullable in the source code.

For Kotlin types, it means that `null` value is allowed to be represented by this type.
In practice it means that the type was declared with a question mark at the end.
For non-Kotlin types, it means the type or the symbol which was declared with this type
is annotated with a runtime-retained nullability annotation such as `javax.annotation.Nullable`.

Note that even if `isMarkedNullable` is false, values of the type can still be `null`.
This may happen if it is a type of the type parameter with a nullable upper bound:

```
fun <T> foo(t: T) {
    // isMarkedNullable == false for t's type, but t can be null here when T = "Any?"
}
```

## Declarations and overloads

### 1. Common

```kotlin
public val isMarkedNullable: Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KType.kt#L35)

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
    val result = source.`isMarkedNullable`
    println(result)
}
```

```text title="Output"
false
```

This example requires `kotlin-reflect:2.4.21`.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
