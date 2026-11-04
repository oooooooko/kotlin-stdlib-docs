# sortBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

根据以指定的 `selector` 函数返回的数值的自然排序顺序,对在位置上的数组中的元素进行排序。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本 采集的样本 采集的采集

??? note "查看英文原文"

    Sorts elements in the array in-place according to natural sort order of the value returned by specified `selector` function.
    
    The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
    relative to each other after sorting.
    
    @sample samples.collections.Collections.Sorting.sortBy

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, R : Comparable<R>> Array<out T>.sortBy(crossinline selector: (T) -> R?): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7389)

### 2. Common

```kotlin
public inline fun <T, R : Comparable<R>> MutableList<T>.sortBy(crossinline selector: (T) -> R?): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1171)

根据以指定的 `selector` 函数返回的数值的自然排序顺序,对列表中的元素进行排序。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

@sample 样本 采集的样本 采集的采集

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    class Dish(val name: String, val calories: Int, val tasteRate: Float) {
        override fun toString(): String = "Dish($name: $calories cal, taste $tasteRate/5)"
    }

    val fridgeContent = mutableListOf(
        Dish("🍨", 207, 4.7f),
        Dish("🥦", 34, 2.3f),
        Dish("🧃", 34, 4.9f)
    )

    // original order
    println(fridgeContent)

    // sort by taste rate (ascending)
    fridgeContent.sortBy { it.tasteRate }
    println(fridgeContent)

    val breadBoxContent = mutableListOf(
        Dish("🥯", 245, 4.8f),
        Dish("🥨", 100, 5.0f),
        Dish("🥐", 245, 4.9f)
    )

    // original order
    println(breadBoxContent)

    // sort by calories (ascending)
    breadBoxContent.sortBy { it.calories }
    // note that the sorting is stable, so the 🥯 is before the 🥐
    println(breadBoxContent)
}
```

```text title="输出"
[Dish(🍨: 207 cal, taste 4.7/5), Dish(🥦: 34 cal, taste 2.3/5), Dish(🧃: 34 cal, taste 4.9/5)]
[Dish(🥦: 34 cal, taste 2.3/5), Dish(🍨: 207 cal, taste 4.7/5), Dish(🧃: 34 cal, taste 4.9/5)]
[Dish(🥯: 245 cal, taste 4.8/5), Dish(🥨: 100 cal, taste 5.0/5), Dish(🥐: 245 cal, taste 4.9/5)]
[Dish(🥨: 100 cal, taste 5.0/5), Dish(🥯: 245 cal, taste 4.8/5), Dish(🥐: 245 cal, taste 4.9/5)]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1416)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
