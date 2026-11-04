# List.listIterator

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回列表元素的列表迭代器( 以正确的顺序) 。

如果需要从特定指数开始对列表进行迭代,则可以使用接受 `Int` 参数的`listIterator`超载,而不是使用此函数,并手工迭代,直到达到所需的指数。

@sample 样本,收集,收集,列表列表

??? note "查看英文原文"

    Returns a list iterator over the elements in this list (in proper sequence).
    
    If the list needs to be iterated starting from a specific index,
    a `listIterator` overload accepting the `Int` parameter could be used instead
    of using this function and manually iterating until the required index is reached.
    
    @sample samples.collections.Collections.Lists.listIterator

## 声明与重载

### 1. Common

```kotlin
public fun listIterator(): ListIterator<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L261)

### 2. Common

```kotlin
public fun listIterator(index: Int): ListIterator<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L272)

返回从指定的 `index` 开始的列表复制器, 返回此列表元素的列表复制器( 正确的序列) 。

@throws 指数外溢值,但`index`小于或大于本清单所列`size`的除外。
@sample 样本. 采集. 集聚. list. list 列表与 Index 的 Iterator

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf('a', 'b')
    val iterator = list.listIterator()

    // "Cursor" is at the beginning of the list,
    // so there is no previous element, only a next one
    println(iterator.hasPrevious())
    println(iterator.hasNext())

    // Let's scan the list in a forward direction
    println(iterator.next())
    println(iterator.next())

    // Cursor is past the end of the list,
    // so there is no next element, only a previous one
    println(iterator.hasPrevious())
    println(iterator.hasNext())

    // Let's scan the list backwards, starting from the end
    println(iterator.previous())
    println(iterator.previous())

    // We ran out of elements
    assertFailsWith<NoSuchElementException> { iterator.previous() }

    // Empty list has an empty iterator
    val emptyListIterator = emptyList<String>().listIterator()
    println(emptyListIterator.hasNext())
    println(emptyListIterator.hasPrevious())
}
```

```text title="输出"
false
true
a
b
true
false
b
a
false
false
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L461)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf('a', 'b', 'c')

    // The iterator will scan elements starting from 'c' (the element at the index = 2)
    val sublistIterator = list.listIterator(index = 2)
    // However, previous elements are also accessible
    println(sublistIterator.hasPrevious())
    // One step forward
    println(sublistIterator.next())
    // Two steps backward
    println(sublistIterator.previous())
    println(sublistIterator.previous())

    // If the index is equal to the length of the list,
    // the iterator's "cursor" will point past the last element and only previous elements
    // will be accessible
    val pastLastIterator = list.listIterator(index = 3)
    println(pastLastIterator.hasPrevious())
    println(pastLastIterator.hasNext())
    println(pastLastIterator.previous())
    println(pastLastIterator.previous())

    // It's an error to use indices outside of list bounds
    assertFailsWith<IndexOutOfBoundsException> { list.listIterator(-1) }
    assertFailsWith<IndexOutOfBoundsException> { list.listIterator(list.size + 1) }
}
```

```text title="输出"
true
c
c
b
true
false
c
b
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L493)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
