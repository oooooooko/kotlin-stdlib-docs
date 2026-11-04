# expm1

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Computes `exp(x) - 1`.

This function can be implemented to produce more precise result for `x` near zero.

Special cases:
  - `expm1(NaN)` is `NaN`
  - `expm1(+Inf)` is `+Inf`
  - `expm1(-Inf)` is `-1.0`

@see `exp` function.
@see `ln1p` function.
@sample samples.math.MathSamples.Doubles.expm1

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun expm1(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L231)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun expm1(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L819)

Computes `exp(x) - 1`.

This function can be implemented to produce a more precise result for `x` near zero.

Special cases:
  - `expm1(NaN)` is `NaN`
  - `expm1(+Inf)` is `+Inf`
  - `expm1(-Inf)` is `-1.0`

@see `exp` function.
@see `ln1p` function.
@sample samples.math.MathSamples.Floats.expm1

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    fun Double.firstFiveDigits(): String = toString().substring(0, 7)

    println(expm1(1.0).firstFiveDigits())
    // While it does not really matter for relatively large x values (like 1.0),
    // the difference is getting more pronounced when x is getting closer to 0.0
    println(exp(1e-17) - 1.0)
    println(expm1(1e-17))

    // special cases
    println(expm1(Double.NaN))
    println(expm1(Double.POSITIVE_INFINITY))
    println(expm1(Double.NEGATIVE_INFINITY))
}
```

```text title="Output"
1.71828
0.0
1.0E-17
NaN
Infinity
-1.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L323)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    fun Float.firstFiveDigits(): String = toString().substring(0, 7)

    println(expm1(1.0f).firstFiveDigits())
    // While it does not really matter for relatively large x values (like 1.0),
    // the difference is getting more pronounced when x is getting closer to 0.0
    println(exp(1e-17f) - 1.0f)
    println(expm1(1e-17f))

    // special cases
    println(expm1(Float.NaN))
    println(expm1(Float.POSITIVE_INFINITY))
    println(expm1(Float.NEGATIVE_INFINITY))
}
```

```text title="Output"
1.71828
0.0
1.0E-17
NaN
Infinity
-1.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L918)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
