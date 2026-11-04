# sortBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Sorts elements in the array in-place according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortBy

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, R : Comparable<R>> Array<out T>.sortBy(crossinline selector: (T) -> R?): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7389)

### 2. Common

```kotlin
public inline fun <T, R : Comparable<R>> MutableList<T>.sortBy(crossinline selector: (T) -> R?): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1171)

Sorts elements in the list in-place according to natural sort order of the value returned by specified `selector` function.

The sort is _stable_. It means that elements for which `selector` returned equal values preserve their order
relative to each other after sorting.

@sample samples.collections.Collections.Sorting.sortBy

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    class Dish(val name: String, val calories: Int, val tasteRate: Float) {
        override fun toString(): String = "Dish($name: $calories cal, taste $tasteRate/5)"
    }

    val fridgeContent = mutableListOf(
        Dish("🍨", 207, 4.7f),
        Dish("🥦", 34, 2.3f),
        Dish("🧃", 34, 4.9f)
    )

    // original order
    println(fridgeContent)

    // sort by taste rate (ascending)
    fridgeContent.sortBy { it.tasteRate }
    println(fridgeContent)

    val breadBoxContent = mutableListOf(
        Dish("🥯", 245, 4.8f),
        Dish("🥨", 100, 5.0f),
        Dish("🥐", 245, 4.9f)
    )

    // original order
    println(breadBoxContent)

    // sort by calories (ascending)
    breadBoxContent.sortBy { it.calories }
    // note that the sorting is stable, so the 🥯 is before the 🥐
    println(breadBoxContent)
}
```

```text title="Output"
[Dish(🍨: 207 cal, taste 4.7/5), Dish(🥦: 34 cal, taste 2.3/5), Dish(🧃: 34 cal, taste 4.9/5)]
[Dish(🥦: 34 cal, taste 2.3/5), Dish(🍨: 207 cal, taste 4.7/5), Dish(🧃: 34 cal, taste 4.9/5)]
[Dish(🥯: 245 cal, taste 4.8/5), Dish(🥨: 100 cal, taste 5.0/5), Dish(🥐: 245 cal, taste 4.9/5)]
[Dish(🥨: 100 cal, taste 5.0/5), Dish(🥯: 245 cal, taste 4.8/5), Dish(🥐: 245 cal, taste 4.9/5)]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1416)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
