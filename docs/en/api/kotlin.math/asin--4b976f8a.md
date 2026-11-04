# asin

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Computes the arc sine of the value `x`;
the returned value is an angle in the range from `-PI/2` to `PI/2` radians.

Special cases:
  - `asin(x)` is `NaN`, when `abs(x) > 1` or x is `NaN`

@sample samples.math.MathSamples.Doubles.asin

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun asin(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L58)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun asin(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L646)

Computes the arc sine of the value `x`;
the returned value is an angle in the range from `-PI/2` to `PI/2` radians.

Special cases:
  - `asin(x)` is `NaN`, when `abs(x) > 1` or x is `NaN`

@sample samples.math.MathSamples.Floats.asin

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-10

    println(asin(0.0))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // asin(1.0) = π/2
    println((asin(1.0) - PI / 2).absoluteValue < epsilon)
    // asin(-1.0) = -π/2
    println((asin(-1.0) - (-PI / 2)).absoluteValue < epsilon)
    // asin(sin(x)) = x
    println((asin(sin(0.123)) - 0.123).absoluteValue < epsilon)

    // special cases
    println(asin(Double.NaN))
    println(asin(1.1))
    println(asin(-2.0))
}
```

```text title="Output"
0.0
true
true
true
NaN
NaN
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L389)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-6f

    println(asin(0.0f))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // asin(1.0) = π/2
    println((asin(1.0f) - PI.toFloat() / 2).absoluteValue < epsilon)
    // asin(-1.0) = -π/2
    println((asin(-1.0f) - (-PI.toFloat() / 2)).absoluteValue < epsilon)
    // asin(sin(x)) = x
    println((asin(sin(0.25f)) - 0.25f).absoluteValue < epsilon)

    // special cases
    println(asin(Float.NaN))
    println(asin(1.1f))
    println(asin(-2.0f))
}
```

```text title="Output"
0.0
true
true
true
NaN
NaN
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L984)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
