# toBooleanStrictOrNull

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if the content of this string is equal to the word "true", `false` if it is equal to "false",
and `null` otherwise.

There is also a lenient version of the function available on nullable String, `String?.toBoolean`.
Note that this function is case-sensitive.

@sample samples.text.Strings.toBooleanStrictOrNull

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun String.toBooleanStrictOrNull(): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1637)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("true".toBooleanStrictOrNull())
    println("True".toBooleanStrictOrNull())
    println("TRUE".toBooleanStrictOrNull())

    println("false".toBooleanStrictOrNull())
    println("False".toBooleanStrictOrNull())
    println("FALSE".toBooleanStrictOrNull())

    println("abc".toBooleanStrictOrNull())
}
```

```text title="Output"
true
null
null
false
null
null
null
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L647)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
