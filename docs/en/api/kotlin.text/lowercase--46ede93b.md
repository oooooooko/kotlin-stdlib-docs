# lowercase

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Converts this character to lower case using Unicode mapping rules of the invariant locale.

This function supports one-to-many character mapping, thus the length of the returned string can be greater than one.
For example, `'\u0130'.lowercase()` returns `"\u0069\u0307"`,
where `'\u0130'` is the LATIN CAPITAL LETTER I WITH DOT ABOVE character (`İ`).
If this character has no lower case mapping, the result of `toString()` of this char is returned.

@sample samples.text.Chars.lowercase

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.lowercase(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L137)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public expect fun String.lowercase(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L40)

Returns a copy of this string converted to lower case using Unicode mapping rules of the invariant locale.

This function supports one-to-many and many-to-one character mapping,
thus the length of the returned string can be different from the length of the original string.

@sample samples.text.Strings.lowercase

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('A', 'Ω', '1', 'a', '+', 'İ')
    val lowercaseChar = chars.map { it.lowercaseChar() }
    val lowercase = chars.map { it.lowercase() }
    println(lowercaseChar)
    println(lowercase)
}
```

```text title="Output"
[a, ω, 1, a, +, i]
[a, ω, 1, a, +, i̇]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L104)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("Iced frappé!".lowercase())
}
```

```text title="Output"
iced frappé!
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L281)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
