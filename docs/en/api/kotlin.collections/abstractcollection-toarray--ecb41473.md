# AbstractCollection.toArray

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns new array of type `Array<Any?>` with the elements of this collection.

## Declarations and overloads

### 1. Common

```kotlin
@JsName("toArray")
    protected open fun toArray(): Array<Any?>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/AbstractCollection.kt#L30)

### 2. Common

```kotlin
protected open fun <T> toArray(array: Array<T>): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/AbstractCollection.kt#L36)

Fills the provided `array` or creates new array of the same type
and fills it with the elements of this collection.

If this collection doesn't fit in the provided `array`,
a new array is created with the same array type and the size of this collection,
and filled with this collection elements.
Otherwise, the specified `array` is filled starting from index 0.
The value of the elements following the collection elements is unspecified.

@return An array containing all elements of this collection.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.collections.*

fun main() {
    val source = object : AbstractCollection<Int>() { override val size = 3; override fun iterator() = listOf(1, 2, 3).iterator() ; fun demonstrate() = `toArray`() }
    val result = source.demonstrate()
    println(result.contentToString())
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
