# thenComparator

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a comparator using the primary comparator and function to calculate a result of comparison.

@sample samples.comparisons.Comparisons.thenComparator

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Comparator<T>.thenComparator(crossinline comparison: (a: T, b: T) -> Int): Comparator<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L187)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("c" to 1, "b" to 2, "a" to 1, "d" to 0, null to 0)

    val valueComparator = compareBy<Pair<String?, Int>> { it.second }
    val map1 = list.sortedWith(valueComparator).toMap()
    println(map1)

    val valueThenKeyComparator = valueComparator
        .thenComparator({ a, b -> compareValues(a.first, b.first) })
    val map2 = list.sortedWith(valueThenKeyComparator).toMap()
    println(map2)
}
```

```text title="Output"
{d=0, null=0, c=1, a=1, b=2}
{null=0, d=0, a=1, c=1, b=2}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L164)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
