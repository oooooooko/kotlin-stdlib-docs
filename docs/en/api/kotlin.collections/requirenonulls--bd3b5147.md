# requireNoNulls

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an original collection containing all the non-`null` elements, throwing an `IllegalArgumentException` if there are any `null` elements.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Any> Array<T?>.requireNoNulls(): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26260)

### 2. Common

```kotlin
public fun <T : Any> Iterable<T?>.requireNoNulls(): Iterable<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3519)

### 3. Common

```kotlin
public fun <T : Any> List<T?>.requireNoNulls(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3532)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*
import kotlin.math.pow
import kotlin.random.Random

fun testPlus(doPlus: (List<String>) -> List<String>) {
        val list = listOf("foo", "bar")
        val list2: List<String> = doPlus(list)
        println(list)
        println(list2)
    }

private fun testMinus(expected: List<String>? = null, doMinus: (List<String>) -> List<String>) {
        val a = listOf("foo", "bar", "bar")
        val b: List<String> = doMinus(a)
        val expected_ = expected ?: listOf("foo")
        println(b.toList())
    }

fun main() {

        val data = arrayListOf<String?>("foo", "bar")
        val notNull = data.requireNoNulls()
        println(notNull)

        val hasNulls = listOf("foo", null, "bar")

        assertFailsWith<IllegalArgumentException> {
            // should throw an exception as we have a null
            hasNulls.requireNoNulls()
        }
    
}
```

```text title="Output"
[foo, bar]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/CollectionTest.kt#L607)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
