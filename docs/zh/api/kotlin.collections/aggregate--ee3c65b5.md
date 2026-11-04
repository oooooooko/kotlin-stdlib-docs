# aggregate

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

`Grouping` 源的元素按键分组,并按顺序对每个组的元素应用 `operation`, 将先前的累计值和当前元素作为参数, 并将结果存储在新地图中 。

每个要素的钥匙由`Grouping.keyOf`函数提供。

@param 操作功能在每一元素上援引,参数如下: - `key`: 该元素所属组的键; - `accumulator`: 该组的累积器当前值为 `null`,如果它是该组中遇到的第一个8,000005; - `element`: 源的元素正在汇总; - `first`: 显示它是该组中遇到的第一个8,00000008。

@return a `Map` 将每一组的关键与组元素汇总的结果联系起来。 @sample 样本。 采集。 分组. 聚合ByRadix

??? note "查看英文原文"

    Groups elements from the `Grouping` source by key and applies `operation` to the elements of each group sequentially,
    passing the previously accumulated value and the current element as arguments, and stores the results in a new map.
    
    The key for each element is provided by the `Grouping.keyOf` function.
    
    @param operation function is invoked on each element with the following parameters:
     - `key`: the key of the group this element belongs to;
     - `accumulator`: the current value of the accumulator of the group, can be `null` if it's the first `element` encountered in the group;
     - `element`: the element from the source being aggregated;
     - `first`: indicates whether it's the first `element` encountered in the group.
    
    @return a `Map` associating the key of each group with the result of aggregation of the group elements.
    @sample samples.collections.Grouping.aggregateByRadix

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public inline fun <T, K, R> Grouping<T, K>.aggregate(
    operation: (key: K, accumulator: R?, element: T, first: Boolean) -> R
): Map<K, R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L34)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val numbers = listOf(3, 4, 5, 6, 7, 8, 9)

    val aggregated = numbers.groupingBy { it % 3 }.aggregate { key, accumulator: StringBuilder?, element, first ->
        if (first) // first element
            StringBuilder().append(key).append(":").append(element)
        else
            accumulator!!.append("-").append(element)
    }

    println(aggregated.values)
}
```

```text title="输出"
[0:3-6-9, 1:4-7, 2:5-8]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/grouping.kt#L25)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
