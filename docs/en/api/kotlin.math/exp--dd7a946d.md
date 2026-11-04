# exp

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Computes Euler's number `e` raised to the power of the value `x`.

Special cases:
  - `exp(NaN)` is `NaN`
  - `exp(+Inf)` is `+Inf`
  - `exp(-Inf)` is `0.0`

@sample samples.math.MathSamples.Doubles.exp

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun exp(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L218)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun exp(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L806)

Computes Euler's number `e` raised to the power of the value `x`.

Special cases:
  - `exp(NaN)` is `NaN`
  - `exp(+Inf)` is `+Inf`
  - `exp(-Inf)` is `0.0`

@sample samples.math.MathSamples.Floats.exp

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    fun Double.firstFiveDigits(): String = toString().substring(0, 7)

    println(exp(1.0).firstFiveDigits())
    println(exp(2.0).firstFiveDigits())
    println(exp(-1.0).firstFiveDigits())

    // special cases
    println(exp(Double.NaN))
    println(exp(Double.POSITIVE_INFINITY))
    println(exp(Double.NEGATIVE_INFINITY))
}
```

```text title="Output"
2.71828
7.38905
0.36787
NaN
Infinity
0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L309)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    fun Float.firstFiveDigits(): String = toString().substring(0, 7)

    println(exp(1.0f).firstFiveDigits())
    println(exp(2.0f).firstFiveDigits())
    println(exp(-1.0f).firstFiveDigits())

    // special cases
    println(exp(Float.NaN))
    println(exp(Float.POSITIVE_INFINITY))
    println(exp(Float.NEGATIVE_INFINITY))
}
```

```text title="Output"
2.71828
7.38905
0.36787
NaN
Infinity
0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L904)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
