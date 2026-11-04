# insert

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Inserts the string representation of the specified byte `value` into this string builder at the specified `index` and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was inserted into this string builder at the specified `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.insert(index: Int, value: Byte): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L345)

### 2. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.insert(index: Int, value: Short): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L356)

Inserts the string representation of the specified short `value` into this string builder at the specified `index` and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was inserted into this string builder at the specified `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

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
import kotlin.text.*

fun main() {
    val source = StringBuilder("kotlin")
    val result = source.`insert`(0, 2.toByte())
    println(result)
}
```

```text title="Output"
2kotlin
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
