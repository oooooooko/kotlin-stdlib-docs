# MatchResult.Destructured.component1

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
        public operator inline fun component1():  String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/regex/MatchResult.kt#L98)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val match = Regex("(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)").matchEntire("abcdefghij")!!
    val groups = match.destructured
    val (a, b, c, d, e, f, g, h, i, j) = groups
    println(listOf(a, b, c, d, e, f, g, h, i, j))
    println(groups.toList())
    println(groups.match.value)
}
```

```text title="Output"
[a, b, c, d, e, f, g, h, i, j]
[a, b, c, d, e, f, g, h, i, j]
abcdefghij
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
