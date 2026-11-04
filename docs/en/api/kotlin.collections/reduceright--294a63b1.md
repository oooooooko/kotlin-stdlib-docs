# reduceRight

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with the last element and applying `operation` from right to left
to each element and current accumulator value.

Throws an exception if this array is empty. If the array can be empty in an expected way,
please use `reduceRightOrNull` instead. It returns `null` when its receiver is empty.

@param `operation` function that takes an element and current accumulator value,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduceRight

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <S, T : S> Array<out T>.reduceRight(operation: (T, acc: S) -> S): S
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23389)

### 2. Common

```kotlin
public inline fun ByteArray.reduceRight(operation: (Byte, acc: Byte) -> Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23411)

### 3. Common

```kotlin
public inline fun ShortArray.reduceRight(operation: (Short, acc: Short) -> Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23433)

### 4. Common

```kotlin
public inline fun IntArray.reduceRight(operation: (Int, acc: Int) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23455)

### 5. Common

```kotlin
public inline fun LongArray.reduceRight(operation: (Long, acc: Long) -> Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23477)

### 6. Common

```kotlin
public inline fun FloatArray.reduceRight(operation: (Float, acc: Float) -> Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23499)

### 7. Common

```kotlin
public inline fun DoubleArray.reduceRight(operation: (Double, acc: Double) -> Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23521)

### 8. Common

```kotlin
public inline fun BooleanArray.reduceRight(operation: (Boolean, acc: Boolean) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23543)

### 9. Common

```kotlin
public inline fun CharArray.reduceRight(operation: (Char, acc: Char) -> Char): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L23565)

### 10. Common

```kotlin
public inline fun <S, T : S> List<T>.reduceRight(operation: (T, acc: S) -> S): S
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3190)

Accumulates value starting with the last element and applying `operation` from right to left
to each element and current accumulator value.

Throws an exception if this list is empty. If the list can be empty in an expected way,
please use `reduceRightOrNull` instead. It returns `null` when its receiver is empty.

@param `operation` function that takes an element and current accumulator value,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduceRight

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reduceRight(operation: (UInt, acc: UInt) -> UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10327)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reduceRight(operation: (ULong, acc: ULong) -> ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10352)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reduceRight(operation: (UByte, acc: UByte) -> UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10377)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reduceRight(operation: (UShort, acc: UShort) -> UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10402)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceRight { string, acc -> acc + string })
    println(strings.reduceRightIndexed { index, string, acc -> acc + string + index })

    assertFails { emptyList<Int>().reduceRight { _, _ -> 0 } }
}
```

```text title="Output"
dcba
dc2b1a0
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1246)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
