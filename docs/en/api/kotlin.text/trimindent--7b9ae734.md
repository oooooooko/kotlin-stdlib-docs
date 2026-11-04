# trimIndent

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Detects a common minimal indent of all the input lines, removes it from every line and also removes the first and the last
lines if they are blank (notice difference blank vs empty).

Note that blank lines do not affect the detected indent level.

In case if there are non-blank lines with no leading whitespace characters (no indent at all) then the
common indent is 0, and therefore this function doesn't change the indentation.

The lines in the original string can be separated with `\r\n` (CRLF), `\n` (LF), or `\r` (CR) characters, however, the lines in the
resulting string will be separated solely with `\n` (LF) character.

@sample samples.text.Strings.trimIndent
@see trimMargin
@see kotlin.text.isBlank

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
public fun String.trimIndent(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Indent.kt#L53)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val withoutIndent =
            """
                ABC
                123
                456
            """.trimIndent()
    println(withoutIndent)
}
```

```text title="Output"
ABC
123
456
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L37)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
