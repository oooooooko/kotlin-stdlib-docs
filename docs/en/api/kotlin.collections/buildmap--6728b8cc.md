# buildMap

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Builds a new read-only `Map` by populating a `MutableMap` using the given `builderAction`
and returning a read-only map with the same key-value pairs.

The map passed as a receiver to the `builderAction` is valid only inside that function.
Using it outside of the function produces an unspecified behavior.

Entries of the map are iterated in the order they were added by the `builderAction`.

The returned map is serializable (JVM).

@sample samples.collections.Builders.Maps.buildMapSample

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <K, V> buildMap(@BuilderInference builderAction: MutableMap<K, V>.() -> Unit): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L137)

### 2. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <K, V> buildMap(capacity: Int, @BuilderInference builderAction: MutableMap<K, V>.() -> Unit): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L163)

Builds a new read-only `Map` by populating a `MutableMap` using the given `builderAction`
and returning a read-only map with the same key-value pairs.

The map passed as a receiver to the `builderAction` is valid only inside that function.
Using it outside of the function produces an unspecified behavior.

`capacity` is used to hint the expected number of pairs added in the `builderAction`.

Entries of the map are iterated in the order they were added by the `builderAction`.

The returned map is serializable (JVM).

@throws IllegalArgumentException if the given `capacity` is negative.

@sample samples.collections.Builders.Maps.buildMapSampleWithCapacity

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = mapOf('b' to 2, 'c' to 3)

    val y = buildMap<Char, Int> {
        put('a', 1)
        put('c', 0)
        putAll(x)
        put('d', 4)
    }

    println(y)
}
```

```text title="Output"
{a=1, c=3, b=2, d=4}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L64)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = mapOf('b' to 2, 'c' to 3)

    val y = buildMap<Char, Int>(x.size + 2) {
        put('a', 1)
        put('c', 0)
        putAll(x)
        put('d', 4)
    }

    println(y)
}
```

```text title="Output"
{a=1, c=3, b=2, d=4}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L78)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
