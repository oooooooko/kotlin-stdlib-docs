# setOfNotNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回新的只读集, 要么带有单一个给定元素, 如果不是无效的, 要么在元素为无效的情况下返回空的设置。 返回的集合是可序列的( JVM) @sample 样本. collects. collects. setOnnnull. setofnol

??? note "查看英文原文"

    Returns a new read-only set either with single given element, if it is not null, or empty set if the element is null.
    The returned set is serializable (JVM).
    @sample samples.collections.Collections.Sets.setOfNotNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Any> setOfNotNull(element: T?): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L103)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Any> setOfNotNull(vararg elements: T?): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L111)

返回仅以给定元素为唯一值的新的只读集,这些元素并非空的。集的元素按指定顺序迭代。 返回的集是可序列的( JVM) @sample 样本。 收藏。 集合 。 Set. setOnnonNull

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val empty = setOfNotNull<Any>(null)
    println(empty)

    val singleton = setOfNotNull(42)
    println(singleton)

    val set = setOfNotNull(1, null, 2, null, 3)
    println(set)
}
```

```text title="输出"
[]
[42]
[1, 2, 3]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L629)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
