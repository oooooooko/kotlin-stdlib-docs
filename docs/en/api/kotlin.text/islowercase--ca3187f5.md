# isLowerCase

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if this character is lower case.

A character is considered to be a lower case character if its `category` is `CharCategory.LOWERCASE_LETTER`,
or it has contributory property `Other_Lowercase` as defined by the Unicode Standard.

@sample samples.text.Chars.isLowerCase

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.isLowerCase(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L295)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('a', 'λ', 'A', '1', '+')
    val (lowerCases, notLowerCases) = chars.partition { it.isLowerCase() }
    println(lowerCases)
    println(notLowerCases)
}
```

```text title="Output"
[a, λ]
[A, 1, +]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L77)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
