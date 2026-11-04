# getOrElse

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a character at the given `index` or the result of calling the `defaultValue` function if the `index` is out of bounds of this char sequence.

@sample samples.collections.Collections.Elements.getOrElse

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.getOrElse(index: Int, defaultValue: (Int) -> Char): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L135)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf(1, 2, 3)
    println(list.getOrElse(0) { 42 })
    println(list.getOrElse(2) { 42 })
    println(list.getOrElse(3) { 42 })
    println(list.getOrElse(-1) { 42 })

    val emptyList = emptyList<Int>()
    println(emptyList.getOrElse(0) { "no int" })
}
```

```text title="Output"
1
3
42
42
no int
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1345)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
