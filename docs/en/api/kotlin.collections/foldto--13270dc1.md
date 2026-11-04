# foldTo

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Groups elements from the `Grouping` source by key and applies `operation` to the elements of each group sequentially,
passing the previously accumulated value and the current element as arguments,
and stores the results in the given `destination` map.
An initial value of accumulator is provided by `initialValueSelector` function.

@param initialValueSelector a function that provides an initial value of accumulator for each group.
 It's invoked with parameters:
 - `key`: the key of the group;
 - `element`: the first element being encountered in that group.

If the `destination` map already has a value corresponding to some key, that value is used as an initial value of
the accumulator for that group and the `initialValueSelector` function is not called for that group.

@param operation a function that is invoked on each element with the following parameters:
 - `key`: the key of the group this element belongs to;
 - `accumulator`: the current value of the accumulator of the group;
 - `element`: the element from the source being accumulated.

@return the `destination` map associating the key of each group with the result of accumulating the group elements.
@sample samples.collections.Grouping.foldByEvenLengthWithComputedInitialValueTo

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
public inline fun <T, K, R, M : MutableMap<in K, R>> Grouping<T, K>.foldTo(
    destination: M,
    initialValueSelector: (key: K, element: T) -> R,
    operation: (key: K, accumulator: R, element: T) -> R
): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L114)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public inline fun <T, K, R, M : MutableMap<in K, R>> Grouping<T, K>.foldTo(
    destination: M,
    initialValue: R,
    operation: (accumulator: R, element: T) -> R
): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L166)

Groups elements from the `Grouping` source by key and applies `operation` to the elements of each group sequentially,
passing the previously accumulated value and the current element as arguments,
and stores the results in the given `destination` map.
An initial value of accumulator is the same `initialValue` for each group.

If the `destination` map already has a value corresponding to the key of some group,
that value is used as an initial value of the accumulator for that group.

@param operation a function that is invoked on each element with the following parameters:
 - `accumulator`: the current value of the accumulator of the group;
 - `element`: the element from the source being accumulated.

@return the `destination` map associating the key of each group with the result of accumulating the group elements.
@sample samples.collections.Grouping.foldByEvenLengthWithConstantInitialValueTo

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val fruits = listOf("cherry", "blueberry", "citrus", "apple", "apricot", "banana", "coconut")

    val evenFruits = fruits.groupingBy { it.first() }
        .foldTo(mutableMapOf(), { key, _: String -> key to mutableListOf<String>() },
                { _, accumulator, element ->
                    if (element.length % 2 == 0) accumulator.second.add(element)
                    accumulator
                })

    val sorted = evenFruits.values.sortedBy { it.first }
    println(sorted)

    evenFruits.clear() // evenFruits is a mutable map
}
```

```text title="Output"
[(a, []), (b, [banana]), (c, [cherry, citrus])]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/grouping.kt#L70)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val fruits = listOf("apple", "apricot", "banana", "blueberry", "cherry", "coconut")

    // collect only even length Strings
    val evenFruits = fruits.groupingBy { it.first() }
        .foldTo(mutableMapOf(), emptyList<String>()) { acc, e -> if (e.length % 2 == 0) acc + e else acc }

    println(evenFruits)

    evenFruits.clear() // evenFruits is a mutable map
}
```

```text title="Output"
{a=[], b=[banana], c=[cherry]}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/grouping.kt#L98)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
