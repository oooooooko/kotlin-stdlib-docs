# toUByteArray

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an array of UByte containing all of the elements of this generic array.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Array<out UByte>.toUByteArray(): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4939)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ByteArray.toUByteArray(): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4948)

Returns an array of type `UByteArray`, which is a copy of this array where each element is an unsigned reinterpretation
of the corresponding element of this array.

### 3. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Collection<UByte>.toUByteArray(): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UCollections.kt#L22)

Returns an array of UByte containing all of the elements of this collection.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val data = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte(), 0x5C, 0x0E)

    // Using the default format
    println(data.toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        bytes {
            bytesPerLine = 4
            byteSeparator = " " // One space
            bytePrefix = "0x"
        }
    }
    println(data.toHexString(format))

    // Formatting a segment of the byte array
    println(data.toHexString(startIndex = 2, endIndex = 5, format))

    // Formatting unsigned bytes with the same binary representations yields the same string
    val unsignedData = data.toUByteArray()
    println(unsignedData.toHexString(format))
}
```

```text title="Output"
de2d02c05c0e
0xDE 0x2D 0x02 0xC0
0x5C 0x0E
0x02 0xC0 0x5C
0xDE 0x2D 0x02 0xC0
0x5C 0x0E
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L365)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
