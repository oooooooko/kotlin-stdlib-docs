# Random.nextBytes

`kotlin.random` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Fills a subrange of the specified byte `array` starting from `fromIndex` inclusive and ending `toIndex` exclusive
with random bytes.

@return `array` with the subrange filled with random bytes.

@sample samples.random.Randoms.nextBytes

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
    public open fun nextBytes(array: ByteArray, fromIndex: Int = 0, toIndex: Int = array.size): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L217)

### 2. Common

```kotlin
@IgnorableReturnValue
    public open fun nextBytes(array: ByteArray): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L251)

Fills the specified byte `array` with random bytes and returns it.

@return `array` filled with random bytes.

@sample samples.random.Randoms.nextBytes

### 3. Common

```kotlin
public open fun nextBytes(size: Int): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L261)

Creates a byte array of the specified `size`, filled with random bytes.

@sample samples.random.Randoms.nextBytes

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val bytes = ByteArray(4)
    println(bytes.contentToString())

    Random.nextBytes(bytes, 1, 3)
    // second and third bytes are generated, rest unchanged
    println(bytes.contentToString())

    Random.nextBytes(bytes)
    // all bytes are newly generated
    println(bytes.contentToString())

    val newBytes = Random.nextBytes(5)
    // a new byte array filled with random values
    println(newBytes.contentToString())
}
```

```text title="Output"
[0, 0, 0, 0]
[0, 102, 112, 0]
[-89, -117, 83, 38]
[78, 26, 56, 123, 95]
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L65)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
