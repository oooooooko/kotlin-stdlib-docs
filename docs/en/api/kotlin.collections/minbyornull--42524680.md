# minByOrNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the first element yielding the smallest value of the given `selector` function or `null` if there are no elements.

If there are multiple equal minimal values returned by the `selector` function,
this function returns the first of elements corresponding to these values.

Note that the function `selector` is not invoked when the array contains zero or one elements
because in these cases it is clear which element to return without invoking the `selector`.
Therefore it's recommended to avoid relying on side effects being performed by the `selector` function on each element.

@sample samples.collections.Collections.Aggregates.minMaxByOrNull

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <T, R : Comparable<R>> Array<out T>.minByOrNull(selector: (T) -> R): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19781)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> ByteArray.minByOrNull(selector: (Byte) -> R): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19811)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> ShortArray.minByOrNull(selector: (Short) -> R): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19841)

### 4. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> IntArray.minByOrNull(selector: (Int) -> R): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19871)

### 5. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> LongArray.minByOrNull(selector: (Long) -> R): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19901)

### 6. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> FloatArray.minByOrNull(selector: (Float) -> R): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19931)

### 7. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> DoubleArray.minByOrNull(selector: (Double) -> R): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19961)

### 8. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> BooleanArray.minByOrNull(selector: (Boolean) -> R): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19991)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <R : Comparable<R>> CharArray.minByOrNull(selector: (Char) -> R): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L20021)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <T, R : Comparable<R>> Iterable<T>.minByOrNull(selector: (T) -> R): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2739)

Returns the first element yielding the smallest value of the given `selector` function or `null` if there are no elements.

If there are multiple equal minimal values returned by the `selector` function,
this function returns the first of elements corresponding to these values.

Note that the function `selector` is not invoked when the collection contains zero or one elements
because in these cases it is clear which element to return without invoking the `selector`.
Therefore it's recommended to avoid relying on side effects being performed by the `selector` function on each element.

@sample samples.collections.Collections.Aggregates.minMaxByOrNull

### 11. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun <K, V, R : Comparable<R>> Map<out K, V>.minByOrNull(selector: (Map.Entry<K, V>) -> R): Map.Entry<K, V>?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L444)

Returns the first entry yielding the smallest value of the given `selector` function or `null` if there are no entries.

If there are multiple equal minimal values returned by the `selector` function,
this function returns the first of entries corresponding to these values.

Note that the function `selector` is not invoked when the map contains zero or one entries
because in these cases it is clear which entry to return without invoking the `selector`.
Therefore it's recommended to avoid relying on side effects being performed by the `selector` function on each entry.

@sample samples.collections.Collections.Aggregates.minMaxByOrNull

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UIntArray.minByOrNull(selector: (UInt) -> R): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8611)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> ULongArray.minByOrNull(selector: (ULong) -> R): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8643)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UByteArray.minByOrNull(selector: (UByte) -> R): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8675)

### 15. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R : Comparable<R>> UShortArray.minByOrNull(selector: (UShort) -> R): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8707)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val strings = listOf("abcd", "abc", "ab", "de", "abcde")

    val longestString = strings.maxBy { it.length }
    println(longestString)

    val shortestString = strings.minBy { it.length }
    println(shortestString)

    val emptyList = emptyList<String>()
    // maxBy() and minBy() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.maxBy { it.length } }
    assertFailsWith<NoSuchElementException> { emptyList.minBy { it.length } }
    // maxByOrNull() and minByOrNull() return null if the collection is empty
    println(emptyList.maxByOrNull { it.length })
    println(emptyList.minByOrNull { it.length })
}
```

```text title="Output"
abcde
ab
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1218)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
