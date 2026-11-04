# associateWithTo

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Populates and returns the `destination` mutable map with key-value pairs for each element of the given sequence,
where key is the element itself and value is provided by the `valueSelector` function applied to that key.

If any two elements are equal, the last one overwrites the former value in the map.

The operation is _terminal_.

@sample samples.collections.Collections.Transformations.associateWithTo

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> Sequence<K>.associateWithTo(destination: M, valueSelector: (K) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L949)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String) {
        override fun toString(): String = "$firstName $lastName"
    }

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Jacob", "Bernoulli"))
    val withLengthOfNames = mutableMapOf<Person, Int>()
    println(withLengthOfNames.isEmpty())

    scientists.associateWithTo(withLengthOfNames) { it.firstName.length + it.lastName.length }

    println(withLengthOfNames.isNotEmpty())
    // Jacob Bernoulli only occurs once in the map because only the last pair with the same key gets added
    println(withLengthOfNames)
}
```

```text title="Output"
true
true
{Grace Hopper=11, Jacob Bernoulli=14}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L802)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
