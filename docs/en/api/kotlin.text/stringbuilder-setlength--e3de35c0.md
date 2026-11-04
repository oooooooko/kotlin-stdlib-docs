# StringBuilder.setLength

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Sets the length of this string builder to the specified `newLength`.

 If the `newLength` is less than the current length, it is changed to the specified `newLength`.
 Otherwise, null characters '\u0000' are appended to this string builder until its length is less than the `newLength`.

 Note that in Kotlin/JS `set` operator function has non-constant execution time complexity.
 Therefore, increasing length of this string builder and then updating each character by index may slow down your program.

 @throws IndexOutOfBoundsException or `IllegalArgumentException` if `newLength` is less than zero.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
    public fun setLength(newLength: Int)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L285)

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
    val result = source.`setLength`(2)
    println(result)
}
```

```text title="Output"
kotlin.Unit
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
