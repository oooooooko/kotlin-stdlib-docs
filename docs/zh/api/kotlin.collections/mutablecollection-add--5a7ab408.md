# MutableCollection.add

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定元素添加到收藏中。

如果添加了@return `true` 元素,如果收藏不支持重复,而且该元素已经包含在收藏中,则 `false` 。

@sample 样本、采集资料、收集资料、添加@sample样本、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集资料、收集、收集资料、收集资料、收集资料、收集、收集、收集资料、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、、、、、、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集、收集

??? note "查看英文原文"

    Adds the specified element to the collection.
    
    @return `true` if the element has been added, `false` if the collection does not support duplicates
    and the element is already contained in the collection.
    
    @sample samples.collections.Collections.Lists.add
    @sample samples.collections.Collections.Sets.add

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun add(element: E): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L122)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')
    println(list.add('c'))
    println(list)
}
```

```text title="输出"
true
[a, b, c, c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L334)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set = mutableSetOf('a', 'b', 'c')
    // Sets do not support duplicates, so there is no way to add yet another 'c'
    println(set.add('c'))
    println(set)
}
```

```text title="输出"
false
[a, b, c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L663)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
