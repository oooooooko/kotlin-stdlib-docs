# flatMapIndexedTo

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

`sumByDouble` is deprecated; use `sumOf` in new code.

## Declarations and overloads

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

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1095)

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

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1116)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
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

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
