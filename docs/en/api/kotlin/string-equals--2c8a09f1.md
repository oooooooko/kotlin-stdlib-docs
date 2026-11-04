# String.equals

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Indicates if `other` object is equal to this `String`.

An `other` object is equal to this `String` if and only if it is also a `String`,
it has the same `length` as this String,
and characters at the same positions in each string are equal to each other.

@sample samples.text.Strings.stringEquals

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public override fun equals(other: Any?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/String.kt#L43)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("" == "")
    println("abc" == "abc")

    println("abc" == "abcd")
    println("abc" == "Abc")
    // If a character's case doesn't matter, strings could be compared in a case-insensitive manner
    println("abc".equals("Abc", ignoreCase = true))

    val builder = StringBuilder("abc")
    println(builder)
    // Although the builder holds the same character sequence, it is not a String
    println("abc".equals(builder))
}
```

```text title="Output"
true
true
false
false
true
abc
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L999)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
