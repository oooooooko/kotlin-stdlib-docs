# toMap

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new map containing all key-value pairs from the given collection of pairs.

The returned map preserves the entry iteration order of the original collection.
If any of two pairs would have the same key the last one gets added to the map.

## Declarations and overloads

### 1. Common

```kotlin
public fun <K, V> Iterable<Pair<K, V>>.toMap(): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L713)

### 2. Common

```kotlin
@IgnorableReturnValue
public fun <K, V, M : MutableMap<in K, in V>> Iterable<Pair<K, V>>.toMap(destination: M): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L730)

Populates and returns the `destination` mutable map with key-value pairs from the given collection of pairs.

### 3. Common

```kotlin
public fun <K, V> Array<out Pair<K, V>>.toMap(): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L737)

Returns a new map containing all key-value pairs from the given array of pairs.

The returned map preserves the entry iteration order of the original array.
If any of two pairs would have the same key the last one gets added to the map.

### 4. Common

```kotlin
@IgnorableReturnValue
public fun <K, V, M : MutableMap<in K, in V>> Array<out Pair<K, V>>.toMap(destination: M): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L749)

Populates and returns the `destination` mutable map with key-value pairs from the given array of pairs.

### 5. Common

```kotlin
public fun <K, V> Sequence<Pair<K, V>>.toMap(): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L756)

Returns a new map containing all key-value pairs from the given sequence of pairs.

The returned map preserves the entry iteration order of the original sequence.
If any of two pairs would have the same key the last one gets added to the map.

### 6. Common

```kotlin
@IgnorableReturnValue
public fun <K, V, M : MutableMap<in K, in V>> Sequence<Pair<K, V>>.toMap(destination: M): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L764)

Populates and returns the `destination` mutable map with key-value pairs from the given sequence of pairs.

### 7. Common

```kotlin
@SinceKotlin("1.1")
public fun <K, V> Map<out K, V>.toMap(): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L771)

Returns a new read-only map containing all key-value pairs from the original map.

The returned map preserves the entry iteration order of the original map.

### 8. Common

```kotlin
@SinceKotlin("1.1")
@IgnorableReturnValue
public fun <K, V, M : MutableMap<in K, in V>> Map<out K, V>.toMap(destination: M): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L791)

Populates and returns the `destination` mutable map with key-value pairs from the given map.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("c" to 1, "b" to 2, "a" to 1, "d" to 0, null to 0)

    val valueComparator = compareBy<Pair<String?, Int>> { it.second }
    val map1 = list.sortedWith(valueComparator).toMap()
    println(map1)

    val valueThenKeyComparator = valueComparator
        .thenComparator({ a, b -> compareValues(a.first, b.first) })
    val map2 = list.sortedWith(valueThenKeyComparator).toMap()
    println(map2)
}
```

```text title="Output"
{d=0, null=0, c=1, a=1, b=2}
{null=0, d=0, a=1, c=1, b=2}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L164)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
