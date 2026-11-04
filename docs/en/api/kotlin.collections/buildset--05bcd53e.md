# buildSet

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Builds a new read-only `Set` by populating a `MutableSet` using the given `builderAction`
and returning a read-only set with the same elements.

The set passed as a receiver to the `builderAction` is valid only inside that function.
Using it outside of the function produces an unspecified behavior.

Elements of the set are iterated in the order they were added by the `builderAction`.

The returned set is serializable (JVM).

@sample samples.collections.Builders.Sets.buildSetSample

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <E> buildSet(@BuilderInference builderAction: MutableSet<E>.() -> Unit): Set<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L122)

### 2. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <E> buildSet(capacity: Int, @BuilderInference builderAction: MutableSet<E>.() -> Unit): Set<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L148)

Builds a new read-only `Set` by populating a `MutableSet` using the given `builderAction`
and returning a read-only set with the same elements.

The set passed as a receiver to the `builderAction` is valid only inside that function.
Using it outside of the function produces an unspecified behavior.

`capacity` is used to hint the expected number of elements added in the `builderAction`.

Elements of the set are iterated in the order they were added by the `builderAction`.

The returned set is serializable (JVM).

@throws IllegalArgumentException if the given `capacity` is negative.

@sample samples.collections.Builders.Sets.buildSetSampleWithCapacity

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = setOf('a', 'b')

    val y = buildSet {
        add('b')
        addAll(x)
        add('c')
    }

    println(y)
}
```

```text title="Output"
[b, a, c]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L36)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = setOf('a', 'b')

    val y = buildSet(x.size + 2) {
        add('b')
        addAll(x)
        add('c')
    }

    println(y)
}
```

```text title="Output"
[b, a, c]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L49)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
