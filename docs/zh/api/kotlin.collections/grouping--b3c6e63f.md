# Grouping

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

表示具有`keyOf`功能的元素来源,可适用于每个元素以获得其键。

A`Grouping`结构是分组和组合作业的一个中间步骤:它们按键组成元素,然后折叠每个组,并有一些总合作业。

其创建方式是将 `keySelector: (T) -> K` 函数附加于元素源。要获取 `Grouping` 实例,请使用 `groupingBy` 扩展功能之一: - `Iterable.groupingBy` - `Sequence.groupingBy` - `Array.groupingBy` - `Array.groupingBy` - `CharSequence.groupingBy`

现有组和倍操作列表,见`Grouping`的扩展功能。

??? note "查看英文原文"

    Represents a source of elements with a `keyOf` function, which can be applied to each element to get its key.
    
    A `Grouping` structure serves as an intermediate step in group-and-fold operations:
    they group elements by their keys and then fold each group with some aggregating operation.
    
    It is created by attaching `keySelector: (T) -> K` function to a source of elements.
    To get an instance of `Grouping` use one of `groupingBy` extension functions:
    - `Iterable.groupingBy`
    - `Sequence.groupingBy`
    - `Array.groupingBy`
    - `CharSequence.groupingBy`
    
    For the list of group-and-fold operations available, see the extension functions for `Grouping`.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public interface Grouping<T, out K>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L11)

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
import kotlin.collections.*

fun main() {
    val value = listOf(1, 2, 3).groupingBy { it % 2 }
    println(value)
}
```

```text title="输出"
ExampleKt$main$$inlined$groupingBy$1@2b193f2d
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
