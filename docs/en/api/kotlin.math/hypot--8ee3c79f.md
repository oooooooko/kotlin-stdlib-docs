# hypot

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Computes `sqrt(x^2 + y^2)` without intermediate overflow or underflow.

Special cases:
  - returns `+Inf` if any of arguments is infinite
  - returns `NaN` if any of arguments is `NaN` and the other is not infinite

@sample samples.math.MathSamples.Doubles.hypot

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun hypot(x: Double, y: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L193)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun hypot(x: Float, y: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L781)

Computes `sqrt(x^2 + y^2)` without intermediate overflow or underflow.

Special cases:
  - returns `+Inf` if any of arguments is infinite
  - returns `NaN` if any of arguments is `NaN` and the other is not infinite

@sample samples.math.MathSamples.Floats.hypot

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // sqrt(6 * 6 + 8 * 8) = sqrt(36 + 64) = sqrt(100) = 10
    println(hypot(6.0, 8.0))

    // special cases
    println(hypot(Double.NaN, 2.0))
    println(hypot(1.0, Double.NaN))
    println(hypot(Double.POSITIVE_INFINITY, 2.0))
    println(hypot(1.0, Double.NEGATIVE_INFINITY))
}
```

```text title="Output"
10.0
NaN
NaN
Infinity
Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L264)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // sqrt(6 * 6 + 8 * 8) = sqrt(36 + 64) = sqrt(100) = 10
    println(hypot(6.0f, 8.0f))

    // special cases
    println(hypot(Float.NaN, 2.0f))
    println(hypot(1.0f, Float.NaN))
    println(hypot(Float.POSITIVE_INFINITY, 2.0f))
    println(hypot(1.0f, Float.NEGATIVE_INFINITY))
}
```

```text title="Output"
10.0
NaN
NaN
Infinity
Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L859)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
