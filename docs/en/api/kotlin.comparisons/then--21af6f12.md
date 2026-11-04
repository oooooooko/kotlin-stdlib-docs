# then

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Combines this comparator and the given `comparator` such that the latter is applied only
when the former considered values equal.

@sample samples.comparisons.Comparisons.then

## Declarations and overloads

### 1. Common

```kotlin
public infix fun <T> Comparator<T>.then(comparator: Comparator<in T>): Comparator<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L199)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("A", "aa", "b", "bb", "a")

    val lengthThenCaseInsensitive = compareBy<String> { it.length }
        .then(String.CASE_INSENSITIVE_ORDER)

    val sorted = list.sortedWith(lengthThenCaseInsensitive)

    println(sorted)
}
```

```text title="Output"
[A, a, b, aa, bb]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L178)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
