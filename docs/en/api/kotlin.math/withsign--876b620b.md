# withSign

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns this value with the sign bit same as of the `sign` value.

If `sign` is `NaN` the sign of the result is undefined.

@sample samples.math.MathSamples.Doubles.withSignDouble

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.withSign(sign: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L492)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.withSign(sign: Int): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L502)

Returns this value with the sign bit same as of the `sign` value.

@sample samples.math.MathSamples.Doubles.withSignInt

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.withSign(sign: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1084)

Returns this value with the sign bit same as of the `sign` value.

If `sign` is `NaN` the sign of the result is undefined.

@sample samples.math.MathSamples.Floats.withSignFloat

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.withSign(sign: Int): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1094)

Returns this value with the sign bit same as of the `sign` value.

@sample samples.math.MathSamples.Floats.withSignInt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14.withSign(3.14))
    println(3.14.withSign(-3.14))
    println((-3.14).withSign(-3.14))
    println((-3.14).withSign(0.0))
    println(Double.NaN.withSign(-1.0))
}
```

```text title="Output"
3.14
-3.14
-3.14
3.14
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L223)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14.withSign(100))
    println(3.14.withSign(-100))
    println((-3.14).withSign(-100))
    println((-3.14).withSign(0))
    println(Double.NaN.withSign(-1))
}
```

```text title="Output"
3.14
-3.14
-3.14
3.14
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L232)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14f.withSign(3.14f))
    println(3.14f.withSign(-3.14f))
    println((-3.14f).withSign(-3.14f))
    println((-3.14f).withSign(0.0f))
    println(Float.NaN.withSign(-1.0f))
}
```

```text title="Output"
3.14
-3.14
-3.14
3.14
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L817)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14f.withSign(100))
    println(3.14f.withSign(-100))
    println((-3.14f).withSign(-100))
    println((-3.14f).withSign(0))
    println(Float.NaN.withSign(-1))
}
```

```text title="Output"
3.14
-3.14
-3.14
3.14
NaN
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L826)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
