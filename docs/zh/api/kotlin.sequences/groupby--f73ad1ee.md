# groupBy

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

以给定 `keySelector` 函数返回的键返回的原始序列的组元素组,对每个元素适用,并返回一个地图,其中每个组键与相应元素列表相关联。

返回的地图保留了从原始序列中产生的钥匙的输入迭代顺序。

操作为 _flintinal_。

@sample 样本、采集、采集、变形、组别

??? note "查看英文原文"

    Groups elements of the original sequence by the key returned by the given `keySelector` function
    applied to each element and returns a map where each group key is associated with a list of corresponding elements.
    
    The returned map preserves the entry iteration order of the keys produced from the original sequence.
    
    The operation is _terminal_.
    
    @sample samples.collections.Collections.Transformations.groupBy

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, K> Sequence<T>.groupBy(keySelector: (T) -> K): Map<K, List<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1169)

### 2. Common

```kotlin
public inline fun <T, K, V> Sequence<T>.groupBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1183)

`valueTransform` 函数返回的组值, 适用于给定 `keySelector` 函数返回的最初序列的每个元素, 并返回给定 `keySelector` 函数返回的每个元素, 返回一个地图, 显示每个组键与相应值列表相关联 。

返回的地图保留了从原始序列中产生的钥匙的输入迭代顺序。

操作为 _flintinal_。

@sample 样本、采集、采集、转换、ByKeys和Vales组

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val words = listOf("a", "abc", "ab", "def", "abcd")
    val byLength = words.groupBy { it.length }

    println(byLength.keys)
    println(byLength.values)

    val mutableByLength: MutableMap<Int, MutableList<String>> = words.groupByTo(mutableMapOf()) { it.length }
    // same content as in byLength map, but the map is mutable
    println(mutableByLength == byLength)
}
```

```text title="输出"
[1, 3, 2, 4]
[[a], [abc, def], [ab], [abcd]]
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L826)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val nameToTeam = listOf("Alice" to "Marketing", "Bob" to "Sales", "Carol" to "Marketing")
    val namesByTeam = nameToTeam.groupBy({ it.second }, { it.first })
    println(namesByTeam)

    val mutableNamesByTeam = nameToTeam.groupByTo(HashMap(), { it.second }, { it.first })
    // same content as in namesByTeam map, but the map is mutable
    println(mutableNamesByTeam == namesByTeam)
}
```

```text title="输出"
{Marketing=[Alice, Carol], Sales=[Bob]}
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L839)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
