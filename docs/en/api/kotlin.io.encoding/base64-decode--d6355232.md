# Base64.decode

`kotlin.io.encoding` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Decodes symbols from the specified `source` array or its subrange.
Returns a `ByteArray` containing the resulting bytes.

The requirement, prohibition, or optionality of padding in the input symbols
is determined by the `PaddingOption` set for this `Base64` instance.

@param source the array to decode symbols from.
@param startIndex the beginning (inclusive) of the subrange to decode, 0 by default.
@param endIndex the end (exclusive) of the subrange to decode, size of the `source` array by default.

@throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` array indices.
@throws IllegalArgumentException when `startIndex > endIndex`.
@throws IllegalArgumentException when the symbols for decoding are not padded as required by the `PaddingOption`
  set for this `Base64` instance, or when there are extra symbols after the padding.

@return a `ByteArray` with the resulting bytes.

@sample samples.io.encoding.Base64Samples.decodeFromByteArraySample

## Declarations and overloads

### 1. Common

```kotlin
public fun decode(source: ByteArray, startIndex: Int = 0, endIndex: Int = source.size): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L264)

### 2. Common

```kotlin
public fun decode(source: CharSequence, startIndex: Int = 0, endIndex: Int = source.length): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L334)

Decodes symbols from the specified `source` char sequence or its substring.
Returns a `ByteArray` containing the resulting bytes.

The requirement, prohibition, or optionality of padding in the input symbols
is determined by the `PaddingOption` set for this `Base64` instance.

@param source the char sequence to decode symbols from.
@param startIndex the beginning (inclusive) of the substring to decode, 0 by default.
@param endIndex the end (exclusive) of the substring to decode, length of the `source` by default.

@throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` indices.
@throws IllegalArgumentException when `startIndex > endIndex`.
@throws IllegalArgumentException when the symbols for decoding are not padded as required by the `PaddingOption`
  set for this `Base64` instance, or when there are extra symbols after the padding.

@return a `ByteArray` with the resulting bytes.

@sample samples.io.encoding.Base64Samples.decodeFromStringSample

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    // get a byte array filled with data, for instance, by reading it from a network
    val data = byteArrayOf(0x61, 0x47, 0x56, 0x73, 0x62, 0x47, 0x38, 0x3d)
    // decode data from the array
    println(Base64.decode(data).contentEquals("hello".encodeToByteArray()))

    val dataInTheMiddle = byteArrayOf(0x00, 0x00, 0x61, 0x47, 0x56, 0x73, 0x62, 0x47, 0x38, 0x3d, 0x00, 0x00)
    // decode base64-encoded data from the middle of a buffer
    val decoded = Base64.decode(dataInTheMiddle, startIndex = 2, endIndex = 10)
    println(decoded.contentEquals("hello".encodeToByteArray()))
}
```

```text title="Output"
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L317)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    println(Base64.decode("/wD+AP0=").contentEquals(byteArrayOf(-1, 0, -2, 0, -3)))

    val embeddedB64 = "Data is: \"/wD+AP0=\""
    // find '"' indices and extract base64-encoded data in between
    val decoded = Base64.decode(
        embeddedB64,
        startIndex = embeddedB64.indexOf('"') + 1,
        endIndex = embeddedB64.lastIndexOf('"')
    )
    println(decoded.contentEquals(byteArrayOf(-1, 0, -2, 0, -3)))
}
```

```text title="Output"
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L330)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
