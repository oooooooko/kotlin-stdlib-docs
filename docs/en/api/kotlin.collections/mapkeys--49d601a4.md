# mapKeys

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new Map with entries having the keys obtained by applying the `transform` function to each entry in this
`Map` and the values of this map.

In case if any two entries are mapped to the equal keys, the value of the latter one will overwrite
the value associated with the former one.

The returned map preserves the entry iteration order of the original map.

@sample samples.collections.Maps.Transformations.mapKeys

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <K, V, R> Map<out K, V>.mapKeys(transform: (Map.Entry<K, V>) -> R): Map<R, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L613)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

private class OperationOnRange<E, R>(
        val element: E,
        val fromIndex: Int,
        val toIndex: Int,
        val expectedResult: R
    )

private fun UIntArray.toUByteArray(): UByteArray {
    return UByteArray(size) { get(it).toUByte() }
}

private fun UIntArray.toUShortArray(): UShortArray {
    return UShortArray(size) { get(it).toUShort() }
}

private fun UIntArray.toULongArray(): ULongArray {
    return ULongArray(size) { get(it).toULong() }
}

fun main() {

        val expected = mapOf(1u to "one", 2u to "two", 3u to "three")
        println(uintArrayOf(2u, 3u).associateWithTo(expected.toMutableMap()) { it.toString() })
        println(ubyteArrayOf(2u, 3u).associateWithTo(expected.mapKeys { it.key.toUByte() }.toMutableMap()) { it.toString() })
        println(ushortArrayOf(2u, 3u).associateWithTo(expected.mapKeys { it.key.toUShort() }.toMutableMap()) { it.toString() })
        println(ulongArrayOf(2u, 3u).associateWithTo(expected.mapKeys { it.key.toULong() }.toMutableMap()) { it.toString() })
    
}
```

```text title="Output"
{1=one, 2=2, 3=3}
{1=one, 2=2, 3=3}
{1=one, 2=2, 3=3}
{1=one, 2=2, 3=3}
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/UnsignedArraysTest.kt#L828)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
