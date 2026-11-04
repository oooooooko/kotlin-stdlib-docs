# emptyArray

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an empty array of the specified type `T`.

## Declarations and overloads

### 1. Common

```kotlin
@Suppress("REIFIED_TYPE_PARAMETER_NO_INLINE")
public expect fun <reified T> emptyArray(): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ArrayIntrinsics.kt#L8)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import java.util.Collections
import kotlin.test.*

@Suppress("HasPlatformType", "UNCHECKED_CAST")
    fun <T> platformNull() = Collections.singletonList(null as T).first()

fun main() {

        println(platformNull<Array<String>>() contentDeepEquals emptyArray<String>())
        println(arrayOf("a", "b") contentDeepEquals platformNull<Array<String>>())
    
}
```

```text title="Output"
false
false
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/jvm/test/collections/ArraysJVMTest.kt#L48)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
