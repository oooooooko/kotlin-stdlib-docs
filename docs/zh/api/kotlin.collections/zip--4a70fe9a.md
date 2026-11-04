# zip

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回从 `this` 矩阵和具有相同索引的 `other` 矩阵元素中构建的对数列表。 返回列表的长度为最短的集合长度 。

@sample 样本 采集 可行 操作 齐

??? note "查看英文原文"

    Returns a list of pairs built from the elements of `this` array and the `other` array with the same index.
    The returned list has length of the shortest collection.
    
    @sample samples.collections.Iterables.Operations.zipIterable

## 声明与重载

### 1. Common

```kotlin
public infix fun <T, R> Array<out T>.zip(other: Array<out R>): List<Pair<T, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26453)

### 2. Common

```kotlin
public infix fun <R> ByteArray.zip(other: Array<out R>): List<Pair<Byte, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26463)

### 3. Common

```kotlin
public infix fun <R> ShortArray.zip(other: Array<out R>): List<Pair<Short, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26473)

### 4. Common

```kotlin
public infix fun <R> IntArray.zip(other: Array<out R>): List<Pair<Int, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26483)

### 5. Common

```kotlin
public infix fun <R> LongArray.zip(other: Array<out R>): List<Pair<Long, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26493)

### 6. Common

```kotlin
public infix fun <R> FloatArray.zip(other: Array<out R>): List<Pair<Float, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26503)

### 7. Common

```kotlin
public infix fun <R> DoubleArray.zip(other: Array<out R>): List<Pair<Double, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26513)

### 8. Common

```kotlin
public infix fun <R> BooleanArray.zip(other: Array<out R>): List<Pair<Boolean, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26523)

### 9. Common

```kotlin
public infix fun <R> CharArray.zip(other: Array<out R>): List<Pair<Char, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26533)

### 10. Common

```kotlin
public inline fun <T, R, V> Array<out T>.zip(other: Array<out R>, transform: (a: T, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26543)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 11. Common

```kotlin
public inline fun <R, V> ByteArray.zip(other: Array<out R>, transform: (a: Byte, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26559)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 12. Common

```kotlin
public inline fun <R, V> ShortArray.zip(other: Array<out R>, transform: (a: Short, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26575)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 13. Common

```kotlin
public inline fun <R, V> IntArray.zip(other: Array<out R>, transform: (a: Int, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26591)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 14. Common

```kotlin
public inline fun <R, V> LongArray.zip(other: Array<out R>, transform: (a: Long, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26607)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 15. Common

```kotlin
public inline fun <R, V> FloatArray.zip(other: Array<out R>, transform: (a: Float, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26623)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 16. Common

```kotlin
public inline fun <R, V> DoubleArray.zip(other: Array<out R>, transform: (a: Double, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26639)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 17. Common

```kotlin
public inline fun <R, V> BooleanArray.zip(other: Array<out R>, transform: (a: Boolean, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26655)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 18. Common

```kotlin
public inline fun <R, V> CharArray.zip(other: Array<out R>, transform: (a: Char, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26671)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 19. Common

```kotlin
public infix fun <T, R> Array<out T>.zip(other: Iterable<R>): List<Pair<T, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26687)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 20. Common

```kotlin
public infix fun <R> ByteArray.zip(other: Iterable<R>): List<Pair<Byte, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26697)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 21. Common

```kotlin
public infix fun <R> ShortArray.zip(other: Iterable<R>): List<Pair<Short, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26707)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 22. Common

```kotlin
public infix fun <R> IntArray.zip(other: Iterable<R>): List<Pair<Int, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26717)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 23. Common

```kotlin
public infix fun <R> LongArray.zip(other: Iterable<R>): List<Pair<Long, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26727)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 24. Common

```kotlin
public infix fun <R> FloatArray.zip(other: Iterable<R>): List<Pair<Float, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26737)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 25. Common

```kotlin
public infix fun <R> DoubleArray.zip(other: Iterable<R>): List<Pair<Double, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26747)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 26. Common

```kotlin
public infix fun <R> BooleanArray.zip(other: Iterable<R>): List<Pair<Boolean, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26757)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 27. Common

```kotlin
public infix fun <R> CharArray.zip(other: Iterable<R>): List<Pair<Char, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26767)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 28. Common

```kotlin
public inline fun <T, R, V> Array<out T>.zip(other: Iterable<R>, transform: (a: T, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26777)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 29. Common

```kotlin
public inline fun <R, V> ByteArray.zip(other: Iterable<R>, transform: (a: Byte, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26795)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 30. Common

```kotlin
public inline fun <R, V> ShortArray.zip(other: Iterable<R>, transform: (a: Short, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26813)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 31. Common

```kotlin
public inline fun <R, V> IntArray.zip(other: Iterable<R>, transform: (a: Int, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26831)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 32. Common

```kotlin
public inline fun <R, V> LongArray.zip(other: Iterable<R>, transform: (a: Long, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26849)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 33. Common

```kotlin
public inline fun <R, V> FloatArray.zip(other: Iterable<R>, transform: (a: Float, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26867)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 34. Common

```kotlin
public inline fun <R, V> DoubleArray.zip(other: Iterable<R>, transform: (a: Double, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26885)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 35. Common

```kotlin
public inline fun <R, V> BooleanArray.zip(other: Iterable<R>, transform: (a: Boolean, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26903)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 36. Common

```kotlin
public inline fun <R, V> CharArray.zip(other: Iterable<R>, transform: (a: Char, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26921)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 37. Common

```kotlin
public infix fun ByteArray.zip(other: ByteArray): List<Pair<Byte, Byte>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26939)

### 38. Common

```kotlin
public infix fun ShortArray.zip(other: ShortArray): List<Pair<Short, Short>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26949)

### 39. Common

```kotlin
public infix fun IntArray.zip(other: IntArray): List<Pair<Int, Int>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26959)

### 40. Common

```kotlin
public infix fun LongArray.zip(other: LongArray): List<Pair<Long, Long>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26969)

### 41. Common

```kotlin
public infix fun FloatArray.zip(other: FloatArray): List<Pair<Float, Float>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26979)

### 42. Common

```kotlin
public infix fun DoubleArray.zip(other: DoubleArray): List<Pair<Double, Double>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26989)

### 43. Common

```kotlin
public infix fun BooleanArray.zip(other: BooleanArray): List<Pair<Boolean, Boolean>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26999)

### 44. Common

```kotlin
public infix fun CharArray.zip(other: CharArray): List<Pair<Char, Char>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27009)

### 45. Common

```kotlin
public inline fun <V> ByteArray.zip(other: ByteArray, transform: (a: Byte, b: Byte) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27019)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 46. Common

```kotlin
public inline fun <V> ShortArray.zip(other: ShortArray, transform: (a: Short, b: Short) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27035)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 47. Common

```kotlin
public inline fun <V> IntArray.zip(other: IntArray, transform: (a: Int, b: Int) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27051)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 48. Common

```kotlin
public inline fun <V> LongArray.zip(other: LongArray, transform: (a: Long, b: Long) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27067)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 49. Common

```kotlin
public inline fun <V> FloatArray.zip(other: FloatArray, transform: (a: Float, b: Float) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27083)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 50. Common

```kotlin
public inline fun <V> DoubleArray.zip(other: DoubleArray, transform: (a: Double, b: Double) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27099)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 51. Common

```kotlin
public inline fun <V> BooleanArray.zip(other: BooleanArray, transform: (a: Boolean, b: Boolean) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27115)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 52. Common

```kotlin
public inline fun <V> CharArray.zip(other: CharArray, transform: (a: Char, b: Char) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27131)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 53. Common

```kotlin
public infix fun <T, R> Iterable<T>.zip(other: Array<out R>): List<Pair<T, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3828)

返回从 `this` 收藏元素和 `other` 矩阵中构建的对数列表, 并具有相同的索引。 返回列表的长度为最短的收藏长度 。

@sample 样本 采集 可行 操作 齐

### 54. Common

```kotlin
public inline fun <T, R, V> Iterable<T>.zip(other: Array<out R>, transform: (a: T, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3838)

返回从 `this` 收藏和`other`矩阵元素中构建的数值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的收藏长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 55. Common

```kotlin
public infix fun <T, R> Iterable<T>.zip(other: Iterable<R>): List<Pair<T, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3856)

返回从`this` 收藏和 `other` 收藏中构建的配对列表, 并使用相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 56. Common

```kotlin
public inline fun <T, R, V> Iterable<T>.zip(other: Iterable<R>, transform: (a: T, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3866)

返回从 `this` 收藏和`other`收藏中构建的数值列表, 使用对每对元素适用的`transform`功能, 以相同的索引, 返回每对元素。 返回列表的长度为最短收藏的长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 57. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UIntArray.zip(other: Array<out R>): List<Pair<UInt, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11755)

### 58. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> ULongArray.zip(other: Array<out R>): List<Pair<ULong, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11767)

### 59. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UByteArray.zip(other: Array<out R>): List<Pair<UByte, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11779)

### 60. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UShortArray.zip(other: Array<out R>): List<Pair<UShort, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11791)

### 61. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UIntArray.zip(other: Array<out R>, transform: (a: UInt, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11803)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 62. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> ULongArray.zip(other: Array<out R>, transform: (a: ULong, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11822)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 63. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UByteArray.zip(other: Array<out R>, transform: (a: UByte, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11841)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 64. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UShortArray.zip(other: Array<out R>, transform: (a: UShort, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11860)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素提供的`transform`函数,具有相同的指数。返回列表的长度为最短的集合长度 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 65. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UIntArray.zip(other: Iterable<R>): List<Pair<UInt, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11879)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 66. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> ULongArray.zip(other: Iterable<R>): List<Pair<ULong, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11891)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 67. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UByteArray.zip(other: Iterable<R>): List<Pair<UByte, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11903)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 68. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun <R> UShortArray.zip(other: Iterable<R>): List<Pair<UShort, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11915)

返回从 `this` 收藏和 `other` 矩阵元素中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的收藏 。

@sample 样本 采集 可行 操作 齐

### 69. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UIntArray.zip(other: Iterable<R>, transform: (a: UInt, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11927)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 70. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> ULongArray.zip(other: Iterable<R>, transform: (a: ULong, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11948)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 71. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UByteArray.zip(other: Iterable<R>, transform: (a: UByte, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11969)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 72. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, V> UShortArray.zip(other: Iterable<R>, transform: (a: UShort, b: R) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11990)

返回从 `this` 矩阵和`other` 收藏元素中构建的数值列表, 使用对每对元素适用的`transform`函数, 使用相同的索引, 返回每对元素。 返回列表的长度为最短的收藏 。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 73. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun UIntArray.zip(other: UIntArray): List<Pair<UInt, UInt>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12011)

### 74. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun ULongArray.zip(other: ULongArray): List<Pair<ULong, ULong>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12023)

### 75. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun UByteArray.zip(other: UByteArray): List<Pair<UByte, UByte>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12035)

### 76. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public infix fun UShortArray.zip(other: UShortArray): List<Pair<UShort, UShort>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12047)

### 77. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V> UIntArray.zip(other: UIntArray, transform: (a: UInt, b: UInt) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12059)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 78. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V> ULongArray.zip(other: ULongArray, transform: (a: ULong, b: ULong) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12078)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 79. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V> UByteArray.zip(other: UByteArray, transform: (a: UByte, b: UByte) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12097)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

### 80. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V> UShortArray.zip(other: UShortArray, transform: (a: UShort, b: UShort) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L12116)

返回从 `this` 矩阵和`other` 矩阵元素中构建的值列表,这些元素使用对每对元素应用的`transform`函数,具有相同的指数。返回列表的长度为最短的矩阵。

@sample 样本、采集的样本、可使用性、操作、可转换的可转换操作

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val listA = listOf("a", "b", "c")
    val listB = listOf(1, 2, 3, 4)
    println(listA zip listB)
}
```

```text title="输出"
[(a, 1), (b, 2), (c, 3)]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L60)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val listA = listOf("a", "b", "c")
    val listB = listOf(1, 2, 3, 4)
    val result = listA.zip(listB) { a, b -> "$a$b" }
    println(result)
}
```

```text title="输出"
[a1, b2, c3]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L67)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
