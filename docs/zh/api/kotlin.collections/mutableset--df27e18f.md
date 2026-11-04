# MutableSet

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

通用的、无顺序的、支持增删和删除元素的独特元素集,在它们上面循环,检查某个收藏是否含有特定值。

如果某一特定用途案件不需要对一套方法进行修改,则可以使用只读对应方法`Set`。

`MutableSet`延长了`Set`的合同,其职能允许增删元素。

与`Set`不同,`iterator`返回的迭代器允许在迭代期间修改套装。

在另外说明之前,`MutableSet`的履行并非完全安全,除非另有说明,否则`MutableSet`的履行是无法安全地进行修改的,除非
明确同步可能导致数据腐败、丢失和运行时错误。

@param E 即集所含元素的类型。变音集在元素类型中是无变的。

??? note "查看英文原文"

    A generic unordered collection of unique elements that supports adding and removing elements, iterating over them
    and checking if a collection contains a particular value.
    
    If a particular use case does not require set's modification,
    a read-only counterpart, `Set` could be used instead.
    
    `MutableSet` extends `Set` contract with functions allowing to add and remove elements.
    
    Unlike `Set`, an iterator returned by `iterator` allows modifying the set during iteration.
    
    Until stated otherwise, `MutableSet` implementations are not thread-safe and their modification without
    explicit synchronization may result in data corruption, loss, and runtime errors.
    
    @param E the type of elements contained in the set. The mutable set is invariant in its element type.

## 声明与重载

### 1. Common

```kotlin
public expect interface MutableSet<E> : Set<E>, MutableCollection<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L471)

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
    val value = linkedSetOf(1, 2, 3)
    println(value)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
