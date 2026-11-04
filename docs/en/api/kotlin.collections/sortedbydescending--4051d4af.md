# sortedByDescending

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedByDescending

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, R : Comparable<R>> Array<out T>.sortedByDescending(crossinline selector: (T) -> R?): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7850)

### 2. Common

```kotlin
public inline fun <R : Comparable<R>> ByteArray.sortedByDescending(crossinline selector: (Byte) -> R?): List<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7862)

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayByDescending

### 3. Common

```kotlin
public inline fun <R : Comparable<R>> ShortArray.sortedByDescending(crossinline selector: (Short) -> R?): List<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7874)

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayByDescending

### 4. Common

```kotlin
public inline fun <R : Comparable<R>> IntArray.sortedByDescending(crossinline selector: (Int) -> R?): List<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7886)

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayByDescending

### 5. Common

```kotlin
public inline fun <R : Comparable<R>> LongArray.sortedByDescending(crossinline selector: (Long) -> R?): List<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7898)

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayByDescending

### 6. Common

```kotlin
public inline fun <R : Comparable<R>> FloatArray.sortedByDescending(crossinline selector: (Float) -> R?): List<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7910)

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayByDescending

### 7. Common

```kotlin
public inline fun <R : Comparable<R>> DoubleArray.sortedByDescending(crossinline selector: (Double) -> R?): List<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7922)

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayByDescending

### 8. Common

```kotlin
public inline fun <R : Comparable<R>> BooleanArray.sortedByDescending(crossinline selector: (Boolean) -> R?): List<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7934)

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayByDescending

### 9. Common

```kotlin
public inline fun <R : Comparable<R>> CharArray.sortedByDescending(crossinline selector: (Char) -> R?): List<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7946)

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayByDescending

### 10. Common

```kotlin
public inline fun <T, R : Comparable<R>> Iterable<T>.sortedByDescending(crossinline selector: (T) -> R?): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1230)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    class Dish(val name: String, val calories: Int, val tasteRate: Float) {
        override fun toString(): String = "Dish($name: $calories cal, taste $tasteRate/5)"
    }

    val fridgeContent = listOf(Dish("🥦", 34, 2.3f), Dish("🧃", 34, 4.9f), Dish("🍨", 207, 4.7f))

    val tastyDishes = fridgeContent.sortedByDescending { it.tasteRate }
    println(tastyDishes)

    val energeticDishes = fridgeContent.sortedByDescending { it.calories }
    // note that the sorting is stable, so the 🥦 is before the 🧃
    println(energeticDishes)

    // the original collection remains unchanged
    println(fridgeContent)
}
```

```text title="Output"
[Dish(🧃: 34 cal, taste 4.9/5), Dish(🍨: 207 cal, taste 4.7/5), Dish(🥦: 34 cal, taste 2.3/5)]
[Dish(🍨: 207 cal, taste 4.7/5), Dish(🥦: 34 cal, taste 2.3/5), Dish(🧃: 34 cal, taste 4.9/5)]
[Dish(🥦: 34 cal, taste 2.3/5), Dish(🧃: 34 cal, taste 4.9/5), Dish(🍨: 207 cal, taste 4.7/5)]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1523)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val unsorted = intArrayOf(3, 1, 2, 4)

    val sortedByValue = unsorted.sortedByDescending { it % 3 }
    // the sorting is stable: the order of 1 (1 % 3 == 1) and 4 (4 % 3 == 1) was preserved
    println(sortedByValue)

    val mapping = mapOf(1 to "one", 2 to "two", 3 to "three", 4 to "four")
    val sortedByPronunciation = unsorted.sortedByDescending {
        // take a key to sort by from the mapping
        mapping.getOrDefault(it, "unknown")
    }
    // two > three > one > four, lexicographically
    println(sortedByPronunciation)

    // the original array remains unchanged
    println(unsorted.toList())
}
```

```text title="Output"
[2, 1, 4, 3]
[2, 3, 1, 4]
[3, 1, 2, 4]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1542)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
