# Random.nextInt

`kotlin.random` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Gets the next random `Int` from the random number generator.

Generates an `Int` random value uniformly distributed between `Int.MIN_VALUE` and `Int.MAX_VALUE` (inclusive).

@sample samples.random.Randoms.nextInt

## Declarations and overloads

### 1. Common

```kotlin
public open fun nextInt(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L35)

### 2. Common

```kotlin
public open fun nextInt(until: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L44)

Gets the next random non-negative `Int` from the random number generator less than the specified `until` bound.

Generates an `Int` random value uniformly distributed between `0` (inclusive) and the specified `until` bound (exclusive).

@param until must be positive.

@throws IllegalArgumentException if `until` is negative or zero.

@sample samples.random.Randoms.nextIntFromUntil

### 3. Common

```kotlin
public open fun nextInt(from: Int, until: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L57)

Gets the next random `Int` from the random number generator in the specified range.

Generates an `Int` random value uniformly distributed between the specified `from` (inclusive) and `until` (exclusive) bounds.

@throws IllegalArgumentException if `from` is greater than or equal to `until`.

@sample samples.random.Randoms.nextIntFromUntil

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val randomInts = List(5) { Random.nextInt() }
    println(randomInts)
    val sortedRandomInts = randomInts.sorted()
    println(sortedRandomInts)
}
```

```text title="Output"
[-664942724, 1630502718, -985679184, 823598579, 151027799]
[-985679184, -664942724, 151027799, 823598579, 1630502718]
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L111)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val menu = listOf("Omelette", "Porridge", "Cereal", "Chicken", "Pizza", "Pasta")
    val forBreakfast = Random.nextInt(until = 3).let { menu[it] }
    val forLunch = Random.nextInt(from = 3, until = 6).let { menu[it] }
    // new meals every time
    println("Today I want $forBreakfast for breakfast, and $forLunch for lunch.")
}
```

```text title="Output"
Today I want Omelette for breakfast, and Pasta for lunch.
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L119)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
