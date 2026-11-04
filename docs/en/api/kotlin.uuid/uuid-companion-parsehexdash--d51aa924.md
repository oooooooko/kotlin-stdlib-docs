# Uuid.Companion.parseHexDash

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses a uuid from the standard hex-and-dash string representation as described in `Uuid.toHexDashString`.

This function is case-insensitive, and for a valid `hexDashString`, the following property holds:
```kotlin
val uuid = Uuid.parseHexDash(hexDashString)
assertEquals(uuid.toHexDashString(), hexDashString.lowercase())
```

The standard textual representation of uuids, also known as hex-and-dash format, is specified by
[RFC 9562 section 4](https://www.rfc-editor.org/rfc/rfc9562.html#section-4).

@param hexDashString A string in the format "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  where each 'x' is a hexadecimal digit, either lowercase or uppercase.
@throws IllegalArgumentException If the `hexDashString` is not a 36-character string
  in the standard uuid format.
@return A uuid equivalent to the specified uuid string.

@see Uuid.toHexDashString
@see Uuid.parseHexDashOrNull
@sample samples.uuid.Uuids.parseHexDash

## Declarations and overloads

### 1. Common

```kotlin
public fun parseHexDash(hexDashString: String): Uuid
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L441)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.parseHexDash("550E8400-e29b-41d4-A716-446655440000") // case insensitive
    println(uuid)

    assertFailsWith<IllegalArgumentException> { Uuid.parseHexDash("550E8400/e29b/41d4/A716/446655440000") }
}
```

```text title="Output"
550e8400-e29b-41d4-a716-446655440000
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L192)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
