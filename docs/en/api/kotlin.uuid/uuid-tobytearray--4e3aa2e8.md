# Uuid.toByteArray

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a byte array representation of this uuid.

The returned array contains 16 bytes. Each byte in the array sequentially represents
the next 8 bits of the uuid, starting from the most significant 8 bits
in the first byte to the least significant 8 bits in the last byte.

@see Uuid.fromByteArray
@sample samples.uuid.Uuids.toByteArray

## Declarations and overloads

### 1. Common

```kotlin
public fun toByteArray(): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L203)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.fromULongs(0x550E8400E29B41D4uL, 0xA716446655440000uL)
    println(uuid.toByteArray().joinToString { it.toHexString() })
}
```

```text title="Output"
55, 0e, 84, 00, e2, 9b, 41, d4, a7, 16, 44, 66, 55, 44, 00, 00
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L106)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
