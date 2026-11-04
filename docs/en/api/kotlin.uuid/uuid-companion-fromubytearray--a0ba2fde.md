# Uuid.Companion.fromUByteArray

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a uuid from an array containing 128 bits split into 16 unsigned bytes.

Each unsigned byte in the `ubyteArray` sequentially represents
the next 8 bits of the uuid, starting from the most significant 8 bits
in the first byte to the least significant 8 bits in the last byte.

@param ubyteArray A 16-byte array containing the uuid bits.
@throws IllegalArgumentException If the size of the `ubyteArray` is not exactly 16.
@return A new uuid based on the specified bits.

@see Uuid.toUByteArray
@sample samples.uuid.Uuids.fromUByteArray

## Declarations and overloads

### 1. Common

```kotlin
@ExperimentalUnsignedTypes
        public fun fromUByteArray(ubyteArray: UByteArray): Uuid
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L358)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val ubyteArray = ubyteArrayOf(
        0x55u, 0x0Eu, 0x84u, 0x00u, 0xE2u, 0x9Bu, 0x41u, 0xD4u,
        0xA7u, 0x16u, 0x44u, 0x66u, 0x55u, 0x44u, 0x00u, 0x00u
    )
    val uuid = Uuid.fromUByteArray(ubyteArray)
    println(uuid)
}
```

```text title="Output"
550e8400-e29b-41d4-a716-446655440000
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L156)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
