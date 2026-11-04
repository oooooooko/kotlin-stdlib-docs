# partition

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Splits the original char sequence into a pair of char sequences,
where *first* char sequence contains characters for which `predicate` yielded `true`,
while *second* char sequence contains characters for which `predicate` yielded `false`.

@sample samples.text.Strings.partition

## Declarations and overloads

### 1. Common

```kotlin
public inline fun CharSequence.partition(predicate: (Char) -> Boolean): Pair<CharSequence, CharSequence>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2374)

### 2. Common

```kotlin
public inline fun String.partition(predicate: (Char) -> Boolean): Pair<String, String>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2394)

Splits the original string into a pair of strings,
where *first* string contains characters for which `predicate` yielded `true`,
while *second* string contains characters for which `predicate` yielded `false`.

@sample samples.text.Strings.partition

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun isVowel(c: Char) = "aeuio".contains(c, ignoreCase = true)
    val string = "Discussion"
    val result = string.partition(::isVowel)
    println(result)
}
```

```text title="Output"
(iuio, Dscssn)
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L265)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
