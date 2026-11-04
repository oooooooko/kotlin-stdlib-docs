# titlecase

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Converts this character to title case using Unicode mapping rules of the invariant locale.

This function supports one-to-many character mapping, thus the length of the returned string can be greater than one.
For example, `'\uFB00'.titlecase()` returns `"\u0046\u0066"`,
where `'\uFB00'` is the LATIN SMALL LIGATURE FF character (`ﬀ`).
If this character has no title case mapping, the result of `uppercase` is returned instead.

@sample samples.text.Chars.titlecase

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun Char.titlecase(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L194)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('a', 'ǅ', 'ŉ', '+', 'ß')
    val titlecaseChar = chars.map { it.titlecaseChar() }
    val titlecase = chars.map { it.titlecase() }
    println(titlecaseChar)
    println(titlecase)
}
```

```text title="Output"
[A, ǅ, ŉ, +, ß]
[A, ǅ, ʼN, +, Ss]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L131)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
