# groupBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Groups elements of the original array by the key returned by the given `keySelector` function
applied to each element and returns a map where each group key is associated with a list of corresponding elements.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupBy

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, K> Array<out T>.groupBy(keySelector: (T) -> K): Map<K, List<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12271)

### 2. Common

```kotlin
public inline fun <K> ByteArray.groupBy(keySelector: (Byte) -> K): Map<K, List<Byte>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12283)

### 3. Common

```kotlin
public inline fun <K> ShortArray.groupBy(keySelector: (Short) -> K): Map<K, List<Short>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12295)

### 4. Common

```kotlin
public inline fun <K> IntArray.groupBy(keySelector: (Int) -> K): Map<K, List<Int>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12307)

### 5. Common

```kotlin
public inline fun <K> LongArray.groupBy(keySelector: (Long) -> K): Map<K, List<Long>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12319)

### 6. Common

```kotlin
public inline fun <K> FloatArray.groupBy(keySelector: (Float) -> K): Map<K, List<Float>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12331)

### 7. Common

```kotlin
public inline fun <K> DoubleArray.groupBy(keySelector: (Double) -> K): Map<K, List<Double>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12343)

### 8. Common

```kotlin
public inline fun <K> BooleanArray.groupBy(keySelector: (Boolean) -> K): Map<K, List<Boolean>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12355)

### 9. Common

```kotlin
public inline fun <K> CharArray.groupBy(keySelector: (Char) -> K): Map<K, List<Char>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12367)

### 10. Common

```kotlin
public inline fun <T, K, V> Array<out T>.groupBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12379)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 11. Common

```kotlin
public inline fun <K, V> ByteArray.groupBy(keySelector: (Byte) -> K, valueTransform: (Byte) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12392)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 12. Common

```kotlin
public inline fun <K, V> ShortArray.groupBy(keySelector: (Short) -> K, valueTransform: (Short) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12405)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 13. Common

```kotlin
public inline fun <K, V> IntArray.groupBy(keySelector: (Int) -> K, valueTransform: (Int) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12418)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 14. Common

```kotlin
public inline fun <K, V> LongArray.groupBy(keySelector: (Long) -> K, valueTransform: (Long) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12431)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 15. Common

```kotlin
public inline fun <K, V> FloatArray.groupBy(keySelector: (Float) -> K, valueTransform: (Float) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12444)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 16. Common

```kotlin
public inline fun <K, V> DoubleArray.groupBy(keySelector: (Double) -> K, valueTransform: (Double) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12457)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 17. Common

```kotlin
public inline fun <K, V> BooleanArray.groupBy(keySelector: (Boolean) -> K, valueTransform: (Boolean) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12470)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 18. Common

```kotlin
public inline fun <K, V> CharArray.groupBy(keySelector: (Char) -> K, valueTransform: (Char) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12483)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 19. Common

```kotlin
public inline fun <T, K> Iterable<T>.groupBy(keySelector: (T) -> K): Map<K, List<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1662)

Groups elements of the original collection by the key returned by the given `keySelector` function
applied to each element and returns a map where each group key is associated with a list of corresponding elements.

The returned map preserves the entry iteration order of the keys produced from the original collection.

@sample samples.collections.Collections.Transformations.groupBy

### 20. Common

```kotlin
public inline fun <T, K, V> Iterable<T>.groupBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1674)

Groups values returned by the `valueTransform` function applied to each element of the original collection
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original collection.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K> UIntArray.groupBy(keySelector: (UInt) -> K): Map<K, List<UInt>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5411)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K> ULongArray.groupBy(keySelector: (ULong) -> K): Map<K, List<ULong>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5426)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K> UByteArray.groupBy(keySelector: (UByte) -> K): Map<K, List<UByte>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5441)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K> UShortArray.groupBy(keySelector: (UShort) -> K): Map<K, List<UShort>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5456)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V> UIntArray.groupBy(keySelector: (UInt) -> K, valueTransform: (UInt) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5471)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V> ULongArray.groupBy(keySelector: (ULong) -> K, valueTransform: (ULong) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5487)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V> UByteArray.groupBy(keySelector: (UByte) -> K, valueTransform: (UByte) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5503)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V> UShortArray.groupBy(keySelector: (UShort) -> K, valueTransform: (UShort) -> V): Map<K, List<V>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5519)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and returns a map where each group key is associated with a list of corresponding values.

The returned map preserves the entry iteration order of the keys produced from the original array.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val words = listOf("a", "abc", "ab", "def", "abcd")
    val byLength = words.groupBy { it.length }

    println(byLength.keys)
    println(byLength.values)

    val mutableByLength: MutableMap<Int, MutableList<String>> = words.groupByTo(mutableMapOf()) { it.length }
    // same content as in byLength map, but the map is mutable
    println(mutableByLength == byLength)
}
```

```text title="Output"
[1, 3, 2, 4]
[[a], [abc, def], [ab], [abcd]]
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L826)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val nameToTeam = listOf("Alice" to "Marketing", "Bob" to "Sales", "Carol" to "Marketing")
    val namesByTeam = nameToTeam.groupBy({ it.second }, { it.first })
    println(namesByTeam)

    val mutableNamesByTeam = nameToTeam.groupByTo(HashMap(), { it.second }, { it.first })
    // same content as in namesByTeam map, but the map is mutable
    println(mutableNamesByTeam == namesByTeam)
}
```

```text title="Output"
{Marketing=[Alice, Carol], Sales=[Bob]}
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L839)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
