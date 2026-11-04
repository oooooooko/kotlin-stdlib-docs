# elementAtOrElse

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an element at the given `index` or the result of calling the `defaultValue` function if the `index` is out of bounds of this sequence.

The operation is _terminal_.

@sample samples.collections.Collections.Elements.elementAtOrElse

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Sequence<T>.elementAtOrElse(index: Int, defaultValue: (Int) -> T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L40)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf(1, 2, 3)
    println(list.elementAtOrElse(0) { 42 })
    println(list.elementAtOrElse(2) { 42 })
    println(list.elementAtOrElse(3) { 42 })

    val emptyList = emptyList<Int>()
    println(emptyList.elementAtOrElse(0) { "no int" })
}
```

```text title="Output"
1
3
42
no int
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1324)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
