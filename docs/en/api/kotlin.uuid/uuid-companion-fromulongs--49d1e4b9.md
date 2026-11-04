# Uuid.Companion.fromULongs

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a uuid from specified 128 bits split into two 64-bit ULongs.

This function interprets the provided `ULong` values in big-endian byte order.

@param mostSignificantBits The most significant 64 bits of the uuid.
@param leastSignificantBits The least significant 64 bits of the uuid.
@return A new uuid based on the specified bits.

@see Uuid.toULongs
@sample samples.uuid.Uuids.fromULongs

## Declarations and overloads

### 1. Common

```kotlin
public fun fromULongs(mostSignificantBits: ULong, leastSignificantBits: ULong): Uuid
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L321)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.fromULongs(0x550E8400E29B41D4uL, 0xA716446655440000uL)
    println(uuid)
}
```

```text title="Output"
550e8400-e29b-41d4-a716-446655440000
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L140)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
