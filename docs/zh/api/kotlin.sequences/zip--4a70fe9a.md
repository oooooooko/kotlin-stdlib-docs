# zip

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回从 `this` 序列和`other`序列元素中和同一种指数中构建的值序列。 由此产生的序列在输入序列最短的结束后立即结束。

操作是 _ 中间线 _ 和 _ 无国籍 。

@sample 样本 采集 序列 变形 zip

??? note "查看英文原文"

    Returns a sequence of values built from the elements of `this` sequence and the `other` sequence with the same index.
    The resulting sequence ends as soon as the shortest input sequence ends.
    
    The operation is _intermediate_ and _stateless_.
    
    @sample samples.collections.Sequences.Transformations.zip

## 声明与重载

### 1. Common

```kotlin
public infix fun <T, R> Sequence<T>.zip(other: Sequence<R>): Sequence<Pair<T, R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3245)

### 2. Common

```kotlin
public fun <T, R, V> Sequence<T>.zip(other: Sequence<R>, transform: (a: T, b: R) -> V): Sequence<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3257)

返回从 `this` 序列元素和`other`序列元素中构建的数值序列,这些元素使用对每对元素适用的`transform`函数,具有相同的指数,并使用对每对元素的`transform`函数。因此的序列在输入序列最短的结束后立即结束。

操作是 _ 中间线 _ 和 _ 无国籍 。

@sample 样本、采集资料、序列、变形、变形、变形

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
    val result = source.`zip`(sequenceOf(1, 2, 3))
    println(result.toList())
}
```

```text title="输出"
[(1, 1), (2, 2), (3, 3)]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
