# LinkedHashSet

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

执行`MutableSet`号哈希表,维持插入命令。

这个类储存独特的元素, 使用散列表数据结构, 提供快速查看并确保不存储重复元素, 同时保持加入元素的顺序, 并充分实施`MutableSet` 合同, 提供所有标准操作, 包括查找、 插入和移除 。

∮无元素

`LinkedHashSet` 接受 `null` 作为元素。由于元素是独特的,最多可在集中存在`null`元素。

元素的散列法和平等合同

`LinkedHashSet` 依靠`Any.hashCode`和 `Any.equals` 这两个元素的功能来组织和定位这些元素。如果其 `Any.equals` 函数返回`true`,则元素被视为相等,而等值元素必须具有相同的 `Any.hashCode` 价值。 违反这一合同可能导致不正确的行为,例如存储的重复元素或无法获取元素。

`Any.hashCode`和`Any.equals`功能在元素对象的寿命期间应当一致和不可改变。修改元素,在将其散列代码或平等添加到`LinkedHashSet`之后改变其散列代码或平等,可能导致元素无法达到。

□ 性能特点

以下的性能特征假定,元素的`Any.hashCode`功能在散列表上统一分布,最大限度地减少碰撞。 造成许多碰撞的差散功能会降低性能。

`LinkedHashSet`为共同业务提供有效的执行:

- ** 查看** ( `contains` ): O(1)时间 - ** 吸入和清除** (`add`, `remove`): O(1)时间 - ** 试看**: O(n)时间

∮循环顺序

`LinkedHashSet` 元素的迭代顺序是可预测的。元素按插入集的顺序迭代,从最老的到最新的。即使重新组合(当元素被添加或删除,内部容量被调整),也保留了插入顺序。

请注意,如果元素被 _re- intered_ 插入集,插入顺序不会受到影响。当调用`add(e)`时,输入元素`e`, 并且该元素已经包含相当于`e`的元素时, 输入元素`e` 。

如果不需要可预测的迭代顺序,则考虑使用 `HashSet` ,这可能会有稍好一点的性能特征。

□ 使用准则

`LinkedHashSet` 使用一个内部数据结构, 其容量为一定的 * 容量 * , 即它可以在需要增长之前存储的元素的最大数量。 添加元素后, 集跟踪其 * 载荷因子 * , 即元素数量与当前容量之比。 当该比率超过一定阈值时, 设定自动增加其容量并进行 * 重排 * , 重建内部数据结构以重新分配元素。 重排是一个相对昂贵的操作, 暂时影响性能。 当创建 `LinkedHashSet` 时, 您可以选择为初始容量和载荷因子阈值提供值。 注意这些参数只是执行的提示, 并且可以忽略 。

为优化业绩和记忆使用:

- 如果事先知道元素数量,使用初始容量的建筑师
以避免随着集组的生长而多次重复重复操作。
- 在创建集时选择适当的负载系数。 降低负载系数会减少碰撞
概率但使用更多内存,而较高负载系数则保存内存,但可能会增加
检查时间。 默认负载系数通常提供良好的平衡。
- 确保元素物体具有分布良好的`Any.hashCode`执行装置,以尽量减少碰撞
并保持良好的业绩。
- 在添加多个元素时,在多个单人`add`调用上,优于`addAll`。

∮线条安全

`LinkedHashSet` 并非线索安全。 如果多个线索同时访问实例, 至少一个线索修改它, 则需要外部同步 。

@param E 即集所含元素的类型。变音集在元素类型中是无变的。

??? note "查看英文原文"

    A hash table implementation of `MutableSet` that maintains insertion order.
    
    This class stores unique elements using a hash table data structure that provides fast lookups
    and ensures no duplicate elements are stored, while also maintaining the order in which elements
    were inserted. It fully implements the `MutableSet` contract, providing all standard set operations
    including lookup, insertion, and removal.
    
    ## Null elements
    
    `LinkedHashSet` accepts `null` as an element. Since elements are unique, at most one `null` element
    can exist in the set.
    
    ## Element's hash code and equality contracts
    
    `LinkedHashSet` relies on the `Any.hashCode` and `Any.equals` functions of elements to organize and locate them.
    Elements are considered equal if their `Any.equals` function returns `true`, and elements that are equal
    must have the same `Any.hashCode` value. Violating this contract can lead to incorrect behavior, such as
    duplicate elements being stored or elements becoming unreachable.
    
    The `Any.hashCode` and `Any.equals` functions should be consistent and immutable during the lifetime
    of the element objects. Modifying an element in a way that changes its hash code or equality
    after it has been added to a `LinkedHashSet` may lead to the element becoming unreachable.
    
    ## Performance characteristics
    
    The performance characteristics below assume that the `Any.hashCode` function of elements distributes
    them uniformly across the hash table, minimizing collisions. A poor hash function that causes
    many collisions can degrade performance.
    
    `LinkedHashSet` provides efficient implementation for common operations:
    
    - **Lookup** (`contains`): O(1) time
    - **Insertion and removal** (`add`, `remove`): O(1) time
    - **Iteration**: O(n) time
    
    ## Iteration order
    
    `LinkedHashSet` maintains a predictable iteration order for its elements.
    Elements are iterated in the order they were inserted into the set, from oldest to newest.
    This insertion order is preserved even when the set is rehashed (when elements are added or removed
    and the internal capacity is adjusted).
    
    Note that the insertion order is not affected if an element is _re-inserted_ into the set.
    An element `e` is re-inserted into the set when `add(e)` is called and the set already contains
    an element equal to `e`.
    
    If predictable iteration order is not required, consider using `HashSet`, which may have
    slightly better performance characteristics.
    
    ## Usage guidelines
    
    `LinkedHashSet` uses an internal data structure with a finite *capacity* - the maximum number of elements
    it can store before needing to grow. As elements are added, the set tracks its *load factor*, which is
    the ratio of the number of elements to the current capacity. When this ratio exceeds a certain threshold,
    the set automatically increases its capacity and performs *rehashing* - rebuilding the internal data
    structure to redistribute elements. Rehashing is a relatively expensive operation that temporarily impacts
    performance. When creating a `LinkedHashSet`, you can optionally provide values for the initial capacity and
    load factor threshold. Note that these parameters are just hints for the implementation and can be ignored.
    
    To optimize performance and memory usage:
    
    - If the number of elements is known in advance, use the constructor with initial capacity
      to avoid multiple rehashing operations as the set grows.
    - Choose an appropriate load factor when creating the set. A lower load factor reduces collision
      probability but uses more memory, while a higher load factor saves memory but may increase
      lookup time. The default load factor typically provides a good balance.
    - Ensure element objects have well-distributed `Any.hashCode` implementations to minimize collisions
      and maintain good performance.
    - Prefer `addAll` over multiple individual `add` calls when adding multiple elements.
    
    ## Thread safety
    
    `LinkedHashSet` is not thread-safe. If multiple threads access an instance concurrently and at least
    one thread modifies it, external synchronization is required.
    
    @param E the type of elements contained in the set. The mutable set is invariant in its element type.

## 声明与重载

### 1. Common

```kotlin
public expect class LinkedHashSet<E> : MutableSet<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/LinkedHashSet.kt#L8)

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
