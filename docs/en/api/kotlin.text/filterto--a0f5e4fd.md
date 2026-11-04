# filterTo

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends all characters matching the given `predicate` to the given `destination`.

@sample samples.collections.Collections.Filtering.filterTo

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : Appendable> CharSequence.filterTo(destination: C, predicate: (Char) -> Boolean): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L510)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers: List<Int> = listOf(1, 2, 3, 4, 5, 6, 7)
    val evenNumbers = mutableListOf<Int>()
    val notMultiplesOf3 = mutableListOf<Int>()

    println(evenNumbers)

    numbers.filterTo(evenNumbers) { it % 2 == 0 }
    numbers.filterNotTo(notMultiplesOf3) { number -> number % 3 == 0 }

    println(evenNumbers)
    println(notMultiplesOf3)
}
```

```text title="Output"
[]
[2, 4, 6]
[1, 2, 4, 5, 7]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1575)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
