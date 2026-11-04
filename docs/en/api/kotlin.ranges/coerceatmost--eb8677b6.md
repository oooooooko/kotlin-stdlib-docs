# coerceAtMost

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMostComparable

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Comparable<T>> T.coerceAtMost(maximumValue: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1316)

### 2. Common

```kotlin
public fun Byte.coerceAtMost(maximumValue: Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1327)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMost

### 3. Common

```kotlin
public fun Short.coerceAtMost(maximumValue: Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1338)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMost

### 4. Common

```kotlin
public fun Int.coerceAtMost(maximumValue: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1349)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMost

### 5. Common

```kotlin
public fun Long.coerceAtMost(maximumValue: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1360)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMost

### 6. Common

```kotlin
public fun Float.coerceAtMost(maximumValue: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1371)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMost

### 7. Common

```kotlin
public fun Double.coerceAtMost(maximumValue: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1382)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMost

### 8. Common

```kotlin
@SinceKotlin("1.5")
public fun UInt.coerceAtMost(maximumValue: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L448)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMostUnsigned

### 9. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.coerceAtMost(maximumValue: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L460)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMostUnsigned

### 10. Common

```kotlin
@SinceKotlin("1.5")
public fun UByte.coerceAtMost(maximumValue: UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L472)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMostUnsigned

### 11. Common

```kotlin
@SinceKotlin("1.5")
public fun UShort.coerceAtMost(maximumValue: UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L484)

Ensures that this value is not greater than the specified `maximumValue`.

@return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtMostUnsigned

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(DayOfWeek.FRIDAY.coerceAtMost(DayOfWeek.SATURDAY))
    println(DayOfWeek.FRIDAY.coerceAtMost(DayOfWeek.WEDNESDAY))
}
```

```text title="Output"
FRIDAY
WEDNESDAY
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L55)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10.coerceAtMost(5))
    println(10.coerceAtMost(20))
}
```

```text title="Output"
5
10
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L43)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10u.coerceAtMost(5u))
    println(10u.coerceAtMost(20u))
}
```

```text title="Output"
5
10
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L49)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
