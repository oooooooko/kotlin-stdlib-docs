# flatten

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a sequence of all elements from all sequences in this sequence.

The operation is _intermediate_ and _stateless_.

@sample samples.collections.Sequences.Transformations.flattenSequenceOfSequences

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Sequence<Sequence<T>>.flatten(): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L108)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("flattenSequenceOfIterable")
public fun <T> Sequence<Iterable<T>>.flatten(): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L117)

Returns a sequence of all elements from all iterables in this sequence.

The operation is _intermediate_ and _stateless_.

@sample samples.collections.Sequences.Transformations.flattenSequenceOfLists

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

```text title="Output"
[0, 1, 0, 1, 2]
[0, 1, 0, 1, 2]
[0, 1, 0, 1, 2]
[0, 1, 0, 1, 2]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/SequenceTest.kt#L604)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
