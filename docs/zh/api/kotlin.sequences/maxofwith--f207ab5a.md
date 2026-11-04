# maxOfWith

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回在`selector`函数产生的所有数值中,根据`comparator`所提供的`comparator`,在序列中每个元素应用的最大值。

如果多个元素产生最大值,此函数返回这些值的第一个值。

@throws 否 元素例外,如果序列为空。

操作为 _flintinal_。

@sample 样本、采集的样本、采集的样本、采集的样本、分类、与基因的混合样本、与基因的混合样本、

??? note "查看英文原文"

    Returns the largest value according to the provided `comparator`
    among all values produced by `selector` function applied to each element in the sequence.
    
    If multiple elements produce the maximal value, this function returns the first of those values.
    
    @throws NoSuchElementException if the sequence is empty.
    
    The operation is _terminal_.
    
    @sample samples.collections.Collections.Aggregates.maxOfWithMinOfWithGeneric

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.internal.InlineOnly
public inline fun <T, R> Sequence<T>.maxOfWith(comparator: Comparator<in R>, selector: (T) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1962)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    data class Book(val title: String, val publishYear: Int, val rating: Double)

    // A custom Comparator that orders strings by their length
    val lengthComparator = compareBy<String> { it.length }

    // The longest and shortest book titles
    val books = listOf(
        Book("Red Sand", 2004, 3.5),
        Book("Silver Bullet", 2009, 4.4),
        Book("Clear Water", 2018, 4.1),
        Book("Night Sky", 2023, 3.8)
    )
    println(books.maxOfWith(lengthComparator) { it.title })
    println(books.minOfWith(lengthComparator) { it.title })

    val emptyList = listOf<Book>()

    // maxOfWith() and minOfWith() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.maxOfWith(lengthComparator) { it.title } }
    assertFailsWith<NoSuchElementException> { emptyList.minOfWith(lengthComparator) { it.title } }

    // maxOfWithOrNull() and minOfWithOrNull() return null if the collection is empty
    println(emptyList.maxOfWithOrNull(lengthComparator) { it.title })
    println(emptyList.minOfWithOrNull(lengthComparator) { it.title })
}
```

```text title="输出"
Silver Bullet
Red Sand
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1190)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
