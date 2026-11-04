# minOf

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the smaller of two values.

If values are equal, returns the first one.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
public expect fun <T : Comparable<T>> minOf(a: T, b: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L202)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Byte, b: Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L210)

Returns the smaller of two values.

### 3. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Short, b: Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L216)

Returns the smaller of two values.

### 4. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Int, b: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L222)

Returns the smaller of two values.

### 5. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Long, b: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L228)

Returns the smaller of two values.

### 6. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Float, b: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L234)

Returns the smaller of two values.

If either value is `NaN`, returns `NaN`.

### 7. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Double, b: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L242)

Returns the smaller of two values.

If either value is `NaN`, returns `NaN`.

### 8. Common

```kotlin
@SinceKotlin("1.1")
public expect fun <T : Comparable<T>> minOf(a: T, b: T, c: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L250)

Returns the smaller of three values.

If there are multiple equal minimal values, returns the first of them.

### 9. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Byte, b: Byte, c: Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L258)

Returns the smaller of three values.

### 10. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Short, b: Short, c: Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L265)

Returns the smaller of three values.

### 11. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Int, b: Int, c: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L272)

Returns the smaller of three values.

### 12. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Long, b: Long, c: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L279)

Returns the smaller of three values.

### 13. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Float, b: Float, c: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L286)

Returns the smaller of three values.

If any value is `NaN`, returns `NaN`.

### 14. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Double, b: Double, c: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L295)

Returns the smaller of three values.

If any value is `NaN`, returns `NaN`.

### 15. Common

```kotlin
@SinceKotlin("1.1")
public fun <T> minOf(a: T, b: T, c: T, comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L304)

Returns the smaller of three values according to the order specified by the given `comparator`.

If there are multiple equal minimal values, returns the first of them.

### 16. Common

```kotlin
@SinceKotlin("1.1")
public fun <T> minOf(a: T, b: T, comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L314)

Returns the smaller of two values according to the order specified by the given `comparator`.

If values are equal, returns the first one.

### 17. Common

```kotlin
@SinceKotlin("1.4")
public expect fun <T : Comparable<T>> minOf(a: T, vararg other: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L324)

Returns the smaller of the given values.

If there are multiple equal minimal values, returns the first of them.

### 18. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Byte, vararg other: Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L332)

Returns the smaller of the given values.

### 19. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Short, vararg other: Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L338)

Returns the smaller of the given values.

### 20. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Int, vararg other: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L344)

Returns the smaller of the given values.

### 21. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Long, vararg other: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L350)

Returns the smaller of the given values.

### 22. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Float, vararg other: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L356)

Returns the smaller of the given values.

If any value is `NaN`, returns `NaN`.

### 23. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Double, vararg other: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L364)

Returns the smaller of the given values.

If any value is `NaN`, returns `NaN`.

### 24. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> minOf(a: T, vararg other: T, comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L372)

Returns the smaller of the given values according to the order specified by the given `comparator`.

If there are multiple equal minimal values, returns the first of them.

### 25. Common

```kotlin
@SinceKotlin("1.5")
public fun minOf(a: UInt, b: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L132)

Returns the smaller of two values.

### 26. Common

```kotlin
@SinceKotlin("1.5")
public fun minOf(a: ULong, b: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L140)

Returns the smaller of two values.

### 27. Common

```kotlin
@SinceKotlin("1.5")
public fun minOf(a: UByte, b: UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L148)

Returns the smaller of two values.

### 28. Common

```kotlin
@SinceKotlin("1.5")
public fun minOf(a: UShort, b: UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L156)

Returns the smaller of two values.

### 29. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun minOf(a: UInt, b: UInt, c: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L164)

Returns the smaller of three values.

### 30. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun minOf(a: ULong, b: ULong, c: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L173)

Returns the smaller of three values.

### 31. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun minOf(a: UByte, b: UByte, c: UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L182)

Returns the smaller of three values.

### 32. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun minOf(a: UShort, b: UShort, c: UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L191)

Returns the smaller of three values.

### 33. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun minOf(a: UInt, vararg other: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L200)

Returns the smaller of the given values.

### 34. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun minOf(a: ULong, vararg other: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L211)

Returns the smaller of the given values.

### 35. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun minOf(a: UByte, vararg other: UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L222)

Returns the smaller of the given values.

### 36. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun minOf(a: UShort, vararg other: UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L233)

Returns the smaller of the given values.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.comparisons.*

fun main() {
    val result = `minOf`(1, 1)
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
