# foldIndexed

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with `initial` value and applying `operation` from left to right
to current accumulator value and each element with its index in the original sequence.

Returns the specified `initial` value if the sequence is empty.

@param `operation` function that takes the index of an element, current accumulator value
and the element itself, and calculates the next accumulator value.

The operation is _terminal_.

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, R> Sequence<T>.foldIndexed(initial: R, operation: (index: Int, acc: R, T) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1620)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
true
0
0
7
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/SequenceTest.kt#L130)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
