# minBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the first element yielding the smallest value of the given `selector` function.

If there are multiple equal minimal values returned by the `selector` function,
this function returns the first of elements corresponding to these values.

Note that the function `selector` is not invoked when the array contains zero or one elements
because in these cases it is clear which element to return without invoking the `selector`.
Therefore it's recommended to avoid relying on side effects being performed by the `selector` function on each element.

@throws NoSuchElementException if the array is empty.

@sample samples.collections.Collections.Aggregates.minMaxByOrNull

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <T, R : Comparable<R>> Array<out T>.minBy(selector: (T) -> R): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19475)

### 2. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> ByteArray.minBy(selector: (Byte) -> R): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19509)

### 3. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> ShortArray.minBy(selector: (Short) -> R): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19543)

### 4. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> IntArray.minBy(selector: (Int) -> R): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19577)

### 5. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> LongArray.minBy(selector: (Long) -> R): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19611)

### 6. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> FloatArray.minBy(selector: (Float) -> R): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19645)

### 7. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> DoubleArray.minBy(selector: (Double) -> R): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19679)

### 8. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> BooleanArray.minBy(selector: (Boolean) -> R): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19713)

### 9. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> CharArray.minBy(selector: (Char) -> R): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19747)

### 10. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <T, R : Comparable<R>> Iterable<T>.minBy(selector: (T) -> R): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2705)

Returns the first element yielding the smallest value of the given `selector` function.

If there are multiple equal minimal values returned by the `selector` function,
this function returns the first of elements corresponding to these values.

Note that the function `selector` is not invoked when the collection contains zero or one elements
because in these cases it is clear which element to return without invoking the `selector`.
Therefore it's recommended to avoid relying on side effects being performed by the `selector` function on each element.

@throws NoSuchElementException if the collection is empty.

@sample samples.collections.Collections.Aggregates.minMaxByOrNull

### 11. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow")
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <K, V, R : Comparable<R>> Map<out K, V>.minBy(selector: (Map.Entry<K, V>) -> R): Map.Entry<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L422)

Returns the first entry yielding the smallest value of the given `selector` function.

If there are multiple equal minimal values returned by the `selector` function,
this function returns the first of entries corresponding to these values.

Note that the function `selector` is not invoked when the map contains zero or one entries
because in these cases it is clear which entry to return without invoking the `selector`.
Therefore it's recommended to avoid relying on side effects being performed by the `selector` function on each entry.

@throws NoSuchElementException if the map is empty.

@sample samples.collections.Collections.Aggregates.minMaxByOrNull

### 12. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow-U")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> UIntArray.minBy(selector: (UInt) -> R): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8467)

### 13. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow-U")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> ULongArray.minBy(selector: (ULong) -> R): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8503)

### 14. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow-U")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> UByteArray.minBy(selector: (UByte) -> R): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8539)

### 15. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minByOrThrow-U")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <R : Comparable<R>> UShortArray.minBy(selector: (UShort) -> R): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8575)

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
