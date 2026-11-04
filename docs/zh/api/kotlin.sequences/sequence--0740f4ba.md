# Sequence

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

序列通过它的迭代器返回值。 值被低沉地评估, 序列可能无限 。

序列可以反复多次反复,但某些序列执行可能会限制自己只重复一次。 这一点在文件(如`generateSequence`超载)中具体提到。 后一种序列在第二次试图重复时会提出一个例外。

序列操作,如 `Sequence.map` ,`Sequence.filter`等 通常保存着序列的该财产 如果它不保存的话,它也会被记录在操作文件上

@param T 序列中元素的类型 。

??? note "查看英文原文"

    A sequence that returns values through its iterator. The values are evaluated lazily, and the sequence
    is potentially infinite.
    
    Sequences can be iterated multiple times, however some sequence implementations might constrain themselves
    to be iterated only once. That is mentioned specifically in their documentation (e.g. `generateSequence` overload).
    The latter sequences throw an exception on an attempt to iterate them the second time.
    
    Sequence operations, like `Sequence.map`, `Sequence.filter` etc, generally preserve that property of a sequence, and
    again it's documented for an operation if it doesn't.
    
    @param T the type of elements in the sequence.

## 声明与重载

### 1. Common

```kotlin
public interface Sequence<out T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequence.kt#L8)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Sequence(crossinline iterator: () -> Iterator<T>): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L14)

给 `iterator` 函数, `iterator` 函数构建了 `Sequence` 函数, 返回该函数提供的 `Iterator` 值。 值被低沉地评估, 序列可能无限 。

@sample 样本、采集资料、序列、建筑、从试运行器中采集的序列

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
    val value = sequenceOf(1, 2, 3)
    println(value)
}
```

```text title="输出"
kotlin.collections.ArraysKt___ArraysKt$asSequence$$inlined$Sequence$1@511d50c0
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
