# MutableList

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

通用定序要素集,支持添加、替换和删除元素,以及迭接包含元素,用索引检索,并检查某个收藏是否含有特定值。

如果某一特定用途情况不需要修改清单,则可以使用只读对应数据`List`,代之以只读对应数据`List`。

`MutableList` 延长`List`合同,其职能允许增加、替换和删除元素。

与`List`不同的是,`iterator`和`listIterator`返回的迭代器允许在迭代期间修改清单,`subList`返回的视图也允许修改基本清单。

在另外说明之前,`MutableList`的履行并非完全安全,除非另有说明,否则`MutableList`的履行是无法安全地进行修改的,除非
明确同步可能导致数据腐败、丢失和运行时错误。

@param E 清单中包含的元素类型,变式列表在元素类型中是无变的。

??? note "查看英文原文"

    A generic ordered collection of elements that supports adding, replacing and removing elements, as well as
    iterating over contained elements, accessing them by an index and checking if a collection contains a particular value.
    
    If a particular use case does not require list's modification,
    a read-only counterpart, `List` could be used instead.
    
    `MutableList` extends `List` contract with functions allowing to add, replace and remove elements.
    
    Unlike `List`, iterators returned by `iterator` and `listIterator` allow modifying the list during iteration.
    A view returned by `subList` also allows modifications of the underlying list.
    
    Until stated otherwise, `MutableList` implementations are not thread-safe and their modification without
    explicit synchronization may result in data corruption, loss, and runtime errors.
    
    @param E the type of elements contained in the list. The mutable list is invariant in its element type.

## 声明与重载

### 1. Common

```kotlin
public expect interface MutableList<E> : List<E>, MutableCollection<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L296)

### 2. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public inline fun <T> MutableList(size: Int, init: (index: Int) -> T): MutableList<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L155)

创建带有指定的 `size` 的新的变体列表, 以调用指定的 `init` 函数计算每个元素 。

函数 `init` 由第一个列表元素开始,顺序对每个列表元素要求值。 它应该返回列表元素的值, 并给定其索引 。

@sample 样本、采集的样本、采集的采集物、列表、可变清单、从初始化器中提取的样本

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = MutableList(3) { index -> 'A' + index }
    println(list)

    list.clear()
    println(list)
}
```

```text title="输出"
[A, B, C]
[]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L233)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
