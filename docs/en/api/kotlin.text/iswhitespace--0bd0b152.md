# isWhitespace

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Determines whether a character is whitespace.

A character is considered whitespace if either its Unicode `category``Char.category`
is one of `CharCategory.SPACE_SEPARATOR`, `CharCategory.LINE_SEPARATOR`, `CharCategory.PARAGRAPH_SEPARATOR`,
or it is a `CharCategory.CONTROL` character in range `U+0009..U+000D` or `U+001C..U+001F`.

Returns `true` if the character is whitespace.

@sample samples.text.Chars.isWhitespace

## Declarations and overloads

### 1. Common

```kotlin
public expect fun Char.isWhitespace(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L327)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf(' ', '\t', '\n', '1', 'a', '\u00A0')
    val (whitespaces, notWhitespaces) = chars.partition { it.isWhitespace() }
    // whitespace char codes
    println(whitespaces.map(Char::code))
    // non-whitespace chars
    println(notWhitespaces)
}
```

```text title="Output"
[32, 9, 10, 160]
[1, a]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L59)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
