# groupByTo

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Groups elements of the original array by the key returned by the given `keySelector` function
applied to each element and puts to the `destination` map each group key associated with a list of corresponding elements.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupBy

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, M : MutableMap<in K, MutableList<T>>> Array<out T>.groupByTo(destination: M, keySelector: (T) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12496)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Byte>>> ByteArray.groupByTo(destination: M, keySelector: (Byte) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12514)

### 3. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Short>>> ShortArray.groupByTo(destination: M, keySelector: (Short) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12532)

### 4. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Int>>> IntArray.groupByTo(destination: M, keySelector: (Int) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12550)

### 5. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Long>>> LongArray.groupByTo(destination: M, keySelector: (Long) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12568)

### 6. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Float>>> FloatArray.groupByTo(destination: M, keySelector: (Float) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12586)

### 7. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Double>>> DoubleArray.groupByTo(destination: M, keySelector: (Double) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12604)

### 8. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Boolean>>> BooleanArray.groupByTo(destination: M, keySelector: (Boolean) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12622)

### 9. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Char>>> CharArray.groupByTo(destination: M, keySelector: (Char) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12640)

### 10. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, MutableList<V>>> Array<out T>.groupByTo(destination: M, keySelector: (T) -> K, valueTransform: (T) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12658)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 11. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> ByteArray.groupByTo(destination: M, keySelector: (Byte) -> K, valueTransform: (Byte) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12677)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 12. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> ShortArray.groupByTo(destination: M, keySelector: (Short) -> K, valueTransform: (Short) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12696)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 13. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> IntArray.groupByTo(destination: M, keySelector: (Int) -> K, valueTransform: (Int) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12715)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 14. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> LongArray.groupByTo(destination: M, keySelector: (Long) -> K, valueTransform: (Long) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12734)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 15. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> FloatArray.groupByTo(destination: M, keySelector: (Float) -> K, valueTransform: (Float) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12753)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 16. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> DoubleArray.groupByTo(destination: M, keySelector: (Double) -> K, valueTransform: (Double) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12772)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 17. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> BooleanArray.groupByTo(destination: M, keySelector: (Boolean) -> K, valueTransform: (Boolean) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12791)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 18. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> CharArray.groupByTo(destination: M, keySelector: (Char) -> K, valueTransform: (Char) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12810)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 19. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, M : MutableMap<in K, MutableList<T>>> Iterable<T>.groupByTo(destination: M, keySelector: (T) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1687)

Groups elements of the original collection by the key returned by the given `keySelector` function
applied to each element and puts to the `destination` map each group key associated with a list of corresponding elements.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupBy

### 20. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, MutableList<V>>> Iterable<T>.groupByTo(destination: M, keySelector: (T) -> K, valueTransform: (T) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1705)

Groups values returned by the `valueTransform` function applied to each element of the original collection
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 21. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, M : MutableMap<in K, MutableList<UInt>>> UIntArray.groupByTo(destination: M, keySelector: (UInt) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5535)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, M : MutableMap<in K, MutableList<ULong>>> ULongArray.groupByTo(destination: M, keySelector: (ULong) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5556)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, M : MutableMap<in K, MutableList<UByte>>> UByteArray.groupByTo(destination: M, keySelector: (UByte) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5577)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, M : MutableMap<in K, MutableList<UShort>>> UShortArray.groupByTo(destination: M, keySelector: (UShort) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5598)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> UIntArray.groupByTo(destination: M, keySelector: (UInt) -> K, valueTransform: (UInt) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5619)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 26. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> ULongArray.groupByTo(destination: M, keySelector: (ULong) -> K, valueTransform: (ULong) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5641)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 27. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> UByteArray.groupByTo(destination: M, keySelector: (UByte) -> K, valueTransform: (UByte) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5663)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

@sample samples.collections.Collections.Transformations.groupByKeysAndValues

### 28. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> UShortArray.groupByTo(destination: M, keySelector: (UShort) -> K, valueTransform: (UShort) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5685)

Groups values returned by the `valueTransform` function applied to each element of the original array
by the key returned by the given `keySelector` function applied to the element
and puts to the `destination` map each group key associated with a list of corresponding values.

@return The `destination` map.

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
