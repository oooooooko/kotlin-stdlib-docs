# coerceIn

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceInComparable

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Comparable<T>> T.coerceIn(minimumValue: T?, maximumValue: T?): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1393)

### 2. Common

```kotlin
public fun Byte.coerceIn(minimumValue: Byte, maximumValue: Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1413)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceIn

### 3. Common

```kotlin
public fun Short.coerceIn(minimumValue: Short, maximumValue: Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1427)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceIn

### 4. Common

```kotlin
public fun Int.coerceIn(minimumValue: Int, maximumValue: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1441)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceIn

### 5. Common

```kotlin
public fun Long.coerceIn(minimumValue: Long, maximumValue: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1455)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceIn

### 6. Common

```kotlin
public fun Float.coerceIn(minimumValue: Float, maximumValue: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1469)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceIn

### 7. Common

```kotlin
public fun Double.coerceIn(minimumValue: Double, maximumValue: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1483)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceIn

### 8. Common

```kotlin
@SinceKotlin("1.1")
public fun <T : Comparable<T>> T.coerceIn(range: ClosedFloatingPointRange<T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1497)

Ensures that this value lies in the specified `range`.

@return this value if it's in the `range`, or `range.start` if this value is less than `range.start`, or `range.endInclusive` if this value is greater than `range.endInclusive`.

@sample samples.comparisons.ComparableOps.coerceInFloatingPointRange

### 9. Common

```kotlin
public fun <T : Comparable<T>> T.coerceIn(range: ClosedRange<T>): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1516)

Ensures that this value lies in the specified `range`.

@return this value if it's in the `range`, or `range.start` if this value is less than `range.start`, or `range.endInclusive` if this value is greater than `range.endInclusive`.

@sample samples.comparisons.ComparableOps.coerceInComparable

### 10. Common

```kotlin
public fun Int.coerceIn(range: ClosedRange<Int>): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1535)

Ensures that this value lies in the specified `range`.

@return this value if it's in the `range`, or `range.start` if this value is less than `range.start`, or `range.endInclusive` if this value is greater than `range.endInclusive`.

@sample samples.comparisons.ComparableOps.coerceIn

### 11. Common

```kotlin
public fun Long.coerceIn(range: ClosedRange<Long>): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1554)

Ensures that this value lies in the specified `range`.

@return this value if it's in the `range`, or `range.start` if this value is less than `range.start`, or `range.endInclusive` if this value is greater than `range.endInclusive`.

@sample samples.comparisons.ComparableOps.coerceIn

### 12. Common

```kotlin
@SinceKotlin("1.5")
public fun UInt.coerceIn(minimumValue: UInt, maximumValue: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L496)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceInUnsigned

### 13. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.coerceIn(minimumValue: ULong, maximumValue: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L511)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceInUnsigned

### 14. Common

```kotlin
@SinceKotlin("1.5")
public fun UByte.coerceIn(minimumValue: UByte, maximumValue: UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L526)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceInUnsigned

### 15. Common

```kotlin
@SinceKotlin("1.5")
public fun UShort.coerceIn(minimumValue: UShort, maximumValue: UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L541)

Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.

@return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.

@sample samples.comparisons.ComparableOps.coerceInUnsigned

### 16. Common

```kotlin
@SinceKotlin("1.5")
public fun UInt.coerceIn(range: ClosedRange<UInt>): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L556)

Ensures that this value lies in the specified `range`.

@return this value if it's in the `range`, or `range.start` if this value is less than `range.start`, or `range.endInclusive` if this value is greater than `range.endInclusive`.

@sample samples.comparisons.ComparableOps.coerceInUnsigned

### 17. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.coerceIn(range: ClosedRange<ULong>): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L576)

Ensures that this value lies in the specified `range`.

@return this value if it's in the `range`, or `range.start` if this value is less than `range.start`, or `range.endInclusive` if this value is greater than `range.endInclusive`.

@sample samples.comparisons.ComparableOps.coerceInUnsigned

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    val workingDays = DayOfWeek.MONDAY..DayOfWeek.FRIDAY
    println(DayOfWeek.WEDNESDAY.coerceIn(workingDays))
    println(DayOfWeek.SATURDAY.coerceIn(workingDays))

    println(DayOfWeek.FRIDAY.coerceIn(DayOfWeek.SATURDAY, DayOfWeek.SUNDAY))
}
```

```text title="Output"
WEDNESDAY
FRIDAY
SATURDAY
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L83)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10.coerceIn(1, 100))
    println(10.coerceIn(1..100))
    println(0.coerceIn(1, 100))
    println(500.coerceIn(1, 100))
    assertFailsWith<IllegalArgumentException> {
        10.coerceIn(100, 0)
    }
}
```

```text title="Output"
10
10
1
100
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L61)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10.1.coerceIn(1.0..10.0))
    println(9.9.coerceIn(1.0..10.0))

    assertFailsWith<IllegalArgumentException> { 9.9.coerceIn(1.0..Double.NaN) }
}
```

```text title="Output"
10.0
9.9
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L92)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10u.coerceIn(1u, 100u))
    println(10u.coerceIn(1u..100u))
    println(0u.coerceIn(1u, 100u))
    println(500u.coerceIn(1u, 100u))
    assertFailsWith<IllegalArgumentException> {
        10u.coerceIn(100u, 0u)
    }
}
```

```text title="Output"
10
10
1
100
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L72)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
