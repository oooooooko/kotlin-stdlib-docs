# enumValueOf

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the enum entry of type `T` with the specified `name`.

The `name` must exactly match an existing enum constant of type `T` (case-sensitive).

@throws IllegalArgumentException if no enum constant with the specified `name` exists in `T`.
@sample samples.misc.Enums.enumValueOfSample

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun <reified T : Enum<T>> enumValueOf(name: String): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Library.kt#L105)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.enums.enumEntries
import kotlin.test.*

enum class Direction { NORTH, SOUTH, EAST, WEST }

enum class Empty

fun main() {
    // enum class Direction { NORTH, SOUTH, EAST, WEST }

    val east = enumValueOf<Direction>("EAST")
    println(east)

    // The lookup fails if a string does not correspond to any of the enum entries
    assertFailsWith<IllegalArgumentException> { enumValueOf<Direction>("UP") }
    assertFailsWith<IllegalArgumentException> { enumValueOf<Direction>("") }

    // The lookup is case-sensitive and fails if the name doesn't match any constant
    assertFailsWith<IllegalArgumentException> { enumValueOf<Direction>("east") }
}
```

```text title="Output"
EAST
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/enums.kt#L15)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
