# findLast

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the last character matching the given `predicate`, or `null` if no such character was found.

@sample samples.text.Strings.findLast

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.findLast(predicate: (Char) -> Boolean): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L60)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val text = "a1b2c3d4e5"

    println(text.findLast { it.isLetter() })
    println(text.findLast { it.isUpperCase() })
    println("".findLast { it.isLowerCase() })
}
```

```text title="Output"
e
null
null
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L165)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
