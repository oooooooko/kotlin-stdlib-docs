# getValue

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此只读地图中给定对象的属性值。 @param 此值Ref 此值是请求值的对象( 未使用) 。 @param 属性元数据是该属性的元数据, 用于获取属性的名称, 并查找与此名称相应的数值 。 @return 属性值 。

@throws 否 元素例外,当地图不包含属性名称的价值,也不提供默认默认值(见 `withDefault` )时,则不在此限。

??? note "查看英文原文"

    Returns the value of the property for the given object from this read-only map.
    @param thisRef the object for which the value is requested (not used).
    @param property the metadata for the property, used to get the name of property and lookup the value corresponding to this name in the map.
    @return the property value.
    
    @throws NoSuchElementException when the map doesn't contain value for the property name and doesn't provide an implicit default (see `withDefault`).

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <V, V1 : V> Map<in String, @Exact V>.getValue(thisRef: Any?, property: KProperty<*>): V1
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MapAccessors.kt#L13)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("getVar")
@kotlin.internal.InlineOnly
public inline operator fun <V, V1 : V> MutableMap<in String, out @Exact V>.getValue(thisRef: Any?, property: KProperty<*>): V1
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MapAccessors.kt#L25)

返回此可变映射 。 @param 此值是请求值的对象( 未使用) 。 @param 属性元数据是该属性的元数据, 用于获取属性的名称并查找与此名称相应的数值 。 @return 属性值 。

@throws 否 元素例外,当地图不包含属性名称的价值,也不提供默认默认值(见 `withDefault` )时,则不在此限。

### 3. Common

```kotlin
@SinceKotlin("1.1")
public fun <K, V> Map<K, V>.getValue(key: K): V
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L424)

返回给定的 `key` 的值,如果地图中没有此密钥,则会丢弃例外。

如果地图是`withDefault`创建的,则采用其`defaultValue`提供者功能,而不是破例。

@throws 否 元素例外,当地图不包含指定密钥的值,且没有为该地图提供默认默认值时。

@sample 样本收集 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图 地图

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

```text title="输出"
true
1
42
2
3
4
42
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/MapTest.kt#L77)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
