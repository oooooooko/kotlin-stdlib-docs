# HexFormat.NumberHexFormat.Builder

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Provides an API for building a `NumberHexFormat`.

This class is a [builder](https://en.wikipedia.org/wiki/Builder_pattern) for `NumberHexFormat`, and
serves as the type of the `number` property when creating a new format using the `HexFormat { }` builder
function. Each option in this class corresponds to an option in `NumberHexFormat` and defines it in the
resulting format. For example, use `val format = HexFormat { number.removeLeadingZeros = true }` to set
`NumberHexFormat.removeLeadingZeros`. Refer to `NumberHexFormat` for details about how the configured
format options affect formatting and parsing results.

@sample samples.text.HexFormats.Numbers.numberHexFormat

## Declarations and overloads

### 1. Common

```kotlin
public class Builder internal constructor()
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L536)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val numberHexFormat = HexFormat {
        upperCase = true
        number {
            removeLeadingZeros = true
            minLength = 4
            prefix = "0x"
        }
    }

    println(0x3a.toHexString(numberHexFormat))
    println("0x003A".hexToInt(numberHexFormat))
    // Parsing is case-insensitive
    println("0X003a".hexToInt(numberHexFormat))
}
```

```text title="Output"
0x003A
58
58
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L236)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
