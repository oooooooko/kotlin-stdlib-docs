# buildMap

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用给定的 `builderAction` 以`MutableMap` 以 `MutableMap` 以 popping a `MutableMap` 和 返回一个只读的地图, 并配有相同的键值, 从而构建一个新的只读的 `Map` 。

作为`builderAction`的接收器而通过的地图仅在该函数内有效。使用该函数外的地图会产生一种未指明的行为。

地图条目按`builderAction`号地图所增加的顺序重新迭代。

返回的地图可连号(JVM) 。

@sample 样本采集 建筑建筑图

??? note "查看英文原文"

    Builds a new read-only `Map` by populating a `MutableMap` using the given `builderAction`
    and returning a read-only map with the same key-value pairs.
    
    The map passed as a receiver to the `builderAction` is valid only inside that function.
    Using it outside of the function produces an unspecified behavior.
    
    Entries of the map are iterated in the order they were added by the `builderAction`.
    
    The returned map is serializable (JVM).
    
    @sample samples.collections.Builders.Maps.buildMapSample

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <K, V> buildMap(@BuilderInference builderAction: MutableMap<K, V>.() -> Unit): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L137)

### 2. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <K, V> buildMap(capacity: Int, @BuilderInference builderAction: MutableMap<K, V>.() -> Unit): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L163)

使用给定的 `builderAction` 以`MutableMap` 以 `MutableMap` 以 popping a `MutableMap` 和 返回一个只读的地图, 并配有相同的键值, 从而构建一个新的只读的 `Map` 。

作为`builderAction`的接收器而通过的地图仅在该函数内有效。使用该函数外的地图会产生一种未指明的行为。

`capacity` 用于暗示`builderAction`中预期增加的对数。

地图条目按`builderAction`号地图所增加的顺序重新迭代。

返回的地图可连号(JVM) 。

@throws 非法辩护,如果给定的`capacity`为负数,则例外。

@sample 样本采集 建筑建筑图 建筑图 利用能力建立地图抽样

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = mapOf('b' to 2, 'c' to 3)

    val y = buildMap<Char, Int> {
        put('a', 1)
        put('c', 0)
        putAll(x)
        put('d', 4)
    }

    println(y)
}
```

```text title="输出"
{a=1, c=3, b=2, d=4}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L64)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = mapOf('b' to 2, 'c' to 3)

    val y = buildMap<Char, Int>(x.size + 2) {
        put('a', 1)
        put('c', 0)
        putAll(x)
        put('d', 4)
    }

    println(y)
}
```

```text title="输出"
{a=1, c=3, b=2, d=4}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L78)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
