# ClosedFloatingPointRange.isEmpty

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Declarations and overloads

### 1. Common

```kotlin
override fun isEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L82)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

private fun assertFailsWithIllegalArgument(f: () -> Unit) = assertFailsWith<IllegalArgumentException> { f() }

fun main() {

        println((2..1).isEmpty())
        println((2L..0L).isEmpty())
        println((1.toShort()..(-1).toShort()).isEmpty())
        println((0.toByte()..(-1).toByte()).isEmpty())
        println((0f..-3.14f).isEmpty())
        println((-2.72..-3.14).isEmpty())
        println(('z'..'x').isEmpty())

        println((1 downTo 2).isEmpty())
        println((0L downTo 2L).isEmpty())
        println((2 downTo 1).isEmpty())
        println((2L downTo 0L).isEmpty())
        println(('a' downTo 'z').isEmpty())
        println(('z'..'a' step 2).isEmpty())

        println(("range".."progression").isEmpty())
    
}
```

```text title="Output"
true
true
true
true
true
true
true
true
true
false
false
true
true
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/ranges/RangeTest.kt#L327)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
