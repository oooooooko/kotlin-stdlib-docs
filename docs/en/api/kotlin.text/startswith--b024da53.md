# startsWith

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if this string starts with the specified prefix.

@param prefix the prefix from which this string should start with.
@param ignoreCase the flag indicating if the string characters should be compared with the `prefix` characters
 in a case-insensitive manner; by default, comparison is case-sensitive.

@sample samples.text.Strings.startsWithPrefixCaseSensitive
@sample samples.text.Strings.startsWithPrefixCaseInsensitive

## Declarations and overloads

### 1. Common

```kotlin
public expect fun String.startsWith(prefix: String, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L459)

### 2. Common

```kotlin
public expect fun String.startsWith(prefix: String, startIndex: Int, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L471)

Returns `true` if a substring of this string starting at the specified offset `startIndex` starts with the specified prefix.

@param prefix the prefix from which this string's substring beginning at `startIndex` should start with.
@param startIndex the start index (inclusive).
@param ignoreCase the flag indicating if the string characters should be compared with the `prefix` characters
 in a case-insensitive manner; by default, comparison is case-sensitive.

@sample samples.text.Strings.startsWithPrefixAtPositionCaseSensitive
@sample samples.text.Strings.startsWithPrefixAtPositionCaseInsensitive

### 3. Common

```kotlin
public fun CharSequence.startsWith(char: Char, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L876)

Returns `true` if this char sequence starts with the specified character.

### 4. Common

```kotlin
public fun CharSequence.startsWith(prefix: CharSequence, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L888)

Returns `true` if this char sequence starts with the specified prefix.

### 5. Common

```kotlin
public fun CharSequence.startsWith(prefix: CharSequence, startIndex: Int, ignoreCase: Boolean = false): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L898)

Returns `true` if a substring of this char sequence starting at the specified offset `startIndex` starts with the specified prefix.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.startsWith("abc"))
    println(str.startsWith("ABC"))
    println(str.startsWith("bcd"))
    println(str.startsWith("abcdef"))
}
```

```text title="Output"
true
false
false
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L875)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.startsWith("abc", ignoreCase = true))
    println(str.startsWith("ABC", ignoreCase = true))
    println(str.startsWith("bcd", ignoreCase = true))
}
```

```text title="Output"
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L884)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.startsWith("abc", startIndex = 1))
    println(str.startsWith("BCD", startIndex = 1))
    println(str.startsWith("bcd", startIndex = 1))
}
```

```text title="Output"
false
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L892)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.startsWith("abc", startIndex = 1, ignoreCase = true))
    println(str.startsWith("bcd", startIndex = 1, ignoreCase = true))
    println(str.startsWith("BCD", startIndex = 1, ignoreCase = true))
}
```

```text title="Output"
false
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L900)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
