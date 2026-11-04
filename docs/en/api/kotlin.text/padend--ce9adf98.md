# padEnd

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a char sequence with content of this char sequence padded at the end
to the specified `length` with the specified character or space.

@param length the desired string length.
@param padChar the character to pad string with, if it has length less than the `length` specified. Space is used by default.
@return Returns a char sequence of length at least `length` consisting of `this` char sequence appended with `padChar` as many times
as are necessary to reach that length.
@sample samples.text.Strings.padEnd

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.padEnd(length: Int, padChar: Char = ' '): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L240)

### 2. Common

```kotlin
public fun String.padEnd(length: Int, padChar: Char = ' '): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L263)

Pads the string to the specified `length` at the end with the specified character or space.

@param length the desired string length.
@param padChar the character to pad string with, if it has length less than the `length` specified. Space is used by default.
@return Returns a string of length at least `length` consisting of `this` string appended with `padChar` as many times
as are necessary to reach that length.
@sample samples.text.Strings.padEnd

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val padWithSpace = "125".padEnd(5)
    println("'$padWithSpace'")

    val padWithChar = "a".padEnd(5, '.')
    println("'$padWithChar'")

    // string is returned as is, when its length is greater than the specified
    val noPadding = "abcde".padEnd(3)
    println("'$noPadding'")
}
```

```text title="Output"
'125  '
'a....'
'abcde'
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L304)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
