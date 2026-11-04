# Uuid.compareTo

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Compares this uuid with the `other` uuid for lexical order.

Returns zero if this uuid is lexically equal to the specified other uuid, a negative number
if it's less than the other, or a positive number if it's greater than the other.

This function compares the two 128-bit uuids bit by bit sequentially,
starting from the most significant bit to the least significant.
`this` uuid is considered less than `other` if, at the first position where corresponding bits
of the two uuids differ, the bit in `this` is zero and the bit in `other` is one.
Conversely, `this` is considered greater than `other` if, at the first differing position,
the bit in `this` is one and the bit in `other` is zero.
If no differing bits are found, the two uuids are considered equal.

The result of the comparison of `this` and `other` uuids is equivalent to:
```kotlin
this.toString().compareTo(other.toString())
```

@sample samples.uuid.Uuids.compareTo

## Declarations and overloads

### 1. Common

```kotlin
override fun compareTo(other: Uuid): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L251)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid1 = Uuid.parse("49d6d991-c780-4eb5-8585-5169c25af912")
    val uuid2 = Uuid.parse("c0bac692-7208-4448-a8fe-3e3eb128db2a")
    val uuid3 = Uuid.parse("49d6d991-aa92-4da0-917e-527c69621cb7")

    println(uuid1 < uuid2)
    println(uuid1 > uuid3)

    val sortedUuids = listOf(uuid1, uuid2, uuid3).sorted()

    println(sortedUuids[0])
    println(sortedUuids[1])
    println(sortedUuids[2])
}
```

```text title="Output"
true
true
49d6d991-aa92-4da0-917e-527c69621cb7
49d6d991-c780-4eb5-8585-5169c25af912
c0bac692-7208-4448-a8fe-3e3eb128db2a
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L290)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
