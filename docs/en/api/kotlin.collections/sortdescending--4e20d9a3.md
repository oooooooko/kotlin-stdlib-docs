# sortDescending

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Sorts elements in the array in-place descending according to their natural sort order.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Comparable<T>> Array<out T>.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7413)

### 2. Common

```kotlin
public fun ByteArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7422)

Sorts elements in the array in-place descending according to their natural sort order.

### 3. Common

```kotlin
public fun ShortArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7432)

Sorts elements in the array in-place descending according to their natural sort order.

### 4. Common

```kotlin
public fun IntArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7442)

Sorts elements in the array in-place descending according to their natural sort order.

### 5. Common

```kotlin
public fun LongArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7452)

Sorts elements in the array in-place descending according to their natural sort order.

### 6. Common

```kotlin
public fun FloatArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7462)

Sorts elements in the array in-place descending according to their natural sort order.

### 7. Common

```kotlin
public fun DoubleArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7472)

Sorts elements in the array in-place descending according to their natural sort order.

### 8. Common

```kotlin
public fun CharArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7482)

Sorts elements in the array in-place descending according to their natural sort order.

### 9. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Comparable<T>> Array<out T>.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9852)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 10. Common

```kotlin
@SinceKotlin("1.4")
public fun ByteArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9869)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 11. Common

```kotlin
@SinceKotlin("1.4")
public fun ShortArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9885)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 12. Common

```kotlin
@SinceKotlin("1.4")
public fun IntArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9901)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 13. Common

```kotlin
@SinceKotlin("1.4")
public fun LongArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9917)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 14. Common

```kotlin
@SinceKotlin("1.4")
public fun FloatArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9933)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 15. Common

```kotlin
@SinceKotlin("1.4")
public fun DoubleArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9949)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 16. Common

```kotlin
@SinceKotlin("1.4")
public fun CharArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9965)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 17. Common

```kotlin
public fun <T : Comparable<T>> MutableList<T>.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1195)

Sorts elements in the list in-place descending according to their natural sort order.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

### 18. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3543)

Sorts elements in the array in-place descending according to their natural sort order.

### 19. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3555)

Sorts elements in the array in-place descending according to their natural sort order.

### 20. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3567)

Sorts elements in the array in-place descending according to their natural sort order.

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sortDescending(): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3579)

Sorts elements in the array in-place descending according to their natural sort order.

### 22. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UIntArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4791)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 23. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun ULongArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4808)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 24. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UByteArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4825)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

### 25. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UShortArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4842)

Sorts elements of the array in the specified range in-place.
The elements are sorted descending according to their natural sort order.

@param fromIndex the start of the range (inclusive) to sort.
@param toIndex the end of the range (exclusive) to sort.

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
    val result = source.`sortDescending`()
    println(result)
}
```

```text title="Output"
kotlin.Unit
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
