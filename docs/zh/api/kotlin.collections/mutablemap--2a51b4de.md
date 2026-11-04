# MutableMap

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

收藏收藏的对象(钥匙和值),支持检索每个关键值的对应值,并添加新的、删除或更新现有的对。

地图键是独一无二的; 地图每个关键键只有一个值。 相反, 同一个值可以与多个独有的密钥连结 。

如果某一特定用途的情况不需要修改地图,则可以使用只读对应数据`Map`。

`MutableMap`延长了`Map`的合同,其功能允许添加、删除和更新关键值和值之间的绘图。

与`Map`、`keys`、`values`和`entries`不同,收集的物品都是可变的,而且其变化更新了地图。

在另外说明之前,`MutableMap`的履行并非完全安全,除非另有说明,否则`MutableMap`的履行是无法安全地进行修改的,除非
明确同步可能导致数据腐败、丢失和运行时错误。

@param K 地图密钥类型。 地图的关键类型是无变的。 @param V 地图值类型是无变的。 变的地图值类型是无变的。

??? note "查看英文原文"

    A collection that holds pairs of objects (keys and values) and supports retrieving
    the value corresponding to each key, as well as adding new, removing or updating existing pairs.
    
    Map keys are unique; the map holds only one value for each key. In contrast, the same value can be associated with several unique keys.
    
    If a particular use case does not require map's modification, a read-only counterpart, `Map` could be used instead.
    
    `MutableMap` extends `Map` contract with functions allowing to add, remove and update mapping between keys and values.
    
    Unlike `Map`, `keys`, `values` and `entries` collections are all mutable, and changes in them update the map.
    
    Until stated otherwise, `MutableMap` implementations are not thread-safe and their modification without
    explicit synchronization may result in data corruption, loss, and runtime errors.
    
    @param K the type of map keys. The map is invariant in its key type.
    @param V the type of map values. The mutable map is invariant in its value type.

## 声明与重载

### 1. Common

```kotlin
public expect interface MutableMap<K, V> : Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L654)

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
    val value = linkedMapOf("a" to 1, "b" to 2)
    println(value)
}
```

```text title="输出"
{a=1, b=2}
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
