# minOfOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

??? note "查看英文原文"

    Returns the smallest value among all values produced by `selector` function
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
public inline fun <T> Array<out T>.minOfOrNull(selector: (T) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20717)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ByteArray.minOfOrNull(selector: (Byte) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20739)

### 3. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ShortArray.minOfOrNull(selector: (Short) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20761)

### 4. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun IntArray.minOfOrNull(selector: (Int) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20783)

### 5. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun LongArray.minOfOrNull(selector: (Long) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20805)

### 6. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun FloatArray.minOfOrNull(selector: (Float) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20827)

### 7. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun DoubleArray.minOfOrNull(selector: (Double) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20849)

### 8. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun BooleanArray.minOfOrNull(selector: (Boolean) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20871)

### 9. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun CharArray.minOfOrNull(selector: (Char) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20893)

### 10. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.minOfOrNull(selector: (T) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20915)

### 11. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ByteArray.minOfOrNull(selector: (Byte) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20937)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun ShortArray.minOfOrNull(selector: (Short) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20959)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun IntArray.minOfOrNull(selector: (Int) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20981)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun LongArray.minOfOrNull(selector: (Long) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21003)

### 15. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun FloatArray.minOfOrNull(selector: (Float) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21025)

### 16. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun DoubleArray.minOfOrNull(selector: (Double) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21047)

### 17. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun BooleanArray.minOfOrNull(selector: (Boolean) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21069)

### 18. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun CharArray.minOfOrNull(selector: (Char) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21091)

### 19. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R : Comparable<R>> Array<out T>.minOfOrNull(selector: (T) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21113)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、

### 20. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ByteArray.minOfOrNull(selector: (Byte) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21137)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 21. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ShortArray.minOfOrNull(selector: (Short) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21161)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 22. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> IntArray.minOfOrNull(selector: (Int) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21185)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 23. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> LongArray.minOfOrNull(selector: (Long) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21209)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 24. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> FloatArray.minOfOrNull(selector: (Float) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21233)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 25. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> DoubleArray.minOfOrNull(selector: (Double) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21257)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 26. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> BooleanArray.minOfOrNull(selector: (Boolean) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21281)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 27. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> CharArray.minOfOrNull(selector: (Char) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21305)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 28. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Iterable<T>.minOfOrNull(selector: (T) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2846)

返回在收藏中每个元素应用的 `selector` 函数产生的所有值中最小值,如果收藏为空,则返回 `null` 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

### 29. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T> Iterable<T>.minOfOrNull(selector: (T) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2869)

返回在收藏中每个元素应用的 `selector` 函数产生的所有值中最小值,如果收藏为空,则返回 `null` 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

### 30. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R : Comparable<R>> Iterable<T>.minOfOrNull(selector: (T) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2892)

返回在收藏中每个元素应用的 `selector` 函数产生的所有值中最小值,如果收藏为空,则返回 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、

### 31. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.minOfOrNull(selector: (Map.Entry<K, V>) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L516)

返回在由 `selector` 函数生成的所有数值中最小值, 以适用于地图中每个条目的`null` 函数计算, 如果地图为空, 则以 `null` 返回 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

### 32. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.minOfOrNull(selector: (Map.Entry<K, V>) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L532)

返回在由 `selector` 函数生成的所有数值中最小值, 以适用于地图中每个条目的`null` 函数计算, 如果地图为空, 则以 `null` 返回 。

如果 `selector` 函数产生的任何值为`NaN`,则返回结果为`NaN`。

@sample 样本、采集的样本、采集的样本、采集的样本、汇总的样本、最小值的样本、 移动结果的样本

### 33. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <K, V, R : Comparable<R>> Map<out K, V>.minOfOrNull(selector: (Map.Entry<K, V>) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L548)

返回在由 `selector` 函数生成的所有数值中最小值, 以适用于地图中每个条目的`null` 函数计算, 如果地图为空, 则以 `null` 返回 。

如果多个条目产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、 样本、

### 34. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.minOfOrNull(selector: (UInt) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9047)

### 35. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.minOfOrNull(selector: (ULong) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9070)

### 36. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.minOfOrNull(selector: (UByte) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9093)

### 37. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.minOfOrNull(selector: (UShort) -> Double): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9116)

### 38. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.minOfOrNull(selector: (UInt) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9139)

### 39. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.minOfOrNull(selector: (ULong) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9162)

### 40. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.minOfOrNull(selector: (UByte) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9185)

### 41. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.minOfOrNull(selector: (UShort) -> Float): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9208)

### 42. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UIntArray.minOfOrNull(selector: (UInt) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9231)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 43. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ULongArray.minOfOrNull(selector: (ULong) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9256)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 44. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UByteArray.minOfOrNull(selector: (UByte) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9281)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、最低程度

### 45. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UShortArray.minOfOrNull(selector: (UShort) -> R): R?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9306)

返回在 `selector` 函数产生的所有值中最小值,如果数组为空,则返回对数组中每个元素应用的最小值,或 `null` 。

如果多个元素产生最小值,此函数返回这些值中的第一个值。

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
