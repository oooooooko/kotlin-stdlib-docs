# nextUBytes

`kotlin.random` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Fills the specified unsigned byte `array` with random bytes and returns it.

@return `array` filled with random bytes.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@IgnorableReturnValue
public fun Random.nextUBytes(array: UByteArray): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L113)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Random.nextUBytes(size: Int): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L126)

Creates an unsigned byte array of the specified `size`, filled with random bytes.

### 3. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@IgnorableReturnValue
public fun Random.nextUBytes(array: UByteArray, fromIndex: Int = 0, toIndex: Int = array.size): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L133)

Fills a subrange of the specified `UByte` `array` starting from `fromIndex` inclusive and ending `toIndex` exclusive with random UBytes.

@return `array` with the subrange filled with random bytes.

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
import kotlin.random.*

fun main() {
    val source = Random(42)
    val result = source.`nextUBytes`(ubyteArrayOf(1u, 2u, 3u))
    println(result.contentToString())
}
```

```text title="Output"
[204, 239, 57]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
