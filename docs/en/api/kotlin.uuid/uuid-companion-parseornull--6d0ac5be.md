# Uuid.Companion.parseOrNull

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Parses a uuid from one of the supported string representations, returning `null` if it matches none of them.

This function supports parsing the standard hex-and-dash and the hexadecimal string representations.
For details about the hex-and-dash format, refer to `toHexDashString`.
If parsing only the hex-and-dash format is desired, use `parseHexDashOrNull` instead.
For details about the hexadecimal format, refer to `toHexString`.
If parsing only the hexadecimal format is desired, use `parseHexOrNull` instead.

Note that this function is case-insensitive,
meaning both lowercase and uppercase hexadecimal digits are considered valid.
Additionally, support for more uuid formats may be introduced in the future.
Therefore, users should not rely on the rejection of formats not currently supported.

@param uuidString A string in one of the supported uuid formats.
@return A uuid equivalent to the specified uuid string, or `null`,
if the string does not conform any of supported formats.

@see Uuid.parseHexDashOrNull
@see Uuid.parseHexOrNull
@see Uuid.parse
@sample samples.uuid.Uuids.parseOrNull

## Declarations and overloads

### 1. Common

```kotlin
public fun parseOrNull(uuidString: String): Uuid?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L410)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    // Parsing is case-insensitive
    val uuid1 = Uuid.parseOrNull("550E8400-e29b-41d4-A716-446655440000") // hex-and-dash
    val uuid2 = Uuid.parseOrNull("550e8400E29b41D4a716446655440000") // hexadecimal

    println(uuid1 == uuid2)
    println(uuid1)
    println(uuid2)

    println(Uuid.parseOrNull("I'm not a UUID, sorry"))
}
```

```text title="Output"
true
550e8400-e29b-41d4-a716-446655440000
550e8400-e29b-41d4-a716-446655440000
null
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L179)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
