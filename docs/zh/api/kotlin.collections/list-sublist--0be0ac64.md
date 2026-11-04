# List.subList

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回指定 `fromIndex` (包括) 和 `toIndex` (不包括) 之间的此列表部分的视图。 返回列表支持此列表, 因此返回列表中的非结构变化会反映在此列表中, 反之亦然 。

基数列表的结构变化使得视图的行为未指明。

@throws 指数外溢值,如果`fromIndex`低于零或 `toIndex` 大于 `size` ,则除外。 @throws 非法辩护( `fromIndex` )超过`toIndex`。

@sample 样本、采集资料、收集资料、清单、次清单

??? note "查看英文原文"

    Returns a view of the portion of this list between the specified `fromIndex` (inclusive) and `toIndex` (exclusive).
    The returned list is backed by this list, so non-structural changes in the returned list are reflected in this list,
    and vice versa.
    
    Structural changes in the base list make the behavior of the view unspecified.
    
    @throws IndexOutOfBoundsException if `fromIndex` less than zero or `toIndex` greater than `size` of this list.
    @throws IllegalArgumentException of `fromIndex` is greater than `toIndex`.
    
    @sample samples.collections.Collections.Lists.subList

## 声明与重载

### 1. Common

```kotlin
public fun subList(fromIndex: Int, toIndex: Int): List<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L281)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf(1, 2, 3, 4, 5)
    println(list.subList(2, 4))

    val mutableList = mutableListOf(1, 2, 3, 4, 5)
    val subList = mutableList.subList(2, 4)
    println(subList)

    mutableList[3] = -1
    println(subList)

    assertFailsWith<IndexOutOfBoundsException> { list.subList(0, 100) }
}
```

```text title="输出"
[3, 4]
[3, 4]
[3, -1]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L430)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
