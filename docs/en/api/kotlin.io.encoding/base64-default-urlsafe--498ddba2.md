# Base64.Default.UrlSafe

`kotlin.io.encoding` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The "base64url" encoding specified by [`RFC 4648 section 5`](https://www.rfc-editor.org/rfc/rfc4648#section-5),
Base 64 Encoding with URL and Filename Safe Alphabet.

Uses "The URL and Filename safe Base 64 Alphabet" as specified in Table 2 of RFC 4648 for encoding and decoding,
consisting of `'A'..'Z'`, `'a'..'z'`, `'-'` and `'_'` characters.

This instance is configured with the padding option set to `PaddingOption.PRESENT`.
Use the `withPadding` function to create a new instance with a different padding option if necessary.

Encode operation does not add any line separator character.
Decode operation throws if it encounters a character outside the base64url alphabet.

@sample samples.io.encoding.Base64Samples.urlSafeEncodingSample

## Declarations and overloads

### 1. Common

```kotlin
public val UrlSafe: Base64
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L721)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val encoded = Base64.UrlSafe.encode("Hello? :> ".encodeToByteArray())
    println(encoded)
}
```

```text title="Output"
SGVsbG8_IDo-IA==
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L246)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
