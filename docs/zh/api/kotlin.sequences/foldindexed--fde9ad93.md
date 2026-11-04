# foldIndexed

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

累积值为 `initial` ,并用 `operation` 从左向右对当前累积值和每个元素的指数在原序列中应用`operation`。

如果序列为空,则返回指定的 `initial` 值。

@param `operation` 函数,该函数采用元素的索引、当前累积值和元素本身,并计算下一个累积值。

操作为 _flintinal_。

??? note "查看英文原文"

    Accumulates value starting with `initial` value and applying `operation` from left to right
    to current accumulator value and each element with its index in the original sequence.
    
    Returns the specified `initial` value if the sequence is empty.
    
    @param `operation` function that takes the index of an element, current accumulator value
    and the element itself, and calculates the next accumulator value.
    
    The operation is _terminal_.

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, R> Sequence<T>.foldIndexed(initial: R, operation: (index: Int, acc: R, T) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1620)

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

        var count = 0
        val data = sequenceOf("foo", "bar")
        val newData = data.onEachIndexed { i, e -> count += i + e.length }
        println(data !== newData)
        println(count)

        data.forEach {  }
        println(count)

        val sum = newData.foldIndexed(0) { i, acc, e -> acc + i + e.length }
        println(count)
    
}
```

```text title="输出"
true
0
0
7
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/SequenceTest.kt#L130)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
