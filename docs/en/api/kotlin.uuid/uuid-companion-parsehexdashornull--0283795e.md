# Uuid.Companion.parseHexDashOrNull

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses a uuid from the standard hex-and-dash string representation as described in `Uuid.toHexDashString`,
returning `null` is a string has a different format.

This function is case-insensitive, and for a valid `hexDashString`, the following property holds:
```kotlin
val uuid = Uuid.parseHexDashOrNull(hexDashString)!!
assertEquals(uuid.toHexDashString(), hexDashString.lowercase())
```

The standard textual representation of uuids, also known as hex-and-dash format, is specified by
[RFC 9562 section 4](https://www.rfc-editor.org/rfc/rfc9562.html#section-4).

@param hexDashString A string in the format "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  where each 'x' is a hexadecimal digit, either lowercase or uppercase.
@return A uuid equivalent to the specified uuid string, or `null`, if the string does not conform the format.

@see Uuid.toHexDashString
@see Uuid.parseHexDash
@sample samples.uuid.Uuids.parseHexDashOrNull

## Declarations and overloads

### 1. Common

```kotlin
public fun parseHexDashOrNull(hexDashString: String): Uuid?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L471)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.parseHexDashOrNull("550E8400-e29b-41d4-A716-446655440000") // case insensitive
    println(uuid)

    println(Uuid.parseHexDashOrNull("550E8400/e29b/41d4/A716/446655440000"))
}
```

```text title="Output"
550e8400-e29b-41d4-a716-446655440000
null
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L200)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
