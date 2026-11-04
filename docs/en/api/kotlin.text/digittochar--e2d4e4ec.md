# digitToChar

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the Char that represents this decimal digit.
Throws an exception if this value is not in the range `0..9`.

If this value is in `0..9`, the decimal digit Char with code `'0'.code + this` is returned.

@sample samples.text.Chars.digitToChar

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun Int.digitToChar(): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L78)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public fun Int.digitToChar(radix: Int): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L94)

Returns the Char that represents this numeric digit value in the specified `radix`.
Throws an exception if the `radix` is not in the range `2..36` or if this value is not in the range `0 until radix`.

If this value is less than `10`, the decimal digit Char with code `'0'.code + this` is returned.
Otherwise, the uppercase Latin letter with code `'A'.code + this - 10` is returned.

@sample samples.text.Chars.digitToChar

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*
import kotlin.test.*



fun main() {
    println(5.digitToChar())
    println(3.digitToChar(radix = 8))
    println(10.digitToChar(radix = 16))
    println(20.digitToChar(radix = 36))

    // radix argument should be in 2..36
    assertFails { 0.digitToChar(radix = 1) }
    assertFails { 1.digitToChar(radix = 100) }
    // only 0 and 1 digits are valid for binary numbers
    assertFails { 5.digitToChar(radix = 2) }
    // radix = 10 is used by default
    assertFails { 10.digitToChar() }
    // a negative integer is not a digit in any radix
    assertFails { (-1).digitToChar() }
}
```

```text title="Output"
5
3
A
K
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L221)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
