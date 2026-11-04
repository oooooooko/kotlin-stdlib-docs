# generateSequence

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个序列,该序列引用函数计算每次迭代的下一个值,直到函数返回 `null` 。

返回的序列只能重复一次。

@see 限制

@sample 样本、采集资料、序列、建筑、基因序列

??? note "查看英文原文"

    Returns a sequence which invokes the function to calculate the next value on each iteration until the function returns `null`.
    
    The returned sequence is constrained to be iterated only once.
    
    @see constrainOnce
    @see kotlin.sequences.sequence
    
    @sample samples.collections.Sequences.Building.generateSequence

## 声明与重载

### 1. Common

```kotlin
public fun <T : Any> generateSequence(nextFunction: () -> T?): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L681)

### 2. Common

```kotlin
@kotlin.internal.LowPriorityInOverloadResolution
public fun <T : Any> generateSequence(seed: T?, nextFunction: (T) -> T?): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L695)

返回由起始值 `seed` 和函数`nextFunction`定义的序列,该函数用来计算下一个值,根据每个迭代的上一个值计算。

序列产生值直到它遇到第一个 `null` 值。 如果 `seed` 是 `null`, 则生成一个空序列 。

序列可以重复多次,每次从`seed`开始。

@see 科特林序列

@sample 样本、采集资料、序列、结构、基因序列、种子

### 3. Common

```kotlin
public fun <T : Any> generateSequence(seedFunction: () -> T?, nextFunction: (T) -> T?): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L715)

返回函数 `seedFunction` 定义的序列,该函数被引用来产生起始值,返回函数 `seedFunction` 定义的序列,返回函数 `nextFunction` 的序列,该函数被引用来计算根据每个迭代上一个函数计算的下一个数值。

序列生成值直到它遇到第一个 `null` 值。 如果 `seedFunction` 返回 `null`, 则生成一个空序列 。

序列可以重复多次。

@see 科特林序列

@sample 样本、采集资料、序列、结构、与贫虫种子的基因序列

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.stream.*
import kotlin.streams.*



fun main() {
    val evenNumbersSequence: Sequence<Int> = generateSequence(2, { it + 2 }).take(5)
    val evenNumberStream: Stream<Int> = evenNumbersSequence.asStream()
    println(evenNumberStream.toList())
}
```

```text title="输出"
[2, 4, 6, 8, 10]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/streams/streams.kt#L42)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
