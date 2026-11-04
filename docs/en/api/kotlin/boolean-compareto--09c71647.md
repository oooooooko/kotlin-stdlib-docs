# Boolean.compareTo

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Compares this `Boolean` with the specified `Boolean``other` for order. Returns zero if both are equal to each other,
a negative number if `this``Boolean` is `false` and `other` is `true`,
or a positive number if `this``Boolean` is `true` and `other` is `false`.

In other words, `false` is considered to be "less than" `true`.

@sample samples.misc.BooleanSamples.compareTo

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public override fun compareTo(other: Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Boolean.kt#L38)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertTrue



fun main() {
    // false is equal to false, and true is equal to true
    println(false.compareTo(false))
    println(true.compareTo(true))

    // But false is less than true, and true is greater than false
    println(false.compareTo(true) < 0)
    println(true.compareTo(false) > 0)
}
```

```text title="Output"
0
0
true
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/BooleanSamples.kt#L12)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
