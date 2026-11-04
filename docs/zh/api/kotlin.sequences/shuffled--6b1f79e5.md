# shuffled

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个序列,该序列生成元素,随机地生成该序列的元素。

请注意,序列的每一次迭代都返回不同顺序的元素。

操作是 _ 中间线 _ 和 _ tateful_ 。

??? note "查看英文原文"

    Returns a sequence that yields elements of this sequence randomly shuffled.
    
    Note that every iteration of the sequence returns elements in a different order.
    
    The operation is _intermediate_ and _stateful_.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> Sequence<T>.shuffled(): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L153)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> Sequence<T>.shuffled(random: Random): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L163)

返回一个序列,该序列生成此序列的元素,使用指定的 `random` 实例随机地进行洗涤,作为随机性的来源。

请注意,序列的每一次迭代都返回不同顺序的元素。

操作是 _ 中间线 _ 和 _ tateful_ 。

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
    val result = source.`shuffled`()
    println(result.toList())
}
```

```text title="输出"
[1, 2, 3]
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
