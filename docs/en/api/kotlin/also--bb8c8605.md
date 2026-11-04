# also

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Calls the specified function `block` with `this` value as its argument and returns `this` value.

For detailed usage information see the documentation for [scope functions](https://kotlinlang.org/docs/reference/scope-functions.html#also).

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("1.1")
@IgnorableReturnValue
public inline fun <T> T.also(block: (T) -> Unit): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Standard.kt#L91)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.io.*
import kotlin.io.encoding.*



fun main() {
    ByteArrayOutputStream().also { out ->
        out.encodingWith(Base64.Default).use {
            it.write("Hello World!!".encodeToByteArray())
        }
        println(out.toString())
    }
}
```

```text title="Output"
SGVsbG8gV29ybGQhIQ==
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64Streams.kt#L30)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
