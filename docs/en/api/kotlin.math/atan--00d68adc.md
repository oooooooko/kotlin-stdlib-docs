# atan

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Computes the arc tangent of the value `x`;
the returned value is an angle in the range from `-PI/2` to `PI/2` radians.

Special cases:
  - `atan(NaN)` is `NaN`

@sample samples.math.MathSamples.Doubles.atan

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun atan(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L82)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun atan(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L670)

Computes the arc tangent of the value `x`;
the returned value is an angle in the range from `-PI/2` to `PI/2` radians.

Special cases:
  - `atan(NaN)` is `NaN`

@sample samples.math.MathSamples.Floats.atan

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-10

    println(atan(0.0))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // atan(1.0) = π/4
    println((atan(1.0) - PI / 4).absoluteValue < epsilon)
    // atan(-1.0) = -π/4
    println((atan(-1.0) - (-PI / 4)).absoluteValue < epsilon)
    // atan(tan(x)) = x
    println((atan(tan(0.123)) - 0.123).absoluteValue < epsilon)

    // special cases
    println(atan(Double.NaN))
}
```

```text title="Output"
0.0
true
true
true
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L427)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-6f

    println(atan(0.0f))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // atan(1.0) = π/4
    println((atan(1.0f) - PI.toFloat() / 4).absoluteValue < epsilon)
    // atan(-1.0) = -π/4
    println((atan(-1.0f) - (-PI.toFloat() / 4)).absoluteValue < epsilon)
    // atan(tan(x)) = x
    println((atan(tan(0.25f)) - 0.25f).absoluteValue < epsilon)

    // special cases
    println(atan(Float.NaN))
}
```

```text title="Output"
0.0
true
true
true
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1022)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
