# retainAll

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

只保留指定收藏中包含的收藏元素。

能够克服 `retainAll` 型安全限制,要求通过`Collection<E>`型的收集。

如果从收藏中移除任何元素,@return `true` ;如果收藏没有修改,`false`。

??? note "查看英文原文"

    Retains only the elements in this collection that are contained in the specified collection.
    
    Allows to overcome type-safety restriction of `retainAll` that requires to pass a collection of type `Collection<E>`.
    
    @return `true` if any element was removed from the collection, `false` if the collection was not modified.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <@kotlin.internal.OnlyInputTypes T> MutableCollection<out T>.retainAll(elements: Collection<T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L36)

### 2. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.retainAll(elements: Iterable<T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L180)

只保留 `MutableCollection` 中包含于给定的`elements`收藏中的元素。

### 3. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.retainAll(elements: Array<out T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L188)

只保留给定的 `elements` 阵列中所含的`MutableCollection` 的元素。

### 4. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableCollection<in T>.retainAll(elements: Sequence<T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L199)

只保留给定的 `elements` 序列中所含的 `MutableCollection` 元素。

### 5. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableIterable<T>.retainAll(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L227)

仅保留与给定的 `predicate` 匹配的`MutableIterable` 元素。

如果从该收藏中移除任何元素,@return `true` ,则所有元素保留且收集未经修改,即 `false` 。

### 6. Common

```kotlin
@IgnorableReturnValue
public fun <T> MutableList<T>.retainAll(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L292)

仅保留与给定的 `predicate` 匹配的`MutableList` 元素。

如果从该收藏中移除任何元素,@return `true` ,则所有元素保留且收集未经修改,即 `false` 。

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
    val result = source.`retainAll`(listOf(1, 2, 3))
    println(result)
}
```

```text title="输出"
false
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
