# Pair

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents a generic pair of two values.

There is no meaning attached to values in this class, it can be used for any purpose.
Pair exhibits value semantics, i.e. two pairs are equal if both components are equal.

An example of decomposing it into values:
@sample samples.misc.Tuples.pairDestructuring

@param A type of the first value.
@param B type of the second value.
@property first First value.
@property second Second value.
@constructor Creates a new instance of Pair.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.js.JsImplicitExport(couldBeConvertedToExplicitExport = true)
public data class Pair<out A, out B>(
    public val first: A,
    public val second: B
) : Serializable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Tuples.kt#L11)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val (a, b) = Pair(1, "x")
    println(a)
    println(b)
}
```

```text title="Output"
1
x
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/tuples.kt#L8)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
