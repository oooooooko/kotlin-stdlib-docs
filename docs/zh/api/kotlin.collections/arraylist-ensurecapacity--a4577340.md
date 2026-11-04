# ArrayList.ensureCapacity

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

确保该清单的能力至少等于指定的`minCapacity`。

如果现有容量低于`minCapacity`,则用更大的容量分配新的后备储存,否则,这种方法不采取行动,而只是返回。

当事先知道清单的最终大小时,此操作可用于尽量减少递增重新分配的数量,在增加许多要素时改进业绩。

在联署材料的目标方面,由于联署材料的内部执行,这种方法没有效果。

@param 能力达到理想的最低能力。

@sample 样本、采集资料、收集资料、清单、 激光清单、 增强能力

??? note "查看英文原文"

    Ensures that the capacity of this list is at least equal to the specified `minCapacity`.
    
    If the current capacity is less than the `minCapacity`, a new backing storage is allocated with greater capacity.
    Otherwise, this method takes no action and simply returns.
    
    This operation can be used to minimize the number of incremental reallocations when the eventual size
    of the list is known in advance, improving performance when adding many elements.
    
    On the JS target, this method has no effect due to the internal JS implementation.
    
    @param minCapacity the desired minimum capacity.
    
    @sample samples.collections.Collections.Lists.ArrayList.ensureCapacity

## 声明与重载

### 1. Common

```kotlin
public fun ensureCapacity(minCapacity: Int)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/ArrayList.kt#L93)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // Suppose we have an existing list with unknown current capacity
    val list = arrayListOf(1, 2, 3, 4, 5)

    // When we know in advance that we'll add many elements,
    // we can pre-allocate capacity to avoid multiple reallocations
    val elementsToAdd = 1000
    list.ensureCapacity(list.size + elementsToAdd)

    // Now adding elements won't trigger internal array resizing
    // until we exceed the ensured capacity
    for (i in 1..elementsToAdd) {
        list.add(i)
    }

    println(list.size)
    println(list.first())
    println(list.last())
}
```

```text title="输出"
1005
1
1000
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L540)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
