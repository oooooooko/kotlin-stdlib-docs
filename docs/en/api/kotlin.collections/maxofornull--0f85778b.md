# maxOfOrNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If any of values produced by `selector` function is `NaN`, the returned result is `NaN`.

@sample samples.collections.Collections.Aggregates.maxOfMinOfFloatingResult

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.maxOfOrNull(selector: (T) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17745)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ByteArray.maxOfOrNull(selector: (Byte) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17767)

### 3. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ShortArray.maxOfOrNull(selector: (Short) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17789)

### 4. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun IntArray.maxOfOrNull(selector: (Int) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17811)

### 5. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun LongArray.maxOfOrNull(selector: (Long) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17833)

### 6. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun FloatArray.maxOfOrNull(selector: (Float) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17855)

### 7. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun DoubleArray.maxOfOrNull(selector: (Double) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17877)

### 8. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun BooleanArray.maxOfOrNull(selector: (Boolean) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17899)

### 9. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun CharArray.maxOfOrNull(selector: (Char) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17921)

### 10. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.maxOfOrNull(selector: (T) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17943)

### 11. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ByteArray.maxOfOrNull(selector: (Byte) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17965)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ShortArray.maxOfOrNull(selector: (Short) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17987)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun IntArray.maxOfOrNull(selector: (Int) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18009)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun LongArray.maxOfOrNull(selector: (Long) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18031)

### 15. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun FloatArray.maxOfOrNull(selector: (Float) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18053)

### 16. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun DoubleArray.maxOfOrNull(selector: (Double) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18075)

### 17. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun BooleanArray.maxOfOrNull(selector: (Boolean) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18097)

### 18. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun CharArray.maxOfOrNull(selector: (Char) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18119)

### 19. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R : Comparable<R>> Array<out T>.maxOfOrNull(selector: (T) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18141)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfGeneric

### 20. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ByteArray.maxOfOrNull(selector: (Byte) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18165)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 21. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ShortArray.maxOfOrNull(selector: (Short) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18189)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 22. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> IntArray.maxOfOrNull(selector: (Int) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18213)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 23. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> LongArray.maxOfOrNull(selector: (Long) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18237)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 24. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> FloatArray.maxOfOrNull(selector: (Float) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18261)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 25. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> DoubleArray.maxOfOrNull(selector: (Double) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18285)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 26. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> BooleanArray.maxOfOrNull(selector: (Boolean) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18309)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 27. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> CharArray.maxOfOrNull(selector: (Char) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18333)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 28. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Iterable<T>.maxOfOrNull(selector: (T) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2422)

Returns the largest value among all values produced by `selector` function
applied to each element in the collection or `null` if the collection is empty.

If any of values produced by `selector` function is `NaN`, the returned result is `NaN`.

@sample samples.collections.Collections.Aggregates.maxOfMinOfFloatingResult

### 29. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Iterable<T>.maxOfOrNull(selector: (T) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2445)

Returns the largest value among all values produced by `selector` function
applied to each element in the collection or `null` if the collection is empty.

If any of values produced by `selector` function is `NaN`, the returned result is `NaN`.

@sample samples.collections.Collections.Aggregates.maxOfMinOfFloatingResult

### 30. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R : Comparable<R>> Iterable<T>.maxOfOrNull(selector: (T) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2468)

Returns the largest value among all values produced by `selector` function
applied to each element in the collection or `null` if the collection is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfGeneric

### 31. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.maxOfOrNull(selector: (Map.Entry<K, V>) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L318)

Returns the largest value among all values produced by `selector` function
applied to each entry in the map or `null` if the map is empty.

If any of values produced by `selector` function is `NaN`, the returned result is `NaN`.

@sample samples.collections.Collections.Aggregates.maxOfMinOfFloatingResult

### 32. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.maxOfOrNull(selector: (Map.Entry<K, V>) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L334)

Returns the largest value among all values produced by `selector` function
applied to each entry in the map or `null` if the map is empty.

If any of values produced by `selector` function is `NaN`, the returned result is `NaN`.

@sample samples.collections.Collections.Aggregates.maxOfMinOfFloatingResult

### 33. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V, R : Comparable<R>> Map<out K, V>.maxOfOrNull(selector: (Map.Entry<K, V>) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L350)

Returns the largest value among all values produced by `selector` function
applied to each entry in the map or `null` if the map is empty.

If multiple entries produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfGeneric

### 34. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.maxOfOrNull(selector: (UInt) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7687)

### 35. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.maxOfOrNull(selector: (ULong) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7710)

### 36. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.maxOfOrNull(selector: (UByte) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7733)

### 37. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.maxOfOrNull(selector: (UShort) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7756)

### 38. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.maxOfOrNull(selector: (UInt) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7779)

### 39. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.maxOfOrNull(selector: (ULong) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7802)

### 40. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.maxOfOrNull(selector: (UByte) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7825)

### 41. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.maxOfOrNull(selector: (UShort) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7848)

### 42. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UIntArray.maxOfOrNull(selector: (UInt) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7871)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 43. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ULongArray.maxOfOrNull(selector: (ULong) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7896)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 44. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UByteArray.maxOfOrNull(selector: (UByte) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7921)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

### 45. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UShortArray.maxOfOrNull(selector: (UShort) -> R): R?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7946)

Returns the largest value among all values produced by `selector` function
applied to each element in the array or `null` if the array is empty.

If multiple elements produce the maximal value, this function returns the first of those values.

@sample samples.collections.Collections.Aggregates.maxOfMinOfPrimitive

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    data class Rectangle(val width: Double, val height: Double) {
        val aspectRatio: Double get() = if (height != 0.0) width / height else Double.NaN
    }

    // The largest and smallest width-to-height ratios
    val rectangles = listOf(
        Rectangle(15.0, 10.0),
        Rectangle(25.0, 20.0),
        Rectangle(40.0, 30.0),
    )
    println(rectangles.maxOf { it.aspectRatio })
    println(rectangles.minOf { it.aspectRatio })

    // Aspect ratio of a point (0.0 by 0.0) is NaN, hence the result is NaN
    val rectanglesAndPoint = rectangles + Rectangle(0.0, 0.0)
    println(rectanglesAndPoint.maxOf { it.aspectRatio })
    println(rectanglesAndPoint.minOf { it.aspectRatio })

    val emptyList = emptyList<Rectangle>()

    // maxOf() and minOf() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.maxOf { it.aspectRatio } }
    assertFailsWith<NoSuchElementException> { emptyList.minOf { it.aspectRatio } }

    // maxOfOrNull() and minOfOrNull() return null if the collection is empty
    println(emptyList.maxOfOrNull { it.aspectRatio })
    println(emptyList.minOfOrNull { it.aspectRatio })
}
```

```text title="Output"
1.5
1.25
NaN
NaN
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1138)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    // The length of the longest and shortest names
    val names = listOf("Alice", "Bob", "Carol")
    println(names.maxOf { it.length })
    println(names.minOf { it.length })

    val emptyList = emptyList<String>()

    // maxOf() and minOf() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.maxOf { it.length } }
    assertFailsWith<NoSuchElementException> { emptyList.minOf { it.length } }

    // maxOfOrNull() and minOfOrNull() return null if the collection is empty
    println(emptyList.maxOfOrNull { it.length })
    println(emptyList.minOfOrNull { it.length })
}
```

```text title="Output"
5
3
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1120)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    // The largest and smallest last digits in the array
    val numbers = intArrayOf(13, 7, 22, 64)
    println(numbers.maxOf { it % 10 })
    println(numbers.minOf { it % 10 })

    val emptyArray = intArrayOf()

    // maxOf() and minOf() throw if the array is empty
    assertFailsWith<NoSuchElementException> { emptyArray.maxOf { it % 10 } }
    assertFailsWith<NoSuchElementException> { emptyArray.minOf { it % 10 } }

    // maxOfOrNull() and minOfOrNull() return null if the array is empty
    println(emptyArray.maxOfOrNull { it % 10 })
    println(emptyArray.minOfOrNull { it % 10 })
}
```

```text title="Output"
7
2
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1102)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
