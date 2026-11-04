# associateByTo

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function applied to each character of the given char sequence
and value is the character itself.

If any two characters would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.text.Strings.associateByTo

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Char>> CharSequence.associateByTo(destination: M, keySelector: (Char) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L724)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> CharSequence.associateByTo(destination: M, keySelector: (Char) -> K, valueTransform: (Char) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L741)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to characters of the given char sequence.

If any two characters would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.text.Strings.associateByToWithValueTransform

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character by its code
    val result = mutableMapOf<Int, Char>()
    string.associateByTo(result) { char -> char.code }
    // notice each char code occurs only once
    println(result)
}
```

```text title="Output"
{98=b, 111=o, 110=n, 101=e, 32= , 106=j, 117=u, 114=r, 233=é}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L216)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character by the code of its upper case equivalent and transform the character to upper case
    val result = mutableMapOf<Int, Char>()
    string.associateByTo(result, { char -> char.uppercaseChar().code }, { char -> char.uppercaseChar() })
    // notice each char code occurs only once
    println(result)
}
```

```text title="Output"
{66=B, 79=O, 78=N, 69=E, 32= , 74=J, 85=U, 82=R, 201=É}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L226)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
