# reduce

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with the first element and applying `operation` from left to right
to current accumulator value and each element.

Throws an exception if this array is empty. If the array can be empty in an expected way,
please use `reduceOrNull` instead. It returns `null` when its receiver is empty.

@param `operation` function that takes current accumulator value and an element,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduce

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <S, T : S> Array<out T>.reduce(operation: (acc: S, T) -> S): S
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22597)

### 2. Common

```kotlin
public inline fun ByteArray.reduce(operation: (acc: Byte, Byte) -> Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22619)

### 3. Common

```kotlin
public inline fun ShortArray.reduce(operation: (acc: Short, Short) -> Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22641)

### 4. Common

```kotlin
public inline fun IntArray.reduce(operation: (acc: Int, Int) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22663)

### 5. Common

```kotlin
public inline fun LongArray.reduce(operation: (acc: Long, Long) -> Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22685)

### 6. Common

```kotlin
public inline fun FloatArray.reduce(operation: (acc: Float, Float) -> Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22707)

### 7. Common

```kotlin
public inline fun DoubleArray.reduce(operation: (acc: Double, Double) -> Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22729)

### 8. Common

```kotlin
public inline fun BooleanArray.reduce(operation: (acc: Boolean, Boolean) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22751)

### 9. Common

```kotlin
public inline fun CharArray.reduce(operation: (acc: Char, Char) -> Char): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22773)

### 10. Common

```kotlin
public inline fun <S, T : S> Iterable<T>.reduce(operation: (acc: S, T) -> S): S
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3100)

Accumulates value starting with the first element and applying `operation` from left to right
to current accumulator value and each element.

Throws an exception if this collection is empty. If the collection can be empty in an expected way,
please use `reduceOrNull` instead. It returns `null` when its receiver is empty.

@param `operation` function that takes current accumulator value and an element,
and calculates the next accumulator value.

@sample samples.collections.Collections.Aggregates.reduce

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reduce(operation: (acc: UInt, UInt) -> UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9935)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reduce(operation: (acc: ULong, ULong) -> ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9960)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reduce(operation: (acc: UByte, UByte) -> UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9985)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reduce(operation: (acc: UShort, UShort) -> UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10010)

### 15. Common

```kotlin
@SinceKotlin("1.1")
public inline fun <S, T : S, K> Grouping<T, K>.reduce(
    operation: (key: K, accumulator: S, element: T) -> S
): Map<K, S>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L192)

Groups elements from the `Grouping` source by key and applies the reducing `operation` to the elements of each group
sequentially starting from the second element of the group,
passing the previously accumulated value and the current element as arguments,
and stores the results in a new map.
An initial value of accumulator is the first element of the group.

@param operation a function that is invoked on each subsequent element of the group with the following parameters:
 - `key`: the key of the group this element belongs to;
 - `accumulator`: the current value of the accumulator of the group;
 - `element`: the element from the source being accumulated.

@return a `Map` associating the key of each group with the result of accumulating the group elements.
@sample samples.collections.Grouping.reduceByMaxVowels

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

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val animals = listOf("raccoon", "reindeer", "cow", "camel", "giraffe", "goat")

    // grouping by first char and collect only max of contains vowels
    val compareByVowelCount = compareBy { s: String -> s.count { it in "aeiou" } }

    val maxVowels = animals.groupingBy { it.first() }.reduce { _, a, b -> maxOf(a, b, compareByVowelCount) }

    println(maxVowels)
}
```

```text title="Output"
{r=reindeer, c=camel, g=giraffe}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/grouping.kt#L111)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
