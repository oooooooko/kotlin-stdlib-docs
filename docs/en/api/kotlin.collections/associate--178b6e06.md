# associate

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a `Map` containing key-value pairs provided by `transform` function
applied to elements of the given array.

If any of two pairs would have the same key the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitives

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, K, V> Array<out T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10097)

### 2. Common

```kotlin
public inline fun <K, V> ByteArray.associate(transform: (Byte) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10112)

### 3. Common

```kotlin
public inline fun <K, V> ShortArray.associate(transform: (Short) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10127)

### 4. Common

```kotlin
public inline fun <K, V> IntArray.associate(transform: (Int) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10142)

### 5. Common

```kotlin
public inline fun <K, V> LongArray.associate(transform: (Long) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10157)

### 6. Common

```kotlin
public inline fun <K, V> FloatArray.associate(transform: (Float) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10172)

### 7. Common

```kotlin
public inline fun <K, V> DoubleArray.associate(transform: (Double) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10187)

### 8. Common

```kotlin
public inline fun <K, V> BooleanArray.associate(transform: (Boolean) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10202)

### 9. Common

```kotlin
public inline fun <K, V> CharArray.associate(transform: (Char) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10217)

### 10. Common

```kotlin
public inline fun <T, K, V> Iterable<T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1353)

Returns a `Map` containing key-value pairs provided by `transform` function
applied to elements of the given collection.

If any of two pairs would have the same key the last one gets added to the map.

The returned map preserves the entry iteration order of the original collection.

@sample samples.collections.Collections.Transformations.associate

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val names = listOf("Grace Hopper", "Jacob Bernoulli", "Johann Bernoulli")

    val byLastName = names.associate { it.split(" ").let { (firstName, lastName) -> lastName to firstName } }

    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="Output"
{Hopper=Grace, Bernoulli=Johann}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L708)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
