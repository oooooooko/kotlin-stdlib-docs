# Random.nextDouble

`kotlin.random` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Gets the next random `Double` value uniformly distributed between 0 (inclusive) and 1 (exclusive).

@sample samples.random.Randoms.nextDouble

## Declarations and overloads

### 1. Common

```kotlin
public open fun nextDouble(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L167)

### 2. Common

```kotlin
public open fun nextDouble(until: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L174)

Gets the next random non-negative `Double` from the random number generator less than the specified `until` bound.

Generates a `Double` random value uniformly distributed between 0 (inclusive) and `until` (exclusive).

`until` must be a fininte number otherwise the behavior is unspecified.

@throws IllegalArgumentException if `until` is negative or zero.

@sample samples.random.Randoms.nextDoubleFromUntil

### 3. Common

```kotlin
public open fun nextDouble(from: Double, until: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L187)

Gets the next random `Double` from the random number generator in the specified range.

Generates a `Double` random value uniformly distributed between the specified `from` (inclusive) and `until` (exclusive) bounds.

`from` and `until` must be finite numbers otherwise the behavior is unspecified.

@throws IllegalArgumentException if `from` is greater than or equal to `until`.

@sample samples.random.Randoms.nextDoubleFromUntil

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    if (Random.nextDouble() <= 0.3) {
        println("There was 30% possibility of rainy weather today and it is raining.")
    } else {
        println("There was 70% possibility of sunny weather today and the sun is shining.")
    }
}
```

```text title="Output"
There was 30% possibility of rainy weather today and it is raining.
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L83)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val firstAngle = Random.nextDouble(until = Math.PI / 6);
    println(sin(firstAngle) < 0.5)

    val secondAngle = Random.nextDouble(from = Math.PI / 6, until = Math.PI / 2)
    val sinValue = sin(secondAngle)
    println(sinValue >= 0.5 && sinValue < 1.0)
}
```

```text title="Output"
true
true
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L92)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
