# reduceRightOrNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with the last element and applying `operation` from right to left
to each element and current accumulator value.

Returns `null` if the array is empty.

@param `operation` function that takes an element and current accumulator value,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduceRightOrNull

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <S, T : S> Array<out T>.reduceRightOrNull(operation: (T, acc: S) -> S): S?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L24001)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public inline fun ByteArray.reduceRightOrNull(operation: (Byte, acc: Byte) -> Byte): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L24023)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public inline fun ShortArray.reduceRightOrNull(operation: (Short, acc: Short) -> Short): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L24045)

### 4. Common

```kotlin
@SinceKotlin("1.4")
public inline fun IntArray.reduceRightOrNull(operation: (Int, acc: Int) -> Int): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L24067)

### 5. Common

```kotlin
@SinceKotlin("1.4")
public inline fun LongArray.reduceRightOrNull(operation: (Long, acc: Long) -> Long): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L24089)

### 6. Common

```kotlin
@SinceKotlin("1.4")
public inline fun FloatArray.reduceRightOrNull(operation: (Float, acc: Float) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L24111)

### 7. Common

```kotlin
@SinceKotlin("1.4")
public inline fun DoubleArray.reduceRightOrNull(operation: (Double, acc: Double) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L24133)

### 8. Common

```kotlin
@SinceKotlin("1.4")
public inline fun BooleanArray.reduceRightOrNull(operation: (Boolean, acc: Boolean) -> Boolean): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L24155)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public inline fun CharArray.reduceRightOrNull(operation: (Char, acc: Char) -> Char): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L24177)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <S, T : S> List<T>.reduceRightOrNull(operation: (T, acc: S) -> S): S?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3261)

Accumulates value starting with the last element and applying `operation` from right to left
to each element and current accumulator value.

Returns `null` if the list is empty.

@param `operation` function that takes an element and current accumulator value,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduceRightOrNull

### 11. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reduceRightOrNull(operation: (UInt, acc: UInt) -> UInt): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10631)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reduceRightOrNull(operation: (ULong, acc: ULong) -> ULong): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10655)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reduceRightOrNull(operation: (UByte, acc: UByte) -> UByte): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10679)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reduceRightOrNull(operation: (UShort, acc: UShort) -> UShort): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10703)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceRightOrNull { string, acc -> acc + string })
    println(strings.reduceRightIndexedOrNull { index, string, acc -> acc + string + index })

    println(emptyList<String>().reduceRightOrNull { _, _ -> "" })
}
```

```text title="Output"
dcba
dc2b1a0
null
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1264)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
