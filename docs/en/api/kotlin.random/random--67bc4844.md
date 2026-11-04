# Random

`kotlin.random` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

An abstract class that is implemented by random number generator algorithms.

The companion object `Random.Default` is the default instance of `Random`.

To get a seeded instance of random generator use `Random` function.

@sample samples.random.Randoms.defaultRandom

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
public abstract class Random
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L12)

### 2. Common

```kotlin
@SinceKotlin("1.3")
public fun Random(seed: Int): Random
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L314)

Returns a repeatable random number generator seeded with the given `seed` `Int` value.

Two generators with the same seed produce the same sequence of values within the same version of Kotlin runtime.

*Note:* Future versions of Kotlin may change the algorithm of this seeded number generator so that it will return
a sequence of values different from the current one for a given seed.

On JVM the returned generator is NOT thread-safe. Do not invoke it from multiple threads without proper synchronization.

@sample samples.random.Randoms.seededRandom

### 3. Common

```kotlin
@SinceKotlin("1.3")
public fun Random(seed: Long): Random
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L329)

Returns a repeatable random number generator seeded with the given `seed` `Long` value.

Two generators with the same seed produce the same sequence of values within the same version of Kotlin runtime.

*Note:* Future versions of Kotlin may change the algorithm of this seeded number generator so that it will return
a sequence of values different from the current one for a given seed.

On JVM the returned generator is NOT thread-safe. Do not invoke it from multiple threads without proper synchronization.

@sample samples.random.Randoms.seededRandom

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val randomValues = List(10) { Random.nextInt(0, 100) }
    // prints new sequence every time
    println(randomValues)

    val nextValues = List(10) { Random.nextInt(0, 100) }
    println(nextValues)
    println(randomValues != nextValues)
}
```

```text title="Output"
[98, 80, 29, 18, 13, 1, 73, 6, 42, 78]
[98, 5, 35, 94, 26, 43, 42, 77, 37, 6]
true
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L14)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    fun getRandomList(random: Random): List<Int> =
        List(10) { random.nextInt(0, 100) }

    val randomValues1 = getRandomList(Random(42))
    // prints the same sequence every time
    println(randomValues1)

    val randomValues2 = getRandomList(Random(42))
    // random with the same seed produce the same sequence
    println(randomValues1 == randomValues2)

    val randomValues3 = getRandomList(Random(0))
    // random with another seed produce another sequence
    println(randomValues3)
}
```

```text title="Output"
[33, 40, 41, 2, 41, 32, 21, 40, 69, 87]
true
[14, 48, 57, 67, 82, 7, 61, 27, 14, 59]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L25)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
