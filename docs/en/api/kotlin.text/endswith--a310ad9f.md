# endsWith

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if this string ends with the specified suffix.

@param suffix the suffix with which this string should end with.
@param ignoreCase the flag indicating if the string characters should be compared with the `suffix` characters
 in a case-insensitive manner; by default, comparison is case-sensitive.

@sample samples.text.Strings.endsWithSuffixCaseSensitive
@sample samples.text.Strings.endsWithSuffixCaseInsensitive

## Declarations and overloads

### 1. Common

```kotlin
public expect fun String.endsWith(suffix: String, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L484)

### 2. Common

```kotlin
public fun CharSequence.endsWith(char: Char, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L882)

Returns `true` if this char sequence ends with the specified character.

### 3. Common

```kotlin
public fun CharSequence.endsWith(suffix: CharSequence, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L908)

Returns `true` if this char sequence ends with the specified suffix.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.endsWith("cde"))
    println(str.endsWith("CDE"))
    println(str.endsWith("bcd"))
    println(str.endsWith("_abcde"))
}
```

```text title="Output"
true
false
false
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L908)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.endsWith("cde", ignoreCase = true))
    println(str.endsWith("CDE", ignoreCase = true))
    println(str.endsWith("bcd", ignoreCase = true))
}
```

```text title="Output"
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L917)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
