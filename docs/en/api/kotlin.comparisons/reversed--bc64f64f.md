# reversed

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a comparator that imposes the reverse ordering of this comparator.

 @sample samples.comparisons.Comparisons.reversed

## Declarations and overloads

### 1. Common

```kotlin
@Suppress("EXTENSION_SHADOWED_BY_MEMBER")
public fun <T> Comparator<T>.reversed(): Comparator<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L294)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("aa", "b", "bb", "a")

    val lengthThenString = compareBy<String> { it.length }.thenBy { it }

    val sorted = list.sortedWith(lengthThenString)
    println(sorted)

    val sortedReversed = list.sortedWith(lengthThenString.reversed())
    println(sortedReversed)
}
```

```text title="Output"
[a, b, aa, bb]
[bb, aa, b, a]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L236)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
