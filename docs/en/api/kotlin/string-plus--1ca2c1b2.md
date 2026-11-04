# String.plus

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a string obtained by concatenating this string with the string representation of the given `other` object.

@sample samples.text.Strings.stringPlus

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public operator fun plus(other: Any?): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/String.kt#L16)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("Ko" + "dee")
    // 2 is not a string, but plus concatenates its string representation with the "Kotlin " string
    println("Kotlin " + 2)
    // list is converted to a String first and then concatenated with the "Numbers: " string
    println("Numbers: " + listOf(1, 2, 3))
}
```

```text title="Output"
Kodee
Kotlin 2
Numbers: [1, 2, 3]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1016)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
