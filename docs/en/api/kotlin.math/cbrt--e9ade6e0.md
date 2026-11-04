# cbrt

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the cube root of `x`. For any `x`, `cbrt(-x) == -cbrt(x)`;
that is, the cube root of a negative value is the negative of the cube root
of that value's magnitude.

Special cases:
  - If the argument is `NaN`, then the result is `NaN`.
  - If the argument is infinite, then the result is an infinity with the same sign as the argument.
  - If the argument is zero, then the result is a zero with the same sign as the argument.

@sample samples.math.MathSamples.Doubles.cbrt

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.8")
public expect fun cbrt(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L421)

### 2. Common

```kotlin
@SinceKotlin("1.8")
@WasExperimental(ExperimentalStdlibApi::class)
public expect fun cbrt(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1011)

Returns the cube root of `x`. For any `x`, `cbrt(-x) == -cbrt(x)`;
that is, the cube root of a negative value is the negative of the cube root
of that value's magnitude.

Special cases:
  - If the argument is `NaN`, then the result is `NaN`.
  - If the argument is infinite, then the result is an infinity with the same sign as the argument.
  - If the argument is zero, then the result is a zero with the same sign as the argument.

@sample samples.math.MathSamples.Floats.cbrt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(cbrt(8.0))
    println(cbrt(-8.0))

    // special cases
    println(cbrt(Double.NaN))
    println(cbrt(Double.POSITIVE_INFINITY))
    println(cbrt(Double.NEGATIVE_INFINITY))
    println(cbrt(-0.0))
}
```

```text title="Output"
2.0
-2.0
NaN
Infinity
-Infinity
-0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L241)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(cbrt(8.0f))
    println(cbrt(-8.0f))

    // special cases
    println(cbrt(Float.NaN))
    println(cbrt(Float.POSITIVE_INFINITY))
    println(cbrt(Float.NEGATIVE_INFINITY))
    println(cbrt(-0.0f))
}
```

```text title="Output"
2.0
-2.0
NaN
Infinity
-Infinity
-0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L835)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
