# MutableCollection.retainAll

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

只保留指定收藏中包含的收藏元素。

如果从收藏中移除任何元素,@return `true` ;如果收藏没有修改,`false`。

@sample 样本 采集 采集 采集 保存

??? note "查看英文原文"

    Retains only the elements in this collection that are contained in the specified collection.
    
    @return `true` if any element was removed from the collection, `false` if the collection was not modified.
    
    @sample samples.collections.Collections.Collections.retainAll

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun retainAll(elements: Collection<E>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L169)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val collection: MutableCollection<Char> = mutableSetOf('a', 'b', 'c')

    // Nothing was removed
    println(collection.retainAll(listOf('a', 'b', 'c')))
    println(collection)

    println(collection.retainAll(listOf('a', 'e', 'i', 'o')))
    println(collection)
}
```

```text title="输出"
false
[a, b, c]
true
[a]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L125)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
