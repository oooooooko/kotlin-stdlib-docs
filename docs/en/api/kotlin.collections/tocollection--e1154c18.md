# toCollection

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends all elements to the given `destination` collection.

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public fun <T, C : MutableCollection<in T>> Array<out T>.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11256)

### 2. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Byte>> ByteArray.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11267)

### 3. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Short>> ShortArray.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11278)

### 4. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Int>> IntArray.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11289)

### 5. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Long>> LongArray.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11300)

### 6. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Float>> FloatArray.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11311)

### 7. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Double>> DoubleArray.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11322)

### 8. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Boolean>> BooleanArray.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11333)

### 9. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Char>> CharArray.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11344)

### 10. Common

```kotlin
@IgnorableReturnValue
public fun <T, C : MutableCollection<in T>> Iterable<T>.toCollection(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1480)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.random.Random
import kotlin.random.nextInt
import kotlin.test.*

fun <T, C : MutableCollection<T>> testOperation(before: List<T>, after: List<T>, expectedModified: Boolean, toMutableCollection: (List<T>) -> C) =
        fun(operation: (C.() -> Boolean)) {
            val list = toMutableCollection(before)
            println(list.operation())
            println(list)
        }

fun <T> testOperation(before: List<T>, after: List<T>, expectedModified: Boolean) =
        testOperation(before, after, expectedModified, { it.toMutableList() })

private fun <T> forAllStandardMutableLists(data: List<T>, block: (MutableList<T>) -> Unit) {
        block(data.toMutableList())
        block(ArrayDeque(data))
        buildList {
            addAll(data)
            block(this)
        }
    }

fun main() {

        val data = listOf("foo", "bar")

        testOperation(emptyList(), data, true).let { assertAdd ->
            assertAdd { addAll(data) }
            assertAdd { addAll(data.toTypedArray()) }
            assertAdd { addAll(data.toTypedArray().asIterable()) }
            assertAdd { addAll(data.asSequence()) }
        }

        testOperation(data, data, false, { it.toCollection(LinkedHashSet()) }).let { assertAdd ->
            assertAdd { addAll(data) }
            assertAdd { addAll(data.toTypedArray()) }
            assertAdd { addAll(data.toTypedArray().asIterable()) }
            assertAdd { addAll(data.asSequence()) }
        }
    
}
```

```text title="Output"
true
[foo, bar]
true
[foo, bar]
true
[foo, bar]
true
[foo, bar]
false
[foo, bar]
false
[foo, bar]
false
[foo, bar]
false
[foo, bar]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/MutableCollectionsTest.kt#L25)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
