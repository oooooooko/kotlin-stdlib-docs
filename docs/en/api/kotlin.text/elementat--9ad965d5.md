# elementAt

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a character at the given `index` or throws an `IndexOutOfBoundsException` if the `index` is out of bounds of this char sequence.

@sample samples.text.Strings.elementAt

## Declarations and overloads

### 1. Common

```kotlin
public expect fun CharSequence.elementAt(index: Int): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L20)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val string = "kotlin"
    println(string.elementAt(0))
    println(string.elementAt(5))
    assertFailsWith<IndexOutOfBoundsException> { string.elementAt(-1) }
    assertFailsWith<IndexOutOfBoundsException> { string.elementAt(6) }

    val empty = ""
    assertFailsWith<IndexOutOfBoundsException> { empty.elementAt(0) }
}
```

```text title="Output"
k
n
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L103)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
