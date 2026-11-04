# ceil

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Rounds the given value `x` to an integer towards positive infinity.

Special cases:
  - `ceil(x)` is `x` where `x` is `NaN` or `+Inf` or `-Inf` or already a mathematical integer.

@return the smallest double value that is greater than or equal to the given value `x` and is a mathematical integer.

@sample samples.math.MathSamples.Doubles.ceil
@sample samples.math.MathSamples.Doubles.roundingModes

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun ceil(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L318)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun ceil(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L906)

Rounds the given value `x` to an integer towards positive infinity.

Special cases:
  - `ceil(x)` is `x` where `x` is `NaN` or `+Inf` or `-Inf` or already a mathematical integer.

@return the smallest Float value that is greater than or equal to the given value `x` and is a mathematical integer.

@sample samples.math.MathSamples.Floats.ceil
@sample samples.math.MathSamples.Floats.roundingModes

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(ceil(3.14159))
    println(ceil(-1.1))
    // 10.0 is already an "integer", so no rounding will take place
    println(ceil(10.0))
    // Special cases
    println(ceil(Double.NaN))
    println(ceil(Double.POSITIVE_INFINITY))
    println(ceil(Double.NEGATIVE_INFINITY))
}
```

```text title="Output"
4.0
-1.0
10.0
NaN
Infinity
-Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L27)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(floor(3.5))
    println(ceil(3.5))
    println(truncate(3.5))
    println(round(3.5))
    println(round(3.49))

    println(floor(-3.5))
    println(ceil(-3.5))
    println(truncate(-3.5))
    println(round(-3.5))
    println(round(-3.49))
}
```

```text title="Output"
3.0
4.0
3.0
4.0
3.0
-4.0
-3.0
-3.0
-4.0
-3.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L67)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(ceil(3.14159f))
    println(ceil(-1.1f))
    // 10.0 is already an "integer", so no rounding will take place
    println(ceil(10.0f))
    // Special cases
    println(ceil(Float.NaN))
    println(ceil(Float.POSITIVE_INFINITY))
    println(ceil(Float.NEGATIVE_INFINITY))
}
```

```text title="Output"
4.0
-1.0
10.0
NaN
Infinity
-Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L621)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(floor(3.5f))
    println(ceil(3.5f))
    println(truncate(3.5f))
    println(round(3.5f))
    println(round(3.49f))

    println(floor(-3.5f))
    println(ceil(-3.5f))
    println(truncate(-3.5f))
    println(round(-3.5f))
    println(round(-3.49f))
}
```

```text title="Output"
3.0
4.0
3.0
4.0
3.0
-4.0
-3.0
-3.0
-4.0
-3.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L661)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
