# sortedByDescending

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个序列,该序列产生该序列的元素,根据自然排序顺序排序,依指定 `selector` 函数返回的数值的自然排序顺序排序。

类型是 _stair_。 这意味着在排序后, `selector` 返回等值的元素保持彼此相对的顺序。

操作是 _ 中间线 _ 和 _ tateful_ 。

@sample 样本采集 序列 分类 分类 生物降解

??? note "查看英文原文"

    Returns a sequence that yields elements of this sequence sorted descending according to natural sort order of the value returned by specified `selector` function.
    
    The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
    relative to each other after sorting.
    
    The operation is _intermediate_ and _stateful_.
    
    @sample samples.collections.Sequences.Sorting.sortedByDescending

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, R : Comparable<R>> Sequence<T>.sortedByDescending(crossinline selector: (T) -> R?): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L786)

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
import kotlin.sequences.*

fun main() {
    val source = sequenceOf(1, 2, 3)
    val result = source.`sortedByDescending`({ it.toString().length })
    println(result.toList())
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
