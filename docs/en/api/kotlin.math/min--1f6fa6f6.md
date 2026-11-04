# min

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the smaller of two values.

If either value is `NaN`, then the result is `NaN`.

@sample samples.math.MathSamples.Doubles.min

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun min(a: Double, b: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L400)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun min(a: Float, b: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L990)

Returns the smaller of two values.

If either value is `NaN`, then the result is `NaN`.

@sample samples.math.MathSamples.Floats.min

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun min(a: Int, b: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1149)

Returns the smaller of two values.

@sample samples.math.MathSamples.Ints.min

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun min(a: Long, b: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1202)

Returns the smaller of two values.

@sample samples.math.MathSamples.Longs.min

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun min(a: UInt, b: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UMath.kt#L8)

Returns the smaller of two values.

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun min(a: ULong, b: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UMath.kt#L17)

Returns the smaller of two values.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(min(-1.0, 1.0))
    println(min(1.0, -1.0))
    println(min(-3.0, -1.0))
    println(min(-0.0, 0.0))

    // special cases
    println(min(Double.NaN, 0.0))
    println(min(-9000.0, Double.NaN))
    // Note that MIN_VALUE has a different meaning compared to Long.MIN_VALUE or Int.MIN_VALUE
    println(min(Double.MIN_VALUE, 0.0))
    println(min(Double.POSITIVE_INFINITY, Double.MAX_VALUE) == Double.MAX_VALUE)
}
```

```text title="Output"
-1.0
-1.0
-3.0
-0.0
NaN
NaN
0.0
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L469)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(min(-1.0f, 1.0f))
    println(min(1.0f, -1.0f))
    println(min(-3.0f, -1.0f))
    println(min(-0.0f, 0.0f))

    // special cases
    println(min(Float.NaN, 0.0f))
    println(min(-9000.0f, Float.NaN))
    // Note that MIN_VALUE has a different meaning compared to Long.MIN_VALUE or Int.MIN_VALUE
    println(min(Float.MIN_VALUE, 0.0f))
    println(min(Float.POSITIVE_INFINITY, Float.MAX_VALUE) == Float.MAX_VALUE)
}
```

```text title="Output"
-1.0
-1.0
-3.0
-0.0
NaN
NaN
0.0
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1064)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(min(-1, 1))
    println(min(1, -1))
    println(min(-3, -1))
}
```

```text title="Output"
-1
-1
-3
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1270)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(min(-1L, 1L))
    println(min(1L, -1L))
    println(min(-3L, -1L))
}
```

```text title="Output"
-1
-1
-3
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1229)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
