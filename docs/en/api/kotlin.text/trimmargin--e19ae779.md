# trimMargin

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Trims leading whitespace characters followed by `marginPrefix` from every line of a source string and removes
the first and the last lines if they are blank (note the difference in `isBlank` vs. `isEmpty`).

Doesn't affect a line if it doesn't contain `marginPrefix` except the first and the last blank lines.

The lines in the original string can be separated with `\r\n` (CRLF), `\n` (LF), or `\r` (CR) characters, however, the lines in the
resulting string will be separated solely with `\n` (LF) character.

@param marginPrefix non-blank string, which is used as a margin delimiter. Default is `|` (pipe character).

@sample samples.text.Strings.trimMargin
@see trimIndent
@see kotlin.text.isWhitespace

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
public fun String.trimMargin(marginPrefix: String = "|"): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Indent.kt#L11)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val withoutMargin1 = """ABC
                    |123
                    |456""".trimMargin()
    println(withoutMargin1)

    val withoutMargin2 = """
        #XYZ
        #foo
        #bar
    """.trimMargin("#")
    println(withoutMargin2)
}
```

```text title="Output"
ABC
123
456
XYZ
foo
bar
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L48)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
