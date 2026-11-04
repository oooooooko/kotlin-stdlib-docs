# getOrPutIfMissing

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the value for the given `key` if the value is present.
Otherwise, calls the `defaultValue` function,
puts its result into the map under the given key, and returns the call result.

In contrast to `getOrPutIfNull`, this function returns
the mapped value, even if that value is `null`.

When the given `key` is not in this map, the result of `defaultValue`,
even if `null`, is put into the map under the key.
If `defaultValue` throws an exception, the exception is rethrown.

Note that the operation is not guaranteed to be atomic if the map is being modified concurrently.

@throws NullPointerException if the specified `key` or the result of `defaultValue` is `null`,
  and this map does not support `null` keys or values.

@sample samples.collections.Maps.Usage.getOrPutIfMissing

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
@kotlin.internal.InlineOnly
@ExperimentalStdlibApi
public inline fun <K, V> MutableMap<K, V>.getOrPutIfMissing(key: K, crossinline defaultValue: () -> V): V
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L500)

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
import kotlin.collections.*

fun main() {
    val source = linkedMapOf("a" to 1, "b" to 2)
    val result = source.`getOrPutIfMissing`("a", { 42 })
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
