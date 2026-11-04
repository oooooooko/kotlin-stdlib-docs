# windowed

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定`size`滑动窗口窗口的抓图序列, 与给定`step`相伴, 每个抓图都是列表 。

几个最后清单中的内容可能少于给定的`size`。

`size` 和 `step` 都必须是正数, 并且可以大于此序列中元素的数量。 @param 大小, 每个窗口中要取取取的元素数量 。 @param 每一步要移动窗口的元素数量, 每一步都一步, 默认 1 8,000000005 部分窗口控制是否在结尾保留部分窗口, 如果有的话, 默认是 `false`, 这意味着部分窗口将无法保存

@sample 样本采集 序列 变形 取窗

??? note "查看英文原文"

    Returns a sequence of snapshots of the window of the given `size`
    sliding along this sequence with the given `step`, where each
    snapshot is a list.
    
    Several last lists may have fewer elements than the given `size`.
    
    Both `size` and `step` must be positive and can be greater than the number of elements in this sequence.
    @param size the number of elements to take in each window
    @param step the number of elements to move the window forward by on an each step, by default 1
    @param partialWindows controls whether or not to keep partial windows in the end if any,
    by default `false` which means partial windows won't be preserved
    
    @sample samples.collections.Sequences.Transformations.takeWindows

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun <T> Sequence<T>.windowed(size: Int, step: Int = 1, partialWindows: Boolean = false): Sequence<List<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3203)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public fun <T, R> Sequence<T>.windowed(size: Int, step: Int = 1, partialWindows: Boolean = false, transform: (List<T>) -> R): Sequence<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3223)

返回对每个列表应用给定的 `transform` 函数的结果序列,每个列表代表给定的 `size` 滑动窗口的视图,并随此序列与给定的 `step` 的 `step` 的视图。

请注意, 列表传递到 `transform` 函数时长, 并且仅在该函数中有效。 您不应该保存它, 也不应该允许它以某种方式逃脱, 除非您对它做了一个快照。 几个最后列表中的内容可能少于给定的 `size` 。

`size` 和 `step` 都必须是正数, 并且可以大于此序列中元素的数量。 @param 大小, 每个窗口中要取取取的元素数量 。 @param 每一步要移动窗口的元素数量, 每一步都一步, 默认 1 8,000000005 部分窗口控制是否在结尾保留部分窗口, 如果有的话, 默认是 `false`, 这意味着部分窗口将无法保存

@sample 样本、采集资料、序列、变形、平均窗口

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
    val result = source.`windowed`(2)
    println(result.toList())
}
```

```text title="输出"
[[1, 2], [2, 3]]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
