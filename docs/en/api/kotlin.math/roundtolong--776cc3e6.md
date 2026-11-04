# roundToLong

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Rounds this `Double` value to the nearest integer and converts the result to `Long`.
Ties are rounded towards positive infinity.

Special cases:
  - `x.roundToLong() == Long.MAX_VALUE` when `x > Long.MAX_VALUE`
  - `x.roundToLong() == Long.MIN_VALUE` when `x < Long.MIN_VALUE`

@throws IllegalArgumentException when this value is `NaN`
@sample samples.math.MathSamples.Doubles.roundToLong

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.roundToLong(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L593)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.roundToLong(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1117)

Rounds this `Float` value to the nearest integer and converts the result to `Long`.
Ties are rounded towards positive infinity.

Special cases:
  - `x.roundToLong() == Long.MAX_VALUE` when `x > Long.MAX_VALUE`
  - `x.roundToLong() == Long.MIN_VALUE` when `x < Long.MIN_VALUE`

@throws IllegalArgumentException when this value is `NaN`
@sample samples.math.MathSamples.Floats.roundToLong

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    println(3.14159.roundToLong())
    println((-10.0).roundToLong())
    // Values greater than Long.MAX_VALUE are rounded to Long.MAX_VALUE
    println((Long.MAX_VALUE.toDouble() * 2.0).roundToLong() == Long.MAX_VALUE)
    println(Double.POSITIVE_INFINITY.roundToLong() == Long.MAX_VALUE)
    // Values smaller than Long.MIN_VALUE are rounded to Long.MIN_VALUE
    println((Long.MIN_VALUE.toDouble() * 2.0).roundToLong() == Long.MIN_VALUE)
    println(Double.NEGATIVE_INFINITY.roundToLong() == Long.MIN_VALUE)
    // NaN could not be rounded to Long
    assertFailsWith<IllegalArgumentException> { Double.NaN.roundToLong() }
}
```

```text title="Output"
3
-10
true
true
true
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L96)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    println(3.14159f.roundToLong())
    println((-10.0f).roundToLong())
    // Values greater than Long.MAX_VALUE are rounded to Long.MAX_VALUE
    println((Long.MAX_VALUE.toFloat() * 2.0f).roundToLong() == Long.MAX_VALUE)
    println(Float.POSITIVE_INFINITY.roundToLong() == Long.MAX_VALUE)
    // Values smaller than Long.MIN_VALUE are rounded to Long.MIN_VALUE
    println((Long.MIN_VALUE.toFloat() * 2.0f).roundToLong() == Long.MIN_VALUE)
    println(Float.NEGATIVE_INFINITY.roundToLong() == Long.MIN_VALUE)
    // NaN could not be rounded to Long
    assertFailsWith<IllegalArgumentException> { Float.NaN.roundToLong() }
}
```

```text title="Output"
3
-10
true
true
true
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L690)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
