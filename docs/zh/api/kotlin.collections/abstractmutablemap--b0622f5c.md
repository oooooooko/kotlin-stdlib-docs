# AbstractMutableMap

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

提供 `MutableMap` 接口的骨骼实施。

执行者必须执行`entries`财产,这些财产应返回可变的地图条目和`put`功能。

@param K 地图密钥类型。 地图的关键类型是无变的。 @param V 地图值类型是无变的。 地图的值类型是无变的。

??? note "查看英文原文"

    Provides a skeletal implementation of the `MutableMap` interface.
    
    The implementor is required to implement `entries` property, which should return mutable set of map entries, and `put` function.
    
    @param K the type of map keys. The map is invariant in its key type.
    @param V the type of map values. The map is invariant in its value type.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
public expect abstract class AbstractMutableMap<K, V> : MutableMap<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/AbstractMutableMap.kt#L8)

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
    val value = object : AbstractMutableMap<String, Int>() { private val data = mutableMapOf("a" to 1); override val entries get() = data.entries; override fun put(key: String, value: Int) = data.put(key, value) }
    println(value)
}
```

```text title="输出"
{a=1}
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
