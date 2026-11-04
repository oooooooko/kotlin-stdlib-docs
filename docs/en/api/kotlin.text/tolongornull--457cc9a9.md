# toLongOrNull

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses the string to a `Long` number or returns `null` if the string is not a valid representation of a `Long`.

The string must consist of an optional leading `+` or `-` sign and decimal digits (`0-9`),
and fit the valid `Long` value range (within `Long.MIN_VALUE..Long.MAX_VALUE`),
otherwise `null` is returned.

@sample samples.text.Numbers.toLongOrNull

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
public fun String.toLongOrNull(): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringNumberConversions.kt#L142)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public fun String.toLongOrNull(radix: Int): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringNumberConversions.kt#L154)

Parses the string as a `Long` number and returns the result
or `null` if the string is not a valid representation of a number.

@throws IllegalArgumentException when `radix` is not a valid radix for string to number conversion.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    println("0".toLongOrNull())
    println("42".toLongOrNull())
    println("042".toLongOrNull())
    println("-42".toLongOrNull())
    // Long.MAX_VALUE
    println("9223372036854775807".toLongOrNull())
    // Long overflow
    println("9223372036854775808".toLongOrNull())
    // 'a' is not a digit
    println("-1a".toLongOrNull())
    // underscore
    println("1_00".toLongOrNull())
    // whitespaces
    println(" 22 ".toLongOrNull())
}
```

```text title="Output"
0
42
42
-42
9223372036854775807
null
null
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/Numbers.kt#L139)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
