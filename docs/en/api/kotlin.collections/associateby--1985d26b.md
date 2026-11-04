# associateBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a `Map` containing the elements from the given array indexed by the key
returned from `keySelector` function applied to each element.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesBy

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, K> Array<out T>.associateBy(keySelector: (T) -> K): Map<K, T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10232)

### 2. Common

```kotlin
public inline fun <K> ByteArray.associateBy(keySelector: (Byte) -> K): Map<K, Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10247)

### 3. Common

```kotlin
public inline fun <K> ShortArray.associateBy(keySelector: (Short) -> K): Map<K, Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10262)

### 4. Common

```kotlin
public inline fun <K> IntArray.associateBy(keySelector: (Int) -> K): Map<K, Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10277)

### 5. Common

```kotlin
public inline fun <K> LongArray.associateBy(keySelector: (Long) -> K): Map<K, Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10292)

### 6. Common

```kotlin
public inline fun <K> FloatArray.associateBy(keySelector: (Float) -> K): Map<K, Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10307)

### 7. Common

```kotlin
public inline fun <K> DoubleArray.associateBy(keySelector: (Double) -> K): Map<K, Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10322)

### 8. Common

```kotlin
public inline fun <K> BooleanArray.associateBy(keySelector: (Boolean) -> K): Map<K, Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10337)

### 9. Common

```kotlin
public inline fun <K> CharArray.associateBy(keySelector: (Char) -> K): Map<K, Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10352)

### 10. Common

```kotlin
public inline fun <T, K, V> Array<out T>.associateBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10367)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByWithValueTransform

### 11. Common

```kotlin
public inline fun <K, V> ByteArray.associateBy(keySelector: (Byte) -> K, valueTransform: (Byte) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10381)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByWithValueTransform

### 12. Common

```kotlin
public inline fun <K, V> ShortArray.associateBy(keySelector: (Short) -> K, valueTransform: (Short) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10395)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByWithValueTransform

### 13. Common

```kotlin
public inline fun <K, V> IntArray.associateBy(keySelector: (Int) -> K, valueTransform: (Int) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10409)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByWithValueTransform

### 14. Common

```kotlin
public inline fun <K, V> LongArray.associateBy(keySelector: (Long) -> K, valueTransform: (Long) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10423)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByWithValueTransform

### 15. Common

```kotlin
public inline fun <K, V> FloatArray.associateBy(keySelector: (Float) -> K, valueTransform: (Float) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10437)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByWithValueTransform

### 16. Common

```kotlin
public inline fun <K, V> DoubleArray.associateBy(keySelector: (Double) -> K, valueTransform: (Double) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10451)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByWithValueTransform

### 17. Common

```kotlin
public inline fun <K, V> BooleanArray.associateBy(keySelector: (Boolean) -> K, valueTransform: (Boolean) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10465)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByWithValueTransform

### 18. Common

```kotlin
public inline fun <K, V> CharArray.associateBy(keySelector: (Char) -> K, valueTransform: (Char) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10479)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original array.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByWithValueTransform

### 19. Common

```kotlin
public inline fun <T, K> Iterable<T>.associateBy(keySelector: (T) -> K): Map<K, T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1368)

Returns a `Map` containing the elements from the given collection indexed by the key
returned from `keySelector` function applied to each element.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original collection.

@sample samples.collections.Collections.Transformations.associateBy

### 20. Common

```kotlin
public inline fun <T, K, V> Iterable<T>.associateBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1383)

Returns a `Map` containing the values provided by `valueTransform` and indexed by `keySelector` functions applied to elements of the given collection.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

The returned map preserves the entry iteration order of the original collection.

@sample samples.collections.Collections.Transformations.associateByWithValueTransform

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String) {
        override fun toString(): String = "$firstName $lastName"
    }

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = scientists.associateBy { it.lastName }

    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="Output"
{Hopper=Grace Hopper, Bernoulli=Johann Bernoulli}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L718)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String)

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = scientists.associateBy({ it.lastName }, { it.firstName })

    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="Output"
{Hopper=Grace, Bernoulli=Johann}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L732)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
