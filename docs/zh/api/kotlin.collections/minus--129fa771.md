# minus

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含原始收藏全部元素的列表, 但不首次出现给定的 `element` 。

??? note "查看英文原文"

    Returns a list containing all elements of the original collection without the first occurrence of the given `element`.

## 声明与重载

### 1. Common

```kotlin
public operator fun <T> Iterable<T>.minus(element: T): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3578)

### 2. Common

```kotlin
public operator fun <T> Iterable<T>.minus(elements: Array<out T>): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3587)

返回包含原始收藏全部元素的列表, 但给定 `elements` 矩阵中包含元素除外 。

### 3. Common

```kotlin
public operator fun <T> Iterable<T>.minus(elements: Iterable<T>): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3595)

返回包含原始收藏全部元素的列表, 但给定的 `elements` 收藏中包含元素除外 。

### 4. Common

```kotlin
public operator fun <T> Iterable<T>.minus(elements: Sequence<T>): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3605)

返回包含原始收藏全部元素的列表, 但给定`elements`序列中包含元素除外 。

### 5. Common

```kotlin
public operator fun <T> Set<T>.minus(element: T): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sets.kt#L22)

返回包含原始集全部元素的一组,但给定的`element`除外。

返回的集保存原集的元素迭代顺序。

### 6. Common

```kotlin
public operator fun <T> Set<T>.minus(elements: Array<out T>): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sets.kt#L33)

返回包含原始集全部元素的一组,但给定的 `elements` 矩阵中包含元素除外。

返回的集保存原集的元素迭代顺序。

### 7. Common

```kotlin
public operator fun <T> Set<T>.minus(elements: Iterable<T>): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sets.kt#L44)

返回包含原始集全部元素的一组,但给定的`elements`收藏中包含元素除外。

返回的集保存原集的元素迭代顺序。

### 8. Common

```kotlin
public operator fun <T> Set<T>.minus(elements: Sequence<T>): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sets.kt#L60)

返回包含原始集所有元素的一组,但给定`elements`序列中包含元素除外。

返回的集保存原集的元素迭代顺序。

### 9. Common

```kotlin
@SinceKotlin("1.1")
public operator fun <K, V> Map<out K, V>.minus(key: K): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L885)

返回包含原始地图所有条目的地图,但有给定`key`条目的条目除外。

返回的地图保留原始地图的条目迭代顺序。

### 10. Common

```kotlin
@SinceKotlin("1.1")
public operator fun <K, V> Map<out K, V>.minus(keys: Iterable<K>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L894)

返回包含原始地图所有条目的地图,但那些在给定的`keys`收藏中包含其键子的条目除外。

返回的地图保留原始地图的条目迭代顺序。

### 11. Common

```kotlin
@SinceKotlin("1.1")
public operator fun <K, V> Map<out K, V>.minus(keys: Array<out K>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L904)

返回包含原始地图所有条目的地图,但那些键包含在给定的 `keys` 矩阵中的条目除外。

返回的地图保留原始地图的条目迭代顺序。

### 12. Common

```kotlin
@SinceKotlin("1.1")
public operator fun <K, V> Map<out K, V>.minus(keys: Sequence<K>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L914)

返回包含原始地图所有条目的地图,但以给定`keys`序列中包含的密钥为主的条目除外。

返回的地图保留原始地图的条目迭代顺序。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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
    val source = listOf(1, 2, 3)
    val result = source.`minus`(1)
    println(result)
}
```

```text title="输出"
[2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
