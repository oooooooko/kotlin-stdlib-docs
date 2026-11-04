# toCollection

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends all elements to the given `destination` collection.

The operation is _terminal_.

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public fun <T, C : MutableCollection<in T>> Sequence<T>.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L968)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*
import java.io.File
import java.io.Reader
import java.io.StringReader
import java.net.URL
import java.util.ArrayList

private fun sample(): Reader = StringReader("Hello\nWorld");

fun main() {

        // TODO we should maybe zap the useLines approach as it encourages
        // use of iterators which don't close the underlying stream
        val list1 = sample().useLines { it.toList() }
        val list2 = sample().useLines<ArrayList<String>>{ it.toCollection(arrayListOf()) }

        println(list1)
        println(list2)
    
}
```

```text title="Output"
[Hello, World]
[Hello, World]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/jvm/test/io/ReadWrite.kt#L153)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
