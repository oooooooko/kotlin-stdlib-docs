# ArrayList.trimToSize

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

试图减少用于该清单的存储量。

如果该列表的后台存储量大于保持其当前元素所需的数量,那么它可能会被调整大小,以提高空间效率。 当该列表预计不会进一步增长时,此操作可以帮助减少内存消耗。

在联署材料的目标方面,由于联署材料的内部执行,这种方法没有效果。

@sample 样本、采集样本、采集采集样本、列表、阵列样本、

??? note "查看英文原文"

    Attempts to reduce the storage used for this list.
    
    If the backing storage of this list is larger than necessary to hold its current elements,
    then it may be resized to become more space efficient.
    This operation can help reduce memory consumption when the list is not expected to grow further.
    
    On the JS target, this method has no effect due to the internal JS implementation.
    
    @sample samples.collections.Collections.Lists.ArrayList.trimToSize

## 声明与重载

### 1. Common

```kotlin
public fun trimToSize()
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/ArrayList.kt#L80)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = ArrayList<Int>(1000)
    // Add only a few elements
    list.addAll(listOf(1, 2, 3))
    println(list)

    // The list has capacity for 1000 elements, but only 3 are used.
    // trimToSize() can help reduce memory usage by resizing the backing storage
    // to fit the actual number of elements.
    list.trimToSize()

    // The list content remains the same
    println(list)
    println(list.size)
}
```

```text title="输出"
[1, 2, 3]
[1, 2, 3]
3
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L523)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
