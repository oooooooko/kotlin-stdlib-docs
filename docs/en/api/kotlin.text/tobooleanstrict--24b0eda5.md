# toBooleanStrict

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if the content of this string is equal to the word "true", `false` if it is equal to "false",
and throws an exception otherwise.

There is also a lenient version of the function available on nullable String, `String?.toBoolean`.
Note that this function is case-sensitive.

@sample samples.text.Strings.toBooleanStrict

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun String.toBooleanStrict(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1621)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    println("true".toBooleanStrict())
    assertFails { "True".toBooleanStrict() }
    assertFails { "TRUE".toBooleanStrict() }

    println("false".toBooleanStrict())
    assertFails { "False".toBooleanStrict() }
    assertFails { "FALSE".toBooleanStrict() }

    assertFails { "abc".toBooleanStrict() }
}
```

```text title="Output"
true
false
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L634)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
