# zipWithNext

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在此序列中返回每两个相邻元素的对数序列。

如果返回的序列包含两个元素以下, 则返回的序列为空 。

操作是 _ 中间线 _ 和 _ 无国籍 。

@sample 样本、采集物、采集物、转化物、与下一个相接

??? note "查看英文原文"

    Returns a sequence of pairs of each two adjacent elements in this sequence.
    
    The returned sequence is empty if this sequence contains less than two elements.
    
    The operation is _intermediate_ and _stateless_.
    
    @sample samples.collections.Collections.Transformations.zipWithNext

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun <T> Sequence<T>.zipWithNext(): Sequence<Pair<T, T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3270)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public fun <T, R> Sequence<T>.zipWithNext(transform: (a: T, b: T) -> R): Sequence<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3284)

返回一个序列,其中包含对本序列中每对两个相邻元素对给定的 `transform` 函数应用结果。

如果返回的序列包含两个元素以下, 则返回的序列为空 。

操作是 _ 中间线 _ 和 _ 无国籍 。

@sample 样本、采集物、采集物、变异物、与下一个FindDeltas的相接

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val letters = ('a'..'f').toList()
    val pairs = letters.zipWithNext()

    println(letters)
    println(pairs)
}
```

```text title="输出"
[a, b, c, d, e, f]
[(a, b), (b, c), (c, d), (d, e), (e, f)]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L937)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val values = listOf(1, 4, 9, 16, 25, 36)
    val deltas = values.zipWithNext { a, b -> b - a }

    println(deltas)
}
```

```text title="输出"
[3, 5, 7, 9, 11]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L946)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
