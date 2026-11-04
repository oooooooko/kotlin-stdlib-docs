# minus

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a sequence containing all elements of the original sequence without the first occurrence of the given `element`.

The operation is _intermediate_ and _stateless_.

## Declarations and overloads

### 1. Common

```kotlin
public operator fun <T> Sequence<T>.minus(element: T): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3045)

### 2. Common

```kotlin
public operator fun <T> Sequence<T>.minus(elements: Array<out T>): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3059)

Returns a sequence containing all elements of original sequence except the elements contained in the given `elements` array.

Note that the source sequence and the array being subtracted are iterated only when an `iterator` is requested from
the resulting sequence. Changing any of them between successive calls to `iterator` may affect the result.

The operation is _intermediate_ and _stateful_.

### 3. Common

```kotlin
public operator fun <T> Sequence<T>.minus(elements: Iterable<T>): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3076)

Returns a sequence containing all elements of original sequence except the elements contained in the given `elements` collection.

Note that the source sequence and the collection being subtracted are iterated only when an `iterator` is requested from
the resulting sequence. Changing any of them between successive calls to `iterator` may affect the result.

The operation is _intermediate_ and _stateful_.

### 4. Common

```kotlin
public operator fun <T> Sequence<T>.minus(elements: Sequence<T>): Sequence<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3096)

Returns a sequence containing all elements of original sequence except the elements contained in the given `elements` sequence.

Note that the source sequence and the sequence being subtracted are iterated only when an `iterator` is requested from
the resulting sequence. Changing any of them between successive calls to `iterator` may affect the result.

The operation is _intermediate_ for this sequence and _terminal_ and _stateful_ for the `elements` sequence.

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
import kotlin.sequences.*

fun main() {
    val source = sequenceOf(1, 2, 3)
    val result = source.`minus`(1)
    println(result.toList())
}
```

```text title="Output"
[2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
