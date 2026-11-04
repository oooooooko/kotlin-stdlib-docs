# ifEmpty

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns this array if it's not empty
or the result of calling `defaultValue` function if the array is empty.

@sample samples.collections.Arrays.Usage.arrayIfEmpty

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
@Suppress("UPPER_BOUND_CANNOT_BE_ARRAY")
public inline fun <C, R> C.ifEmpty(defaultValue: () -> R): R where C : Array<*>, C : R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Arrays.kt#L67)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline fun <C, R> C.ifEmpty(defaultValue: () -> R): R where C : Collection<*>, C : R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L274)

Returns this collection if it's not empty
or the result of calling `defaultValue` function if the collection is empty.

@sample samples.collections.Collections.Collections.collectionIfEmpty

### 3. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline fun <M, R> M.ifEmpty(defaultValue: () -> R): R where M : Map<*, *>, M : R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L228)

Returns this map if it's not empty
or the result of calling `defaultValue` function if the map is empty.

@sample samples.collections.Maps.Usage.mapIfEmpty

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val empty: List<Int> = emptyList()

    val emptyOrNull: List<Int>? = empty.ifEmpty { null }
    println(emptyOrNull)

    val emptyOrDefault: List<Any> = empty.ifEmpty { listOf("default") }
    println(emptyOrDefault)

    val nonEmpty = listOf("x")
    val sameList: List<String> = nonEmpty.ifEmpty { listOf("empty") }
    println(nonEmpty === sameList)
}
```

```text title="Output"
null
[default]
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L56)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
