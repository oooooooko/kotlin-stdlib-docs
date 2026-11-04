# HashMap

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

执行 `MutableMap` 的散列表

此类储存关键值对, 使用散列表数据结构, 提供基于密钥的快速查看。 它充分执行`MutableMap` 合同, 提供所有标准的地图操作, 包括插入、 删除和按密钥查找值 。

∮无键和值

`HashMap` 接受 `null` 作为密钥。 由于密钥是独特的, 最多有一个带有 `null` 密钥的条目可以在地图中存在。 `HashMap` 也接受 8 00000005 作为值, 多条目可能具有 8 00000006 值 。

# # 关键的散列代码和平等合同

`HashMap` 依赖于组织和定位条目的钥匙`Any.hashCode`和 `Any.equals` 函数。 如果其 `Any.equals` 函数返回 `true`, 则键被视为相等, 而等值的钥匙必须具有相同的 `Any.hashCode` 值。 违反此合同可能导致不正确的行为 。

`Any.hashCode`和`Any.equals`的功能在寿命期内应保持一致和不可改变
键。 修改关键对象, 修改其散列代码或平等
在`HashMap`中用作密钥后,输入可能无法到达。

□ 性能特点

以下的性能特征假定,钥匙的 `Any.hashCode` 功能在散列表上统一分布,最大限度地减少碰撞。 造成许多碰撞的差散功能会降低性能。

`HashMap`为共同业务提供有效的执行:

- ** 查看** ( `get` , `containsKey` ): O(1)时间 - ** 吸入和移除** ( `put` , `remove` ): O(1)时间 - ** Value搜索** ( `containsValue` ): O(n)时间,要求扫描所有条目 - ** 试看** ( `entries` , `keys` , `values`): O(n)时间:

∮循环顺序

`HashMap` 并不保证其键、值或条目的任何特定迭代顺序。 迭代顺序无法预测, 并在地图被重新拼接时( 当添加或删除条目并调整内部容量时) 可能会改变。 不要依赖任何特定的迭代顺序 。

如果需要可预见迭代令,应考虑使用 `LinkedHashMap` ,维持插入令。

□ 使用准则

`HashMap` 使用一个内部数据结构, 其容量为一定的 * 容量 * , 即它可以在需要增长之前存储的最大条目数量。 添加条目后, 地图跟踪其 * 载荷因子 * , 即条目数量与当前容量之比。 当该比例超过一定阈值时, 地图自动增加其容量并进行 * 重排 * , 重建内部数据结构以重新分配条目。 重排是一个相对昂贵的操作, 暂时影响性能。 当创建 `HashMap` 时, 您可以选择为初始容量和载荷因子阈值提供值。 注意这些参数只是执行的提示, 并且可以忽略 。

为优化业绩和记忆使用:

- 如果事先知道条目数目,使用初始容量的建筑师
以避免随着地图的扩展而发生多次重击操作。
- 创建地图时选择适当的负载系数。 降低负载系数会减少碰撞
概率但使用更多内存,而较高负载系数则保存内存,但可能会增加
检查时间。 默认负载系数通常提供良好的平衡。
- 确保关键物体有分布得分良好的`Any.hashCode`执行,以尽量减少碰撞
并保持良好的业绩。
- 添加多个条目时,在多个单人`put`调用上,更倾向于`putAll`。

∮线条安全

`HashMap` 并非线索安全。 如果多个线索同时访问实例, 至少一个线索修改它, 则需要外部同步 。

@param K 地图密钥类型。 地图的关键类型是无变的。 @param V 地图值类型是无变的。 变的地图值类型是无变的。

??? note "查看英文原文"

    A hash table implementation of `MutableMap`.
    
    This class stores key-value pairs using a hash table data structure that provides fast lookups
    based on keys. It fully implements the `MutableMap` contract, providing all standard map operations
    including insertion, removal, and lookup of values by key.
    
    ## Null keys and values
    
    `HashMap` accepts `null` as a key. Since keys are unique, at most one entry with a `null` key
    can exist in the map. `HashMap` also accepts `null` as a value, and multiple entries can have
    `null` values.
    
    ## Key's hash code and equality contracts
    
    `HashMap` relies on the `Any.hashCode` and `Any.equals` functions of keys to organize and locate entries.
    Keys are considered equal if their `Any.equals` function returns `true`, and keys that are equal must
    have the same `Any.hashCode` value. Violating this contract can lead to incorrect behavior.
    
    The `Any.hashCode` and `Any.equals` functions should be consistent and immutable during the lifetime
    of the key objects. Modifying a key object in a way that changes its hash code or equality
    after it has been used as a key in a `HashMap` may lead to the entry becoming unreachable.
    
    ## Performance characteristics
    
    The performance characteristics below assume that the `Any.hashCode` function of keys distributes
    them uniformly across the hash table, minimizing collisions. A poor hash function that causes
    many collisions can degrade performance.
    
    `HashMap` provides efficient implementation for common operations:
    
    - **Lookup** (`get`, `containsKey`): O(1) time
    - **Insertion and removal** (`put`, `remove`): O(1) time
    - **Value search** (`containsValue`): O(n) time, requires scanning all entries
    - **Iteration** (`entries`, `keys`, `values`): O(n) time
    
    ## Iteration order
    
    `HashMap` does not guarantee any particular order for iteration over its keys, values, or entries.
    The iteration order is unpredictable and may change when the map is rehashed (when entries are
    added or removed and the internal capacity is adjusted). Do not rely on any specific iteration order.
    
    If a predictable iteration order is required, consider using `LinkedHashMap`, which maintains
    insertion order.
    
    ## Usage guidelines
    
    `HashMap` uses an internal data structure with a finite *capacity* - the maximum number of entries
    it can store before needing to grow. As entries are added, the map tracks its *load factor*, which is
    the ratio of the number of entries to the current capacity. When this ratio exceeds a certain threshold,
    the map automatically increases its capacity and performs *rehashing* - rebuilding the internal data
    structure to redistribute entries. Rehashing is a relatively expensive operation that temporarily impacts
    performance. When creating a `HashMap`, you can optionally provide values for the initial capacity and
    load factor threshold. Note that these parameters are just hints for the implementation and can be ignored.
    
    To optimize performance and memory usage:
    
    - If the number of entries is known in advance, use the constructor with initial capacity
      to avoid multiple rehashing operations as the map grows.
    - Choose an appropriate load factor when creating the map. A lower load factor reduces collision
      probability but uses more memory, while a higher load factor saves memory but may increase
      lookup time. The default load factor typically provides a good balance.
    - Ensure key objects have well-distributed `Any.hashCode` implementations to minimize collisions
      and maintain good performance.
    - Prefer `putAll` over multiple individual `put` calls when adding multiple entries.
    
    ## Thread safety
    
    `HashMap` is not thread-safe. If multiple threads access an instance concurrently and at least
    one thread modifies it, external synchronization is required.
    
    @param K the type of map keys. The map is invariant in its key type.
    @param V the type of map values. The mutable map is invariant in its value type.

## 声明与重载

### 1. Common

```kotlin
public expect class HashMap<K, V> : MutableMap<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashMap.kt#L8)

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
    val value = hashMapOf("a" to 1)
    println(value)
}
```

```text title="输出"
{a=1}
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
