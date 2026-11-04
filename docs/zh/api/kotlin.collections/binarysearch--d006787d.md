# binarySearch

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用二进制搜索算法搜索此列表或其所提供 `element` 的范围。 预计将根据该列表各元素的可比较自然顺序按升序排序, 否则结果将无法定义 。

如果列表中包含的多个元素等于指定的 `element` ,则无法保证能找到该元素。

`null` 值被认为低于任何非null值。

@return 该元素的索引,如果它包含在指定范围内的列表中;否则,倒置插入点 `(-insertion point - 1)`。插入点被定义为插入该元素的索引,以便该列表(或指定的列表子序列)仍然分类。 @sample 样本。 集合。 集合。 Lists. binarySearchOnComparable @sample 样本。 集合。 集合。 集合。 集合。 集合。 Lister. binarySearchOn

??? note "查看英文原文"

    Searches this list or its range for the provided `element` using the binary search algorithm.
    The list is expected to be sorted into ascending order according to the Comparable natural ordering of its elements,
    otherwise the result is undefined.
    
    If the list contains multiple elements equal to the specified `element`, there is no guarantee which one will be found.
    
    `null` value is considered to be less than any non-null value.
    
    @return the index of the element, if it is contained in the list within the specified range;
    otherwise, the inverted insertion point `(-insertion point - 1)`.
    The insertion point is defined as the index at which the element should be inserted,
    so that the list (or the specified subrange of list) still remains sorted.
    @sample samples.collections.Collections.Lists.binarySearchOnComparable
    @sample samples.collections.Collections.Lists.binarySearchWithBoundaries

## 声明与重载

### 1. Common

```kotlin
public fun <T : Comparable<T>> List<T?>.binarySearch(element: T?, fromIndex: Int = 0, toIndex: Int = size): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L315)

### 2. Common

```kotlin
public fun <T> List<T>.binarySearch(element: T, comparator: Comparator<in T>, fromIndex: Int = 0, toIndex: Int = size): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L352)

使用二进制搜索算法搜索此列表或它所提供 `element` 的域。 预计将按照指定的 `comparator` 进行递升排序, 否则结果未定义 。

如果列表中包含的多个元素等于指定的 `element` ,则无法保证能找到该元素。

`null` 值被认为低于任何非null值。

@return 该元素的索引,如果它包含在指定范围内的列表中;否则,倒置插入点 `(-insertion point - 1)` . 。插入点被定义为插入该元素的索引,以便该列表(或指定的列表子序列)仍然按照指定的 `comparator` . @sample. @sample 样本进行分类。 收集。 集合。 Lists. BinarySearchOn和Complator

### 3. Common

```kotlin
public fun <T> List<T>.binarySearch(fromIndex: Int = 0, toIndex: Int = size, comparison: (T) -> Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L417)

搜索此列表或其范围, 以查找给定的 `comparison` 函数使用二进制搜索算法返回零的元素 。

列表预计将进行排序, 以便 `comparison` 函数返回值的符号在列表元素上上升, 即负值在零之前, 零值在正值之前。 否则, 结果是未定义的 。

如果清单中包含 `comparison` 返回零的多个元素,则无法保证能找到一个元素。

@param 比较功能, 被搜索列表元素被调用时返回零。 对于目标元素之前出现的元素, 函数必须返回负值; 对于目标元素之后出现的元素, 函数必须返回正值 。

发现元素的索引 @return 如果在指定范围内的列表中包含该元素; 否则, 倒置插入点 `(-insertion point - 1)` 。 插入点被定义为插入该元素的索引, 以便该列表( 或指定的列表子范围) 仍然分类。 @sample 样本. 收藏。 集合 。 Lists. binarySearchOncomparsonFunction

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = mutableListOf('a', 'b', 'c', 'd', 'e')
    println(list.binarySearch('d'))

    list.remove('d')

    val invertedInsertionPoint = list.binarySearch('d')
    val actualInsertionPoint = -(invertedInsertionPoint + 1)
    println(actualInsertionPoint)

    list.add(actualInsertionPoint, 'd')
    println(list)
}
```

```text title="输出"
3
3
[a, b, c, d, e]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L274)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf('a', 'b', 'c', 'd', 'e')
    println(list.binarySearch('d'))

    // element is out of range from the left
    println(list.binarySearch('b', fromIndex = 2) < 0)

    // element is out of range from the right
    println(list.binarySearch('d', toIndex = 2) < 0)
}
```

```text title="输出"
3
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L289)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val colors = listOf("Blue", "green", "ORANGE", "Red", "yellow")
    println(colors.binarySearch("RED", String.CASE_INSENSITIVE_ORDER))
}
```

```text title="输出"
3
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L301)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Box(val value: String)

    val values = listOf("A", "ant", "binding", "Box", "cell")
    val boxes = values.map { Box(it) }

    val valueToFind = "box"
    // `boxes` list is sorted according to the following comparison function
    val index = boxes.binarySearch { String.CASE_INSENSITIVE_ORDER.compare(it.value, valueToFind) }

    if (index >= 0) {
        println("Value at $index is ${boxes[index]}")
    } else {
        println("Box with value=$valueToFind was not found")
    }
}
```

```text title="输出"
Value at 3 is Box(value=Box)
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L316)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
