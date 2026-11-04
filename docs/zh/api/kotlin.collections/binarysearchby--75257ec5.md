# binarySearchBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

搜索此列表或其范围, 以显示一个元素, 其键由指定的 `selector` 函数返回后, 其值等于 提供的 `key` 值, 使用二进制搜索算法。 列表预计将按照元素键的可比较自然顺序按升序排序。 否则结果将未定义 。

如果清单中包含有 `key` 的多个元素,则无法保证能找到该元素。

`null` 值被认为低于任何非null值。

@return 元素的索引与指定的 `key` , 如果它包含在指定的范围内, 则包含在指定的范围内的列表中; 否则, 倒置插入点 `(-insertion point - 1)`。 插入点被定义为插入元素的索引, 这样列表( 或指定的子列表) 仍然保留分类。 @sample 样本。 收藏。 集合 。 Lists. Binary SearchByKey

??? note "查看英文原文"

    Searches this list or its range for an element having the key returned by the specified `selector` function
    equal to the provided `key` value using the binary search algorithm.
    The list is expected to be sorted into ascending order according to the Comparable natural ordering of keys of its elements.
    otherwise the result is undefined.
    
    If the list contains multiple elements with the specified `key`, there is no guarantee which one will be found.
    
    `null` value is considered to be less than any non-null value.
    
    @return the index of the element with the specified `key`, if it is contained in the list within the specified range;
    otherwise, the inverted insertion point `(-insertion point - 1)`.
    The insertion point is defined as the index at which the element should be inserted,
    so that the list (or the specified subrange of list) still remains sorted.
    @sample samples.collections.Collections.Lists.binarySearchByKey

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, K : Comparable<K>> List<T>.binarySearchBy(
    key: K?,
    fromIndex: Int = 0,
    toIndex: Int = size,
    crossinline selector: (T) -> K?
): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L388)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Box(val value: Int)

    val numbers = listOf(1, 3, 7, 10, 12)
    val boxes = numbers.map { Box(it) }
    println(boxes.binarySearchBy(10) { it.value })
}
```

```text title="输出"
3
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L307)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
