# sortedBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedBy

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, R : Comparable<R>> Array<out T>.sortedBy(crossinline selector: (T) -> R?): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7742)

### 2. Common

```kotlin
public inline fun <R : Comparable<R>> ByteArray.sortedBy(crossinline selector: (Byte) -> R?): List<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7754)

Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayBy

### 3. Common

```kotlin
public inline fun <R : Comparable<R>> ShortArray.sortedBy(crossinline selector: (Short) -> R?): List<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7766)

Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayBy

### 4. Common

```kotlin
public inline fun <R : Comparable<R>> IntArray.sortedBy(crossinline selector: (Int) -> R?): List<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7778)

Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayBy

### 5. Common

```kotlin
public inline fun <R : Comparable<R>> LongArray.sortedBy(crossinline selector: (Long) -> R?): List<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7790)

Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayBy

### 6. Common

```kotlin
public inline fun <R : Comparable<R>> FloatArray.sortedBy(crossinline selector: (Float) -> R?): List<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7802)

Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayBy

### 7. Common

```kotlin
public inline fun <R : Comparable<R>> DoubleArray.sortedBy(crossinline selector: (Double) -> R?): List<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7814)

Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayBy

### 8. Common

```kotlin
public inline fun <R : Comparable<R>> BooleanArray.sortedBy(crossinline selector: (Boolean) -> R?): List<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7826)

Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayBy

### 9. Common

```kotlin
public inline fun <R : Comparable<R>> CharArray.sortedBy(crossinline selector: (Char) -> R?): List<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7838)

Returns a list of all elements sorted according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortedPrimitiveArrayBy

### 10. Common

```kotlin
public inline fun <T, R : Comparable<R>> Iterable<T>.sortedBy(crossinline selector: (T) -> R?): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1218)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    class Dish(val name: String, val calories: Int, val tasteRate: Float) {
        override fun toString(): String = "Dish($name: $calories cal, taste $tasteRate/5)"
    }

    val fridgeContent = listOf(Dish("🍨", 207, 4.7f), Dish("🥦", 34, 2.3f), Dish("🧃", 34, 4.9f))

    val dullDishes = fridgeContent.sortedBy { it.tasteRate }
    println(dullDishes)

    val lightDishes = fridgeContent.sortedBy { it.calories }
    // note that the sorting is stable, so the 🥦 is before the 🧃
    println(lightDishes)

    // the original collection remains unchanged
    println(fridgeContent)
}
```

```text title="Output"
[Dish(🥦: 34 cal, taste 2.3/5), Dish(🍨: 207 cal, taste 4.7/5), Dish(🧃: 34 cal, taste 4.9/5)]
[Dish(🥦: 34 cal, taste 2.3/5), Dish(🧃: 34 cal, taste 4.9/5), Dish(🍨: 207 cal, taste 4.7/5)]
[Dish(🍨: 207 cal, taste 4.7/5), Dish(🥦: 34 cal, taste 2.3/5), Dish(🧃: 34 cal, taste 4.9/5)]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1484)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val unsorted = intArrayOf(3, 1, 2, 4)

    val sortedByRemainder = unsorted.sortedBy { it % 3 }
    // the sorting is stable: the order of 1 (1 % 3 == 1) and 4 (4 % 3 == 1) was preserved
    println(sortedByRemainder)

    val mapping = mapOf(1 to "one", 2 to "two", 3 to "three", 4 to "four")
    val sortedByPronunciation = unsorted.sortedBy {
        // take a key to sort by from the mapping
        mapping.getOrDefault(it, "unknown")
    }
    // four < one < three < two, lexicographically
    println(sortedByPronunciation)

    // the original array remains unchanged
    println(unsorted.toList())
}
```

```text title="Output"
[3, 1, 4, 2]
[4, 1, 3, 2]
[3, 1, 2, 4]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1503)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
