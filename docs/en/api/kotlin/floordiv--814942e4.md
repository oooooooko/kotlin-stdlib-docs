# floorDiv

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Divides this value by the other value, flooring the result to an integer that is closer to negative infinity.
@sample samples.misc.Builtins.floorDiv

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.floorDiv(other: Byte): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L15)

### 2. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.floorDiv(other: Short): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L37)

### 3. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.floorDiv(other: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L59)

### 4. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.floorDiv(other: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L81)

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.floorDiv(other: Byte): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L103)

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.floorDiv(other: Short): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L125)

### 7. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.floorDiv(other: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L147)

### 8. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.floorDiv(other: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L169)

### 9. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.floorDiv(other: Byte): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L191)

### 10. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.floorDiv(other: Short): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L213)

### 11. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.floorDiv(other: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L235)

### 12. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.floorDiv(other: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L262)

### 13. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.floorDiv(other: Byte): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L284)

### 14. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.floorDiv(other: Short): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L306)

### 15. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.floorDiv(other: Int): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L328)

### 16. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.floorDiv(other: Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L350)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    // Regular integer division (/) truncates toward zero
    println((-7) / 3)
    // floorDiv rounds toward negative infinity
    println((-7).floorDiv(3))
    println(7.floorDiv(3))
    println(7.floorDiv(-3))

    // Dividing by zero throws, just like the / operator
    assertFailsWith<ArithmeticException> { 1.floorDiv(0) }
}
```

```text title="Output"
-2
-3
2
-3
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/builtins.kt#L47)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
