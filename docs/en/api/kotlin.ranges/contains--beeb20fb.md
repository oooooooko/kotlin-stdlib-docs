# contains

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if this range contains the specified `element`.

Always returns `false` if the `element` is `null`.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline operator fun IntRange.contains(element: Int?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L284)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline operator fun LongRange.contains(element: Long?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L295)

### 3. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline operator fun CharRange.contains(element: Char?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L306)

### 4. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
public operator fun ClosedRange<Int>.contains(value: Byte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L317)

Checks if the specified `value` belongs to this range.

### 5. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
public operator fun ClosedRange<Long>.contains(value: Byte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L325)

Checks if the specified `value` belongs to this range.

### 6. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
public operator fun ClosedRange<Short>.contains(value: Byte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L333)

Checks if the specified `value` belongs to this range.

### 7. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Int>.contains(value: Byte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L361)

Checks if the specified `value` belongs to this range.

### 8. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Long>.contains(value: Byte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L371)

Checks if the specified `value` belongs to this range.

### 9. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Short>.contains(value: Byte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L381)

Checks if the specified `value` belongs to this range.

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntRange.contains(value: Byte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L391)

Checks if the specified `value` belongs to this range.

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongRange.contains(value: Byte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L399)

Checks if the specified `value` belongs to this range.

### 12. Common

```kotlin
@kotlin.jvm.JvmName("floatRangeContains")
public operator fun ClosedRange<Float>.contains(value: Double): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L447)

Checks if the specified `value` belongs to this range.

### 13. Common

```kotlin
@kotlin.jvm.JvmName("doubleRangeContains")
public operator fun ClosedRange<Double>.contains(value: Float): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L495)

Checks if the specified `value` belongs to this range.

### 14. Common

```kotlin
@kotlin.jvm.JvmName("doubleRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Double>.contains(value: Float): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L503)

Checks if the specified `value` belongs to this range.

### 15. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
public operator fun ClosedRange<Long>.contains(value: Int): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L513)

Checks if the specified `value` belongs to this range.

### 16. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
public operator fun ClosedRange<Byte>.contains(value: Int): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L521)

Checks if the specified `value` belongs to this range.

### 17. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
public operator fun ClosedRange<Short>.contains(value: Int): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L529)

Checks if the specified `value` belongs to this range.

### 18. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Long>.contains(value: Int): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L557)

Checks if the specified `value` belongs to this range.

### 19. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Byte>.contains(value: Int): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L567)

Checks if the specified `value` belongs to this range.

### 20. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Short>.contains(value: Int): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L577)

Checks if the specified `value` belongs to this range.

### 21. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongRange.contains(value: Int): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L587)

Checks if the specified `value` belongs to this range.

### 22. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
public operator fun ClosedRange<Int>.contains(value: Long): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L595)

Checks if the specified `value` belongs to this range.

### 23. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
public operator fun ClosedRange<Byte>.contains(value: Long): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L603)

Checks if the specified `value` belongs to this range.

### 24. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
public operator fun ClosedRange<Short>.contains(value: Long): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L611)

Checks if the specified `value` belongs to this range.

### 25. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Int>.contains(value: Long): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L639)

Checks if the specified `value` belongs to this range.

### 26. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Byte>.contains(value: Long): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L649)

Checks if the specified `value` belongs to this range.

### 27. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Short>.contains(value: Long): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L659)

Checks if the specified `value` belongs to this range.

### 28. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntRange.contains(value: Long): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L669)

Checks if the specified `value` belongs to this range.

### 29. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
public operator fun ClosedRange<Int>.contains(value: Short): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L677)

Checks if the specified `value` belongs to this range.

### 30. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
public operator fun ClosedRange<Long>.contains(value: Short): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L685)

Checks if the specified `value` belongs to this range.

### 31. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
public operator fun ClosedRange<Byte>.contains(value: Short): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L693)

Checks if the specified `value` belongs to this range.

### 32. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Int>.contains(value: Short): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L721)

Checks if the specified `value` belongs to this range.

### 33. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Long>.contains(value: Short): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L731)

Checks if the specified `value` belongs to this range.

### 34. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Byte>.contains(value: Short): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L741)

Checks if the specified `value` belongs to this range.

### 35. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntRange.contains(value: Short): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L751)

Checks if the specified `value` belongs to this range.

### 36. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongRange.contains(value: Short): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L759)

Checks if the specified `value` belongs to this range.

### 37. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline operator fun UIntRange.contains(element: UInt?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L196)

### 38. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline operator fun ULongRange.contains(element: ULong?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L207)

### 39. Common

```kotlin
@SinceKotlin("1.5")
public operator fun UIntRange.contains(value: UByte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L218)

Checks if the specified `value` belongs to this range.

### 40. Common

```kotlin
@SinceKotlin("1.5")
public operator fun ULongRange.contains(value: UByte): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L226)

Checks if the specified `value` belongs to this range.

### 41. Common

```kotlin
@SinceKotlin("1.5")
public operator fun ULongRange.contains(value: UInt): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L234)

Checks if the specified `value` belongs to this range.

### 42. Common

```kotlin
@SinceKotlin("1.5")
public operator fun UIntRange.contains(value: ULong): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L242)

Checks if the specified `value` belongs to this range.

### 43. Common

```kotlin
@SinceKotlin("1.5")
public operator fun UIntRange.contains(value: UShort): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L250)

Checks if the specified `value` belongs to this range.

### 44. Common

```kotlin
@SinceKotlin("1.5")
public operator fun ULongRange.contains(value: UShort): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L258)

Checks if the specified `value` belongs to this range.

### 45. Common

```kotlin
@SinceKotlin("2.3")
@kotlin.internal.InlineOnly
public inline operator fun <T, R> R.contains(element: T?): Boolean where T : Comparable<T>, R : ClosedRange<T>, R : Iterable<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L260)

Returns `true` if this iterable range contains the specified `element`.

Always returns `false` if the `element` is `null`.

### 46. Common

```kotlin
@SinceKotlin("2.3")
@WasExperimental(ExperimentalStdlibApi::class)
@kotlin.internal.InlineOnly
public inline operator fun <T, R> R.contains(element: T?): Boolean where T : Comparable<T>, R : OpenEndRange<T>, R : Iterable<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L286)

Returns `true` if this iterable range contains the specified `element`.

Always returns `false` if the `element` is `null`.

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
import kotlin.ranges.*

fun main() {
    val source = 1..3
    val result = source.`contains`(2)
    println(result)
}
```

```text title="Output"
true
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
