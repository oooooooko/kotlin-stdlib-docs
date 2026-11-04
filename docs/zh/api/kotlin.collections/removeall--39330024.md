# removeAll

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

删除指定收藏中包含的所有收藏元素 。

能够克服 `removeAll` 型安全限制,要求通过`Collection<E>`型的收集。

如果从收藏中移走任何特定元素,@return `true` ;如果收藏没有修改,`false`。

??? note "查看英文原文"

    Removes all of this collection's elements that are also contained in the specified collection.
    
    Allows to overcome type-safety restriction of `removeAll` that requires to pass a collection of type `Collection<E>`.
    
    @return `true` if any of the specified elements was removed from the collection, `false` if the collection was not modified.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <@kotlin.internal.OnlyInputTypes T> MutableCollection<out T>.removeAll(elements: Collection<T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L24)

### 2. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.removeAll(elements: Iterable<T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L155)

删除此 `MutableCollection` 中包含于给定 `elements` 收藏中的所有元素。

### 3. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.removeAll(elements: Sequence<T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L163)

删除 `MutableCollection` 中包含于给定 `elements` 序列中的所有元素。

### 4. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.removeAll(elements: Array<out T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L172)

删除给定的 `elements` 矩阵中包含的 `MutableCollection` 数组中的所有元素。

### 5. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableIterable<T>.removeAll(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L219)

从此 `MutableIterable` 中删除所有元素, 与给定 `predicate` 匹配 。

如果从该收藏中移除任何元素,@return `true` ,则`false`,如果未移除元素,而且收集工作没有修改,则 `false` 。

### 6. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableList<T>.removeAll(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L284)

从此 `MutableList` 中删除所有元素, 与给定 `predicate` 匹配 。

如果从该收藏中移除任何元素,@return `true` ,则`false`,如果未移除元素,而且收集工作没有修改,则 `false` 。

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
    val source = mutableListOf(1, 2, 3)
    val result = source.`removeAll`(listOf(1, 2, 3))
    println(result)
}
```

```text title="输出"
true
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
