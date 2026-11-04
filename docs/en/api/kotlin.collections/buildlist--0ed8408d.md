# buildList

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Builds a new read-only `List` by populating a `MutableList` using the given `builderAction`
and returning a read-only list with the same elements.

The list passed as a receiver to the `builderAction` is valid only inside that function.
Using it outside of the function produces an unspecified behavior.

The returned list is serializable (JVM).

@sample samples.collections.Builders.Lists.buildListSample

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <E> buildList(@BuilderInference builderAction: MutableList<E>.() -> Unit): List<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L172)

### 2. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <E> buildList(capacity: Int, @BuilderInference builderAction: MutableList<E>.() -> Unit): List<E>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L196)

Builds a new read-only `List` by populating a `MutableList` using the given `builderAction`
and returning a read-only list with the same elements.

The list passed as a receiver to the `builderAction` is valid only inside that function.
Using it outside of the function produces an unspecified behavior.

The returned list is serializable (JVM).

`capacity` is used to hint the expected number of elements added in the `builderAction`.

@throws IllegalArgumentException if the given `capacity` is negative.

@sample samples.collections.Builders.Lists.buildListSampleWithCapacity

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = listOf('b', 'c')

    val y = buildList {
        add('a')
        addAll(x)
        add('d')
    }

    println(y)
}
```

```text title="Output"
[a, b, c, d]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L8)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = listOf('b', 'c')

    val y = buildList(x.size + 2) {
        add('a')
        addAll(x)
        add('d')
    }

    println(y)
}
```

```text title="Output"
[a, b, c, d]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L21)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
