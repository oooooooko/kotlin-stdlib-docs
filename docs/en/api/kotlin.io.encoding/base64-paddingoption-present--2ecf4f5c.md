# Base64.PaddingOption.PRESENT

`kotlin.io.encoding` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Pad on encode, require padding on decode.

When encoding, the result is padded with `'='` to reach an integral multiple of 4 symbols.
When decoding, correctly padded input is required. The padding character `'='` marks the end
of the encoded data, and subsequent symbols are prohibited.

This represents the canonical form of Base64 encoding.

@sample samples.io.encoding.Base64Samples.paddingOptionPresentSample

## Declarations and overloads

### 1. Common

```kotlin
PRESENT,
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L91)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*
import kotlin.test.*



fun main() {
    val format = HexFormat { upperCase = true; bytes.byteSeparator = " " }
    val bytes = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte())

    // The predefined Base64 instances are configured with PaddingOption.PRESENT.
    // Hence, the same instance is returned.
    val isSameInstance = Base64.Default.withPadding(Base64.PaddingOption.PRESENT) === Base64.Default
    println(isSameInstance)

    // PaddingOption.PRESENT pads on encode, and requires padded input on decode
    println(Base64.Default.encode(bytes))
    println(Base64.Default.decode("3i0CwA==").toHexString(format))
    // PaddingOption.PRESENT requires the decode input to be properly padded
    assertFailsWith<IllegalArgumentException> {
        Base64.Default.decode("3i0CwA")
    }
}
```

```text title="Output"
true
3i0CwA==
DE 2D 02 C0
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L115)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
