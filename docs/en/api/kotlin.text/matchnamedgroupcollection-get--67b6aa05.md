# MatchNamedGroupCollection.get

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a named group with the specified `name`.
@return An instance of `MatchGroup` if the group with the specified `name` was matched or `null` otherwise.
@throws IllegalArgumentException if there is no group with the specified `name` defined in the regex pattern.
@throws UnsupportedOperationException if this match group collection doesn't support getting match groups by name,
for example, when it's not supported by the current platform.

## Declarations and overloads

### 1. Common

```kotlin
public operator fun get(name: String): MatchGroup?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/regex/MatchResult.kt#L35)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val match = Regex("(?<word>[a-z]+)-(?<number>[0-9]+)").matchEntire("item-42")!!
    println(match.groups["word"]?.value)
    println(match.groups["number"]?.value)
}
```

```text title="Output"
item
42
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
