# Random.nextBits

`kotlin.random` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Gets the next random `bitCount` number of bits.

Generates an `Int` whose lower `bitCount` bits are filled with random values and the remaining upper bits are zero.

@param bitCount number of bits to generate, must be in range 0..32, otherwise the behavior is unspecified.

@sample samples.random.Randoms.nextBits

## Declarations and overloads

### 1. Common

```kotlin
public abstract fun nextBits(bitCount: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L24)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    // always generates a 0
    println(Random.nextBits(0))
    // randomly generates a 0 or 1
    println(Random.nextBits(1))
    // generates a random non-negative Int value less than 256
    println(Random.nextBits(8))
    // generates a random Int value, may generate a negative value as well
    println(Random.nextBits(32))
}
```

```text title="Output"
0
1
24
-1960694883
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L43)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
