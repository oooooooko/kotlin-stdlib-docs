# floor

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Rounds the given value `x` to an integer towards negative infinity.

Special cases:
  - `floor(x)` is `x` where `x` is `NaN` or `+Inf` or `-Inf` or already a mathematical integer.

@return the largest double value that is smaller than or equal to the given value `x` and is a mathematical integer.

@sample samples.math.MathSamples.Doubles.floor
@sample samples.math.MathSamples.Doubles.roundingModes

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun floor(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L332)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun floor(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L920)

Rounds the given value `x` to an integer towards negative infinity.

Special cases:
  - `floor(x)` is `x` where `x` is `NaN` or `+Inf` or `-Inf` or already a mathematical integer.

@return the largest Float value that is smaller than or equal to the given value `x` and is a mathematical integer.

@sample samples.math.MathSamples.Floats.floor
@sample samples.math.MathSamples.Floats.roundingModes

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(floor(3.14159))
    println(floor(-1.1))
    // 10.0 is already an "integer", so no rounding will take place
    println(floor(10.0))
    // Special cases
    println(floor(Double.NaN))
    println(floor(Double.POSITIVE_INFINITY))
    println(floor(Double.NEGATIVE_INFINITY))
}
```

```text title="Output"
3.0
-2.0
10.0
NaN
Infinity
-Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L15)

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
    println(floor(3.14159f))
    println(floor(-1.1f))
    // 10.0 is already an "integer", so no rounding will take place
    println(floor(10.0f))
    // Special cases
    println(floor(Float.NaN))
    println(floor(Float.POSITIVE_INFINITY))
    println(floor(Float.NEGATIVE_INFINITY))
}
```

```text title="Output"
3.0
-2.0
10.0
NaN
Infinity
-Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L609)

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
