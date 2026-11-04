# pow

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Raises this value to the power `x`.

Special cases:
  - `b.pow(0.0)` is `1.0`
  - `b.pow(1.0) == b`
  - `b.pow(NaN)` is `NaN`
  - `NaN.pow(x)` is `NaN` for `x != 0.0`
  - `b.pow(Inf)` is `NaN` for `abs(b) == 1.0`
  - `b.pow(x)` is `NaN` for `b < 0` and `x` is finite and not an integer

@sample samples.math.MathSamples.Doubles.powDouble

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.pow(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L439)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.pow(n: Int): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L455)

Raises this value to the integer power `n`.

See the other overload of `pow` for details.

@sample samples.math.MathSamples.Doubles.powInt

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.pow(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1031)

Raises this value to the power `x`.

Special cases:
  - `b.pow(0.0)` is `1.0`
  - `b.pow(1.0) == b`
  - `b.pow(NaN)` is `NaN`
  - `NaN.pow(x)` is `NaN` for `x != 0.0`
  - `b.pow(Inf)` is `NaN` for `abs(b) == 1.0`
  - `b.pow(x)` is `NaN` for `b < 0` and `x` is finite and not an integer

@sample samples.math.MathSamples.Floats.powFloat

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.pow(n: Int): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1047)

Raises this value to the integer power `n`.

See the other overload of `pow` for details.

@sample samples.math.MathSamples.Floats.powInt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(2.0.pow(2.0))
    println(3.0.pow(1.0))
    println(4.0.pow(0.0))
    println(2.0.pow(-2.0))
    println(4.0.pow(0.5))
    println((-2.0).pow(2.0))

    // special cases
    println(Double.NaN.pow(42.0))
    println(Double.NaN.pow(0.0))
    println(3.0.pow(Double.NaN))
    println((-2.0).pow(0.75))
    println(1.0.pow(Double.POSITIVE_INFINITY))
    println(1.0.pow(Double.NEGATIVE_INFINITY))
    println(2.0.pow(Double.POSITIVE_INFINITY))
    println(2.0.pow(Double.NEGATIVE_INFINITY))
}
```

```text title="Output"
4.0
3.0
1.0
0.25
2.0
4.0
NaN
1.0
NaN
NaN
NaN
NaN
Infinity
0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L276)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(2.0.pow(2))
    println(3.0.pow(1))
    println(4.0.pow(0))
    println(2.0.pow(-2))
    println((-2.0).pow(2))

    // special cases
    println(Double.NaN.pow(42))
    println(Double.NaN.pow(0))
}
```

```text title="Output"
4.0
3.0
1.0
0.25
4.0
NaN
1.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L296)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(2.0f.pow(2.0f))
    println(3.0f.pow(1.0f))
    println(4.0f.pow(0.0f))
    println(2.0f.pow(-2.0f))
    println(4.0f.pow(0.5f))
    println((-2.0f).pow(2.0f))

    // special cases
    println(Float.NaN.pow(42.0f))
    println(Float.NaN.pow(0.0f))
    println(3.0f.pow(Float.NaN))
    println((-2.0f).pow(0.75f))
    println(1.0f.pow(Float.POSITIVE_INFINITY))
    println(1.0f.pow(Float.NEGATIVE_INFINITY))
    println(2.0f.pow(Float.POSITIVE_INFINITY))
    println(2.0f.pow(Float.NEGATIVE_INFINITY))
}
```

```text title="Output"
4.0
3.0
1.0
0.25
2.0
4.0
NaN
1.0
NaN
NaN
NaN
NaN
Infinity
0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L871)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(2.0f.pow(2))
    println(3.0f.pow(1))
    println(4.0f.pow(0))
    println(2.0f.pow(-2))
    println((-2.0f).pow(2))

    // special cases
    println(Float.NaN.pow(42))
    println(Float.NaN.pow(0))
}
```

```text title="Output"
4.0
3.0
1.0
0.25
4.0
NaN
1.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L891)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
