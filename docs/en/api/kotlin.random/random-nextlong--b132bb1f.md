# Random.nextLong

`kotlin.random` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Gets the next random `Long` from the random number generator.

Generates a `Long` random value uniformly distributed between `Long.MIN_VALUE` and `Long.MAX_VALUE` (inclusive).

@sample samples.random.Randoms.nextLong

## Declarations and overloads

### 1. Common

```kotlin
public open fun nextLong(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L90)

### 2. Common

```kotlin
public open fun nextLong(until: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L99)

Gets the next random non-negative `Long` from the random number generator less than the specified `until` bound.

Generates a `Long` random value uniformly distributed between `0` (inclusive) and the specified `until` bound (exclusive).

@param until must be positive.

@throws IllegalArgumentException if `until` is negative or zero.

@sample samples.random.Randoms.nextLongFromUntil

### 3. Common

```kotlin
public open fun nextLong(from: Long, until: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L112)

Gets the next random `Long` from the random number generator in the specified range.

Generates a `Long` random value uniformly distributed between the specified `from` (inclusive) and `until` (exclusive) bounds.

@throws IllegalArgumentException if `from` is greater than or equal to `until`.

@sample samples.random.Randoms.nextLongFromUntil

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val randomLongs = List(5) { Random.nextLong() }
    println(randomLongs)
    val sortedRandomLongs = randomLongs.sorted()
    println(sortedRandomLongs)
}
```

```text title="Output"
[2794585803082347552, -970640935169720525, -8649369868795669496, -718227385778462985, -2108943675280592755]
[-8649369868795669496, -2108943675280592755, -970640935169720525, -718227385778462985, 2794585803082347552]
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L128)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val fileSize = Random.nextLong(until = 1_099_511_627_776)
    println("A file of $fileSize bytes fits on a 1TB storage.")
    val long = Random.nextLong(Int.MAX_VALUE + 1L, Long.MAX_VALUE)
    println("Number $long doesn't fit in an Int.")
}
```

```text title="Output"
A file of 588943339707 bytes fits on a 1TB storage.
Number 1434451857117903338 doesn't fit in an Int.
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L136)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
