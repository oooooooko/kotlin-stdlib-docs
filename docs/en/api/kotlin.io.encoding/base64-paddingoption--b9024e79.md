# Base64.PaddingOption

`kotlin.io.encoding` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

An enumeration of the possible padding options for Base64 encoding and decoding.

Constants of this enum class can be passed to the `withPadding` function to create a new Base64 instance
with the specified padding option. Each padding option affects the encode and decode operations of the
Base64 instance in the following way:

| PaddingOption                    | On encode    | On decode                |
|----------------------------------|--------------|--------------------------|
| `PaddingOption.PRESENT`          | Emit padding | Padding is required      |
| `PaddingOption.ABSENT`           | Omit padding | Padding must not present |
| `PaddingOption.PRESENT_OPTIONAL` | Emit padding | Padding is optional      |
| `PaddingOption.ABSENT_OPTIONAL`  | Omit padding | Padding is optional      |

These options provide flexibility in handling the padding characters (`'='`) and enable compatibility with
various Base64 libraries and protocols.

@sample samples.io.encoding.Base64Samples.paddingOptionSample

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.0")
    public enum class PaddingOption
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L70)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*
import kotlin.test.*



fun main() {
    val format = HexFormat {
        upperCase = true
        bytes.byteSeparator = " "
    }

    val bytes = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte())

    // The Base64.Default instance is configured with PaddingOption.PRESENT
    println(Base64.Default.encode(bytes))
    println(Base64.Default.decode("3i0CwA==").toHexString(format))
    // PaddingOption.PRESENT requires the decode input to be properly padded
    assertFailsWith<IllegalArgumentException> {
        Base64.Default.decode("3i0CwA")
    }

    // Create a new instance with PaddingOption.ABSENT that uses the Base64.Default alphabet
    val base64AbsentPadding = Base64.Default.withPadding(Base64.PaddingOption.ABSENT)

    println(base64AbsentPadding.encode(bytes))
    println(base64AbsentPadding.decode("3i0CwA").toHexString(format))
    // PaddingOption.ABSENT requires the decode input not to be padded
    assertFailsWith<IllegalArgumentException> {
        base64AbsentPadding.decode("3i0CwA==")
    }

    // Create a new instance with PaddingOption.PRESENT_OPTIONAL that uses the Base64.Default alphabet
    val base64PresentOptionalPadding = Base64.Default.withPadding(Base64.PaddingOption.PRESENT_OPTIONAL)

    println(base64PresentOptionalPadding.encode(bytes))
    // PaddingOption.PRESENT_OPTIONAL allows both padded and unpadded decode inputs
    println(base64PresentOptionalPadding.decode("3i0CwA==").toHexString(format))
    println(base64PresentOptionalPadding.decode("3i0CwA").toHexString(format))
    // However, partially padded input is prohibited
    assertFailsWith<IllegalArgumentException> {
        base64PresentOptionalPadding.decode("3i0CwA=")
    }

    // Create a new instance with PaddingOption.ABSENT_OPTIONAL that uses the Base64.Default alphabet
    val base64AbsentOptionalPadding = Base64.Default.withPadding(Base64.PaddingOption.ABSENT_OPTIONAL)

    println(base64AbsentOptionalPadding.encode(bytes))
    // PaddingOption.ABSENT_OPTIONAL allows both padded and unpadded decode inputs
    println(base64AbsentOptionalPadding.decode("3i0CwA").toHexString(format))
    println(base64AbsentOptionalPadding.decode("3i0CwA==").toHexString(format))
    // However, partially padded input is prohibited
    assertFailsWith<IllegalArgumentException> {
        base64AbsentOptionalPadding.decode("3i0CwA=")
    }
}
```

```text title="Output"
3i0CwA==
DE 2D 02 C0
3i0CwA
DE 2D 02 C0
3i0CwA==
DE 2D 02 C0
DE 2D 02 C0
3i0CwA
DE 2D 02 C0
DE 2D 02 C0
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L50)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
