# absoluteValue

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the absolute value of this value.

Special cases:
  - `NaN.absoluteValue` is `NaN`

@see abs function
@sample samples.math.MathSamples.Doubles.absoluteValue

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect val Double.absoluteValue: Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L465)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect val Float.absoluteValue: Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1057)

Returns the absolute value of this value.

Special cases:
  - `NaN.absoluteValue` is `NaN`

@see abs function
@sample samples.math.MathSamples.Floats.absoluteValue

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect val Int.absoluteValue: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1165)

Returns the absolute value of this value.

Special cases:
  - `Int.MIN_VALUE.absoluteValue` is `Int.MIN_VALUE` due to an overflow

@see abs function
@sample samples.math.MathSamples.Ints.absoluteValue

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect val Long.absoluteValue: Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1218)

Returns the absolute value of this value.

Special cases:
  - `Long.MIN_VALUE.absoluteValue` is `Long.MIN_VALUE` due to an overflow

@see abs function
@sample samples.math.MathSamples.Longs.absoluteValue

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14.absoluteValue)
    println((-3.14).absoluteValue)
    println((-0.0).absoluteValue)
    println(Double.NEGATIVE_INFINITY.absoluteValue)
    println(Double.NaN.absoluteValue)
}
```

```text title="Output"
3.14
3.14
0.0
Infinity
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L214)

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
    println(42.absoluteValue)
    println((-42).absoluteValue)
    // Special case: can't get the absolute value due to an overflow
    println(Int.MIN_VALUE.absoluteValue == Int.MIN_VALUE)
}
```

```text title="Output"
42
42
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1253)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(42L.absoluteValue)
    println((-42L).absoluteValue)
    // Special case: can't get the absolute value due to an overflow
    println(Long.MIN_VALUE.absoluteValue == Long.MIN_VALUE)
}
```

```text title="Output"
42
42
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1212)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
