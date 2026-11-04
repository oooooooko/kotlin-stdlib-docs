# iterator

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Builds an `Iterator` lazily yielding values one by one.

If the consuming code stops using the iterator without `Iterator.hasNext` returning `false` first,
the remainder of the computation will not run at all.
In particular, it means that `finally` blocks may be left unexecuted:

```
val singleElementIterator = iterator {
    try {
        yield(1)
        // no code after the `yield(1)` line will be executed!
    } finally {
        println("This line will not run")
    }
}
// only get the first element, do not attempt evaluating the rest of them
if (singleElementIterator.hasNext()) {
    println(singleElementIterator.next())
}
```

@sample samples.collections.Sequences.Building.buildIterator
@sample samples.collections.Iterables.Building.iterable

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@Suppress("DEPRECATION")
public fun <T> iterator(@BuilderInference block: suspend SequenceScope<T>.() -> Unit): Iterator<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L45)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val iterable = Iterable {
        iterator {
            yield(42)
            yieldAll(1..5 step 2)
        }
    }
    val result = iterable.mapIndexed { index, value -> "$index: $value" }
    println(result)

    // can be iterated many times
    repeat(2) {
        val sum = iterable.sum()
        println(sum)
    }
}
```

```text title="Output"
[0: 42, 1: 1, 2: 3, 3: 5]
51
51
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L26)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
