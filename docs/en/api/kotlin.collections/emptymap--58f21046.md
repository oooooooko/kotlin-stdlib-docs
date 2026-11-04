# emptyMap

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an empty read-only map of specified type.

The returned map is serializable (JVM).
@sample samples.collections.Maps.Instantiation.emptyReadOnlyMap

## Declarations and overloads

### 1. Common

```kotlin
public fun <K, V> emptyMap(): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L34)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*
import kotlin.math.pow

fun testPlusAssign(doPlusAssign: (MutableMap<String, Int>) -> Unit) {
        val map = hashMapOf("a" to 1, "b" to 2)
        doPlusAssign(map)
        println(map.size)
        println(map["a"])
        println(map["b"])
        println(map["c"])
    }

fun testPlus(doPlus: (Map<String, Int>) -> Map<String, Int>) {
        val original = mapOf("A" to 1, "B" to 2)
        val extended = doPlus(original)
        println(extended.size)
        println(extended["A"])
        println(extended["B"])
        println(extended["C"])
    }

fun <K, V> testPlusAny(mapObject: Any, pair: Pair<K, V>) {
        val map = mapObject as Map<*, *>
        fun assertContains(map: Map<*, *>) = println(map[pair.first])

        assertContains(map + pair)
        assertContains(map + listOf(pair))
        assertContains(map + arrayOf(pair))
        assertContains(map + sequenceOf(pair))
        assertContains(map + mapOf(pair))
    }

fun testMinus(doMinus: (Map<String, Int>) -> Map<String, Int>) {
        val original = mapOf("A" to 1, "B" to 2)
        val shortened = doMinus(original)
        println(shortened.entries.single().toPair())
    }

fun testMinusAssign(doMinusAssign: (MutableMap<String, Int>) -> Unit) {
        val original = hashMapOf("A" to 1, "B" to 2)
        doMinusAssign(original)
        println(original.entries.single().toPair())
    }

fun testIdempotent(operation: (Map<String, Int>) -> Map<String, Int>) {
        val original = mapOf("A" to 1, "B" to 2)
        println(operation(original))
    }

fun testIdempotentAssign(operation: (MutableMap<String, Int>) -> Unit) {
        val original = hashMapOf("A" to 1, "B" to 2)
        val result = HashMap(original)
        operation(result)
        println(result)
    }

private fun <K, V> expectMinMaxWith(min: Pair<K, V>, max: Pair<K, V>, elements: Map<K, V>, comparator: Comparator<Map.Entry<K, V>>) {
        println(elements.minWithOrNull(comparator)?.toPair())
        println(elements.maxWithOrNull(comparator)?.toPair())
        println(elements.minWith(comparator).toPair())
        println(elements.maxWith(comparator).toPair())
    }

private inline fun <K, V, R : Comparable<R>> expectMinMaxBy(min: Pair<K, V>, max: Pair<K, V>, elements: Map<K, V>, selector: (Map.Entry<K, V>) -> R) {
        println(elements.minBy(selector).toPair())
        println(elements.minByOrNull(selector)?.toPair())
        println(elements.maxBy(selector).toPair())
        println(elements.maxByOrNull(selector)?.toPair())
    }

private inline fun <K, V, R : Comparable<R>> expectMinMaxOf(min: R, max: R, elements: Map<K, V>, selector: (Map.Entry<K, V>) -> R) {
        println(elements.minOf(selector))
        println(elements.minOfOrNull(selector))
        println(elements.maxOf(selector))
        println(elements.maxOfOrNull(selector))
    }

private inline fun <K, V, R> expectMinMaxOfWith(min: R, max: R, elements: Map<K, V>, comparator: Comparator<R>, selector: (Map.Entry<K, V>) -> R) {
        println(elements.minOfWith(comparator, selector))
        println(elements.minOfWithOrNull(comparator, selector))
        println(elements.maxOfWith(comparator, selector))
        println(elements.maxOfWithOrNull(comparator, selector))
    }

fun main() {

        testPlusAny(emptyMap<String, String>(), 1 to "A")
        testPlusAny(mapOf("A" to null), "A" as CharSequence to 2)
    
}
```

```text title="Output"
A
A
A
A
A
2
2
2
2
2
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/MapTest.kt#L708)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
