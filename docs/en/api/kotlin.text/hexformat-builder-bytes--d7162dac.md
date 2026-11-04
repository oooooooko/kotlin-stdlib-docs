# HexFormat.Builder.bytes

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Defines `HexFormat.bytes` of the format being built.

Refer to `BytesHexFormat` for details about the available format options, their impact on formatting and
parsing results, and their default settings.

## Declarations and overloads

### 1. Common

```kotlin
public val bytes: BytesHexFormat.Builder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L655)

### 2. Common

```kotlin
@InlineOnly
        public inline fun bytes(builderAction: BytesHexFormat.Builder.() -> Unit)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L687)

Provides a scope for configuring the `bytes` property.

The receiver of the `builderAction` is the `bytes` property. Thus, inside the braces one can configure its
options directly. This convenience function is intended to enable the configuration of multiple options
within a single block. For example, the snippet:
```kotlin
val format = HexFormat {
    bytes {
        bytesPerLine = 16
        bytesPerGroup = 8
        byteSeparator = " "
    }
}
```
is equivalent to:
```kotlin
val format = HexFormat {
    bytes.bytesPerLine = 16
    bytes.bytesPerGroup = 8
    bytes.byteSeparator = " "
}
```

Refer to `BytesHexFormat` for details about the available format options, their impact on formatting and
parsing results, and their default settings.

@param builderAction The function that is applied to the `bytes` property, providing a scope for directly
  configuring its options.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*
import kotlin.test.*



fun main() {
    val format = HexFormat { upperCase = true; bytes.byteSeparator = " " }
    val bytes = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte())

    val base64AbsentPadding = Base64.Default.withPadding(Base64.PaddingOption.ABSENT)

    // PaddingOption.ABSENT does not pad on encode, and requires unpadded input on decode
    println(base64AbsentPadding.encode(bytes))
    println(base64AbsentPadding.decode("3i0CwA").toHexString(format))
    // PaddingOption.ABSENT requires the decode input not to be padded
    assertFailsWith<IllegalArgumentException> {
        base64AbsentPadding.decode("3i0CwA==")
    }
}
```

```text title="Output"
3i0CwA
DE 2D 02 C0
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L134)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
