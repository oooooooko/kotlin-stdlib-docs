# indexOfLast

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns index of the last character matching the given `predicate`, or -1 if the char sequence does not contain such character.

@sample samples.text.Strings.indexOfLast

## Declarations and overloads

### 1. Common

```kotlin
public inline fun CharSequence.indexOfLast(predicate: (Char) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L171)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "Kotlin knowledge"

    println(string.indexOfLast { it == 'K' })
    println(string.indexOfLast { it == 'k' })
    println(string.indexOfLast { it == 'n' })
    println(string.indexOfLast { it == ' ' })
    println(string.indexOfLast { it == 'z' })

    val emptyString = "";
    println(emptyString.indexOfLast { it == 'z' })
}
```

```text title="Output"
0
7
8
6
-1
-1
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1130)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
