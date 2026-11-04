# toMap

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含从给定配对集合中获取的所有关键值的新的地图。

返回的地图保留原始收藏的条目迭代顺序。 如果两对中的任何一个都有相同的密钥, 最后一个可以添加到地图中 。

??? note "查看英文原文"

    Returns a new map containing all key-value pairs from the given collection of pairs.
    
    The returned map preserves the entry iteration order of the original collection.
    If any of two pairs would have the same key the last one gets added to the map.

## 声明与重载

### 1. Common

```kotlin
public fun <K, V> Iterable<Pair<K, V>>.toMap(): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L713)

### 2. Common

```kotlin
@IgnorableReturnValue
public fun <K, V, M : MutableMap<in K, in V>> Iterable<Pair<K, V>>.toMap(destination: M): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L730)

弹出并返回 `destination` 移动图, 包含来自给定配对集合的配对的配对配对配对。

### 3. Common

```kotlin
public fun <K, V> Array<out Pair<K, V>>.toMap(): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L737)

返回包含从给定的对数组中所有关键值对的新地图。

返回的地图保留原始数组的条目迭代顺序。 如果两对中的任何一个都有相同的键, 最后一个键会被添加到地图中 。

### 4. Common

```kotlin
@IgnorableReturnValue
public fun <K, V, M : MutableMap<in K, in V>> Array<out Pair<K, V>>.toMap(destination: M): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L749)

弹出并返回 `destination` 移动图,其中含有来自给定的对数组的配对的配对关键值。

### 5. Common

```kotlin
public fun <K, V> Sequence<Pair<K, V>>.toMap(): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L756)

返回包含从给定对数序列中所有关键值对的新地图。

返回的地图保留了原始序列的条目迭代顺序。 如果两对中的任何一个都有相同的键, 最后一个键会被添加到地图中 。

### 6. Common

```kotlin
@IgnorableReturnValue
public fun <K, V, M : MutableMap<in K, in V>> Sequence<Pair<K, V>>.toMap(destination: M): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L764)

弹出并返回 `destination` 移动图,其中含有特定序列中的双对配对的配对关键值。

### 7. Common

```kotlin
@SinceKotlin("1.1")
public fun <K, V> Map<out K, V>.toMap(): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L771)

返回新的只读地图,包含原始地图上的所有关键值对。

返回的地图保留原始地图的条目迭代顺序。

### 8. Common

```kotlin
@SinceKotlin("1.1")
@IgnorableReturnValue
public fun <K, V, M : MutableMap<in K, in V>> Map<out K, V>.toMap(destination: M): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L791)

弹出并返回 `destination` 移动地图,其中含有从给定地图上取出的配对关键值。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("c" to 1, "b" to 2, "a" to 1, "d" to 0, null to 0)

    val valueComparator = compareBy<Pair<String?, Int>> { it.second }
    val map1 = list.sortedWith(valueComparator).toMap()
    println(map1)

    val valueThenKeyComparator = valueComparator
        .thenComparator({ a, b -> compareValues(a.first, b.first) })
    val map2 = list.sortedWith(valueThenKeyComparator).toMap()
    println(map2)
}
```

```text title="输出"
{d=0, null=0, c=1, a=1, b=2}
{null=0, d=0, a=1, c=1, b=2}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L164)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
