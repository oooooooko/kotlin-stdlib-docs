# unzip

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一对列表,其中 * 1* 列表从此序列中每对的首个值中构建, * 秒* 列表从此序列中每对的第二值中构建。

操作为 _flintinal_。

@sample 样本、采集资料、序列、变形、unzip

??? note "查看英文原文"

    Returns a pair of lists, where
    *first* list is built from the first values of each pair from this sequence,
    *second* list is built from the second values of each pair from this sequence.
    
    The operation is _terminal_.
    
    @sample samples.collections.Sequences.Transformations.unzip

## 声明与重载

### 1. Common

```kotlin
public fun <T, R> Sequence<Pair<T, R>>.unzip(): Pair<List<T>, List<R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L134)

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

        val seq = sequenceOf(1 to 'a', 2 to 'b', 3 to 'c')
        val (ints, chars) = seq.unzip()
        println(ints)
        println(chars)
    
}
```

```text title="输出"
[1, 2, 3]
[a, b, c]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/SequenceTest.kt#L630)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
