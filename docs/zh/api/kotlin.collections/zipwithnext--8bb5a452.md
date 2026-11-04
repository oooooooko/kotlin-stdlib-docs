# zipWithNext

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此收藏中每两个相邻元素的对数列表 。

如果此收藏收藏含有两个元素以下, 则返回的列表为空 。

@sample 样本、采集物、采集物、转化物、与下一个相接

??? note "查看英文原文"

    Returns a list of pairs of each two adjacent elements in this collection.
    
    The returned list is empty if this collection contains less than two elements.
    
    @sample samples.collections.Collections.Transformations.zipWithNext

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun <T> Iterable<T>.zipWithNext(): List<Pair<T, T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3883)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public inline fun <T, R> Iterable<T>.zipWithNext(transform: (a: T, b: T) -> R): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3895)

返回包含对本收藏中每对两个相邻元素应用给定的 `transform` 函数的结果的列表 。

如果此收藏收藏含有两个元素以下, 则返回的列表为空 。

@sample 样本、采集物、采集物、变异物、与下一个FindDeltas的相接

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val letters = ('a'..'f').toList()
    val pairs = letters.zipWithNext()

    println(letters)
    println(pairs)
}
```

```text title="输出"
[a, b, c, d, e, f]
[(a, b), (b, c), (c, d), (d, e), (e, f)]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L937)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val values = listOf(1, 4, 9, 16, 25, 36)
    val deltas = values.zipWithNext { a, b -> b - a }

    println(deltas)
}
```

```text title="输出"
[3, 5, 7, 9, 11]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L946)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
