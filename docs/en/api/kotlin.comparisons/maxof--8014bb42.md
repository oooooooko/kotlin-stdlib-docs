# maxOf

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the greater of two values.

If values are equal, returns the first one.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
public expect fun <T : Comparable<T>> maxOf(a: T, b: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L20)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Byte, b: Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L28)

Returns the greater of two values.

### 3. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Short, b: Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L34)

Returns the greater of two values.

### 4. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Int, b: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L40)

Returns the greater of two values.

### 5. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Long, b: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L46)

Returns the greater of two values.

### 6. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Float, b: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L52)

Returns the greater of two values.

If either value is `NaN`, returns `NaN`.

### 7. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Double, b: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L60)

Returns the greater of two values.

If either value is `NaN`, returns `NaN`.

### 8. Common

```kotlin
@SinceKotlin("1.1")
public expect fun <T : Comparable<T>> maxOf(a: T, b: T, c: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L68)

Returns the greater of three values.

If there are multiple equal maximal values, returns the first of them.

### 9. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Byte, b: Byte, c: Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L76)

Returns the greater of three values.

### 10. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Short, b: Short, c: Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L83)

Returns the greater of three values.

### 11. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Int, b: Int, c: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L90)

Returns the greater of three values.

### 12. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Long, b: Long, c: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L97)

Returns the greater of three values.

### 13. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Float, b: Float, c: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L104)

Returns the greater of three values.

If any value is `NaN`, returns `NaN`.

### 14. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Double, b: Double, c: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L113)

Returns the greater of three values.

If any value is `NaN`, returns `NaN`.

### 15. Common

```kotlin
@SinceKotlin("1.1")
public fun <T> maxOf(a: T, b: T, c: T, comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L122)

Returns the greater of three values according to the order specified by the given `comparator`.

If there are multiple equal maximal values, returns the first of them.

### 16. Common

```kotlin
@SinceKotlin("1.1")
public fun <T> maxOf(a: T, b: T, comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L132)

Returns the greater of two values according to the order specified by the given `comparator`.

If values are equal, returns the first one.

### 17. Common

```kotlin
@SinceKotlin("1.4")
public expect fun <T : Comparable<T>> maxOf(a: T, vararg other: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L142)

Returns the greater of the given values.

If there are multiple equal maximal values, returns the first of them.

### 18. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Byte, vararg other: Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L150)

Returns the greater of the given values.

### 19. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Short, vararg other: Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L156)

Returns the greater of the given values.

### 20. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Int, vararg other: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L162)

Returns the greater of the given values.

### 21. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Long, vararg other: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L168)

Returns the greater of the given values.

### 22. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Float, vararg other: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L174)

Returns the greater of the given values.

If any value is `NaN`, returns `NaN`.

### 23. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Double, vararg other: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L182)

Returns the greater of the given values.

If any value is `NaN`, returns `NaN`.

### 24. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> maxOf(a: T, vararg other: T, comparator: Comparator<in T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L190)

Returns the greater of the given values according to the order specified by the given `comparator`.

If there are multiple equal maximal values, returns the first of them.

### 25. Common

```kotlin
@SinceKotlin("1.5")
public fun maxOf(a: UInt, b: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L20)

Returns the greater of two values.

### 26. Common

```kotlin
@SinceKotlin("1.5")
public fun maxOf(a: ULong, b: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L28)

Returns the greater of two values.

### 27. Common

```kotlin
@SinceKotlin("1.5")
public fun maxOf(a: UByte, b: UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L36)

Returns the greater of two values.

### 28. Common

```kotlin
@SinceKotlin("1.5")
public fun maxOf(a: UShort, b: UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L44)

Returns the greater of two values.

### 29. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun maxOf(a: UInt, b: UInt, c: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L52)

Returns the greater of three values.

### 30. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun maxOf(a: ULong, b: ULong, c: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L61)

Returns the greater of three values.

### 31. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun maxOf(a: UByte, b: UByte, c: UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L70)

Returns the greater of three values.

### 32. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun maxOf(a: UShort, b: UShort, c: UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L79)

Returns the greater of three values.

### 33. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun maxOf(a: UInt, vararg other: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L88)

Returns the greater of the given values.

### 34. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun maxOf(a: ULong, vararg other: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L99)

Returns the greater of the given values.

### 35. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun maxOf(a: UByte, vararg other: UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L110)

Returns the greater of the given values.

### 36. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun maxOf(a: UShort, vararg other: UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L121)

Returns the greater of the given values.

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
    val result = `maxOf`(1, 1)
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
