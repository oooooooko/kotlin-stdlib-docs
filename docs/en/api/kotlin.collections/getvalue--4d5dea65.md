# getValue

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the value of the property for the given object from this read-only map.
@param thisRef the object for which the value is requested (not used).
@param property the metadata for the property, used to get the name of property and lookup the value corresponding to this name in the map.
@return the property value.

@throws NoSuchElementException when the map doesn't contain value for the property name and doesn't provide an implicit default (see `withDefault`).

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <V, V1 : V> Map<in String, @Exact V>.getValue(thisRef: Any?, property: KProperty<*>): V1
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MapAccessors.kt#L13)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("getVar")
@kotlin.internal.InlineOnly
public inline operator fun <V, V1 : V> MutableMap<in String, out @Exact V>.getValue(thisRef: Any?, property: KProperty<*>): V1
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MapAccessors.kt#L25)

Returns the value of the property for the given object from this mutable map.
@param thisRef the object for which the value is requested (not used).
@param property the metadata for the property, used to get the name of property and lookup the value corresponding to this name in the map.
@return the property value.

@throws NoSuchElementException when the map doesn't contain value for the property name and doesn't provide an implicit default (see `withDefault`).

### 3. Common

```kotlin
@SinceKotlin("1.1")
public fun <K, V> Map<K, V>.getValue(key: K): V
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L424)

Returns the value for the given `key` or throws an exception if there is no such key in the map.

If the map was created by `withDefault`, resorts to its `defaultValue` provider function
instead of throwing an exception.

@throws NoSuchElementException when the map doesn't contain a value for the specified key and
no implicit default value was provided for that map.

@sample samples.collections.Maps.Usage.getValueWithoutDefault
@sample samples.collections.Maps.Usage.getValueWithDefault

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

        val data: MutableMap<String, Int> = hashMapOf("bar" to 1)
        assertFailsWith<NoSuchElementException> { data.getValue("foo") }.let { e ->
            println("foo" in e.message!!)
        }
        println(data.getValue("bar"))

        val mutableWithDefault = data.withDefault { 42 }
        println(mutableWithDefault.getValue("foo"))

        // verify that it is wrapper
        mutableWithDefault["bar"] = 2
        println(data["bar"])
        data["bar"] = 3
        println(mutableWithDefault["bar"])

        val readonlyWithDefault = (data as Map<String, Int>).withDefault { it.length }
        println(readonlyWithDefault.getValue("loop"))

        val withReplacedDefault = readonlyWithDefault.withDefault { 42 }
        println(withReplacedDefault.getValue("loop"))
    
}
```

```text title="Output"
true
1
42
2
3
4
42
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/MapTest.kt#L77)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
