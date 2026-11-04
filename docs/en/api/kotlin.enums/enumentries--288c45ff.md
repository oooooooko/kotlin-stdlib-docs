# enumEntries

`kotlin.enums` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `EnumEntries` list containing all enum entries for the given enum type `T`.

@see EnumEntries
@sample samples.misc.Enums.enumEntriesSample

## Declarations and overloads

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.0")
public inline fun <reified T : Enum<T>> enumEntries(): EnumEntries<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/enums/EnumEntries.kt#L30)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.enums.enumEntries

enum class Direction { NORTH, SOUTH, EAST, WEST }

enum class Empty

fun main() {
    // enum class Direction { NORTH, SOUTH, EAST, WEST }
    val entries = enumEntries<Direction>()
    println(entries)
    println(entries.indexOf(Direction.EAST))
    println(entries[1])

    // enum class Empty {}
    println(enumEntries<Empty>())
}
```

```text title="Output"
[NORTH, SOUTH, EAST, WEST]
2
SOUTH
[]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/enums.kt#L32)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
