# MutableCollection

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

通用的元素集,支持迭接、添加和删除元素,以及检查收藏中是否包含某些元素。复杂的操作以这一功能为基础,以 `kotlin.collections` 扩展功能的形式提供。

如果某一特定用途情况不需要修改收藏,则可以使用只读对应数据`Collection`。

`MutableCollection`延长了`Collection`的合同,其职能允许增加或删除元素。

`MutableCollection` 是包含多种同质元素的可变物体的最高界面。其他更具体的界面,如`MutableList`、 `MutableSet` 和`MutableMap`,扩展`MutableCollection`,以提供更具体的保证,保证元素的储存、存取和修改方式,并提供更丰富的功能。

与`Collection`不同,`iterator`返回的迭代器可以在迭代期间去除元素。

在另外说明之前,`MutableCollection`的履行并非完全安全,除非另有说明,否则`MutableCollection`的履行是无法安全地进行修改的,除非
明确同步可能导致数据腐败、丢失和运行时错误。

@param E 即收藏中所含元素的类型,变体收藏在其元素类型中是无变的。

??? note "查看英文原文"

    A generic collection of elements that supports iterating, adding and removing elements, as well as checking if the
    collection contains some elements. Complex operations are built upon this
    functionality and provided in form of `kotlin.collections` extension functions.
    
    If a particular use case does not require collection's modification,
    a read-only counterpart, `Collection` could be used instead.
    
    `MutableCollection` extends `Collection` contract with functions allowing to add or remove elements.
    
    `MutableCollection` is a top-level interface for mutable objects aggregating multiple different homogenous elements.
    Other more specific interfaces, like `MutableList`, `MutableSet`, and `MutableMap` extend `MutableCollection` to provide
    more specific guarantees on how elements are stored, accessed and modified, as well as provide richer functionality.
    
    Unlike `Collection`, an iterator returned by `iterator` allows removing elements during iteration.
    
    Until stated otherwise, `MutableCollection` implementations are not thread-safe and their modification without
    explicit synchronization may result in data corruption, loss, and runtime errors.
    
    @param E the type of elements contained in the collection. The mutable collection is invariant in its element type.

## 声明与重载

### 1. Common

```kotlin
public expect interface MutableCollection<E> : Collection<E>, MutableIterable<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L96)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.collections.*

fun main() {
    val value = mutableListOf(1, 2, 3)
    println(value)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
