# isLetter

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if this character is a letter.

A character is considered to be a letter if its `category` is `CharCategory.UPPERCASE_LETTER`,
`CharCategory.LOWERCASE_LETTER`, `CharCategory.TITLECASE_LETTER`, `CharCategory.MODIFIER_LETTER`, or `CharCategory.OTHER_LETTER`.

@sample samples.text.Chars.isLetter

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.isLetter(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L252)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('a', 'β', '+', '1')
    val (letters, notLetters) = chars.partition { it.isLetter() }
    println(letters)
    println(notLetters)
}
```

```text title="Output"
[a, β]
[+, 1]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L9)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
