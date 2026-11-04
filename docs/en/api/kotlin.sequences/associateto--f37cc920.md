# associateTo

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Populates and returns the `destination` mutable map with key-value pairs
provided by `transform` function applied to each element of the given sequence.

If any of two pairs would have the same key the last one gets added to the map.

The operation is _terminal_.

@sample samples.collections.Collections.Transformations.associateTo

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, in V>> Sequence<T>.associateTo(destination: M, transform: (T) -> Pair<K, V>): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L913)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String)

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = mutableMapOf<String, String>()
    println(byLastName.isEmpty())

    scientists.associateTo(byLastName) { it.lastName to it.firstName }

    println(byLastName.isNotEmpty())
    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="Output"
true
true
{Hopper=Grace, Bernoulli=Johann}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L778)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
