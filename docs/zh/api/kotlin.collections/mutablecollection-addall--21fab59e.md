# MutableCollection.addAll

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定收藏的全部元素添加到此收藏中 。

如果在收藏中添加了任何特定元素,@return `true` ;如果收藏没有修改,则`false`。

@sample 样本采集 采集 添加了所有 @sample 样本 采集 采集 采集

??? note "查看英文原文"

    Adds all of the elements of the specified collection to this collection.
    
    @return `true` if any of the specified elements was added to the collection, `false` if the collection was not modified.
    
    @sample samples.collections.Collections.Lists.addAll
    @sample samples.collections.Collections.Sets.addAll

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun addAll(elements: Collection<E>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L147)

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



fun main() {
    val set = mutableSetOf('a', 'b', 'c')
    // All three elements are in set, nothing will be added
    println(set.addAll(listOf('a', 'b', 'c')))
    // At least one element will be added, 'd'
    println(set.addAll(listOf('a', 'b', 'c', 'd')))
    println(set)
}
```

```text title="输出"
false
true
[a, b, c, d]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L671)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
