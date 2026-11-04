# Base64

`kotlin.io.encoding` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Provides Base64 encoding and decoding functionality.
Base64 encoding, as defined by the [`RFC 4648`](https://www.rfc-editor.org/rfc/rfc4648) and a few other RFCs,
transforms arbitrary binary data into a sequence of printable characters.

For example, a sequence of bytes `0xC0 0xFF 0xEE` will be transformed to a string `"wP/u"` using a Base64 encoding
defined by the [`RFC 4648`](https://www.rfc-editor.org/rfc/rfc4648). Decoding that string will result in the original
byte sequence.

**Base64 is not an encryption scheme and should not be used when data needs to be secured or obfuscated.**

Characters used by a particular Base64 scheme form an alphabet of 64 regular characters and
an extra padding character.

Almost all Base64 encoding schemes share the same first 62 characters of an alphabet,
which are `'A'..'Z'` followed by `'a'..'z'`, but the last two characters may vary.
[`RFC 4648 section 4`](https://www.rfc-editor.org/rfc/rfc4648#section-4) defines an alphabet that uses
`'+'` and `'/'` as the last two characters, while the URL-safe alphabet defined in
[`RFC 4648 section 5`](https://www.rfc-editor.org/rfc/rfc4648#section-5) uses `'-'` and `'_'` instead.

When decoding, a Base64 scheme usually accepts only characters from its alphabet, presence of any other characters
is treated as an error (see `Base64.Mime` for an exception to this rule). That also implies
that a Base64 scheme could not decode data encoded by another Base64 scheme if their alphabets differ.

In addition to 64 characters from the alphabet,
Base64-encoded data may also contain one or two padding characters `'='` at its end.
Base64 splits data that needs to be encoded into chunks three bytes long, which are then transformed into
a sequence of four characters (meaning that every character encodes six bits of data).
If the number of bytes constituting input data is not a multiple of three (for instance, input consists of only five bytes),
the data will be padded by zero bits first and only then transformed into Base64-alphabet characters.
If padding takes place, the resulting string is augmented by `'='`. The padding could consist of zero, two or
four bits, thus encoded data will contain zero, one or two padding characters (`'='`), respectively.
The inclusion of padding characters in the resulting string depends on the `PaddingOption` set for the Base64 instance.

This class is not supposed to be inherited or instantiated by calling its constructor.
However, predefined instances of this class are available for use.
The companion object `Base64.Default` is the default instance of `Base64`.
There are also `Base64.UrlSafe` and `Base64.Mime` instances.
The padding option for all predefined instances is set to `PaddingOption.PRESENT`.
New instances with different padding options can be created using the `withPadding` function.

@sample samples.io.encoding.Base64Samples.encodeAndDecode
@sample samples.io.encoding.Base64Samples.encodingDifferences
@sample samples.io.encoding.Base64Samples.padding

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.2")
@WasExperimental(ExperimentalEncodingApi::class)
public open class Base64 private constructor(
    internal val isUrlSafe: Boolean,
    internal val isMimeScheme: Boolean,
    internal val mimeLineLength: Int,
    internal val paddingOption: PaddingOption
)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L10)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val encoded = Base64.Default.encode("Hello, World!".encodeToByteArray())
    println(encoded)

    val decoded = Base64.Default.decode(encoded)
    println(decoded.decodeToString())
}
```

```text title="Output"
SGVsbG8sIFdvcmxkIQ==
Hello, World!
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L14)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*
import kotlin.test.*



fun main() {
    // Default encoding uses '/' and '+' as the last two characters of the Base64 alphabet
    println(Base64.Default.encode(byteArrayOf(-1, 0, -2, 0)))
    // Mime's alphabet is the same as Default's
    println(Base64.Mime.encode(byteArrayOf(-1, 0, -2, 0)))
    // UrlSafe encoding uses '_' and '-' as the last two Base64 alphabet characters
    println(Base64.UrlSafe.encode(byteArrayOf(-1, 0, -2, 0)))

    // UrlSafe uses `-` and `_`, so the following string could not be decoded
    assertFailsWith<IllegalArgumentException> {
        Base64.UrlSafe.decode("/wD+AA==")
    }
}
```

```text title="Output"
/wD+AA==
/wD+AA==
_wD-AA==
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L35)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    // "base".length == 4, which is not multiple of 3;
    // base64-encoded data padded with 4 bits
    println(Base64.Default.encode("base".encodeToByteArray()))
    // "base6".length == 5, which is not multiple of 3;
    // base64-encoded data padded with 2 bits
    println(Base64.Default.encode("base6".encodeToByteArray()))
    // "base64".length == 6, which is the multiple of 3, so no padding is required
    println(Base64.Default.encode("base64".encodeToByteArray()))
}
```

```text title="Output"
YmFzZQ==
YmFzZTY=
YmFzZTY0
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L23)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
