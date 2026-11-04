# sortedBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回根据指定 `selector` 函数返回的值的自然排序顺序排序的所有元素列表 。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本、采集的样本、采集的采集物、分类的样本

??? note "查看英文原文"

    Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.
    
    The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
    relative to each other after sorting.
    
    @sample samples.collections.Collections.Sorting.sortedBy

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, R : Comparable<R>> Array<out T>.sortedBy(crossinline selector: (T) -> R?): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7742)

### 2. Common

```kotlin
public inline fun <R : Comparable<R>> ByteArray.sortedBy(crossinline selector: (Byte) -> R?): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7754)

返回根据指定 `selector` 函数返回的值的自然排序顺序排序的所有元素列表 。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本、采集的样本、采集的采集图

### 3. Common

```kotlin
public inline fun <R : Comparable<R>> ShortArray.sortedBy(crossinline selector: (Short) -> R?): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7766)

返回根据指定 `selector` 函数返回的值的自然排序顺序排序的所有元素列表 。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本、采集的样本、采集的采集图

### 4. Common

```kotlin
public inline fun <R : Comparable<R>> IntArray.sortedBy(crossinline selector: (Int) -> R?): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7778)

返回根据指定 `selector` 函数返回的值的自然排序顺序排序的所有元素列表 。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本、采集的样本、采集的采集图

### 5. Common

```kotlin
public inline fun <R : Comparable<R>> LongArray.sortedBy(crossinline selector: (Long) -> R?): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7790)

返回根据指定 `selector` 函数返回的值的自然排序顺序排序的所有元素列表 。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本、采集的样本、采集的采集图

### 6. Common

```kotlin
public inline fun <R : Comparable<R>> FloatArray.sortedBy(crossinline selector: (Float) -> R?): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7802)

返回根据指定 `selector` 函数返回的值的自然排序顺序排序的所有元素列表 。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本、采集的样本、采集的采集图

### 7. Common

```kotlin
public inline fun <R : Comparable<R>> DoubleArray.sortedBy(crossinline selector: (Double) -> R?): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7814)

返回根据指定 `selector` 函数返回的值的自然排序顺序排序的所有元素列表 。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本、采集的样本、采集的采集图

### 8. Common

```kotlin
public inline fun <R : Comparable<R>> BooleanArray.sortedBy(crossinline selector: (Boolean) -> R?): List<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7826)

返回根据指定 `selector` 函数返回的值的自然排序顺序排序的所有元素列表 。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本、采集的样本、采集的采集图

### 9. Common

```kotlin
public inline fun <R : Comparable<R>> CharArray.sortedBy(crossinline selector: (Char) -> R?): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7838)

返回根据指定 `selector` 函数返回的值的自然排序顺序排序的所有元素列表 。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本、采集的样本、采集的采集图

### 10. Common

```kotlin
public inline fun <T, R : Comparable<R>> Iterable<T>.sortedBy(crossinline selector: (T) -> R?): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1218)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    class Dish(val name: String, val calories: Int, val tasteRate: Float) {
        override fun toString(): String = "Dish($name: $calories cal, taste $tasteRate/5)"
    }

    val fridgeContent = listOf(Dish("🍨", 207, 4.7f), Dish("🥦", 34, 2.3f), Dish("🧃", 34, 4.9f))

    val dullDishes = fridgeContent.sortedBy { it.tasteRate }
    println(dullDishes)

    val lightDishes = fridgeContent.sortedBy { it.calories }
    // note that the sorting is stable, so the 🥦 is before the 🧃
    println(lightDishes)

    // the original collection remains unchanged
    println(fridgeContent)
}
```

```text title="输出"
[Dish(🥦: 34 cal, taste 2.3/5), Dish(🍨: 207 cal, taste 4.7/5), Dish(🧃: 34 cal, taste 4.9/5)]
[Dish(🥦: 34 cal, taste 2.3/5), Dish(🧃: 34 cal, taste 4.9/5), Dish(🍨: 207 cal, taste 4.7/5)]
[Dish(🍨: 207 cal, taste 4.7/5), Dish(🥦: 34 cal, taste 2.3/5), Dish(🧃: 34 cal, taste 4.9/5)]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1484)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val unsorted = intArrayOf(3, 1, 2, 4)

    val sortedByRemainder = unsorted.sortedBy { it % 3 }
    // the sorting is stable: the order of 1 (1 % 3 == 1) and 4 (4 % 3 == 1) was preserved
    println(sortedByRemainder)

    val mapping = mapOf(1 to "one", 2 to "two", 3 to "three", 4 to "four")
    val sortedByPronunciation = unsorted.sortedBy {
        // take a key to sort by from the mapping
        mapping.getOrDefault(it, "unknown")
    }
    // four < one < three < two, lexicographically
    println(sortedByPronunciation)

    // the original array remains unchanged
    println(unsorted.toList())
}
```

```text title="输出"
[3, 1, 4, 2]
[4, 1, 3, 2]
[3, 1, 2, 4]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1503)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
