# aggregate

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Groups elements from the `Grouping` source by key and applies `operation` to the elements of each group sequentially,
passing the previously accumulated value and the current element as arguments, and stores the results in a new map.

The key for each element is provided by the `Grouping.keyOf` function.

@param operation function is invoked on each element with the following parameters:
 - `key`: the key of the group this element belongs to;
 - `accumulator`: the current value of the accumulator of the group, can be `null` if it's the first `element` encountered in the group;
 - `element`: the element from the source being aggregated;
 - `first`: indicates whether it's the first `element` encountered in the group.

@return a `Map` associating the key of each group with the result of aggregation of the group elements.
@sample samples.collections.Grouping.aggregateByRadix

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
public inline fun <T, K, R> Grouping<T, K>.aggregate(
    operation: (key: K, accumulator: R?, element: T, first: Boolean) -> R
): Map<K, R>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L34)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val numbers = listOf(3, 4, 5, 6, 7, 8, 9)

    val aggregated = numbers.groupingBy { it % 3 }.aggregate { key, accumulator: StringBuilder?, element, first ->
        if (first) // first element
            StringBuilder().append(key).append(":").append(element)
        else
            accumulator!!.append("-").append(element)
    }

    println(aggregated.values)
}
```

```text title="Output"
[0:3-6-9, 1:4-7, 2:5-8]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/grouping.kt#L25)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
