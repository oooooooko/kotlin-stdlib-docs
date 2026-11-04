# maxOfOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

??? note "查看英文原文"

    Returns the largest value among all values produced by `selector` function
    applied to each element in the array or `null` if the array is empty.
    
    If any of values produced by `selector` function is `NaN`, the returned result is `NaN`.
    
    @sample samples.collections.Collections.Aggregates.maxOfMinOfFloatingResult

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.maxOfOrNull(selector: (T) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17745)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ByteArray.maxOfOrNull(selector: (Byte) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17767)

### 3. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ShortArray.maxOfOrNull(selector: (Short) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17789)

### 4. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun IntArray.maxOfOrNull(selector: (Int) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17811)

### 5. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun LongArray.maxOfOrNull(selector: (Long) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17833)

### 6. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun FloatArray.maxOfOrNull(selector: (Float) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17855)

### 7. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun DoubleArray.maxOfOrNull(selector: (Double) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17877)

### 8. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun BooleanArray.maxOfOrNull(selector: (Boolean) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17899)

### 9. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun CharArray.maxOfOrNull(selector: (Char) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17921)

### 10. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.maxOfOrNull(selector: (T) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17943)

### 11. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ByteArray.maxOfOrNull(selector: (Byte) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17965)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ShortArray.maxOfOrNull(selector: (Short) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L17987)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun IntArray.maxOfOrNull(selector: (Int) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18009)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun LongArray.maxOfOrNull(selector: (Long) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18031)

### 15. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun FloatArray.maxOfOrNull(selector: (Float) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18053)

### 16. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun DoubleArray.maxOfOrNull(selector: (Double) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18075)

### 17. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun BooleanArray.maxOfOrNull(selector: (Boolean) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18097)

### 18. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun CharArray.maxOfOrNull(selector: (Char) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18119)

### 19. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R : Comparable<R>> Array<out T>.maxOfOrNull(selector: (T) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18141)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、

### 20. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ByteArray.maxOfOrNull(selector: (Byte) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18165)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 21. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ShortArray.maxOfOrNull(selector: (Short) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18189)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 22. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> IntArray.maxOfOrNull(selector: (Int) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18213)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 23. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> LongArray.maxOfOrNull(selector: (Long) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18237)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 24. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> FloatArray.maxOfOrNull(selector: (Float) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18261)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 25. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> DoubleArray.maxOfOrNull(selector: (Double) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18285)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 26. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> BooleanArray.maxOfOrNull(selector: (Boolean) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18309)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 27. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> CharArray.maxOfOrNull(selector: (Char) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18333)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 28. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Iterable<T>.maxOfOrNull(selector: (T) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2422)

返回收藏中每个元素应用的 `selector` 函数产生的所有值中的最大值,如果收藏为空,则返回 `null` 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

### 29. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Iterable<T>.maxOfOrNull(selector: (T) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2445)

返回收藏中每个元素应用的 `selector` 函数产生的所有值中的最大值,如果收藏为空,则返回 `null` 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

### 30. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R : Comparable<R>> Iterable<T>.maxOfOrNull(selector: (T) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2468)

返回收藏中每个元素应用的 `selector` 函数产生的所有值中的最大值,如果收藏为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、

### 31. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.maxOfOrNull(selector: (Map.Entry<K, V>) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L318)

返回在由 `selector` 函数生成的所有数值中的最大值, 返回在地图中每个条目中应用的数值, 如果地图为空, 则返回 `null` 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

### 32. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.maxOfOrNull(selector: (Map.Entry<K, V>) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L334)

返回在由 `selector` 函数生成的所有数值中的最大值, 返回在地图中每个条目中应用的数值, 如果地图为空, 则返回 `null` 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

### 33. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V, R : Comparable<R>> Map<out K, V>.maxOfOrNull(selector: (Map.Entry<K, V>) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L350)

返回在由 `selector` 函数生成的所有数值中的最大值, 返回在地图中每个条目中应用的数值, 如果地图为空, 则返回 `null` 。

如果多个条目产生最大值,此函数返回这些值的第一个。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、

### 34. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.maxOfOrNull(selector: (UInt) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7687)

### 35. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.maxOfOrNull(selector: (ULong) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7710)

### 36. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.maxOfOrNull(selector: (UByte) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7733)

### 37. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.maxOfOrNull(selector: (UShort) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7756)

### 38. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.maxOfOrNull(selector: (UInt) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7779)

### 39. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.maxOfOrNull(selector: (ULong) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7802)

### 40. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.maxOfOrNull(selector: (UByte) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7825)

### 41. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.maxOfOrNull(selector: (UShort) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7848)

### 42. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UIntArray.maxOfOrNull(selector: (UInt) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7871)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 43. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ULongArray.maxOfOrNull(selector: (ULong) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7896)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 44. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UByteArray.maxOfOrNull(selector: (UByte) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7921)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 45. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UShortArray.maxOfOrNull(selector: (UShort) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L7946)

返回 `selector` 函数产生的所有值中最大值的返回,如果数组为空,则返回 `null` 。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

```text title="输出"
1.5
1.25
NaN
NaN
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1138)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
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

```text title="输出"
5
3
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1120)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
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

```text title="输出"
7
2
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1102)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
