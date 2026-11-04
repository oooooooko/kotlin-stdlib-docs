# setOf

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回含有给定元素的新的只读集。集的元素按指定顺序迭代。 返回的集是可序列的( JVM) @sample 样本. collections. Sets.read OnlySet.

??? note "查看英文原文"

    Returns a new read-only set with the given elements.
    Elements of the set are iterated in the order they were specified.
    The returned set is serializable (JVM).
    @sample samples.collections.Collections.Sets.readOnlySet

## 声明与重载

### 1. Common

```kotlin
public fun <T> setOf(vararg elements: T): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L38)

### 2. Common

```kotlin
@SinceKotlin("1.9")
public expect fun <T> setOf(element: T): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L46)

返回仅包含指定对象`element`的新的只读集。

返回的成套设备可序列(JVM) 。

@sample 样本、采集的样本、采集的样本、采集的样本、 种子、 单线的信号

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> setOf(): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L56)

返回一个只读的空集。 返回的集是可序列的( JVM) 。 @sample 样本. collects. Sets. srevenyRead OnlySet

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set1 = setOf(1, 2, 3)
    val set2 = setOf(3, 2, 1)

    // setOf preserves the iteration order of elements
    println(set1)
    println(set2)

    // but the sets with the same elements are equal no matter of order
    println(set1 == set2)
}
```

```text title="输出"
[1, 2, 3]
[3, 2, 1]
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L578)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set = setOf('a')
    println(set)
    println(set.size)
}
```

```text title="输出"
[a]
1
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L591)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set = setOf<String>()
    println(set.isEmpty())

    // another way to create an empty set,
    // type parameter is inferred from the expected type
    val other: Set<Int> = emptySet()

    println(set == other)
    println(set)
}
```

```text title="输出"
true
true
[]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L565)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
