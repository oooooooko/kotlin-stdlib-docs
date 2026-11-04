# associateWithTo

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Populates and returns the `destination` mutable map with key-value pairs for each character of the given char sequence,
where key is the character itself and value is provided by the `valueSelector` function applied to that key.

If any two characters are equal, the last one overwrites the former value in the map.

@sample samples.text.Strings.associateWithTo

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public inline fun <V, M : MutableMap<in Char, in V>> CharSequence.associateWithTo(destination: M, valueSelector: (Char) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L790)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character with its code
    val result = mutableMapOf<Char, Int>()
    string.associateWithTo(result) { char -> char.code }
    // notice each letter occurs only once
    println(result)
}
```

```text title="Output"
{b=98, o=111, n=110, e=101,  =32, j=106, u=117, r=114, é=233}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L255)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
