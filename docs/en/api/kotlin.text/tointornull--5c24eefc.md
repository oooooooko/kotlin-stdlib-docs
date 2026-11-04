# toIntOrNull

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses the string to an `Int` number or returns `null` if the string is not a valid representation of an `Int`.

The string must consist of an optional leading `+` or `-` sign and decimal digits (`0-9`),
and fit the valid `Int` value range (within `Int.MIN_VALUE..Int.MAX_VALUE`),
otherwise `null` is returned.

@sample samples.text.Numbers.toIntOrNull

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
public fun String.toIntOrNull(): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringNumberConversions.kt#L62)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public fun String.toIntOrNull(radix: Int): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringNumberConversions.kt#L74)

Parses the string as an `Int` number and returns the result
or `null` if the string is not a valid representation of a number.

@throws IllegalArgumentException when `radix` is not a valid radix for string to number conversion.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    println("0".toIntOrNull())
    println("42".toIntOrNull())
    println("042".toIntOrNull())
    println("-42".toIntOrNull())
    // Int.MAX_VALUE
    println("2147483647".toIntOrNull())
    // Int overflow
    println("2147483648".toIntOrNull())
    // 'a' is not a digit
    println("-1a".toIntOrNull())
    // underscore
    println("1_00".toIntOrNull())
    // whitespaces
    println(" 22 ".toIntOrNull())
}
```

```text title="Output"
0
42
42
-42
2147483647
null
null
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/Numbers.kt#L103)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
