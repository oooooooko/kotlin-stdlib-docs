# encodeToByteArray

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Encodes this string to an array of bytes in UTF-8 encoding.

Any malformed char sequence is replaced by the replacement byte sequence.

@sample samples.text.Strings.encodeToByteArray

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun String.encodeToByteArray(): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L348)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun String.encodeToByteArray(
    startIndex: Int = 0,
    endIndex: Int = this.length,
    throwOnInvalidSequence: Boolean = false
): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L358)

Encodes this string or its substring to an array of bytes in UTF-8 encoding.

@param startIndex the beginning (inclusive) of the substring to encode, 0 by default.
@param endIndex the end (exclusive) of the substring to encode, length of this string by default.
@param throwOnInvalidSequence specifies whether to throw an exception on malformed char sequence or replace.

@throws IndexOutOfBoundsException if `startIndex` is less than zero or `endIndex` is greater than the length of this string.
@throws IllegalArgumentException if `startIndex` is greater than `endIndex`.
@throws CharacterCodingException if this string contains malformed char sequence and `throwOnInvalidSequence` is true.

@sample samples.text.Strings.encodeToByteArray

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val format = HexFormat { bytes { groupSeparator = " "; bytesPerGroup = 1 } }

    // \u00a0 is a non-breaking space
    val str = "Kòtlin\u00a02.1.255"

    // The original string contains 14 characters, but some of them are represented with multiple UTF-8 code units
    val byteArray = str.encodeToByteArray()
    println(byteArray.toHexString(format))

    // Replacing all "wide" characters with some ASCII ones results in a byte sequence matching the length of the string
    val byteArrayWithAsciiCharacters = str.replace("\u00a0", " ").replace("ò", "o").encodeToByteArray()
    println(byteArrayWithAsciiCharacters.toHexString(format))

    val byteArrayWithVersion = str.encodeToByteArray(startIndex = 7)
    println(byteArrayWithVersion.toHexString(format))

    val byteArrayWithoutTheVersion = str.encodeToByteArray(startIndex = 0, endIndex = 6)
    println(byteArrayWithoutTheVersion.toHexString(format))
}
```

```text title="Output"
4b c3 b2 74 6c 69 6e c2 a0 32 2e 31 2e 32 35 35
4b 6f 74 6c 69 6e 20 32 2e 31 2e 32 35 35
32 2e 31 2e 32 35 35
4b c3 b2 74 6c 69 6e
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L832)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
