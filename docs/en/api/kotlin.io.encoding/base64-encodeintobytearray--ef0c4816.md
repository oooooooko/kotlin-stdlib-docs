# Base64.encodeIntoByteArray

`kotlin.io.encoding` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Encodes bytes from the specified `source` array or its subrange and writes resulting symbols into the `destination` array.
Returns the number of symbols written.

Whether the encoding result is padded with `'='` depends on the `PaddingOption` set for this `Base64` instance.

@param source the array to encode bytes from.
@param destination the array to write symbols into.
@param destinationOffset the starting index in the `destination` array to write symbols to, 0 by default.
@param startIndex the beginning (inclusive) of the subrange to encode, 0 by default.
@param endIndex the end (exclusive) of the subrange to encode, size of the `source` array by default.

@throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` array indices.
@throws IllegalArgumentException when `startIndex > endIndex`.
@throws IndexOutOfBoundsException when the resulting symbols don't fit into the `destination` array starting at the specified `destinationOffset`,
or when that index is out of the `destination` array indices range.

@return the number of symbols written into `destination` array.

@sample samples.io.encoding.Base64Samples.encodeIntoByteArraySample

## Declarations and overloads

### 1. Common

```kotlin
public fun encodeIntoByteArray(
        source: ByteArray,
        destination: ByteArray,
        destinationOffset: Int = 0,
        startIndex: Int = 0,
        endIndex: Int = source.size
    ): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L180)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val data = byteArrayOf(-1, 0, -2, 0, -3)
    val outputBuffer = ByteArray(1024)

    var bufferPosition = 0
    // encode data into buffer using Base64 encoding
    // and keep track of the number of bytes written
    bufferPosition += Base64.encodeIntoByteArray(data, outputBuffer)
    println(outputBuffer.decodeToString(endIndex = bufferPosition))

    outputBuffer[bufferPosition++] = '|'.code.toByte()

    // encode data subrange to the buffer, writing it from the given offset
    bufferPosition += Base64.encodeIntoByteArray(
        data,
        destination = outputBuffer,
        destinationOffset = bufferPosition,
        startIndex = 1,
        endIndex = 3
    )
    println(outputBuffer.decodeToString(endIndex = bufferPosition))
}
```

```text title="Output"
/wD+AP0=
/wD+AP0=|AP4=
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L263)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
