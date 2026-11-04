# toShort

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses the string to a `Short` number.

The string must consist of an optional leading `+` or `-` sign and decimal digits (`0-9`),
and fit the valid `Short` value range (within `Short.MIN_VALUE..Short.MAX_VALUE`),
otherwise a `NumberFormatException` will be thrown.

@throws NumberFormatException if the string is not a valid representation of a `Short`.
@sample samples.text.Numbers.toShort

## Declarations and overloads

### 1. Common

```kotlin
public expect fun String.toShort(): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L569)

### 2. Common

```kotlin
public expect fun String.toShort(radix: Int): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L581)

Parses the string as a `Short` number and returns the result.
@throws NumberFormatException if the string is not a valid representation of a number.
@throws IllegalArgumentException when `radix` is not a valid radix for string to number conversion.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    println("0".toShort())
    println("42".toShort())
    println("042".toShort())
    println("-42".toShort())
    // Short.MAX_VALUE
    println("32767".toShort())
    // Short overflow
    assertFailsWith<NumberFormatException> { "32768".toShort() }
    // 'a' is not a digit
    assertFailsWith<NumberFormatException> { "-1a".toShort() }
    // underscore
    assertFailsWith<NumberFormatException> { "1_000".toShort() }
    // whitespaces
    assertFailsWith<NumberFormatException> { " 1000 ".toShort() }
}
```

```text title="Output"
0
42
42
-42
32767
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/Numbers.kt#L49)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
