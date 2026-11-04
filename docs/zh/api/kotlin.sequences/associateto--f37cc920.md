# associateTo

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

弹出并返回`destination`变形图,配有由 `transform` 功能提供的配对钥匙,适用于给定序列的每个元素。

如果两对中的任何一个有相同的键, 最后的键会被添加到地图上。

操作为 _flintinal_。

@sample 样本、采集、采集、变形、关联

??? note "查看英文原文"

    Populates and returns the `destination` mutable map with key-value pairs
    provided by `transform` function applied to each element of the given sequence.
    
    If any of two pairs would have the same key the last one gets added to the map.
    
    The operation is _terminal_.
    
    @sample samples.collections.Collections.Transformations.associateTo

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, in V>> Sequence<T>.associateTo(destination: M, transform: (T) -> Pair<K, V>): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L913)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String)

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = mutableMapOf<String, String>()
    println(byLastName.isEmpty())

    scientists.associateTo(byLastName) { it.lastName to it.firstName }

    println(byLastName.isNotEmpty())
    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="输出"
true
true
{Hopper=Grace, Bernoulli=Johann}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L778)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
