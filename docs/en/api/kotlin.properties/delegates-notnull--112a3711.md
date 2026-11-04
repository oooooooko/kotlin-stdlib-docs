# Delegates.notNull

`kotlin.properties` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a property delegate for a read/write property with a non-`null` value that is initialized not during
object construction time but at a later time. Trying to read the property before the initial value has been
assigned results in an exception.

@sample samples.properties.Delegates.notNullDelegate

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Any> notNull(): ReadWriteProperty<Any?, T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Delegates.kt#L14)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.properties.Delegates
import kotlin.test.*



fun main() {
    var max: Int by Delegates.notNull()

    assertFailsWith<IllegalStateException> { println(max) }

    max = 10
    println(max)
}
```

```text title="Output"
10
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/properties/delegates.kt#L55)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
