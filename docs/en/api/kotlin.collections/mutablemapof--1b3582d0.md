# mutableMapOf

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an empty new `MutableMap`.

The returned map preserves the entry iteration order.
@sample samples.collections.Maps.Instantiation.emptyMutableMap

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public inline fun <K, V> mutableMapOf(): MutableMap<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L77)

### 2. Common

```kotlin
public fun <K, V> mutableMapOf(vararg pairs: Pair<K, V>): MutableMap<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L87)

Returns a new `MutableMap` with the specified contents, given as a list of pairs
where the first component is the key and the second is the value.

If multiple pairs have the same key, the resulting map will contain the value from the last of those pairs.

Entries of the map are iterated in the order they were specified.

@sample samples.collections.Maps.Instantiation.mutableMapFromPairs
@sample samples.collections.Maps.Instantiation.emptyMutableMap

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character by its code
    val result = mutableMapOf<Int, Char>()
    string.associateByTo(result) { char -> char.code }
    // notice each char code occurs only once
    println(result)
}
```

```text title="Output"
{98=b, 111=o, 110=n, 101=e, 32= , 106=j, 117=u, 114=r, 233=é}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L216)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
