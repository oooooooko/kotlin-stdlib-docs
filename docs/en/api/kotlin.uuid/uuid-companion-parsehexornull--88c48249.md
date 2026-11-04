# Uuid.Companion.parseHexOrNull

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses a uuid from the hexadecimal string representation as described in `Uuid.toHexString`,
returning `null` if a string has a different format.

This function is case-insensitive, and for a valid `hexString`, the following property holds:
```kotlin
val uuid = Uuid.parseHexOrNull(hexString)!!
assertEquals(uuid.toHexString(), hexString.lowercase())
```

@param hexString A 32-character hexadecimal string representing the uuid, without hyphens.
@return A uuid represented by the specified hexadecimal string, or `null`, if the string does not conform the format.

@see Uuid.toHexString
@see Uuid.parseHex
@sample samples.uuid.Uuids.parseHexOrNull

## Declarations and overloads

### 1. Common

```kotlin
public fun parseHexOrNull(hexString: String): Uuid?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L522)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.parseHexOrNull("550E8400e29b41d4A716446655440000") // case insensitive
    println(uuid)

    println(Uuid.parseHexOrNull("~550E8400e29b41d4A716446655440000~"))
}
```

```text title="Output"
550e8400-e29b-41d4-a716-446655440000
null
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L216)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
