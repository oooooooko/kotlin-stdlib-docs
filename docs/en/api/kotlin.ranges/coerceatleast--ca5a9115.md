# coerceAtLeast

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeastComparable

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Comparable<T>> T.coerceAtLeast(minimumValue: T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1239)

### 2. Common

```kotlin
public fun Byte.coerceAtLeast(minimumValue: Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1250)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeast

### 3. Common

```kotlin
public fun Short.coerceAtLeast(minimumValue: Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1261)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeast

### 4. Common

```kotlin
public fun Int.coerceAtLeast(minimumValue: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1272)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeast

### 5. Common

```kotlin
public fun Long.coerceAtLeast(minimumValue: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1283)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeast

### 6. Common

```kotlin
public fun Float.coerceAtLeast(minimumValue: Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1294)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeast

### 7. Common

```kotlin
public fun Double.coerceAtLeast(minimumValue: Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1305)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeast

### 8. Common

```kotlin
@SinceKotlin("1.5")
public fun UInt.coerceAtLeast(minimumValue: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L400)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeastUnsigned

### 9. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.coerceAtLeast(minimumValue: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L412)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeastUnsigned

### 10. Common

```kotlin
@SinceKotlin("1.5")
public fun UByte.coerceAtLeast(minimumValue: UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L424)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeastUnsigned

### 11. Common

```kotlin
@SinceKotlin("1.5")
public fun UShort.coerceAtLeast(minimumValue: UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L436)

Ensures that this value is not less than the specified `minimumValue`.

@return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.

@sample samples.comparisons.ComparableOps.coerceAtLeastUnsigned

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(DayOfWeek.WEDNESDAY.coerceAtLeast(DayOfWeek.MONDAY))
    println(DayOfWeek.WEDNESDAY.coerceAtLeast(DayOfWeek.FRIDAY))
}
```

```text title="Output"
WEDNESDAY
FRIDAY
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L37)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10.coerceAtLeast(5))
    println(10.coerceAtLeast(20))
}
```

```text title="Output"
10
20
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L25)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10u.coerceAtLeast(5u))
    println(10u.coerceAtLeast(20u))
}
```

```text title="Output"
10
20
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L31)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
