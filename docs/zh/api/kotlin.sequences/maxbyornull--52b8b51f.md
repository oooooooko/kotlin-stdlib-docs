# maxByOrNull

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回第一个产生给定 `selector` 函数最大值的元素,如果没有元素,则返回 `null` 函数的最大值。

如果 `selector` 函数返回了多个等值最大值,则此函数返回与这些值相应的第一个元素。

请注意当序列含有零或一个元素时,不会援引 `selector` 函数,因为在这种情况下,清楚可以不援引`selector`函数返回哪个元素。 因此建议避免依赖`selector`函数对每个元素的副作用。

操作为 _flintinal_。

@sample 样本、采集的样本、采集的采集量、采集的样本、 分类、 最小量By OrNull

??? note "查看英文原文"

    Returns the first element yielding the largest value of the given `selector` function or `null` if there are no elements.
    
    If there are multiple equal maximal values returned by the `selector` function,
    this function returns the first of elements corresponding to these values.
    
    Note that the function `selector` is not invoked when the sequence contains zero or one elements
    because in these cases it is clear which element to return without invoking the `selector`.
    Therefore it's recommended to avoid relying on side effects being performed by the `selector` function on each element.
    
    The operation is _terminal_.
    
    @sample samples.collections.Collections.Aggregates.minMaxByOrNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <T, R : Comparable<R>> Sequence<T>.maxByOrNull(selector: (T) -> R): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1770)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val strings = listOf("abcd", "abc", "ab", "de", "abcde")

    val longestString = strings.maxBy { it.length }
    println(longestString)

    val shortestString = strings.minBy { it.length }
    println(shortestString)

    val emptyList = emptyList<String>()
    // maxBy() and minBy() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.maxBy { it.length } }
    assertFailsWith<NoSuchElementException> { emptyList.minBy { it.length } }
    // maxByOrNull() and minByOrNull() return null if the collection is empty
    println(emptyList.maxByOrNull { it.length })
    println(emptyList.minByOrNull { it.length })
}
```

```text title="输出"
abcde
ab
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1218)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
