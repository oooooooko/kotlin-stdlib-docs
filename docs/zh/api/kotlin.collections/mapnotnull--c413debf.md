# mapNotNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回仅包含对原始数组中每个元素应用给定的 `transform` 函数的非null结果的列表。

@sample 样本、采集物、采集物、转化物、图纸、图纸

??? note "查看英文原文"

    Returns a list containing only the non-null results of applying the given `transform` function
    to each element in the original array.
    
    @sample samples.collections.Collections.Transformations.mapNotNull

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, R : Any> Array<out T>.mapNotNull(transform: (T) -> R?): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13171)

### 2. Common

```kotlin
public inline fun <T, R : Any> Iterable<T>.mapNotNull(transform: (T) -> R?): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1794)

返回仅包含对原始收藏中每个元素应用给定的 `transform` 函数的非null结果的列表。

@sample 样本、采集物、采集物、转化物、图纸、图纸

### 3. Common

```kotlin
public inline fun <K, V, R : Any> Map<out K, V>.mapNotNull(transform: (Map.Entry<K, V>) -> R?): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L132)

返回仅包含对原始地图中每个条目应用给定的 `transform` 函数的非null结果的列表 。

@sample 样本采集 模型 变形图 地图 诺诺

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val strings: List<String> = listOf("12a", "45", "", "3")
    val ints: List<Int> = strings.mapNotNull { it.toIntOrNull() }

    println(ints)
    println(ints.sum())
}
```

```text title="输出"
[45, 3]
48
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L888)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
