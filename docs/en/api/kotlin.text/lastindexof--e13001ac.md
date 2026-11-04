# lastIndexOf

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the index within this char sequence of the last occurrence of the specified character,
starting from the specified `startIndex`.

@param startIndex The index of character to start searching at. The search proceeds backward toward the beginning of the string.
@param ignoreCase `true` to ignore character case when matching a character. By default `false`.
@return An index of the last occurrence of `char` or -1 if none is found.

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.lastIndexOf(char: Char, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1152)

### 2. Common

```kotlin
public fun CharSequence.lastIndexOf(string: String, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1167)

Returns the index within this char sequence of the last occurrence of the specified `string`,
starting from the specified `startIndex`.

@param startIndex The index of character to start searching at. The search proceeds backward toward the beginning of the string.
@param ignoreCase `true` to ignore character case when matching a string. By default `false`.
@return An index of the last occurrence of `string` or -1 if none is found.
@sample samples.text.Strings.lastIndexOf

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun matchDetails(inputString: String, whatToFind: String, startIndex: Int = inputString.length - 1): String {
        val matchIndex = inputString.lastIndexOf(whatToFind, startIndex)
        return "Searching for the last '$whatToFind' in '$inputString' starting at position $startIndex: " +
                if (matchIndex >= 0) "Found at $matchIndex" else "Not found"
    }

    val inputString = "Never ever give up"
    val toFind = "ever"

    println(matchDetails(inputString, toFind))
    println(matchDetails(inputString, toFind, 0))
    println(matchDetails(inputString, toFind, 5))
}
```

```text title="Output"
Searching for the last 'ever' in 'Never ever give up' starting at position 17: Found at 6
Searching for the last 'ever' in 'Never ever give up' starting at position 0: Not found
Searching for the last 'ever' in 'Never ever give up' starting at position 5: Found at 1
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L545)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
