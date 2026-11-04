# zip

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list of pairs built from the elements of `this` array and the `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

## Declarations and overloads

### 1. Common

```kotlin
public infix fun <T, R> Array<out T>.zip(other: Array<out R>): List<Pair<T, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26453)

### 2. Common

```kotlin
public infix fun <R> ByteArray.zip(other: Array<out R>): List<Pair<Byte, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26463)

### 3. Common

```kotlin
public infix fun <R> ShortArray.zip(other: Array<out R>): List<Pair<Short, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26473)

### 4. Common

```kotlin
public infix fun <R> IntArray.zip(other: Array<out R>): List<Pair<Int, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26483)

### 5. Common

```kotlin
public infix fun <R> LongArray.zip(other: Array<out R>): List<Pair<Long, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26493)

### 6. Common

```kotlin
public infix fun <R> FloatArray.zip(other: Array<out R>): List<Pair<Float, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26503)

### 7. Common

```kotlin
public infix fun <R> DoubleArray.zip(other: Array<out R>): List<Pair<Double, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26513)

### 8. Common

```kotlin
public infix fun <R> BooleanArray.zip(other: Array<out R>): List<Pair<Boolean, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26523)

### 9. Common

```kotlin
public infix fun <R> CharArray.zip(other: Array<out R>): List<Pair<Char, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26533)

### 10. Common

```kotlin
public inline fun <T, R, V> Array<out T>.zip(other: Array<out R>, transform: (a: T, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26543)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 11. Common

```kotlin
public inline fun <R, V> ByteArray.zip(other: Array<out R>, transform: (a: Byte, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26559)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 12. Common

```kotlin
public inline fun <R, V> ShortArray.zip(other: Array<out R>, transform: (a: Short, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26575)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 13. Common

```kotlin
public inline fun <R, V> IntArray.zip(other: Array<out R>, transform: (a: Int, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26591)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 14. Common

```kotlin
public inline fun <R, V> LongArray.zip(other: Array<out R>, transform: (a: Long, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26607)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 15. Common

```kotlin
public inline fun <R, V> FloatArray.zip(other: Array<out R>, transform: (a: Float, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26623)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 16. Common

```kotlin
public inline fun <R, V> DoubleArray.zip(other: Array<out R>, transform: (a: Double, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26639)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 17. Common

```kotlin
public inline fun <R, V> BooleanArray.zip(other: Array<out R>, transform: (a: Boolean, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26655)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 18. Common

```kotlin
public inline fun <R, V> CharArray.zip(other: Array<out R>, transform: (a: Char, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26671)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 19. Common

```kotlin
public infix fun <T, R> Array<out T>.zip(other: Iterable<R>): List<Pair<T, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26687)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 20. Common

```kotlin
public infix fun <R> ByteArray.zip(other: Iterable<R>): List<Pair<Byte, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26697)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 21. Common

```kotlin
public infix fun <R> ShortArray.zip(other: Iterable<R>): List<Pair<Short, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26707)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 22. Common

```kotlin
public infix fun <R> IntArray.zip(other: Iterable<R>): List<Pair<Int, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26717)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 23. Common

```kotlin
public infix fun <R> LongArray.zip(other: Iterable<R>): List<Pair<Long, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26727)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 24. Common

```kotlin
public infix fun <R> FloatArray.zip(other: Iterable<R>): List<Pair<Float, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26737)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 25. Common

```kotlin
public infix fun <R> DoubleArray.zip(other: Iterable<R>): List<Pair<Double, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26747)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 26. Common

```kotlin
public infix fun <R> BooleanArray.zip(other: Iterable<R>): List<Pair<Boolean, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26757)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 27. Common

```kotlin
public infix fun <R> CharArray.zip(other: Iterable<R>): List<Pair<Char, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26767)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 28. Common

```kotlin
public inline fun <T, R, V> Array<out T>.zip(other: Iterable<R>, transform: (a: T, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26777)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 29. Common

```kotlin
public inline fun <R, V> ByteArray.zip(other: Iterable<R>, transform: (a: Byte, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26795)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 30. Common

```kotlin
public inline fun <R, V> ShortArray.zip(other: Iterable<R>, transform: (a: Short, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26813)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 31. Common

```kotlin
public inline fun <R, V> IntArray.zip(other: Iterable<R>, transform: (a: Int, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26831)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 32. Common

```kotlin
public inline fun <R, V> LongArray.zip(other: Iterable<R>, transform: (a: Long, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26849)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 33. Common

```kotlin
public inline fun <R, V> FloatArray.zip(other: Iterable<R>, transform: (a: Float, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26867)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 34. Common

```kotlin
public inline fun <R, V> DoubleArray.zip(other: Iterable<R>, transform: (a: Double, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26885)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 35. Common

```kotlin
public inline fun <R, V> BooleanArray.zip(other: Iterable<R>, transform: (a: Boolean, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26903)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 36. Common

```kotlin
public inline fun <R, V> CharArray.zip(other: Iterable<R>, transform: (a: Char, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26921)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 37. Common

```kotlin
public infix fun ByteArray.zip(other: ByteArray): List<Pair<Byte, Byte>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26939)

### 38. Common

```kotlin
public infix fun ShortArray.zip(other: ShortArray): List<Pair<Short, Short>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26949)

### 39. Common

```kotlin
public infix fun IntArray.zip(other: IntArray): List<Pair<Int, Int>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26959)

### 40. Common

```kotlin
public infix fun LongArray.zip(other: LongArray): List<Pair<Long, Long>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26969)

### 41. Common

```kotlin
public infix fun FloatArray.zip(other: FloatArray): List<Pair<Float, Float>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26979)

### 42. Common

```kotlin
public infix fun DoubleArray.zip(other: DoubleArray): List<Pair<Double, Double>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26989)

### 43. Common

```kotlin
public infix fun BooleanArray.zip(other: BooleanArray): List<Pair<Boolean, Boolean>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26999)

### 44. Common

```kotlin
public infix fun CharArray.zip(other: CharArray): List<Pair<Char, Char>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27009)

### 45. Common

```kotlin
public inline fun <V> ByteArray.zip(other: ByteArray, transform: (a: Byte, b: Byte) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27019)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 46. Common

```kotlin
public inline fun <V> ShortArray.zip(other: ShortArray, transform: (a: Short, b: Short) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27035)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 47. Common

```kotlin
public inline fun <V> IntArray.zip(other: IntArray, transform: (a: Int, b: Int) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27051)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 48. Common

```kotlin
public inline fun <V> LongArray.zip(other: LongArray, transform: (a: Long, b: Long) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27067)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 49. Common

```kotlin
public inline fun <V> FloatArray.zip(other: FloatArray, transform: (a: Float, b: Float) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27083)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 50. Common

```kotlin
public inline fun <V> DoubleArray.zip(other: DoubleArray, transform: (a: Double, b: Double) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27099)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 51. Common

```kotlin
public inline fun <V> BooleanArray.zip(other: BooleanArray, transform: (a: Boolean, b: Boolean) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27115)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 52. Common

```kotlin
public inline fun <V> CharArray.zip(other: CharArray, transform: (a: Char, b: Char) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27131)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 53. Common

```kotlin
public infix fun <T, R> Iterable<T>.zip(other: Array<out R>): List<Pair<T, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3828)

Returns a list of pairs built from the elements of `this` collection and the `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 54. Common

```kotlin
public inline fun <T, R, V> Iterable<T>.zip(other: Array<out R>, transform: (a: T, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3838)

Returns a list of values built from the elements of `this` collection and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 55. Common

```kotlin
public infix fun <T, R> Iterable<T>.zip(other: Iterable<R>): List<Pair<T, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3856)

Returns a list of pairs built from the elements of `this` collection and `other` collection with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 56. Common

```kotlin
public inline fun <T, R, V> Iterable<T>.zip(other: Iterable<R>, transform: (a: T, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3866)

Returns a list of values built from the elements of `this` collection and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 57. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UIntArray.zip(other: Array<out R>): List<Pair<UInt, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11755)

### 58. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> ULongArray.zip(other: Array<out R>): List<Pair<ULong, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11767)

### 59. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UByteArray.zip(other: Array<out R>): List<Pair<UByte, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11779)

### 60. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UShortArray.zip(other: Array<out R>): List<Pair<UShort, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11791)

### 61. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UIntArray.zip(other: Array<out R>, transform: (a: UInt, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11803)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 62. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> ULongArray.zip(other: Array<out R>, transform: (a: ULong, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11822)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 63. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UByteArray.zip(other: Array<out R>, transform: (a: UByte, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11841)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 64. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UShortArray.zip(other: Array<out R>, transform: (a: UShort, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11860)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 65. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UIntArray.zip(other: Iterable<R>): List<Pair<UInt, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11879)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 66. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> ULongArray.zip(other: Iterable<R>): List<Pair<ULong, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11891)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 67. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UByteArray.zip(other: Iterable<R>): List<Pair<UByte, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11903)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 68. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UShortArray.zip(other: Iterable<R>): List<Pair<UShort, R>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11915)

Returns a list of pairs built from the elements of `this` collection and `other` array with the same index.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterable

### 69. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UIntArray.zip(other: Iterable<R>, transform: (a: UInt, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11927)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 70. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> ULongArray.zip(other: Iterable<R>, transform: (a: ULong, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11948)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 71. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UByteArray.zip(other: Iterable<R>, transform: (a: UByte, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11969)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 72. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UShortArray.zip(other: Iterable<R>, transform: (a: UShort, b: R) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11990)

Returns a list of values built from the elements of `this` array and the `other` collection with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest collection.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 73. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun UIntArray.zip(other: UIntArray): List<Pair<UInt, UInt>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12011)

### 74. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun ULongArray.zip(other: ULongArray): List<Pair<ULong, ULong>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12023)

### 75. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun UByteArray.zip(other: UByteArray): List<Pair<UByte, UByte>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12035)

### 76. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun UShortArray.zip(other: UShortArray): List<Pair<UShort, UShort>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12047)

### 77. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V> UIntArray.zip(other: UIntArray, transform: (a: UInt, b: UInt) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12059)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 78. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V> ULongArray.zip(other: ULongArray, transform: (a: ULong, b: ULong) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12078)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 79. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V> UByteArray.zip(other: UByteArray, transform: (a: UByte, b: UByte) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12097)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

### 80. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V> UShortArray.zip(other: UShortArray, transform: (a: UShort, b: UShort) -> V): List<V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12116)

Returns a list of values built from the elements of `this` array and the `other` array with the same index
using the provided `transform` function applied to each pair of elements.
The returned list has length of the shortest array.

@sample samples.collections.Iterables.Operations.zipIterableWithTransform

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val listA = listOf("a", "b", "c")
    val listB = listOf(1, 2, 3, 4)
    println(listA zip listB)
}
```

```text title="Output"
[(a, 1), (b, 2), (c, 3)]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L60)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val listA = listOf("a", "b", "c")
    val listB = listOf(1, 2, 3, 4)
    val result = listA.zip(listB) { a, b -> "$a$b" }
    println(result)
}
```

```text title="Output"
[a1, b2, c3]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L67)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
