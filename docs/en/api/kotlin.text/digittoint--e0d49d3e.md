# digitToInt

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the numeric value of the decimal digit that this Char represents.
Throws an exception if this Char is not a valid decimal digit.

A Char is considered to represent a decimal digit if `isDigit` is true for the Char.
In this case, the Unicode decimal digit value of the character is returned.

@sample samples.text.Chars.digitToInt

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun Char.digitToInt(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L11)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public fun Char.digitToInt(radix: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L27)

Returns the numeric value of the digit that this Char represents in the specified `radix`.
Throws an exception if the `radix` is not in the range `2..36` or if this Char is not a valid digit in the specified `radix`.

A Char is considered to represent a digit in the specified `radix` if at least one of the following is true:
 - `isDigit` is `true` for the Char and the Unicode decimal digit value of the character is less than the specified `radix`. In this case the decimal digit value is returned.
 - The Char is one of the uppercase Latin letters 'A' through 'Z' and its `code` is less than `radix + 'A'.code - 10`. In this case, `this.code - 'A'.code + 10` is returned.
 - The Char is one of the lowercase Latin letters 'a' through 'z' and its `code` is less than `radix + 'a'.code - 10`. In this case, `this.code - 'a'.code + 10` is returned.
 - The Char is one of the fullwidth Latin capital letters '\uFF21' through '\uFF3A' and its `code` is less than `radix + 0xFF21 - 10`. In this case, `this.code - 0xFF21 + 10` is returned.
 - The Char is one of the fullwidth Latin small letters '\uFF41' through '\uFF5A' and its `code` is less than `radix + 0xFF41 - 10`. In this case, `this.code - 0xFF41 + 10` is returned.

@sample samples.text.Chars.digitToInt

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*
import kotlin.test.*



fun main() {
    println('5'.digitToInt())
    println('3'.digitToInt(radix = 8))
    println('A'.digitToInt(radix = 16))
    println('k'.digitToInt(radix = 36))

    // radix argument should be in 2..36
    assertFails { '0'.digitToInt(radix = 1) }
    assertFails { '1'.digitToInt(radix = 100) }
    // only 0 and 1 digits are valid for binary numbers
    assertFails { '5'.digitToInt(radix = 2) }
    // radix = 10 is used by default
    assertFails { 'A'.digitToInt() }
    // symbol '+' is not a digit in any radix
    assertFails { '+'.digitToInt() }
    // Only Latin letters are valid for digits greater than 9.
    assertFails { 'β'.digitToInt(radix = 36) }
}
```

```text title="Output"
5
3
10
20
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L181)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
