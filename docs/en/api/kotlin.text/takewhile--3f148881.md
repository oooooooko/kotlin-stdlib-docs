# takeWhile

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a subsequence of this char sequence containing the first characters that satisfy the given `predicate`.

@sample samples.text.Strings.take

## Declarations and overloads

### 1. Common

```kotlin
public inline fun CharSequence.takeWhile(predicate: (Char) -> Boolean): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L639)

### 2. Common

```kotlin
public inline fun String.takeWhile(predicate: (Char) -> Boolean): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L652)

Returns a string containing the first characters that satisfy the given `predicate`.

@sample samples.text.Strings.take

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "<<<First Grade>>>"
    println(string.take(8))
    println(string.takeLast(8))
    println(string.takeWhile { !it.isLetter() })
    println(string.takeLastWhile { !it.isLetter() })
}
```

```text title="Output"
<<<First
Grade>>>
<<<
>>>
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L446)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
