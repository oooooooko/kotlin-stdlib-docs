# uppercase

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Converts this character to upper case using Unicode mapping rules of the invariant locale.

This function supports one-to-many character mapping, thus the length of the returned string can be greater than one.
For example, `'\uFB00'.uppercase()` returns `"\u0046\u0046"`,
where `'\uFB00'` is the LATIN SMALL LIGATURE FF character (`ﬀ`).
If this character has no upper case mapping, the result of `toString()` of this char is returned.

@sample samples.text.Chars.uppercase

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.uppercase(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L169)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public expect fun String.uppercase(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L22)

Returns a copy of this string converted to upper case using Unicode mapping rules of the invariant locale.

This function supports one-to-many and many-to-one character mapping,
thus the length of the returned string can be different from the length of the original string.

@sample samples.text.Strings.uppercase

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('a', 'ω', '1', 'ŉ', 'A', '+', 'ß')
    val uppercaseChar = chars.map { it.uppercaseChar() }
    val uppercase = chars.map { it.uppercase() }
    println(uppercaseChar)
    println(uppercase)
}
```

```text title="Output"
[A, Ω, 1, ŉ, A, +, ß]
[A, Ω, 1, ʼN, A, +, SS]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L85)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("Iced frappé!".uppercase())
}
```

```text title="Output"
ICED FRAPPÉ!
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L286)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
