# Uuid.toHexString

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the hexadecimal string representation of this uuid without hyphens.

The resulting string is in lowercase and consists of 32 characters. Each hexadecimal digit
in the string sequentially represents the next 4 bits of the uuid, starting from the most
significant 4 bits in the first digit to the least significant 4 bits in the last digit.

The returned string is equivalent to:
```kotlin
uuid.toByteArray().toHexString()
```

@see Uuid.parseHex
@sample samples.uuid.Uuids.toHexString

## Declarations and overloads

### 1. Common

```kotlin
public fun toHexString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L181)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.fromULongs(0x550E8400E29B41D4uL, 0xA716446655440000uL)
    println(uuid.toHexString())
}
```

```text title="Output"
550e8400e29b41d4a716446655440000
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L100)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
