# reverse

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Reverses elements in the array in-place.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<T>.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6606)

### 2. Common

```kotlin
public fun ByteArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6621)

### 3. Common

```kotlin
public fun ShortArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6636)

### 4. Common

```kotlin
public fun IntArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6651)

### 5. Common

```kotlin
public fun LongArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6666)

### 6. Common

```kotlin
public fun FloatArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6681)

### 7. Common

```kotlin
public fun DoubleArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6696)

### 8. Common

```kotlin
public fun BooleanArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6711)

### 9. Common

```kotlin
public fun CharArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6726)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> Array<T>.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6741)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 11. Common

```kotlin
@SinceKotlin("1.4")
public fun ByteArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6764)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 12. Common

```kotlin
@SinceKotlin("1.4")
public fun ShortArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6787)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 13. Common

```kotlin
@SinceKotlin("1.4")
public fun IntArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6810)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 14. Common

```kotlin
@SinceKotlin("1.4")
public fun LongArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6833)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 15. Common

```kotlin
@SinceKotlin("1.4")
public fun FloatArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6856)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 16. Common

```kotlin
@SinceKotlin("1.4")
public fun DoubleArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6879)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 17. Common

```kotlin
@SinceKotlin("1.4")
public fun BooleanArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6902)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 18. Common

```kotlin
@SinceKotlin("1.4")
public fun CharArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6925)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 19. Common

```kotlin
public expect fun <T> MutableList<T>.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1143)

Reverses elements in the list in-place.

### 20. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3235)

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3245)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3255)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reverse(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3265)

### 24. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3275)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 25. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3291)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 26. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3307)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 27. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3323)

Reverses elements of the array in the specified range in-place.

@param fromIndex the start of the range (inclusive) to reverse.
@param toIndex the end of the range (exclusive) to reverse.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

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
    val result = source.`reverse`()
    println(result)
}
```

```text title="Output"
kotlin.Unit
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
