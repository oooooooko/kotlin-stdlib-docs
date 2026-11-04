# Uuid.Companion.parseHex

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses a uuid from the hexadecimal string representation as described in `Uuid.toHexString`.

This function is case-insensitive, and for a valid `hexString`, the following property holds:
```kotlin
val uuid = Uuid.parseHex(hexString)
assertEquals(uuid.toHexString(), hexString.lowercase())
```

@param hexString A 32-character hexadecimal string representing the uuid, without hyphens.
@throws IllegalArgumentException If the `hexString` is not a 32-character hexadecimal string.
@return A uuid represented by the specified hexadecimal string.

@see Uuid.toHexString
@see Uuid.parseHexOrNull
@sample samples.uuid.Uuids.parseHex

## Declarations and overloads

### 1. Common

```kotlin
public fun parseHex(hexString: String): Uuid
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L497)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.parseHex("550E8400e29b41d4A716446655440000") // case insensitive
    println(uuid)

    assertFailsWith<IllegalArgumentException> { Uuid.parseHex("~550E8400e29b41d4A716446655440000~") }
}
```

```text title="Output"
550e8400-e29b-41d4-a716-446655440000
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L208)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
