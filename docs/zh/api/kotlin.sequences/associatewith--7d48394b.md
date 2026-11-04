# associateWith

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

a `Map` 返回,其中关键是给定序列的元素,而数值则由适用于每个元素的`valueSelector`函数生成。

如果任何两个元素相等, 最后一个元素会被添加到地图上 。

返回的地图保留了原始序列的输入迭代顺序。

操作为 _flintinal_。

@sample 样本、采集的样本、采集的采集、转化的转化、与

??? note "查看英文原文"

    Returns a `Map` where keys are elements from the given sequence and values are
    produced by the `valueSelector` function applied to each element.
    
    If any two elements are equal, the last one gets added to the map.
    
    The returned map preserves the entry iteration order of the original sequence.
    
    The operation is _terminal_.
    
    @sample samples.collections.Collections.Transformations.associateWith

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
public inline fun <K, V> Sequence<K>.associateWith(valueSelector: (K) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L931)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val words = listOf("a", "abc", "ab", "def", "abcd")
    val withLength = words.associateWith { it.length }
    println(withLength.keys)
    println(withLength.values)
}
```

```text title="输出"
[a, abc, ab, def, abcd]
[1, 3, 2, 3, 4]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L794)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
