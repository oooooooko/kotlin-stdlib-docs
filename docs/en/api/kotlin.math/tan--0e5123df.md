# tan

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Computes the tangent of the angle `x` given in radians.

Special cases:
 - `tan(NaN|+Inf|-Inf)` is `NaN`

@sample samples.math.MathSamples.Doubles.tan

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun tan(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L47)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun tan(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L635)

Computes the tangent of the angle `x` given in radians.

Special cases:
 - `tan(NaN|+Inf|-Inf)` is `NaN`

@sample samples.math.MathSamples.Floats.tan

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-10

    println(tan(0.0))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // tan(π/4) = 1.0
    println((tan(PI / 4) - 1.0).absoluteValue < epsilon)
    // tan(-π/4) = -1.0
    println((tan(-PI / 4) - -1.0).absoluteValue < epsilon)

    // special cases
    println(tan(Double.NaN))
    println(tan(Double.POSITIVE_INFINITY))
    println(tan(Double.NEGATIVE_INFINITY))
}
```

```text title="Output"
0.0
true
true
NaN
NaN
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L372)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-6f

    println(tan(0.0f))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // tan(π/4) = 1.0
    println((tan(PI.toFloat() / 4) - 1.0f).absoluteValue < epsilon)
    // tan(-π/4) = -1.0
    println((tan(-PI.toFloat() / 4) - -1.0f).absoluteValue < epsilon)

    // special cases
    println(tan(Float.NaN))
    println(tan(Float.POSITIVE_INFINITY))
    println(tan(Float.NEGATIVE_INFINITY))
}
```

```text title="Output"
0.0
true
true
NaN
NaN
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L967)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
