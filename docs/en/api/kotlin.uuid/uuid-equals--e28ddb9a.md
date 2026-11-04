# Uuid.equals

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Checks whether this uuid is equal to the specified `other` object.

@param other The object to compare with this uuid.
@return `true` if `other` is an instance of `Uuid`, and consists of the same sequence
  of bits as this uuid; `false` otherwise.

@sample samples.uuid.Uuids.uuidEquals

## Declarations and overloads

### 1. Common

```kotlin
override fun equals(other: Any?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L235)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid1 = Uuid.fromULongs(0x550E8400E29B41D4uL, 0xA716446655440000uL)
    val uuid2 = Uuid.parse("550e8400-e29b-41d4-a716-446655440000")
    val uuid3 = Uuid.parse("550e8400-e29b-41d4-a716-446655440001") // the last bit is one

    println(uuid1 == uuid2)
    println(uuid1 == uuid3)
}
```

```text title="Output"
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L124)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
