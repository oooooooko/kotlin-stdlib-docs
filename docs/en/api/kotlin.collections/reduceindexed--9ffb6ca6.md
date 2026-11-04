# reduceIndexed

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with the first element and applying `operation` from left to right
to current accumulator value and each element with its index in the original array.

Throws an exception if this array is empty. If the array can be empty in an expected way,
please use `reduceIndexedOrNull` instead. It returns `null` when its receiver is empty.

@param `operation` function that takes the index of an element, current accumulator value and the element itself,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduce

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <S, T : S> Array<out T>.reduceIndexed(operation: (index: Int, acc: S, T) -> S): S
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22795)

### 2. Common

```kotlin
public inline fun ByteArray.reduceIndexed(operation: (index: Int, acc: Byte, Byte) -> Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22817)

### 3. Common

```kotlin
public inline fun ShortArray.reduceIndexed(operation: (index: Int, acc: Short, Short) -> Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22839)

### 4. Common

```kotlin
public inline fun IntArray.reduceIndexed(operation: (index: Int, acc: Int, Int) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22861)

### 5. Common

```kotlin
public inline fun LongArray.reduceIndexed(operation: (index: Int, acc: Long, Long) -> Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22883)

### 6. Common

```kotlin
public inline fun FloatArray.reduceIndexed(operation: (index: Int, acc: Float, Float) -> Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22905)

### 7. Common

```kotlin
public inline fun DoubleArray.reduceIndexed(operation: (index: Int, acc: Double, Double) -> Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22927)

### 8. Common

```kotlin
public inline fun BooleanArray.reduceIndexed(operation: (index: Int, acc: Boolean, Boolean) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22949)

### 9. Common

```kotlin
public inline fun CharArray.reduceIndexed(operation: (index: Int, acc: Char, Char) -> Char): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22971)

### 10. Common

```kotlin
public inline fun <S, T : S> Iterable<T>.reduceIndexed(operation: (index: Int, acc: S, T) -> S): S
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3122)

Accumulates value starting with the first element and applying `operation` from left to right
to current accumulator value and each element with its index in the original collection.

Throws an exception if this collection is empty. If the collection can be empty in an expected way,
please use `reduceIndexedOrNull` instead. It returns `null` when its receiver is empty.

@param `operation` function that takes the index of an element, current accumulator value and the element itself,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduce

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reduceIndexed(operation: (index: Int, acc: UInt, UInt) -> UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10035)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reduceIndexed(operation: (index: Int, acc: ULong, ULong) -> ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10060)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reduceIndexed(operation: (index: Int, acc: UByte, UByte) -> UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10085)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reduceIndexed(operation: (index: Int, acc: UShort, UShort) -> UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10110)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduce { acc, string -> acc + string })
    println(strings.reduceIndexed { index, acc, string -> acc + string + index })

    assertFails { emptyList<Int>().reduce { _, _ -> 0 } }
}
```

```text title="Output"
abcd
ab1c2d3
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1237)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
