# copyOf

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns new array which is a copy of the original array.

@sample samples.collections.Arrays.CopyOfOperations.copyOf

## Declarations and overloads

### 1. Common

```kotlin
public expect fun <T> Array<T>.copyOf(): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8676)

### 2. Common

```kotlin
public expect fun ByteArray.copyOf(): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8683)

### 3. Common

```kotlin
public expect fun ShortArray.copyOf(): ShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8690)

### 4. Common

```kotlin
public expect fun IntArray.copyOf(): IntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8697)

### 5. Common

```kotlin
public expect fun LongArray.copyOf(): LongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8704)

### 6. Common

```kotlin
public expect fun FloatArray.copyOf(): FloatArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8711)

### 7. Common

```kotlin
public expect fun DoubleArray.copyOf(): DoubleArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8718)

### 8. Common

```kotlin
public expect fun BooleanArray.copyOf(): BooleanArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8725)

### 9. Common

```kotlin
public expect fun CharArray.copyOf(): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8732)

### 10. Common

```kotlin
public expect fun ByteArray.copyOf(newSize: Int): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8739)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

@sample samples.collections.Arrays.CopyOfOperations.resizedPrimitiveCopyOf

### 11. Common

```kotlin
public expect fun ShortArray.copyOf(newSize: Int): ShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8750)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

@sample samples.collections.Arrays.CopyOfOperations.resizedPrimitiveCopyOf

### 12. Common

```kotlin
public expect fun IntArray.copyOf(newSize: Int): IntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8761)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

@sample samples.collections.Arrays.CopyOfOperations.resizedPrimitiveCopyOf

### 13. Common

```kotlin
public expect fun LongArray.copyOf(newSize: Int): LongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8772)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

@sample samples.collections.Arrays.CopyOfOperations.resizedPrimitiveCopyOf

### 14. Common

```kotlin
public expect fun FloatArray.copyOf(newSize: Int): FloatArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8783)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

@sample samples.collections.Arrays.CopyOfOperations.resizedPrimitiveCopyOf

### 15. Common

```kotlin
public expect fun DoubleArray.copyOf(newSize: Int): DoubleArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8794)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

@sample samples.collections.Arrays.CopyOfOperations.resizedPrimitiveCopyOf

### 16. Common

```kotlin
public expect fun BooleanArray.copyOf(newSize: Int): BooleanArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8805)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with `false` values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with `false` values.

@sample samples.collections.Arrays.CopyOfOperations.resizedPrimitiveCopyOf

### 17. Common

```kotlin
public expect fun CharArray.copyOf(newSize: Int): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8816)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with null char (`\u0000`) values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with null char (`\u0000`) values.

@sample samples.collections.Arrays.CopyOfOperations.resizedPrimitiveCopyOf

### 18. Common

```kotlin
public expect fun <T> Array<T>.copyOf(newSize: Int): Array<T?>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8827)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with `null` values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with `null` values.

@sample samples.collections.Arrays.CopyOfOperations.resizingCopyOf

### 19. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun <T> Array<T>.copyOf(newSize: Int, init: (Int) -> T): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8838)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfArrayWithInitializer

### 20. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun ByteArray.copyOf(newSize: Int, init: (Int) -> Byte): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8865)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfByteArrayWithInitializer

### 21. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun ShortArray.copyOf(newSize: Int, init: (Int) -> Short): ShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8892)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfShortArrayWithInitializer

### 22. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun IntArray.copyOf(newSize: Int, init: (Int) -> Int): IntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8919)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfIntArrayWithInitializer

### 23. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun LongArray.copyOf(newSize: Int, init: (Int) -> Long): LongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8946)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfLongArrayWithInitializer

### 24. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun FloatArray.copyOf(newSize: Int, init: (Int) -> Float): FloatArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8973)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfFloatArrayWithInitializer

### 25. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun DoubleArray.copyOf(newSize: Int, init: (Int) -> Double): DoubleArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9000)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfDoubleArrayWithInitializer

### 26. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun BooleanArray.copyOf(newSize: Int, init: (Int) -> Boolean): BooleanArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9027)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfBooleanArrayWithInitializer

### 27. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun CharArray.copyOf(newSize: Int, init: (Int) -> Char): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9054)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfCharArrayWithInitializer

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.copyOf(): UIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4143)

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.copyOf(): ULongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4155)

### 30. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.copyOf(): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4167)

### 31. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.copyOf(): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4179)

### 32. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.copyOf(newSize: Int): UIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4191)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

### 33. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.copyOf(newSize: Int): ULongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4205)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

### 34. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.copyOf(newSize: Int): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4219)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

### 35. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.copyOf(newSize: Int): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4233)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with zero values if necessary.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array, the extra elements in the copy array are filled with zero values.

### 36. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.copyOf(newSize: Int, init: (Int) -> UInt): UIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4247)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfUIntArrayWithInitializer

### 37. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.copyOf(newSize: Int, init: (Int) -> ULong): ULongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4275)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfULongArrayWithInitializer

### 38. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.copyOf(newSize: Int, init: (Int) -> UByte): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4303)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfUByteArrayWithInitializer

### 39. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.copyOf(newSize: Int, init: (Int) -> UShort): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4331)

Returns new array which is a copy of the original array, resized to the given `newSize`.
The copy is either truncated or padded at the end with values calculated by calling the specified `init` function.

- If `newSize` is less than the size of the original array, the copy array is truncated to the `newSize`.
- If `newSize` is greater than the size of the original array,
the extra elements in the copy array are filled with values calculated by calling the specified `init` function.

The function `init` is called sequentially for each array element in range starting from the index corresponding to the source
array size until `newSize`.
It should return the value for an array element given its index.

@sample samples.collections.Arrays.CopyOfOperations.copyOfUShortArrayWithInitializer

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
import kotlin.collections.*

fun main() {
    val source = arrayOf(1, 2, 3)
    val result = source.`copyOf`()
    println(result.contentToString())
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
