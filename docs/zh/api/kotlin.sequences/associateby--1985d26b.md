# associateBy

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

a `Map` 返回包含从对每个元素适用的`keySelector`函数返回的按键索引的给定序列中元素的`Map`。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留了原始序列的输入迭代顺序。

操作为 _flintinal_。

@sample 样本、采集、采集、转化、关联

??? note "查看英文原文"

    Returns a `Map` containing the elements from the given sequence indexed by the key
    returned from `keySelector` function applied to each element.
    
    If any two elements would have the same key returned by `keySelector` the last one gets added to the map.
    
    The returned map preserves the entry iteration order of the original sequence.
    
    The operation is _terminal_.
    
    @sample samples.collections.Collections.Transformations.associateBy

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, K> Sequence<T>.associateBy(keySelector: (T) -> K): Map<K, T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L844)

### 2. Common

```kotlin
public inline fun <T, K, V> Sequence<T>.associateBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L860)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定序列的各个元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留了原始序列的输入迭代顺序。

操作为 _flintinal_。

@sample 样本、采集、采集、变异、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String) {
        override fun toString(): String = "$firstName $lastName"
    }

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = scientists.associateBy { it.lastName }

    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="输出"
{Hopper=Grace Hopper, Bernoulli=Johann Bernoulli}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L718)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String)

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = scientists.associateBy({ it.lastName }, { it.firstName })

    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="输出"
{Hopper=Grace, Bernoulli=Johann}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L732)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
