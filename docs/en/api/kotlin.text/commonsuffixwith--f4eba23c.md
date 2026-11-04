# commonSuffixWith

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the longest string `suffix` such that this char sequence and `other` char sequence both end with this suffix,
taking care not to split surrogate pairs.
If this and `other` have no common suffix, returns the empty string.

@param ignoreCase `true` to ignore character case when matching a character. By default `false`.
@sample samples.text.Strings.commonSuffixWith

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.commonSuffixWith(other: CharSequence, ignoreCase: Boolean = false): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L942)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("Hot_Tea".commonSuffixWith("iced_tea"))
    println("Hot_Tea".commonSuffixWith("iced_tea", true))
    println("Hot_Tea".commonSuffixWith("Hot_Coffee"))
}
```

```text title="Output"
ea
_Tea
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L439)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
