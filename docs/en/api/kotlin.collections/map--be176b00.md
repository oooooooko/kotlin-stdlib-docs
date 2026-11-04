# Map

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

A collection that holds pairs of objects (keys and values) and supports retrieving the value corresponding to each key,
checking if a collection holds a particular key or a value. Maps also allow iterating over keys, values or key-value pairs (entries).
Complex operations are built upon this functionality and provided in form of `kotlin.collections` extension functions.

Map keys are unique; the map holds only one value for each key. In contrast, the same value can be associated with several unique keys.

It is implementation-specific how `Map` defines key's uniqueness. If not stated otherwise, `Map` implementations are usually
distinguishing elements using `Any.equals`. However, it is not the only way to distinguish elements, and some implementations may use
referential equality or compare elements by some of their properties. It is recommended to explicitly specify how a class
implementing `Map` distinguish elements.

It is also implementation-specific how `Map` handles `null` keys and values: some `Map` implementations may support them, while
other may not. It is recommended to explicitly define key/value nullability policy when implementing `Map`.

`Map` does not guarantee any particular order for iteration over its keys, values, or entries. However, particular implementations
are free to have fixed iteration order, like "smaller", in some sense, keys are visited prior to "larger". In this case,
it is recommended to explicitly document ordering guarantees for the `Map` implementation.

Unlike `Collection` implementations, `Map` implementations must override `Any.toString`, `Any.equals` and `Any.hashCode` functions
and provide implementations such that:
- `Map.toString` should return a string containing string representation of contained key-value pairs in iteration order.
- `Map.equals` should consider two maps equal if and only if they contain the same keys and values associated with these keys
  are equal. Unlike some other `equals` implementations, `Map.equals` should consider two maps equal even
  if they are instances of different classes; the only requirement here is that both maps have to implement `Map` interface.
- `Map.hashCode` should be computed as a sum of `Entry` hash codes, and entry's hash code should be computed as exclusive or (XOR) of
  hash codes corresponding to a key and a value:
  ```kotlin
  var hashCode: Int = 0
  for ((k, v) in entries) hashCode += k.hashCode() xor v.hashCode()
  ```

Functions in this interface support only read-only access to the map; read-write access is supported through
the `MutableMap` interface.

@param K the type of map keys. The map is invariant in its key type, as it
         can accept a key as a parameter (of `containsKey` for example) and return it in a `keys` set.
@param V the type of map values. The map is covariant in its value type.

## Declarations and overloads

### 1. Common

```kotlin
public expect interface Map<K, out V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L516)

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
    val value = linkedMapOf("a" to 1, "b" to 2)
    println(value)
}
```

```text title="Output"
{a=1, b=2}
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
