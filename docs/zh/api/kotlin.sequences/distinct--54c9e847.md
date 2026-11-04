# distinct

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个序列,该序列仅包含与给定序列不同的元素。

在给定序列的等同元素中,产生序列中将只存在第一个元素。结果序列中的各个元素的顺序与源序列中的顺序相同。

操作是 _ 中间线 _ 和 _ tateful_ 。

@sample 样本 采集 采集 变异 分异和分异

??? note "查看英文原文"

    Returns a sequence containing only distinct elements from the given sequence.
    
    Among equal elements of the given sequence, only the first one will be present in the resulting sequence.
    The elements in the resulting sequence are in the same order as they were in the source sequence.
    
    The operation is _intermediate_ and _stateful_.
    
    @sample samples.collections.Collections.Transformations.distinctAndDistinctBy

## 声明与重载

### 1. Common

```kotlin
public fun <T> Sequence<T>.distinct(): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1368)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf('a', 'A', 'b', 'B', 'A', 'a')
    println(list.distinct())
    println(list.distinctBy { it.uppercaseChar() })
}
```

```text title="输出"
[a, A, b, B]
[a, b]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L819)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
