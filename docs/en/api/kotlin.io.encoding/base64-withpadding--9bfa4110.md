# Base64.withPadding

`kotlin.io.encoding` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new `Base64` instance that is equivalent to this instance
but configured with the specified padding `option`.

This method does not modify this instance. If the specified `option` is the same as the current
padding option of this instance, this instance itself is returned. Otherwise, a new instance is created
using the same alphabet but configured with the new padding option.

@sample samples.io.encoding.Base64Samples.withPaddingSample

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.0")
    public fun withPadding(option: PaddingOption): Base64
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L139)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    // The predefined Base64.UrlSafe instance uses PaddingOption.PRESENT.
    // Create a new instance with PaddingOption.ABSENT_OPTIONAL from the Base64.UrlSafe instance.
    val base64UrlSafeCustomPadding = Base64.UrlSafe.withPadding(Base64.PaddingOption.ABSENT_OPTIONAL)

    // The new instance continues using the same UrlSafe alphabet but omits padding when encoding
    println(base64UrlSafeCustomPadding.encode(byteArrayOf(-1, 0, -2, 0)))
    // It allows decoding both padded and unpadded inputs
    println(base64UrlSafeCustomPadding.decode("_wD-AA").contentToString())
    println(base64UrlSafeCustomPadding.decode("_wD-AA==").contentToString())
}
```

```text title="Output"
_wD-AA
[-1, 0, -2, 0]
[-1, 0, -2, 0]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L102)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
