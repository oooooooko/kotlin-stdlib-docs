# mapIndexedNotNullTo

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Applies the given `transform` function to each element and its index in the original array
and appends only the non-null results to the given `destination`.
@param `transform` function that takes the index of an element and the element itself
and returns the result of the transform applied to the element.

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, R : Any, C : MutableCollection<in R>> Array<out T>.mapIndexedNotNullTo(destination: C, transform: (index: Int, T) -> R?): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13033)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, R : Any, C : MutableCollection<in R>> Iterable<T>.mapIndexedNotNullTo(destination: C, transform: (index: Int, T) -> R?): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1768)

Applies the given `transform` function to each element and its index in the original collection
and appends only the non-null results to the given `destination`.
@param `transform` function that takes the index of an element and the element itself
and returns the result of the transform applied to the element.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    println(listOf(1, 2).flatMapTo(mutableListOf<Int>()) { listOf(it, -it) })
    println(listOf(1, 2).flatMapIndexedTo(mutableListOf<Int>()) { index, value -> listOf(index, value) })
    println(listOf(1, 2).mapTo(mutableListOf<String>()) { "v$it" })
    println(listOf(1, 2).mapIndexedTo(mutableListOf<String>()) { index, value -> "$index:$value" })
    println(listOf(1, 2).mapNotNullTo(mutableListOf<Int>()) { it.takeIf { n -> n > 1 } })
    println(listOf(1, 2).mapIndexedNotNullTo(mutableListOf<Int>()) { index, value -> value.takeIf { index > 0 } })
    val values = linkedMapOf("a" to 1, "b" to 2)
    println(values.mapKeysTo(linkedMapOf<String, Int>()) { it.key.uppercase() })
    println(values.mapValues { it.value * 10 })
    println(values.mapValuesTo(linkedMapOf<String, Int>()) { it.value * 10 })
}
```

```text title="Output"
[1, -1, 2, -2]
[0, 1, 1, 2]
[v1, v2]
[0:1, 1:2]
[2]
[2]
{A=1, B=2}
{a=10, b=20}
{a=10, b=20}
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
