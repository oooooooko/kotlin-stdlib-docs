# MutableCollection.remove

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果收藏包含此元素, 从此收藏中删除指定元素的单个实例 。

如果成功地删除了元素, @return `true` ;如果收藏中没有包含,`false`。

@sample 样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、以及和采集的样本、采集的样本、采集的样本、采集的样本、以及、以及、以及、以及、以及和采集的样本、采集的样本、采集的样本、采集的样本、采集的样本、以及、以及在的样本、以及在的样本、采集的样本、采集的样本、采集的样本、以及在的样本、采集的样本中的数据的样本、以及在的样本中的信息、以及

??? note "查看英文原文"

    Removes a single instance of the specified element from this
    collection, if the collection contains it.
    
    @return `true` if the element has been successfully removed; `false` if it was not contained in the collection.
    
    @sample samples.collections.Collections.Lists.remove
    @sample samples.collections.Collections.Sets.remove

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun remove(element: E): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L134)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')

    println(list.remove('a'))
    println(list)

    // There are no more 'a's to remove
    println(list.remove('a'))
    println(list)
}
```

```text title="输出"
true
[b, c]
false
[b, c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L374)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set = mutableSetOf('a', 'b', 'c')

    println(set.remove('a'))
    println(set)

    // There are no more 'a's to remove
    println(set.remove('a'))
    println(set)
}
```

```text title="输出"
true
[b, c]
false
[b, c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L681)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
