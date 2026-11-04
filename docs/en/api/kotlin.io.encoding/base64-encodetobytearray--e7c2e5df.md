# Base64.encodeToByteArray

`kotlin.io.encoding` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Encodes bytes from the specified `source` array or its subrange.
Returns a `ByteArray` containing the resulting symbols.

Whether the encoding result is padded with `'='` depends on the `PaddingOption` set for this `Base64` instance.

Each resulting symbol occupies one byte in the returned byte array.

Use `encode` to get the output in string form.

@param source the array to encode bytes from.
@param startIndex the beginning (inclusive) of the subrange to encode, 0 by default.
@param endIndex the end (exclusive) of the subrange to encode, size of the `source` array by default.

@throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` array indices.
@throws IllegalArgumentException when `startIndex > endIndex`.

@return a `ByteArray` with the resulting symbols.

@sample samples.io.encoding.Base64Samples.encodeToByteArraySample

## Declarations and overloads

### 1. Common

```kotlin
public fun encodeToByteArray(source: ByteArray, startIndex: Int = 0, endIndex: Int = source.size): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L155)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val data = byteArrayOf(-1, 0, -2, 0, -3)

    val encoded = Base64.encodeToByteArray(data)
    println(encoded.contentEquals("/wD+AP0=".encodeToByteArray()))

    val encodedFromSubRange = Base64.encodeToByteArray(data, startIndex = 1, endIndex = 3)
    println(encodedFromSubRange.contentEquals("AP4=".encodeToByteArray()))
}
```

```text title="Output"
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L252)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
