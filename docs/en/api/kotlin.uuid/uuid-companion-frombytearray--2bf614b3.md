# Uuid.Companion.fromByteArray

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a uuid from a byte array containing 128 bits split into 16 bytes.

Each byte in the `byteArray` sequentially represents
the next 8 bits of the uuid, starting from the most significant 8 bits
in the first byte to the least significant 8 bits in the last byte.

@param byteArray A 16-byte array containing the uuid bits.
@throws IllegalArgumentException If the size of the `byteArray` is not exactly 16.
@return A new uuid based on the specified bits.

@see Uuid.toByteArray
@sample samples.uuid.Uuids.fromByteArray

## Declarations and overloads

### 1. Common

```kotlin
public fun fromByteArray(byteArray: ByteArray): Uuid
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L336)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val byteArray = byteArrayOf(
        0x55, 0x0e, 0x84.toByte(), 0x00, 0xe2.toByte(), 0x9b.toByte(), 0x41, 0xd4.toByte(),
        0xa7.toByte(), 0x16, 0x44, 0x66, 0x55, 0x44, 0x00, 0x00
    )
    val uuid = Uuid.fromByteArray(byteArray)
    println(uuid)
}
```

```text title="Output"
550e8400-e29b-41d4-a716-446655440000
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L146)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
