# lowercaseChar

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Converts this character to lower case using Unicode mapping rules of the invariant locale.

This function performs one-to-one character mapping.
To support one-to-many character mapping use the `lowercase` function.
If this character has no mapping equivalent, the character itself is returned.

@sample samples.text.Chars.lowercase

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.lowercaseChar(): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L125)

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

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
