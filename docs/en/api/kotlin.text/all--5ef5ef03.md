# all

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if all characters match the given `predicate`.

Note that if the char sequence contains no characters, the function returns `true`
because there are no characters in it that _do not_ match the predicate.
See a more detailed explanation of this logic concept in ["Vacuous truth"](https://en.wikipedia.org/wiki/Vacuous_truth) article.

@sample samples.text.Strings.allWithPredicate

## Declarations and overloads

### 1. Common

```kotlin
public inline fun CharSequence.all(predicate: (Char) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L1082)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "Kotlin"
    // All characters are letters
    println(string.all { it.isLetter() })
    // Not all of them are lowercase, though
    println(string.all { it.isLowerCase() })
    // And there are definitely no digits
    println(string.all { it.isDigit() })

    // For an empty string `all` always return `true`
    println("".all { true })
    println("".all { false })
}
```

```text title="Output"
true
false
false
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L470)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
