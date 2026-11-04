# foldTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

`Grouping` 源的元素按键分组,并按顺序对每个组的元素应用 `operation`, 传递先前的累计值和当前元素作为参数, 并将结果存储在给定的 `destination` 地图中。 累积的初始值由 `initialValueSelector` 函数提供 。

@param 初始Value 选择函数, 函数为每个组提供初始累积值。 参数为: - `key`: 组的键; - `element`: 该组遇到的第一个元素。

如果 `destination` 地图已经有一个与某些密钥对应的值,则该值用作该组的累积器的初始值,而该组则不要求使用 `initialValueSelector` 函数。

@param 运行一个函数,每个元素都引用以下参数: - `key`:该元素所属组的键; - `accumulator`:该组的积累器当前值; - `element`:源的元素正在积累。

@return 将每个组的关键与组元素积累结果联系起来的 `destination` 地图。 @sample 样本。 收集。 分组。 由 EvenLengthwithCompacted IntialValueTo 组合

??? note "查看英文原文"

    Groups elements from the `Grouping` source by key and applies `operation` to the elements of each group sequentially,
    passing the previously accumulated value and the current element as arguments,
    and stores the results in the given `destination` map.
    An initial value of accumulator is provided by `initialValueSelector` function.
    
    @param initialValueSelector a function that provides an initial value of accumulator for each group.
     It's invoked with parameters:
     - `key`: the key of the group;
     - `element`: the first element being encountered in that group.
    
    If the `destination` map already has a value corresponding to some key, that value is used as an initial value of
    the accumulator for that group and the `initialValueSelector` function is not called for that group.
    
    @param operation a function that is invoked on each element with the following parameters:
     - `key`: the key of the group this element belongs to;
     - `accumulator`: the current value of the accumulator of the group;
     - `element`: the element from the source being accumulated.
    
    @return the `destination` map associating the key of each group with the result of accumulating the group elements.
    @sample samples.collections.Grouping.foldByEvenLengthWithComputedInitialValueTo

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public inline fun <T, K, R, M : MutableMap<in K, R>> Grouping<T, K>.foldTo(
    destination: M,
    initialValueSelector: (key: K, element: T) -> R,
    operation: (key: K, accumulator: R, element: T) -> R
): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L114)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public inline fun <T, K, R, M : MutableMap<in K, R>> Grouping<T, K>.foldTo(
    destination: M,
    initialValue: R,
    operation: (accumulator: R, element: T) -> R
): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L166)

`Grouping` 源的元素按键分组,并按顺序对每个组的元素应用 `operation`, 将先前的累计值和当前元素作为参数传递, 并将结果存储在给定的 `destination` 地图中。 初始累积值为每组的 `initialValue` 。

如果`destination`地图已经有一个与某些组的键相对应的值,则该值用作该组的累积器的初始值。

@param 运行一个函数,每个元素都引用以下参数: - `accumulator` :该组组的积累者的现值; - `element`:源的累积要素。

@return 将每个组的关键与组元素积累结果联系起来的 `destination` 地图。 @sample 样本。 收集。 分组。 由 EvenLength with ConstantIntialValueTo 组合

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val fruits = listOf("cherry", "blueberry", "citrus", "apple", "apricot", "banana", "coconut")

    val evenFruits = fruits.groupingBy { it.first() }
        .foldTo(mutableMapOf(), { key, _: String -> key to mutableListOf<String>() },
                { _, accumulator, element ->
                    if (element.length % 2 == 0) accumulator.second.add(element)
                    accumulator
                })

    val sorted = evenFruits.values.sortedBy { it.first }
    println(sorted)

    evenFruits.clear() // evenFruits is a mutable map
}
```

```text title="输出"
[(a, []), (b, [banana]), (c, [cherry, citrus])]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/grouping.kt#L70)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val fruits = listOf("apple", "apricot", "banana", "blueberry", "cherry", "coconut")

    // collect only even length Strings
    val evenFruits = fruits.groupingBy { it.first() }
        .foldTo(mutableMapOf(), emptyList<String>()) { acc, e -> if (e.length % 2 == 0) acc + e else acc }

    println(evenFruits)

    evenFruits.clear() // evenFruits is a mutable map
}
```

```text title="输出"
{a=[], b=[banana], c=[cherry]}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/grouping.kt#L98)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
