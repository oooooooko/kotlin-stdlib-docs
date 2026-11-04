# ClosedFloatingPointRange

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents a range of floating point numbers.
Extends `ClosedRange` interface providing custom operation `lessThanOrEquals` for comparing values of range domain type.

This interface is implemented by floating point ranges returned by `Float.rangeTo` and `Double.rangeTo` operators to
achieve IEEE-754 comparison order instead of total order of floating point numbers.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
public interface ClosedFloatingPointRange<T : Comparable<T>> : ClosedRange<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L72)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val range: ClosedFloatingPointRange<Double> = 1.0..3.0
    println(2.0 in range)
    println(range.lessThanOrEquals(1.0, 3.0))
    println(range.lessThanOrEquals(Double.NaN, 3.0))
}
```

```text title="Output"
true
true
false
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
