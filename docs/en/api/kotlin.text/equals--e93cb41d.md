# equals

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if this string is equal to `other`, optionally ignoring character case.

Two strings are considered to be equal if they have the same length and the same character at the same index.
If `ignoreCase` is true, the result of `Char.uppercaseChar().lowercaseChar()` on each character is compared.

@param ignoreCase `true` to ignore character case when comparing strings. By default `false`.

## Declarations and overloads

### 1. Common

```kotlin
public expect fun String?.equals(other: String?, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L440)

### 2. Common

```kotlin
public fun Char.equals(other: Char, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L215)

Returns `true` if this character is equal to the `other` character, optionally ignoring character case.

Two characters are considered equal ignoring case if `Char.uppercaseChar().lowercaseChar()` on each character produces the same result.

@param ignoreCase `true` to ignore character case when comparing characters. By default `false`.
@sample samples.text.Chars.equals

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    println('a'.equals('a', false))
    println('a'.equals('A', false))
    println('a'.equals('A', true))
}
```

```text title="Output"
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L156)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
