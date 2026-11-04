# sqrt

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Computes the positive square root of the value `x`.

Special cases:
  - `sqrt(NaN)` is `NaN`
  - `sqrt(-0.0)` is `-0.0`
  - `sqrt(x)` is `NaN` when `x < 0`

@sample samples.math.MathSamples.Doubles.sqrt

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun sqrt(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L205)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun sqrt(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L793)

Computes the positive square root of the value `x`.

Special cases:
  - `sqrt(NaN)` is `NaN`
  - `sqrt(-0.0)` is `-0.0`
  - `sqrt(x)` is `NaN` when `x < 0`

@sample samples.math.MathSamples.Floats.sqrt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(sqrt(9.0))
    println(sqrt(5.76))
    // special cases
    println(sqrt(-0.0))
    println(sqrt(-4.0))
    println(sqrt(Double.NaN))
    println(sqrt(Double.POSITIVE_INFINITY))
}
```

```text title="Output"
3.0
2.4
-0.0
NaN
NaN
Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L253)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(sqrt(9.0f))
    println(sqrt(5.76f))

    // special cases
    println(sqrt(-0.0f))
    println(sqrt(-4.0f))
    println(sqrt(Float.NaN))
    println(sqrt(Float.POSITIVE_INFINITY))
}
```

```text title="Output"
3.0
2.4
-0.0
NaN
NaN
Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L847)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
