# compareValues

`kotlin.comparisons` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Compares two nullable `Comparable` values. Null is considered less than any value.

@sample samples.comparisons.Comparisons.compareValues

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Comparable<*>> compareValues(a: T?, b: T?): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L67)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(compareValues(null, 1) < 0)
    println(compareValues(1, 2) < 0)
    println(compareValues(2, 1) > 0)
    println(compareValues(1, 1) == 0)
}
```

```text title="Output"
true
true
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L58)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
