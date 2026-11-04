# acos

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Computes the arc cosine of the value `x`;
the returned value is an angle in the range from `0.0` to `PI` radians.

Special cases:
  - `acos(x)` is `NaN`, when `abs(x) > 1` or x is `NaN`

@sample samples.math.MathSamples.Doubles.acos

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun acos(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L70)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun acos(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L658)

Computes the arc cosine of the value `x`;
the returned value is an angle in the range from `0.0` to `PI` radians.

Special cases:
  - `acos(x)` is `NaN`, when `abs(x) > 1` or x is `NaN`

@sample samples.math.MathSamples.Floats.acos

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-10

    println(acos(1.0))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // acos(0.0) = π/2
    println((acos(0.0) - PI / 2).absoluteValue < epsilon)
    // acos(-1.0) = π
    println((acos(-1.0) - PI).absoluteValue < epsilon)
    // acos(cos(x)) = x
    println((acos(cos(0.123)) - 0.123).absoluteValue < epsilon)

    // special cases
    println(acos(Double.NaN))
    println(acos(1.1))
    println(acos(-2.0))
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L408)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-6f

    println(acos(1.0f))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // acos(0.0) = π/2
    println((acos(0.0f) - PI.toFloat() / 2).absoluteValue < epsilon)
    // acos(-1.0) = π
    println((acos(-1.0f) - PI.toFloat()).absoluteValue < epsilon)
    // acos(cos(x)) = x
    println((acos(cos(0.25f)) - 0.25f).absoluteValue < epsilon)

    // special cases
    println(acos(Float.NaN))
    println(acos(1.1f))
    println(acos(-2.0f))
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

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1003)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
