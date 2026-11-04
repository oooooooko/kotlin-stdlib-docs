# repeat

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Executes the given function `action` specified number of `times`.

A zero-based index of current iteration is passed as a parameter to the `action` function.

If the `times` parameter is negative or equal to zero, the `action` function is not invoked.

@sample samples.misc.ControlFlow.repeat

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun repeat(times: Int, action: (Int) -> Unit)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Standard.kt#L149)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // greets three times
    repeat(3) {
        println("Hello")
    }

    // greets with an index
    repeat(3) { index ->
        println("Hello with index $index")
    }

    repeat(0) {
        error("We should not get here!")
    }
}
```

```text title="Output"
Hello
Hello
Hello
Hello with index 0
Hello with index 1
Hello with index 2
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/controlFlow.kt#L12)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
