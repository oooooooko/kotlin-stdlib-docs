# ArrayList

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

动态阵列执行 `MutableList` 。

使用内部阵列,这些类储存元素在记忆中相邻,内部阵列会自动增长,并完全执行`MutableList`合同,提供所有标准清单操作,包括索引访问、迭代和修改。作为`RandomAccess`的落实,它提供快速索引访问元素。

□ 性能特点

`ArrayList`为共同业务提供有效的执行:

- ** 封闭存取** (`get`,`set`):O(1) 恒定时间
- ** 直至最后** (`add`): O(1) [amortized](https://en.wikipedia.org/wiki/Amortized_analysis)
恒定时间。 当内部数组满全时, 必须调整其大小, 这需要 O( n) 时间复制
新建较大数组的所有现有元素。 然而,这些调整规模的行动越来越少
随着清单的增加,每个附加单位的平均成本与许多业务一样稳定。
- ** 从最后删除** (`removeLast`, `removeAt``(size - 1)`:O(1) 恒定时间
- ** 插入或删除位置** (`add` 具有索引,`removeAt`):O(n)线性时间,
位置必须移位后作为元素的元素
- ** 搜索作业**(`contains`、`indexOf`、`lastIndexOf`):O(n)线性时间
- ** 延长**:O(n)线性时间

注:关于联署材料的目标,由于实施基本的JavaScript发动机,这些时间复杂性保障可能无法维持。

□ 使用准则

为优化业绩和记忆使用:

- 如果事先知道元素数量,使用初始容量的建筑师
以避免随着列表的增加而出现多次再分配。
- 在预先分配足够储存的预分配要素之前,先使用`ensureCapacity`。
- 在添加多个元素时,在多个单人`add`调用上,优于`addAll`。
- 在所有元素被添加后,如果不再使用,可以减少内存消耗,请打电话给`trimToSize`
预计会增长。

∮线条安全

`ArrayList` 并非线索安全。 如果多个线索同时访问实例, 至少一个线索修改它, 则需要外部同步 。

@paramE 清单中包含的元素类型。

??? note "查看英文原文"

    A dynamic array implementation of `MutableList`.
    
    This class stores elements contiguously in memory using an internal array that automatically
    grows as needed. It fully implements the `MutableList` contract, providing all standard list
    operations including indexed access, iteration, and modification. As an implementation of
    `RandomAccess`, it provides fast indexed access to elements.
    
    ## Performance characteristics
    
    `ArrayList` provides efficient implementation for common operations:
    
    - **Indexed access** (`get`, `set`): O(1) constant time
    - **Appending to the end** (`add`): O(1) [amortized](https://en.wikipedia.org/wiki/Amortized_analysis)
      constant time. When the internal array is full, it must be resized, which takes O(n) time to copy
      all existing elements to a new, larger array. However, these resize operations become less frequent
      as the list grows, making the average cost per appending constant over many operations.
    - **Removing from the end** (`removeLast`, `removeAt``(size - 1)`): O(1) constant time
    - **Inserting or removing at a position** (`add` with index, `removeAt`): O(n) linear time,
      as elements after the position must be shifted
    - **Search operations** (`contains`, `indexOf`, `lastIndexOf`): O(n) linear time
    - **Iteration**: O(n) linear time
    
    Note: On the JS target, these time-complexity guarantees may not hold due to the underlying
    JavaScript engine implementation.
    
    ## Usage guidelines
    
    To optimize performance and memory usage:
    
    - If the number of elements is known in advance, use the constructor with initial capacity
      to avoid multiple reallocations as the list grows.
    - Use `ensureCapacity` before adding many elements to pre-allocate sufficient storage.
    - Prefer `addAll` over multiple individual `add` calls when adding multiple elements.
    - Call `trimToSize` after all elements have been added to reduce memory consumption if no further
      growth is expected.
    
    ## Thread safety
    
    `ArrayList` is not thread-safe. If multiple threads access an instance concurrently and at least
    one thread modifies it, external synchronization is required.
    
    @param E the type of elements contained in the list.

## 声明与重载

### 1. Common

```kotlin
public expect class ArrayList<E> : MutableList<E>, RandomAccess
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/ArrayList.kt#L8)

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
    val value = arrayListOf(1, 2, 3)
    println(value)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
