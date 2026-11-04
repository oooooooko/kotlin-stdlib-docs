# Map.Entry

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

代表由`Map`保有的一对钥匙/价值。

从`Map.entries`套迭代中获取的地图条目不应单独存储,或在获得后很久使用。如果在获得支持地图后对支持地图进行了修改,则该条目的行为将不予说明。

要创建与任何地图不连接的不可变条目, 需要使用 `Map.Entry.copy` 函数 。

`Entry` 执行必须推翻 `Any.toString`、`Any.equals`和`Any.hashCode` 函数
并规定执行,以便:
- `Entry.toString`应返回`key=value`形式的键值对的字符串表示。
- `Entry.equals`如果键是等同的,而价值是等同的,则`Entry`应考虑任何两种`Entry`情况。
- `Entry.hashCode`应作为独家或(XOR)
与密钥和值对应的散列代码: `key.hashCode() xor value.hashCode()`

@param K 条目键的类型。 条目的密钥类型是共变量。 @param V 的条目值类型是共变量。 条目的值类型是共变量。

??? note "查看英文原文"

    Represents a key/value pair held by a `Map`.
    
    Map entries obtained from the iteration of `Map.entries` set are not supposed to be stored separately or
    used long after they are obtained.
    The behavior of an entry is unspecified if the backing map has been modified after the entry was obtained.
    
    To create an immutable entry not connected to any map, one can use `Map.Entry.copy` function.
    
    `Entry` implementations must override `Any.toString`, `Any.equals` and `Any.hashCode` functions
    and provide implementations such that:
    - `Entry.toString` should return a string representation of the key-value pair in form of `key=value`.
    - `Entry.equals` should consider any two instances of `Entry` equal if their keys are equal and values are equal.
    - `Entry.hashCode` should be computed as exclusive or (XOR) of
      hash codes corresponding to a key and a value: `key.hashCode() xor value.hashCode()`
    
    @param K the type of the entry key. The entry is covariant in its key type.
    @param V the type of the entry value. The entry is covariant in its value type.

## 声明与重载

### 1. Common

```kotlin
public interface Entry<out K, out V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L622)

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
    val value = mapOf("a" to 1).entries.first()
    println(value)
}
```

```text title="输出"
a=1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
