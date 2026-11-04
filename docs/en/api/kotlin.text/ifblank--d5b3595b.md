# ifBlank

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns this char sequence if it is not empty and doesn't consist solely of whitespace characters,
or the result of calling `defaultValue` function otherwise.

@sample samples.text.Strings.stringIfBlank

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline fun <C, R> C.ifBlank(defaultValue: () -> R): R where C : CharSequence, C : R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L364)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val blank = "    "

    val blankOrNull: String? = blank.ifBlank { null }
    println(blankOrNull)

    val blankOrDefault = blank.ifBlank { "default" }
    println(blankOrDefault)

    val nonBlank = "abc"
    val sameString = nonBlank.ifBlank { "def" }
    println(nonBlank === sameString)
}
```

```text title="Output"
null
default
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L342)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
