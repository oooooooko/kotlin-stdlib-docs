# indexOf

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the index within this string of the first occurrence of the specified character, starting from the specified `startIndex`.

@param ignoreCase `true` to ignore character case when matching a character. By default `false`.
@return An index of the first occurrence of `char` or -1 if none is found.

## Declarations and overloads

### 1. Common

```kotlin
public fun CharSequence.indexOf(char: Char, startIndex: Int = 0, ignoreCase: Boolean = false): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1124)

### 2. Common

```kotlin
public fun CharSequence.indexOf(string: String, startIndex: Int = 0, ignoreCase: Boolean = false): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1137)

Returns the index within this char sequence of the first occurrence of the specified `string`,
starting from the specified `startIndex`.

@param ignoreCase `true` to ignore character case when matching a string. By default `false`.
@return An index of the first occurrence of `string` or `-1` if none is found.
@sample samples.text.Strings.indexOf

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun matchDetails(inputString: String, whatToFind: String, startIndex: Int = 0): String {
        val matchIndex = inputString.indexOf(whatToFind, startIndex)
        return "Searching for '$whatToFind' in '$inputString' starting at position $startIndex: " +
                if (matchIndex >= 0) "Found at $matchIndex" else "Not found"
    }

    val inputString = "Never ever give up"
    val toFind = "ever"

    println(matchDetails(inputString, toFind))
    println(matchDetails(inputString, toFind, 2))
    println(matchDetails(inputString, toFind, 10))
}
```

```text title="Output"
Searching for 'ever' in 'Never ever give up' starting at position 0: Found at 1
Searching for 'ever' in 'Never ever give up' starting at position 2: Found at 6
Searching for 'ever' in 'Never ever give up' starting at position 10: Not found
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L529)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
