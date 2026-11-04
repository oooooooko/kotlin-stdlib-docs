# mapOf

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new read-only map with the specified contents, given as a list of pairs
where the first value is the key and the second is the value.

If multiple pairs have the same key, the resulting map will contain the value from the last of those pairs.

Entries of the map are iterated in the order they were specified.

The returned map is serializable (JVM).

@sample samples.collections.Maps.Instantiation.mapFromPairs

## Declarations and overloads

### 1. Common

```kotlin
public fun <K, V> mapOf(vararg pairs: Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L42)

### 2. Common

```kotlin
@SinceKotlin("1.9")
public expect fun <K, V> mapOf(pair: Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L57)

Returns a new read-only map, mapping only the specified key to the
specified value.

The returned map is serializable (JVM).

@sample samples.collections.Maps.Instantiation.mapFromPairs

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <K, V> mapOf(): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L68)

Returns an empty read-only map.

The returned map is serializable (JVM).
@sample samples.collections.Maps.Instantiation.emptyReadOnlyMap

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
    val result = `mapOf`(Pair(1, "one"))
    println(result)
}
```

```text title="Output"
{1=one}
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
