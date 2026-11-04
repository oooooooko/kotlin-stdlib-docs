# HexFormat.upperCase

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Specifies whether upper-case hexadecimal digits should be used for formatting, `false` by default.

When this option is set to `true`, formatting functions will use upper-case hexadecimal digits (`0-9`, `A-F`)
to create the hexadecimal representation of the values being formatted. Otherwise, lower-case hexadecimal digits
(`0-9`, `a-f`) will be used.

This option affects the formatting results for both byte arrays and numeric values. However, it **has no effect
on parsing**, which is always performed in a case-insensitive manner.

Note: This option **affects only the case of hexadecimal digits** and does not influence other elements like
`BytesHexFormat.bytePrefix` or `NumberHexFormat.suffix`.

@sample samples.text.HexFormats.HexFormatClass.upperCase

## Declarations and overloads

### 1. Common

```kotlin
public val upperCase: Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L38)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // By default, upperCase is set to false, so lower-case hexadecimal digits are used when formatting.
    println(58.toHexString())
    println(58.toHexString(HexFormat.Default))

    // Setting upperCase to true changes the hexadecimal digits to upper-case.
    println(58.toHexString(HexFormat { upperCase = true }))
    println(58.toHexString(HexFormat.UpperCase))

    // The upperCase option affects only the case of hexadecimal digits.
    val format = HexFormat {
        upperCase = true
        number.prefix = "0x"
    }
    println(58.toHexString(format))

    // The upperCase option also affects how byte arrays are formatted.
    println(byteArrayOf(0x1b, 0xe6.toByte()).toHexString(format))

    // The upperCase option does not affect parsing; parsing is always case-insensitive.
    println("0x0000003a".hexToInt(format))
    println("1BE6".hexToByteArray(format).contentEquals(byteArrayOf(0x1b, 0xe6.toByte())))
}
```

```text title="Output"
0000003a
0000003a
0000003A
0000003A
0x0000003A
1BE6
58
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L51)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
