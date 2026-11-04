# roundToInt

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Rounds this `Double` value to the nearest integer and converts the result to `Int`.
Ties are rounded towards positive infinity.

Special cases:
  - `x.roundToInt() == Int.MAX_VALUE` when `x > Int.MAX_VALUE`
  - `x.roundToInt() == Int.MIN_VALUE` when `x < Int.MIN_VALUE`

@throws IllegalArgumentException when this value is `NaN`
@sample samples.math.MathSamples.Doubles.roundToInt

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.roundToInt(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L579)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.roundToInt(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1103)

Rounds this `Float` value to the nearest integer and converts the result to `Int`.
Ties are rounded towards positive infinity.

Special cases:
  - `x.roundToInt() == Int.MAX_VALUE` when `x > Int.MAX_VALUE`
  - `x.roundToInt() == Int.MIN_VALUE` when `x < Int.MIN_VALUE`

@throws IllegalArgumentException when this value is `NaN`
@sample samples.math.MathSamples.Floats.roundToInt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    println(3.14159.roundToInt())
    println((-10.0).roundToInt())
    // Values greater than Int.MAX_VALUE are rounded to Int.MAX_VALUE
    println((Int.MAX_VALUE.toDouble() + 1.0).roundToInt() == Int.MAX_VALUE)
    println(Double.POSITIVE_INFINITY.roundToInt() == Int.MAX_VALUE)
    // Values smaller than Int.MIN_VALUE are rounded to Int.MIN_VALUE
    println((Int.MIN_VALUE.toDouble() - 1.0).roundToInt() == Int.MIN_VALUE)
    println(Double.NEGATIVE_INFINITY.roundToInt() == Int.MIN_VALUE)
    // NaN could not be rounded to Int
    assertFailsWith<IllegalArgumentException> { Double.NaN.roundToInt() }
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L82)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    println(3.14159f.roundToInt())
    println((-10.0f).roundToInt())
    // Values greater than Int.MAX_VALUE are rounded to Int.MAX_VALUE
    println((Int.MAX_VALUE.toFloat() * 2.0f).roundToInt() == Int.MAX_VALUE)
    println(Float.POSITIVE_INFINITY.roundToInt() == Int.MAX_VALUE)
    // Values smaller than Int.MIN_VALUE are rounded to Int.MIN_VALUE
    println((Int.MIN_VALUE.toFloat() * 2.0f).roundToInt() == Int.MIN_VALUE)
    println(Float.NEGATIVE_INFINITY.roundToInt() == Int.MIN_VALUE)
    // NaN could not be rounded to Int
    assertFailsWith<IllegalArgumentException> { Float.NaN.roundToInt() }
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L676)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
