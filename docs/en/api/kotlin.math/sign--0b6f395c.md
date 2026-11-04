# sign

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the sign of the given value `x`:
  - `-1.0` if the value is negative,
  - zero if the value is zero,
  - `1.0` if the value is positive

Special cases:
  - `sign(NaN)` is `NaN`
  - `sign(-0.0)` is `-0.0`

@sample samples.math.MathSamples.Doubles.signFun

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun sign(x: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L384)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect val Double.sign: Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L477)

Returns the sign of this value:
  - `-1.0` if the value is negative,
  - zero if the value is zero,
  - `1.0` if the value is positive

Special cases:
  - `NaN.sign` is `NaN`
  - `(-0.0).sign` is `-0.0`

@sample samples.math.MathSamples.Doubles.sign

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun sign(x: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L973)

Returns the sign of the given value `x`:
  - `-1.0` if the value is negative,
  - zero if the value is zero,
  - `1.0` if the value is positive

Special cases:
  - `sign(NaN)` is `NaN`
  - `sign(-0.0)` is `-0.0`

@sample samples.math.MathSamples.Floats.signFun

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect val Float.sign: Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1069)

Returns the sign of this value:
  - `-1.0` if the value is negative,
  - zero if the value is zero,
  - `1.0` if the value is positive

Special cases:
  - `NaN.sign` is `NaN`
  - `(-0.0).sign` is `-0.0`

@sample samples.math.MathSamples.Floats.sign

### 5. Common

```kotlin
@SinceKotlin("1.2")
public expect val Int.sign: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1177)

Returns the sign of this value:
  - `-1` if the value is negative,
  - `0` if the value is zero,
  - `1` if the value is positive

@sample samples.math.MathSamples.Ints.sign

### 6. Common

```kotlin
@SinceKotlin("1.2")
public expect val Long.sign: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1230)

Returns the sign of this value:
  - `-1` if the value is negative,
  - `0` if the value is zero,
  - `1` if the value is positive

@sample samples.math.MathSamples.Longs.sign

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(sign(3.14))
    println(sign(-3.14))
    println(sign(0.0))
    println(sign(Double.POSITIVE_INFINITY))
    println(sign(Double.NEGATIVE_INFINITY))

    // Special cases
    println(sign(Double.NaN))
    println(sign(-0.0))
}
```

```text title="Output"
1.0
-1.0
0.0
1.0
-1.0
NaN
-0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L123)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14.sign)
    println((-3.14).sign)
    println(0.0.sign)
    println(Double.POSITIVE_INFINITY.sign)
    println(Double.NEGATIVE_INFINITY.sign)

    // Special cases
    println(Double.NaN.sign)
    println((-0.0).sign)
}
```

```text title="Output"
1.0
-1.0
0.0
1.0
-1.0
NaN
-0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L110)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(sign(3.14f))
    println(sign(-3.14f))
    println(sign(0.0f))
    println(sign(Float.POSITIVE_INFINITY))
    println(sign(Float.NEGATIVE_INFINITY))

    // Special cases
    println(sign(Float.NaN))
    println(sign(-0.0f))
}
```

```text title="Output"
1.0
-1.0
0.0
1.0
-1.0
NaN
-0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L717)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14f.sign)
    println((-3.14f).sign)
    println(0.0f.sign)
    println(Float.POSITIVE_INFINITY.sign)
    println(Float.NEGATIVE_INFINITY.sign)

    // Special cases
    println(Float.NaN.sign)
    println((-0.0f).sign)
}
```

```text title="Output"
1.0
-1.0
0.0
1.0
-1.0
NaN
-0.0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L704)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(0.sign)
    println(9000.sign)
    println((-9000).sign)
    println(Int.MAX_VALUE.sign)
    println(Int.MIN_VALUE.sign)
}
```

```text title="Output"
0
1
-1
1
-1
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1261)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(0L.sign)
    println(9000L.sign)
    println((-9000L).sign)
    println(Long.MAX_VALUE.sign)
    println(Long.MIN_VALUE.sign)
}
```

```text title="Output"
0
1
-1
1
-1
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1220)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
