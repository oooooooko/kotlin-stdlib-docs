# reduceOrNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with the first element and applying `operation` from left to right
to current accumulator value and each element.

Returns `null` if the array is empty.

@param `operation` function that takes current accumulator value and an element,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduceOrNull

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <S, T : S> Array<out T>.reduceOrNull(operation: (acc: S, T) -> S): S?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23191)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public inline fun ByteArray.reduceOrNull(operation: (acc: Byte, Byte) -> Byte): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23213)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public inline fun ShortArray.reduceOrNull(operation: (acc: Short, Short) -> Short): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23235)

### 4. Common

```kotlin
@SinceKotlin("1.4")
public inline fun IntArray.reduceOrNull(operation: (acc: Int, Int) -> Int): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23257)

### 5. Common

```kotlin
@SinceKotlin("1.4")
public inline fun LongArray.reduceOrNull(operation: (acc: Long, Long) -> Long): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23279)

### 6. Common

```kotlin
@SinceKotlin("1.4")
public inline fun FloatArray.reduceOrNull(operation: (acc: Float, Float) -> Float): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23301)

### 7. Common

```kotlin
@SinceKotlin("1.4")
public inline fun DoubleArray.reduceOrNull(operation: (acc: Double, Double) -> Double): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23323)

### 8. Common

```kotlin
@SinceKotlin("1.4")
public inline fun BooleanArray.reduceOrNull(operation: (acc: Boolean, Boolean) -> Boolean): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23345)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public inline fun CharArray.reduceOrNull(operation: (acc: Char, Char) -> Char): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23367)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <S, T : S> Iterable<T>.reduceOrNull(operation: (acc: S, T) -> S): S?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3168)

Accumulates value starting with the first element and applying `operation` from left to right
to current accumulator value and each element.

Returns `null` if the collection is empty.

@param `operation` function that takes current accumulator value and an element,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduceOrNull

### 11. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reduceOrNull(operation: (acc: UInt, UInt) -> UInt): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10231)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reduceOrNull(operation: (acc: ULong, ULong) -> ULong): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10255)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reduceOrNull(operation: (acc: UByte, UByte) -> UByte): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10279)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reduceOrNull(operation: (acc: UShort, UShort) -> UShort): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10303)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceOrNull { acc, string -> acc + string })
    println(strings.reduceIndexedOrNull { index, acc, string -> acc + string + index })

    println(emptyList<String>().reduceOrNull { _, _ -> "" })
}
```

```text title="Output"
abcd
ab1c2d3
null
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1255)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
