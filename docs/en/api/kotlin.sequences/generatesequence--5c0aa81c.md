# generateSequence

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a sequence which invokes the function to calculate the next value on each iteration until the function returns `null`.

The returned sequence is constrained to be iterated only once.

@see constrainOnce
@see kotlin.sequences.sequence

@sample samples.collections.Sequences.Building.generateSequence

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Any> generateSequence(nextFunction: () -> T?): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L681)

### 2. Common

```kotlin
@kotlin.internal.LowPriorityInOverloadResolution
public fun <T : Any> generateSequence(seed: T?, nextFunction: (T) -> T?): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L695)

Returns a sequence defined by the starting value `seed` and the function `nextFunction`,
which is invoked to calculate the next value based on the previous one on each iteration.

The sequence produces values until it encounters first `null` value.
If `seed` is `null`, an empty sequence is produced.

The sequence can be iterated multiple times, each time starting with `seed`.

@see kotlin.sequences.sequence

@sample samples.collections.Sequences.Building.generateSequenceWithSeed

### 3. Common

```kotlin
public fun <T : Any> generateSequence(seedFunction: () -> T?, nextFunction: (T) -> T?): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L715)

Returns a sequence defined by the function `seedFunction`, which is invoked to produce the starting value,
and the `nextFunction`, which is invoked to calculate the next value based on the previous one on each iteration.

The sequence produces values until it encounters first `null` value.
If `seedFunction` returns `null`, an empty sequence is produced.

The sequence can be iterated multiple times.

@see kotlin.sequences.sequence

@sample samples.collections.Sequences.Building.generateSequenceWithLazySeed

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.stream.*
import kotlin.streams.*



fun main() {
    val evenNumbersSequence: Sequence<Int> = generateSequence(2, { it + 2 }).take(5)
    val evenNumberStream: Stream<Int> = evenNumbersSequence.asStream()
    println(evenNumberStream.toList())
}
```

```text title="Output"
[2, 4, 6, 8, 10]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/streams/streams.kt#L42)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
