# max

`kotlin.math` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the greater of two values.

If either value is `NaN`, then the result is `NaN`.

@sample samples.math.MathSamples.Doubles.max

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun max(a: Double, b: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L410)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun max(a: Float, b: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1000)

Returns the greater of two values.

If either value is `NaN`, then the result is `NaN`.

@sample samples.math.MathSamples.Floats.max

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun max(a: Int, b: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1157)

Returns the greater of two values.

@sample samples.math.MathSamples.Ints.max

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun max(a: Long, b: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1210)

Returns the greater of two values.

@sample samples.math.MathSamples.Longs.max

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun max(a: UInt, b: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UMath.kt#L26)

Returns the greater of two values.

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun max(a: ULong, b: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UMath.kt#L35)

Returns the greater of two values.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(max(-1.0, 1.0))
    println(max(1.0, -1.0))
    println(max(-3.0, -1.0))
    println(max(-0.0, 0.0))

    // special cases
    println(max(Double.NaN, 0.0))
    println(max(-9000.0, Double.NaN))
    // Note that MIN_VALUE has a different meaning compared to Long.MIN_VALUE or Int.MIN_VALUE
    println(max(Double.MIN_VALUE, 0.0) == Double.MIN_VALUE)
    println(max(Double.POSITIVE_INFINITY, Double.MAX_VALUE))
}
```

```text title="Output"
1.0
1.0
-1.0
0.0
NaN
NaN
true
Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L484)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(max(-1.0f, 1.0f))
    println(max(1.0f, -1.0f))
    println(max(-3.0f, -1.0f))
    println(max(-0.0f, 0.0f))

    // special cases
    println(max(Float.NaN, 0.0f))
    println(max(-9000.0f, Float.NaN))
    // Note that MIN_VALUE has a different meaning compared to Long.MIN_VALUE or Int.MIN_VALUE
    println(max(Float.MIN_VALUE, 0.0f) == Float.MIN_VALUE)
    println(max(Float.POSITIVE_INFINITY, Float.MAX_VALUE))
}
```

```text title="Output"
1.0
1.0
-1.0
0.0
NaN
NaN
true
Infinity
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1079)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(max(-1, 1))
    println(max(1, -1))
    println(max(-3, -1))
}
```

```text title="Output"
1
1
-1
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1277)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(max(-1L, 1L))
    println(max(1L, -1L))
    println(max(-3L, -1L))
}
```

```text title="Output"
1
1
-1
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1236)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
