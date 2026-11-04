# filterNot

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a char sequence containing only those characters from the original char sequence that do not match the given `predicate`.

@sample samples.text.Strings.filterNot

## Declarations and overloads

### 1. Common

```kotlin
public inline fun CharSequence.filterNot(predicate: (Char) -> Boolean): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L481)

### 2. Common

```kotlin
public inline fun String.filterNot(predicate: (Char) -> Boolean): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L490)

Returns a string containing only those characters from the original string that do not match the given `predicate`.

@sample samples.text.Strings.filterNot

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val text = "a1b2c3d4e5"

    val textWithoutDigits = text.filterNot { it.isDigit() }

    println(textWithoutDigits)
}
```

```text title="Output"
abcde
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L156)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
