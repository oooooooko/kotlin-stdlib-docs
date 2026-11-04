# Random.nextBoolean

`kotlin.random` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Gets the next random `Boolean` value.

@sample samples.random.Randoms.nextBoolean

## Declarations and overloads

### 1. Common

```kotlin
public open fun nextBoolean(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L160)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val presents = listOf("Candy", "Balloon", "Ball")
    // a random partition, the result may be different every time
    val (alicePresents, bobPresents) = presents.partition { Random.nextBoolean() }

    println("Alice receives $alicePresents")
    println("Bob receives $bobPresents")
}
```

```text title="Output"
Alice receives [Candy, Ball]
Bob receives [Balloon]
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L55)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
