# Base64.decodeIntoByteArray

`kotlin.io.encoding` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Decodes symbols from the specified `source` array or its subrange and writes resulting bytes into the `destination` array.
Returns the number of bytes written.

The requirement, prohibition, or optionality of padding in the input symbols
is determined by the `PaddingOption` set for this `Base64` instance.

@param source the array to decode symbols from.
@param destination the array to write bytes into.
@param destinationOffset the starting index in the `destination` array to write bytes to, 0 by default.
@param startIndex the beginning (inclusive) of the subrange to decode, 0 by default.
@param endIndex the end (exclusive) of the subrange to decode, size of the `source` array by default.

@throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` array indices.
@throws IllegalArgumentException when `startIndex > endIndex`.
@throws IndexOutOfBoundsException when the resulting bytes don't fit into the `destination` array starting at the specified `destinationOffset`,
or when that index is out of the `destination` array indices range.
@throws IllegalArgumentException when the symbols for decoding are not padded as required by the `PaddingOption`
  set for this `Base64` instance, or when there are extra symbols after the padding.

@return the number of bytes written into `destination` array.

@sample samples.io.encoding.Base64Samples.decodeIntoByteArrayFromByteArraySample

## Declarations and overloads

### 1. Common

```kotlin
public fun decodeIntoByteArray(
        source: ByteArray,
        destination: ByteArray,
        destinationOffset: Int = 0,
        startIndex: Int = 0,
        endIndex: Int = source.size
    ): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L297)

### 2. Common

```kotlin
public fun decodeIntoByteArray(
        source: CharSequence,
        destination: ByteArray,
        destinationOffset: Int = 0,
        startIndex: Int = 0,
        endIndex: Int = source.length
    ): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L359)

Decodes symbols from the specified `source` char sequence or its substring and writes resulting bytes into the `destination` array.
Returns the number of bytes written.

The requirement, prohibition, or optionality of padding in the input symbols
is determined by the `PaddingOption` set for this `Base64` instance.

@param source the char sequence to decode symbols from.
@param destination the array to write bytes into.
@param destinationOffset the starting index in the `destination` array to write bytes to, 0 by default.
@param startIndex the beginning (inclusive) of the substring to decode, 0 by default.
@param endIndex the end (exclusive) of the substring to decode, length of the `source` by default.

@throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` indices.
@throws IllegalArgumentException when `startIndex > endIndex`.
@throws IndexOutOfBoundsException when the resulting bytes don't fit into the `destination` array starting at the specified `destinationOffset`,
or when that index is out of the `destination` array indices range.
@throws IllegalArgumentException when the symbols for decoding are not padded as required by the `PaddingOption`
  set for this `Base64` instance, or when there are extra symbols after the padding.

@return the number of bytes written into `destination` array.

@sample samples.io.encoding.Base64Samples.decodeIntoByteArraySample

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val outputBuffer = ByteArray(1024)
    // {data:\"ZW5jb2RlZA==\"}
    val data = byteArrayOf(
        123, 100, 97, 116, 97,
        58, 34, 90, 87, 53, 106,
        98, 50, 82, 108, 90, 65,
        61, 61, 34, 125
    )
    val from = data.indexOf('"'.code.toByte()) + 1
    val until = data.lastIndexOf('"'.code.toByte())

    // decode subrange of input data into buffer and remember how many bytes were written
    val bytesWritten = Base64.decodeIntoByteArray(data, destination = outputBuffer, startIndex = from, endIndex = until)
    println(outputBuffer.decodeToString(endIndex = bytesWritten))
}
```

```text title="Output"
encoded
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L365)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val outputBuffer = ByteArray(1024)
    val inputChunks = listOf("Q2h1bmsx", "U2Vjb25kQ2h1bms=", "Y2h1bmsjMw==")

    var bufferPosition = 0
    val chunkIterator = inputChunks.iterator()
    while (bufferPosition < outputBuffer.size && chunkIterator.hasNext()) {
        val chunk = chunkIterator.next()
        // fill buffer with data decoded from base64-encoded chunks
        // and increment current position by the number of decoded bytes
        bufferPosition += Base64.decodeIntoByteArray(
            chunk,
            destination = outputBuffer,
            destinationOffset = bufferPosition
        )
    }
    // consume outputBuffer
    println(outputBuffer.decodeToString(endIndex = bufferPosition))
}
```

```text title="Output"
Chunk1SecondChunkchunk#3
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L344)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
