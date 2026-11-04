# MutableMap.MutableEntry

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents a key/value pair held by a `MutableMap`.

Map entries obtained from the iteration of `MutableMap.entries` set are not supposed to be stored separately or
used long after they are obtained.
The behavior of an entry is unspecified if the backing map has been modified after the entry was obtained,
except when the map was modified through the `setValue` method.

To create an immutable entry not connected to any map, one can use `Map.Entry.copy` function.

@param K the type of the entry key. The entry is invariant in its key type.
@param V the type of the entry value. The entry is invariant in its value type.

## Declarations and overloads

### 1. Common

```kotlin
public interface MutableEntry<K, V> : Map.Entry<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L731)

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
    val value = mutableMapOf("a" to 1).entries.first()
    println(value)
}
```

```text title="Output"
a=1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
