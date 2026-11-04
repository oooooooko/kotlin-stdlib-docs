# HexFormat.Builder.number

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Defines `HexFormat.number` of the format being built.

Refer to `NumberHexFormat` for details about the available format options, their impact on formatting and
parsing results, and their default settings.

## Declarations and overloads

### 1. Common

```kotlin
public val number: NumberHexFormat.Builder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L671)

### 2. Common

```kotlin
@InlineOnly
        public inline fun number(builderAction: NumberHexFormat.Builder.() -> Unit)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L722)

Provides a scope for configuring the `number` property.

The receiver of the `builderAction` is the `number` property. Thus, inside the braces one can configure its
options directly. This convenience function is intended to enable the configuration of multiple options
within a single block. For example, the snippet:
```kotlin
val format = HexFormat {
    number {
        prefix = "&#x"
        suffix = ";"
        removeLeadingZeros = true
    }
}
```
is equivalent to:
```kotlin
val format = HexFormat {
    number.prefix = "&#x"
    number.suffix = ";"
    number.removeLeadingZeros = true
}
```

Refer to `NumberHexFormat` for details about the available format options, their impact on formatting
and parsing results, and their default settings.

@param builderAction The function that is applied to the `number` property, providing a scope for directly
  configuring its options.

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
