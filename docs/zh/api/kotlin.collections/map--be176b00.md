# Map

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

收藏的收藏中包含对对象(钥匙和值),支持检索每个键的相应值,检查收藏中是否持有特定键或值。地图还允许对键、值或键值对(输入)进行迭接。复杂的操作以此功能为基础,以 `kotlin.collections` 扩展功能的形式提供。

地图键是独一无二的; 地图每个关键键只有一个值。 相反, 同一个值可以与多个独有的密钥连结 。

执行是具体执行的,是 `Map` 如何定义关键特性。如果没有另外说明,则`Map`执行通常是使用`Any.equals`区分元素的区分元素。然而,这不是区分元素的唯一方法,有些执行可能使用优惠平等,或者比较其某些属性的元素。建议明确说明执行`Map`的类别如何区分元素。

具体实施也是`Map`如何处理 `null` 钥匙和价值:大约`Map`执行可以支持这些钥匙和价值,而其他则可能不支持,建议在实施`Map`时明确界定关键/价值无效政策。

`Map`并不保证对钥匙、值或条目的迭代命令,但特定执行可自由设定固定迭代命令,例如“较小”的迭代命令,在某种意义上,键在“大”之前会访问,建议明确记录为`Map`执行的保证书。

与 `Collection` 执行不同, `Map`执行必须超越 `Any.toString` 、 `Any.equals`和 `Any.hashCode` 功能,并提供以下执行: - `Map.toString` 应返回含有迭代顺序中包含的钥匙- 双对的字符串表示。 - `Map.equals` 考虑两个地图相等,如果并且只有它们含有与这些钥匙相关的相同键和值,它们才相等。 与其它大约 `equals` 的执行不同, `Map.equals` 执行应该考虑两个地图相等,即使它们属于不同类别; 这里的唯一要求是, 这两张地图都必须执行 `Map` 10接口。 - `Map.hashCode` 应计算为 `Entry` hash代码的总数, 输入的散码应作为与钥匙和值相对应的散码的独家或( XOR) 计算为异号:```kotlin
  var hashCode: Int = 0
  for ((k, v) in entries) hashCode += k.hashCode() xor v.hashCode()
  ```

此接口支持的函数仅读取访问地图; 读写访问通过 `MutableMap` 接口支持。

@param K 地图密钥类型。 地图的关键类型是无变的, 因为它可以接受一个密钥作为参数( 例如 `containsKey`) , 并以 `keys` 设置的`keys` 返回它。 @param V 是地图值类型。 地图的值类型是共变量 。

??? note "查看英文原文"

    A collection that holds pairs of objects (keys and values) and supports retrieving the value corresponding to each key,
    checking if a collection holds a particular key or a value. Maps also allow iterating over keys, values or key-value pairs (entries).
    Complex operations are built upon this functionality and provided in form of `kotlin.collections` extension functions.
    
    Map keys are unique; the map holds only one value for each key. In contrast, the same value can be associated with several unique keys.
    
    It is implementation-specific how `Map` defines key's uniqueness. If not stated otherwise, `Map` implementations are usually
    distinguishing elements using `Any.equals`. However, it is not the only way to distinguish elements, and some implementations may use
    referential equality or compare elements by some of their properties. It is recommended to explicitly specify how a class
    implementing `Map` distinguish elements.
    
    It is also implementation-specific how `Map` handles `null` keys and values: some `Map` implementations may support them, while
    other may not. It is recommended to explicitly define key/value nullability policy when implementing `Map`.
    
    `Map` does not guarantee any particular order for iteration over its keys, values, or entries. However, particular implementations
    are free to have fixed iteration order, like "smaller", in some sense, keys are visited prior to "larger". In this case,
    it is recommended to explicitly document ordering guarantees for the `Map` implementation.
    
    Unlike `Collection` implementations, `Map` implementations must override `Any.toString`, `Any.equals` and `Any.hashCode` functions
    and provide implementations such that:
    - `Map.toString` should return a string containing string representation of contained key-value pairs in iteration order.
    - `Map.equals` should consider two maps equal if and only if they contain the same keys and values associated with these keys
      are equal. Unlike some other `equals` implementations, `Map.equals` should consider two maps equal even
      if they are instances of different classes; the only requirement here is that both maps have to implement `Map` interface.
    - `Map.hashCode` should be computed as a sum of `Entry` hash codes, and entry's hash code should be computed as exclusive or (XOR) of
      hash codes corresponding to a key and a value:
      ```kotlin
      var hashCode: Int = 0
      for ((k, v) in entries) hashCode += k.hashCode() xor v.hashCode()
      ```
    
    Functions in this interface support only read-only access to the map; read-write access is supported through
    the `MutableMap` interface.
    
    @param K the type of map keys. The map is invariant in its key type, as it
             can accept a key as a parameter (of `containsKey` for example) and return it in a `keys` set.
    @param V the type of map values. The map is covariant in its value type.

## 声明与重载

### 1. Common

```kotlin
public expect interface Map<K, out V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L516)

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
