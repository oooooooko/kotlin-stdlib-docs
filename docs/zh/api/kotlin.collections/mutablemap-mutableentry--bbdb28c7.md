# MutableMap.MutableEntry

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

代表由`MutableMap`保有的一对钥匙/价值。

从`MutableMap.entries`套迭代中获取的地图条目不应单独存储,或在获得后很久使用。如果在获得后对支持地图进行了修改,则该条目的行为将不予说明,除非通过`setValue`方法对地图进行了修改。

要创建与任何地图不连接的不可变条目, 需要使用 `Map.Entry.copy` 函数 。

@param K 输入键的类型。 输入的键类型是无变的。 @param V 输入值的类型是无变的。 输入的值类型是无变的。

??? note "查看英文原文"

    Represents a key/value pair held by a `MutableMap`.
    
    Map entries obtained from the iteration of `MutableMap.entries` set are not supposed to be stored separately or
    used long after they are obtained.
    The behavior of an entry is unspecified if the backing map has been modified after the entry was obtained,
    except when the map was modified through the `setValue` method.
    
    To create an immutable entry not connected to any map, one can use `Map.Entry.copy` function.
    
    @param K the type of the entry key. The entry is invariant in its key type.
    @param V the type of the entry value. The entry is invariant in its value type.

## 声明与重载

### 1. Common

```kotlin
public interface MutableEntry<K, V> : Map.Entry<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L731)

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
    val value = mutableMapOf("a" to 1).entries.first()
    println(value)
}
```

```text title="输出"
a=1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
