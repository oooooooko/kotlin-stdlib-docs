# filterIndexed

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a char sequence containing only those characters from the original char sequence that match the given `predicate`.
@param `predicate` function that takes the index of a character and the character itself
and returns the result of predicate evaluation on the character.

@sample samples.collections.Collections.Filtering.filterIndexed

## Declarations and overloads

### 1. Common

```kotlin
public inline fun CharSequence.filterIndexed(predicate: (index: Int, Char) -> Boolean): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L444)

### 2. Common

```kotlin
public inline fun String.filterIndexed(predicate: (index: Int, Char) -> Boolean): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L455)

Returns a string containing only those characters from the original string that match the given `predicate`.
@param `predicate` function that takes the index of a character and the character itself
and returns the result of predicate evaluation on the character.

@sample samples.collections.Collections.Filtering.filterIndexed

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers: List<Int> = listOf(0, 1, 2, 3, 4, 8, 6)
    val numbersOnSameIndexAsValue = numbers.filterIndexed { index, i -> index == i }

    println(numbersOnSameIndexAsValue)
}
```

```text title="Output"
[0, 1, 2, 3, 4, 6]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1610)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
