# flatten

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此序列中所有序列中的所有元素的序列。

操作是 _ 中间线 _ 和 _ 无国籍 。

@sample 样本、采集资料、序列、变形、缩缩缩序列、序列

??? note "查看英文原文"

    Returns a sequence of all elements from all sequences in this sequence.
    
    The operation is _intermediate_ and _stateless_.
    
    @sample samples.collections.Sequences.Transformations.flattenSequenceOfSequences

## 声明与重载

### 1. Common

```kotlin
public fun <T> Sequence<Sequence<T>>.flatten(): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L108)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("flattenSequenceOfIterable")
public fun <T> Sequence<Iterable<T>>.flatten(): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L117)

返回此序列中所有可重复的元素的所有元素的序列。

操作是 _ 中间线 _ 和 _ 无国籍 。

@sample 样本、采集资料、序列、变形、缩缩缩序列

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.random.Random
import kotlin.test.*

private class TriggerSequence<out T>(val source: Sequence<T>) : Sequence<T> {
        var iterated: Boolean = false
            private set

        override fun iterator(): Iterator<T> = source.iterator().also { iterated = true }
    }

fun <T> ensureIsIntermediate(source: Sequence<T>, operation: (Sequence<T>) -> Sequence<*>) {
        TriggerSequence(source).let { s ->
            val result = operation(s)
            println(s.iterated)
            result.iterator().hasNext()
            println(s.iterated)
        }
    }

fun testPlus(doPlus: (Sequence<String>) -> Sequence<String>) {
        val seq = sequenceOf("foo", "bar")
        val seq2: Sequence<String> = doPlus(seq)
        println(seq.toList())
        println(seq2.toList())
    }

private fun testMinus(expected: List<String>? = null, doMinus: (Sequence<String>) -> Sequence<String>) {
        val a = sequenceOf("foo", "bar", "bar")
        val b: Sequence<String> = doMinus(a)
        val expected_ = expected ?: listOf("foo")
        println(b.toList())
    }

private fun <T, C : MutableCollection<in T>> Sequence<T>.takeWhileTo(result: C, predicate: (T) -> Boolean): C {
        for (element in this) if (predicate(element)) result.add(element) else break
        return result
    }

fun fibonacci(): Sequence<Int> {
    // fibonacci terms
    // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, ...
    return generateSequence(Pair(0, 1), { Pair(it.second, it.first + it.second) }).map { it.first * 1 }
}

fun indexSequence(): Sequence<Int> = generateSequence(0) { it + 1 }

fun main() {

        val expected = listOf(0, 1, 0, 1, 2)

        val seq = sequenceOf((0..1).asSequence(), (0..2).asSequence()).flatten()
        println(seq.toList())

        val seqMappedSeq = sequenceOf(1, 2).map { (0..it).asSequence() }.flatten()
        println(seqMappedSeq.toList())

        val seqOfIterable = sequenceOf(0..1, 0..2).flatten()
        println(seqOfIterable.toList())

        val seqMappedIterable = sequenceOf(1, 2).map { 0..it }.flatten()
        println(seqMappedIterable.toList())
    
}
```

```text title="输出"
[0, 1, 0, 1, 2]
[0, 1, 0, 1, 2]
[0, 1, 0, 1, 2]
[0, 1, 0, 1, 2]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/SequenceTest.kt#L604)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
