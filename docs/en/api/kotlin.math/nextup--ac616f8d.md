# nextUp

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the `Double` value nearest to this value in a direction of positive infinity.

Special cases:
  - `NaN.nextUp() is `NaN`
  - `Double.POSITIVE_INFINITY.nextUp() is `+Infinity`
  - `0.0.nextUp()` is `Double.MIN_VALUE`

@see nextTowards
@see nextDown
@see ulp
@sample samples.math.MathSamples.Doubles.nextUp
@sample samples.math.MathSamples.Doubles.discreteValues

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.nextUp(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L529)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // Floating point numbers have discrete representation,
    // so depending on the value's magnitude, the step towards
    // the next representable value will be different
    println(10000.0.nextUp())
    println(100000.0.nextUp())

    // -Infinity is any value large enough to no longer fit Double,
    // so the next value after it towards 0.0 is -Double.MAX_VALUE
    println(Double.NEGATIVE_INFINITY.nextUp() == -Double.MAX_VALUE)

    // For 0.0, the next value is the Double.MIN_VALUE, the smallest representable Double value
    println(0.0.nextUp() == Double.MIN_VALUE)

    // special cases
    println(Double.NaN.nextUp())
    println(Double.POSITIVE_INFINITY.nextUp())
}
```

```text title="Output"
10000.000000000002
100000.00000000001
true
true
NaN
Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L530)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // Unlike true real numbers, Double can only represent a fixed set of discrete values.
    // According to IEEE-754, Double uses a single bit for a sign, 11 bits for the exponent, and 52 for the fraction.
    // The bigger the integer part of the floating point value, the less space remains for "fitting" fractional part.
    // As a result, starting from 2⁵² and until 2⁵³-1 Double values are incremented by 1.0
    // (meaning that there are no in-between values), values from 2⁵³ until 2⁵⁴-1 are incremented by 2.0,
    // but values in between 2⁵¹ and 2⁵²-1 are incremented by 0.5.
    //
    // The "distance" between a current value and the next one (the "increment" mentioned above) is dynamic,
    // it depends on the magnitude of the current value, and it could be checked using Double.ulp.
    val v2_52_53 = 4503599627370498.0 // value in range [2⁵², 2⁵³-1]
    println(v2_52_53.ulp)

    val v2_53_54 = 9007199254740998.0 // value in range [2⁵³, 2⁵⁴-1]
    println(v2_53_54.ulp)

    val v2_51_52 = 4503599627370490.0 // value in range [2⁵¹, 2⁵²-1]
    println(v2_51_52.ulp)

    // Instead of using ulp, you can also check the next and previous values representable with a Double
    // using Double.nextUp and Double.nextDown correspondingly.
    println(9007199254740998.0.nextUp() - 9007199254740998.0)
    println(9007199254740998.0 - 9007199254740998.0.nextDown())

    // As a more flexible alternative to nextUp/nextDown, one may use nextTowards, which accepts a value
    // that works as a direction to increase/decrease a given value towards.
    println(4503599627370496.0.nextTowards(Double.POSITIVE_INFINITY) - 4503599627370496.0)
    println(4503599627370496.0 - 4503599627370496.0.nextTowards(Double.NEGATIVE_INFINITY))
}
```

```text title="Output"
1.0
2.0
0.5
2.0
2.0
1.0
0.5
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L499)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
