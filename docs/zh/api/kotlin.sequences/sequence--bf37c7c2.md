# sequence

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

形成`Sequence` 低沉的 逐个生成值。

如果消费代码在完成之前停止迭接序列, 其余的计算将完全无法运行。 特别是, 这意味着 `finally` 块块可能未执行 :

```
val sequenceOfOne = sequence {
    try {
        yield(1)
        // no code after the `yield(1)` line will be executed!
    } finally {
        println("This line will not run")
    }
}
// only get the first element, do not attempt evaluating the rest of them
println(sequenceOfOne.first())
```

@see 千千科特林. 后继. generates 后继

@sample 样本、采集量、序列、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、

??? note "查看英文原文"

    Builds a `Sequence` lazily yielding values one by one.
    
    If the consuming code stops iterating the sequence before it's completed,
    the remainder of the computation will not run at all.
    In particular, it means that `finally` blocks may be left unexecuted:
    
    ```
    val sequenceOfOne = sequence {
        try {
            yield(1)
            // no code after the `yield(1)` line will be executed!
        } finally {
            println("This line will not run")
        }
    }
    // only get the first element, do not attempt evaluating the rest of them
    println(sequenceOfOne.first())
    ```
    
    @see kotlin.sequences.generateSequence
    
    @sample samples.collections.Sequences.Building.buildSequenceYieldAll
    @sample samples.collections.Sequences.Building.buildFibonacciSequence

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@Suppress("DEPRECATION")
public fun <T> sequence(@BuilderInference block: suspend SequenceScope<T>.() -> Unit): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L16)

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
    val result = `sequence`({ yield(1); yield(2) })
    println(result.toList())
}
```

```text title="输出"
[1, 2]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
