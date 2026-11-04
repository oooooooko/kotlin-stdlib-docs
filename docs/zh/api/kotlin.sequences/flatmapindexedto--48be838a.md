# flatMapIndexedTo

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

`sumByDouble` 已弃用，新代码使用 `sumOf`。

??? note "查看英文原文"

    Appends all elements yielded from results of `transform` function being invoked on each element
    and its index in the original sequence, to the given `destination`.
    
    The operation is _terminal_.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.jvm.JvmName("flatMapIndexedIterableTo")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <T, R, C : MutableCollection<in R>> Sequence<T>.flatMapIndexedTo(destination: C, transform: (index: Int, T) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1095)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.jvm.JvmName("flatMapIndexedSequenceTo")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <T, R, C : MutableCollection<in R>> Sequence<T>.flatMapIndexedTo(destination: C, transform: (index: Int, T) -> Sequence<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1116)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)

import kotlin.sequences.*
fun main() {
    val values = sequence<Int> { yield(1); yieldAll(listOf(2, 3)) }
    println(values.toList())
    println(values.flatMapTo(mutableListOf<Int>()) { sequenceOf(it, -it) })
    println(values.flatMapIndexedTo(mutableListOf<Int>()) { index, value -> sequenceOf(index, value) })
    println(values.mapTo(mutableListOf<String>()) { "v$it" })
    println(values.mapIndexedTo(mutableListOf<String>()) { index, value -> "$index:$value" })
    println(values.mapNotNullTo(mutableListOf<Int>()) { it.takeIf { n -> n > 1 } })
    println(values.mapIndexedNotNullTo(mutableListOf<Int>()) { index, value -> value.takeIf { index > 0 } })
    println(emptySequence<Int>().ifEmpty { sequenceOf(42) }.toList())
    println(values.sumByDouble { it.toDouble() })
}
```

```text title="输出"
[1, 2, 3]
[1, -1, 2, -2, 3, -3]
[0, 1, 1, 2, 2, 3]
[v1, v2, v3]
[0:1, 1:2, 2:3]
[2, 3]
[2, 3]
[42]
6.0
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
