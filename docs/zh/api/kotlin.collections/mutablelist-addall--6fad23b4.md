# MutableList.addAll

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定收藏的全部元素添加到此列表的末尾 。

这些元素附在`elements`收藏品的顺序上。

如果由于行动的结果名单有变动,则 @return `true` 。

@sample 样本 采集的样本 收集的 列表 添加

??? note "查看英文原文"

    Adds all of the elements of the specified collection to the end of this list.
    
    The elements are appended in the order they appear in the `elements` collection.
    
    @return `true` if the list was changed as the result of the operation.
    
    @sample samples.collections.Collections.Lists.addAll

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    override fun addAll(elements: Collection<E>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L329)

### 2. Common

```kotlin
@IgnorableReturnValue
    public fun addAll(index: Int, elements: Collection<E>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L341)

将指定的收藏 `elements` 的全部元素插入到指定 `index` 的列表中。

元素按在`elements`收藏中出现的顺序插入。

最初储存的所有要素,按`index .. index + size - 1`指数,将`elements.size`位置移到最后。

如果`index`等于 `size` ,`elements`将附于清单中。

如果由于行动的结果名单有变动,则 @return `true` 。

@throws 指数外溢值,如果该清单中`index`低于零或大于 `size` ,则除外。

@sample 样本,采集的样本, 收集的样本, 列表, 添加

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')
    println(list.addAll(listOf('a', 'b', 'c')))
    println(list)
}
```

```text title="输出"
true
[a, b, c, a, b, c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L354)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')

    list.addAll(1, listOf('x', 'y', 'z'))
    println(list)

    list.addAll(6, listOf('h', 'i'))
    println(list)

    assertFailsWith<IndexOutOfBoundsException> { list.addAll(100500, listOf('z')) }
}
```

```text title="输出"
[a, x, y, z, b, c]
[a, x, y, z, b, c, h, i]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L361)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
