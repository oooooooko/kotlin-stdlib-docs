# abs

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the absolute value of the given value `x`.

Special cases:
  - `abs(NaN)` is `NaN`

@see absoluteValue extension property for `Double`
@sample samples.math.MathSamples.Doubles.abs

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun abs(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L372)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun abs(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L961)

Returns the absolute value of the given value `x`.

Special cases:
  - `abs(NaN)` is `NaN`

@see absoluteValue extension property for `Float`
@sample samples.math.MathSamples.Floats.absoluteValue

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun abs(n: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1137)

Returns the absolute value of the given value `n`.

Special cases:
  - `abs(Int.MIN_VALUE)` is `Int.MIN_VALUE` due to an overflow

@see absoluteValue extension property for `Int`
@sample samples.math.MathSamples.Ints.abs

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun abs(n: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1190)

Returns the absolute value of the given value `n`.

Special cases:
  - `abs(Long.MIN_VALUE)` is `Long.MIN_VALUE` due to an overflow

@see absoluteValue extension property for `Long`
@sample samples.math.MathSamples.Longs.abs

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(abs(3.14))
    println(abs(-3.14))
    println(abs(-0.0))
    println(abs(Double.NEGATIVE_INFINITY))
    println(abs(Double.NaN))
}
```

```text title="Output"
3.14
3.14
0.0
Infinity
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L205)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14f.absoluteValue)
    println((-3.14f).absoluteValue)
    println((-0.0f).absoluteValue)
    println(Float.NEGATIVE_INFINITY.absoluteValue)
    println(Float.NaN.absoluteValue)
}
```

```text title="Output"
3.14
3.14
0.0
Infinity
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L808)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(abs(42))
    println(abs(-42))
    // Special case: can't get the absolute value due to an overflow
    println(abs(Int.MIN_VALUE) == Int.MIN_VALUE)
}
```

```text title="Output"
42
42
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1245)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(abs(42L))
    println(abs(-42L))
    // Special case: can't get the absolute value due to an overflow
    println(abs(Long.MIN_VALUE) == Long.MIN_VALUE)
}
```

```text title="Output"
42
42
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1204)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
